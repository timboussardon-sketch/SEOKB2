import { and, eq, isNull } from "drizzle-orm";
import { schema } from "../db/client";
import { AppError } from "../core/errors";
import type { DraftSentence } from "../core/claims";
import { renderBody } from "../core/claims";
import { wordCount } from "../core/text";
import type { Deps } from "./deps";
import { logEvent } from "./events";
import { contentHash } from "./steps/draft";
import { setState } from "./transitions";

export type ReviewAction = "APPROVE" | "REJECT" | "RETRY";

/** Actions permises par motif. Une affirmation non étayée ne s'approuve pas : elle se corrige ou s'écarte. */
export const REVIEW_ACTIONS: Record<string, ReviewAction[]> = {
  AMBIGUOUS_ENTITY: ["APPROVE", "REJECT", "RETRY"],
  UNCERTAIN_PRACTICE: ["APPROVE", "REJECT", "RETRY"],
  CONTRADICTORY_EVIDENCE: ["APPROVE", "REJECT", "RETRY"],
  FIRM_ONLY: ["APPROVE", "REJECT"],
  VISIBILITY_INCONCLUSIVE: ["APPROVE", "REJECT", "RETRY"],
  UNSUPPORTED_CLAIM: ["REJECT", "RETRY"],
  STEP_FAILED: ["REJECT", "RETRY"],
};

async function wake(deps: Deps, campaignId: string, prospectId?: string): Promise<void> {
  const [c] = await deps.db.select().from(schema.campaigns).where(eq(schema.campaigns.id, campaignId));
  // Une décision humaine peut rouvrir une campagne terminée ou partielle.
  if (c.status === "PARTIAL" || c.status === "COMPLETED") await deps.db.update(schema.campaigns).set({ status: "RUNNING", stop_reason: null }).where(eq(schema.campaigns.id, campaignId));
  if (prospectId) await deps.queue.send("prospect-advance", { campaignId, prospectId });
  await deps.queue.send("campaign-tick", { campaignId });
}

export async function resolveReview(deps: Deps, itemId: string, action: ReviewAction): Promise<void> {
  const R = schema.review_items;
  const [item] = await deps.db.select().from(R).where(eq(R.id, itemId));
  if (!item || item.status !== "OPEN") throw new AppError("INVALID_INPUT", "Élément de revue introuvable ou déjà traité");
  if (!REVIEW_ACTIONS[item.reason]?.includes(action)) throw new AppError("INVALID_INPUT", `Action ${action} non permise pour ${item.reason}`);
  const [prospect] = await deps.db.select().from(schema.prospects).where(eq(schema.prospects.id, item.prospect_id));
  await deps.db.update(R).set({ status: "RESOLVED", resolution: action, resolved_at: deps.now() }).where(eq(R.id, itemId));
  await logEvent(deps.db, { campaignId: item.campaign_id, prospectId: item.prospect_id, type: "REVIEW_RESOLVED", data: { reason: item.reason, action } });

  if (action === "REJECT") {
    await setState(deps, prospect, "REJECTED", { qualification_status: "REJECTED", qualification_detail: `Écarté en revue (${item.reason})`, review_reason: null });
    return wake(deps, item.campaign_id);
  }
  const resume = prospect.resume_state ?? "DISCOVERED";
  if (action === "APPROVE") {
    const qualifying = ["AMBIGUOUS_ENTITY", "UNCERTAIN_PRACTICE", "CONTRADICTORY_EVIDENCE"].includes(item.reason);
    // Valider un verdict FIRM_ONLY ou INCONCLUSIVE autorise l'audit, jamais le discours d'absence : le verdict reste inchangé.
    await setState(deps, prospect, resume, { review_reason: null, resume_state: null, ...(qualifying ? { qualification_status: "QUALIFIED" } : { force_audit: true }) });
  } else {
    const restart = item.reason === "VISIBILITY_INCONCLUSIVE" || item.reason === "FIRM_ONLY" ? "ENRICHED" : ["AMBIGUOUS_ENTITY", "UNCERTAIN_PRACTICE"].includes(item.reason) ? "DISCOVERED" : resume;
    if (item.reason === "UNSUPPORTED_CLAIM") await deps.db.update(schema.email_drafts).set({ rewrite_rounds: 0, edited_by_human: false }).where(eq(schema.email_drafts.prospect_id, prospect.id));
    await setState(deps, prospect, restart, { review_reason: null, resume_state: null, last_error: null });
  }
  await wake(deps, item.campaign_id, prospect.id);
}

async function invalidateApprovals(deps: Deps, draftId: string, reason: string): Promise<void> {
  const A = schema.approvals;
  await deps.db.update(A).set({ invalidated_at: deps.now(), invalidated_reason: reason }).where(and(eq(A.draft_id, draftId), isNull(A.invalidated_at)));
}

/** Toute modification du brouillon annule son approbation et le renvoie au contrôle factuel. */
export async function editDraft(deps: Deps, prospectId: string, edit: { subject: string; texts: Record<string, string> }): Promise<void> {
  const D = schema.email_drafts;
  const [draft] = await deps.db.select().from(D).where(eq(D.prospect_id, prospectId));
  const [prospect] = await deps.db.select().from(schema.prospects).where(eq(schema.prospects.id, prospectId));
  if (!draft || !prospect) throw new AppError("INVALID_INPUT", "Brouillon introuvable");
  if (!["READY_FOR_REVIEW", "APPROVED", "HUMAN_REVIEW_REQUIRED"].includes(prospect.state)) throw new AppError("INVALID_INPUT", "Brouillon non modifiable dans cet état");
  const sentences = (draft.sentences as DraftSentence[])
    .map((s) => (s.id in edit.texts ? { ...s, text: edit.texts[s.id].trim() } : s))
    .filter((s) => s.text.length > 0);
  const body = renderBody(sentences);
  await deps.db
    .update(D)
    .set({ subject: edit.subject.trim(), sentences, body, word_count: wordCount(body), fact_check: null, edited_by_human: true, content_hash: contentHash(edit.subject.trim(), sentences, draft.recipient), updated_at: deps.now() })
    .where(eq(D.id, draft.id));
  await invalidateApprovals(deps, draft.id, "Brouillon modifié");
  await deps.db.update(schema.review_items).set({ status: "RESOLVED", resolution: "EDIT", resolved_at: deps.now() }).where(and(eq(schema.review_items.prospect_id, prospectId), eq(schema.review_items.reason, "UNSUPPORTED_CLAIM"), eq(schema.review_items.status, "OPEN")));
  await setState(deps, prospect, "DRAFT_READY", { review_reason: null, resume_state: null });
  await logEvent(deps.db, { campaignId: prospect.campaign_id, prospectId, type: "DRAFT_EDITED" });
  await wake(deps, prospect.campaign_id, prospectId);
}

/** L'approbation porte sur une version exacte du message et du destinataire. Elle n'envoie rien. */
export async function approveDraft(deps: Deps, prospectId: string): Promise<void> {
  const [draft] = await deps.db.select().from(schema.email_drafts).where(eq(schema.email_drafts.prospect_id, prospectId));
  const [prospect] = await deps.db.select().from(schema.prospects).where(eq(schema.prospects.id, prospectId));
  if (!draft || !prospect || prospect.state !== "READY_FOR_REVIEW") throw new AppError("INVALID_INPUT", "Ce brouillon n'est pas en attente d'approbation");
  if (!(draft.fact_check as { ok?: boolean } | null)?.ok) throw new AppError("INVALID_INPUT", "Contrôle factuel non validé : approbation refusée");
  if (!draft.recipient) throw new AppError("INVALID_INPUT", "Aucun destinataire : approbation refusée");
  await deps.db.insert(schema.approvals).values({ draft_id: draft.id, content_hash: draft.content_hash, recipient: draft.recipient });
  await setState(deps, prospect, "APPROVED");
}

/** Opposition : le contact est retiré de toutes les campagnes et ne sera pas réimporté. */
export async function suppressProspect(deps: Deps, prospectId: string, reason: string): Promise<void> {
  const [prospect] = await deps.db.select().from(schema.prospects).where(eq(schema.prospects.id, prospectId));
  if (!prospect) throw new AppError("INVALID_INPUT", "Prospect introuvable");
  const [firm] = await deps.db.select().from(schema.firms).where(eq(schema.firms.id, prospect.firm_id));
  const emails = await deps.db.select().from(schema.contacts).where(eq(schema.contacts.firm_id, firm.id));
  const values = [{ value: firm.canonical_domain, kind: "DOMAIN", reason }, ...emails.map((e) => ({ value: e.email, kind: "EMAIL", reason }))];
  await deps.db.insert(schema.suppressions).values(values).onConflictDoNothing();
  const all = await deps.db.select().from(schema.prospects).where(eq(schema.prospects.firm_id, firm.id));
  for (const p of all) {
    if (p.state === "SUPPRESSED" || p.state === "REJECTED") continue;
    const [draft] = await deps.db.select().from(schema.email_drafts).where(eq(schema.email_drafts.prospect_id, p.id));
    if (draft) await invalidateApprovals(deps, draft.id, "Opposition");
    await deps.db.update(schema.prospects).set({ state: "SUPPRESSED", updated_at: deps.now() }).where(eq(schema.prospects.id, p.id));
    await deps.db.update(schema.review_items).set({ status: "RESOLVED", resolution: "REJECT", resolved_at: deps.now() }).where(and(eq(schema.review_items.prospect_id, p.id), eq(schema.review_items.status, "OPEN")));
    await logEvent(deps.db, { campaignId: p.campaign_id, prospectId: p.id, type: "SUPPRESSED", data: { reason } });
    await deps.queue.send("campaign-tick", { campaignId: p.campaign_id });
  }
}

/** Audit manuel d'un prospect déjà observé : possible, sans discours d'absence (le verdict ne change pas). */
export async function forceAudit(deps: Deps, prospectId: string): Promise<void> {
  const [prospect] = await deps.db.select().from(schema.prospects).where(eq(schema.prospects.id, prospectId));
  if (!prospect || prospect.state !== "ARCHIVED_OBSERVED") throw new AppError("INVALID_INPUT", "Audit manuel réservé aux prospects archivés comme déjà observés");
  await setState(deps, prospect, "VISIBILITY_DONE", { force_audit: true });
  await wake(deps, prospect.campaign_id, prospectId);
}
