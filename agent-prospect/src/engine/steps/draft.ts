import { desc, eq } from "drizzle-orm";
import { schema } from "../../db/client";
import { buildBenchmarkPrompts } from "../../core/benchmark";
import { checkDraft, CLAIM_RULE_VERSION, frameVisibility, renderBody, visibilityRequired, visibilitySentence, type ClaimContext, type DraftSentence, type Fact } from "../../core/claims";
import { withRetry } from "../../core/errors";
import { frDate, stableHash, wordCount } from "../../core/text";
import { EMAIL_TEMPLATE_VERSION, renderEmailTemplate } from "../../prompts/email-template";
import type { DraftRequest } from "../../providers/types";
import { metered } from "../budget";
import type { Campaign, Deps, Firm, Prospect, Runtime } from "../deps";
import { logEvent } from "../events";
import { sendToReview, setState } from "../transitions";
import { selectedContact } from "./enrich";
import { topKeywords } from "./keywords";
import { segmentOf } from "./visibility";

// À qui les questions ont été posées, tel que l'email le dit. ChatGPT n'est nommé que pour des réponses relevées à la main dans ChatGPT.
const MODE_FRAGMENT: Record<string, string> = {
  CHATGPT_MANUAL_OBSERVATION: "ChatGPT",
  CLAUDE_API_WEB_SEARCH: "Claude (API avec recherche web)",
  OPENAI_API_WEB_SEARCH: "un modèle d’OpenAI (API avec recherche web)",
  // Codex n'est pas l'interface ChatGPT : on nomme OpenAI, et on précise seulement que c'est l'éditeur de ChatGPT.
  OPENAI_CODEX_WEB_SEARCH: "un modèle d’OpenAI, l’éditeur de ChatGPT,",
  SIMULATION: "une simulation locale",
};
export const SIGNATURE_URL = "https://organikk.co";

export const contentHash = (subject: string, sentences: DraftSentence[], recipient: string | null) => stableHash({ subject, recipient, sentences: sentences.map((s) => [s.kind, s.text, s.evidence_ids]) });

/** Rassemble les seuls faits vérifiés auxquels le brouillon a le droit de s'adosser. */
export async function buildDraftRequest(deps: Deps, campaign: Campaign, prospect: Prospect, firm: Firm): Promise<{ req: DraftRequest; ctx: ClaimContext; recipient: string | null }> {
  const ev = await deps.db.select().from(schema.evidence).where(eq(schema.evidence.prospect_id, prospect.id));
  const [audit] = await deps.db.select().from(schema.audits).where(eq(schema.audits.prospect_id, prospect.id));
  const kws = await deps.db.select().from(schema.keywords).where(eq(schema.keywords.prospect_id, prospect.id)).orderBy(desc(schema.keywords.business_intent_score), desc(schema.keywords.offer_proximity_score), schema.keywords.keyword);
  const [lawyer] = prospect.lawyer_id ? await deps.db.select().from(schema.lawyers).where(eq(schema.lawyers.id, prospect.lawyer_id)) : [];
  const contact = await selectedContact(deps, firm.id);
  const summary = prospect.visibility_summary as { validRuns: number; window_end: string; provider: string; question_count?: number } | null;

  const facts: Fact[] = [
    ...ev.filter((e) => e.kind === "SERVICE").map((e) => ({ id: `service:${e.id}`, text: `${e.value}. ${e.excerpt}`, values: [e.value] })),
    ...ev.filter((e) => e.kind === "CLIENT_TYPE").map((e) => ({ id: `client:${e.id}`, text: e.excerpt, values: [e.value] })),
    ...ev.filter((e) => e.kind === "PRACTICE_AREA").map((e) => ({ id: `practice:${e.id}`, text: e.excerpt, values: [e.value] })),
    ...(audit ? [{ id: `audit:${audit.id}`, text: `Pré-audit portant sur ${audit.pages_analyzed} pages`, values: [audit.pages_analyzed] }] : []),
  ];
  const auditUrl = audit && deps.publicUrl && !audit.share_revoked ? `${deps.publicUrl.replace(/\/$/, "")}/r/${audit.share_token}` : null;
  // Le constat d'absence n'est permis que si le verdict l'établit sur l'échantillon complet.
  const allowed = prospect.visibility_verdict === "NOT_OBSERVED_IN_SAMPLE" && !!summary;
  const date = summary ? frDate(new Date(summary.window_end)) : "";
  const modeFragment = MODE_FRAGMENT[summary?.provider ?? ""] ?? "";
  const exampleQuery = [...buildBenchmarkPrompts(segmentOf(campaign))].sort((a, b) => a.length - b.length)[0];
  // La pratique est nommée avec les mots du site quand ils sont prouvés, sinon avec ceux de la campagne.
  const practiceFact = ev.find((e) => e.kind === "PRACTICE_AREA");
  const clientPhrase = campaign.config.client_type === "entreprise" ? "les entreprises et dirigeants" : campaign.config.client_type === "particulier" ? "les particuliers" : "";
  // Les deux requêtes mises en avant et leur vérification. Seules les vérifications faites avec l'IA nommée dans l'email comptent.
  const top = await topKeywords(deps, campaign, prospect.id);
  const checkProvider = summary?.provider === "CHATGPT_MANUAL_OBSERVATION" ? "CHATGPT_MANUAL_OBSERVATION" : (summary?.provider ?? "");
  const checks = await deps.db.select().from(schema.keyword_checks).where(eq(schema.keyword_checks.prospect_id, prospect.id));
  const keywordChecks = Object.fromEntries(checks.filter((c) => c.provider === checkProvider && c.result !== "UNVERIFIED").map((c) => [c.keyword, c.result === "CITED"]));
  // Nom court de l'IA pour le paragraphe des requêtes : elle vient d'être présentée dans le constat.
  const keywordCheckWho = ({ CHATGPT_MANUAL_OBSERVATION: "ChatGPT", CLAUDE_API_WEB_SEARCH: "Claude", OPENAI_API_WEB_SEARCH: "ce modèle d’OpenAI", OPENAI_CODEX_WEB_SEARCH: "ce modèle d’OpenAI", SIMULATION: "la simulation" } as Record<string, string>)[checkProvider] ?? "";
  const req: DraftRequest = {
    practice: practiceFact?.value ?? campaign.config.practice_area,
    city: campaign.config.location,
    lawyerLastName: lawyer?.last_name ?? null,
    firmName: firm.name,
    facts,
    visibility: { allowed, validRuns: summary?.validRuns ?? 0, date, modeFragment, exampleQuery, sentence: null },
    keywords: top.map((k) => k.keyword),
    keywordChecks,
    keywordCheckWho,
    keywordCount: kws.length,
    auditUrl,
    auditPages: audit?.pages_analyzed ?? null,
    auditFactId: audit ? `audit:${audit.id}` : null,
    contactSourceUrl: contact?.source_url ?? null,
  };
  const ctx: ClaimContext = {
    verdict: (prospect.visibility_verdict as ClaimContext["verdict"]) ?? null,
    modeFragment,
    sampleDate: date,
    validRuns: summary?.validRuns ?? 0,
    questionCount: summary?.question_count ?? campaign.config.visibility_prompts,
    exampleQuery,
    chatgptObserved: summary?.provider === "CHATGPT_MANUAL_OBSERVATION",
    firmName: firm.name,
    clientPhrase,
    keywordChecks,
    keywordCheckWho,
    keywords: kws.map((k) => k.keyword),
    auditUrl,
    lawyerLastName: lawyer?.last_name ?? null,
    allowedUrls: [SIGNATURE_URL, ...(contact ? [contact.source_url] : [])],
  };
  req.visibility.sentence = visibilityRequired(ctx) ? visibilitySentence(ctx) : null;
  return { req, ctx, recipient: contact?.email ?? null };
}

export async function draftStep(deps: Deps, rt: Runtime, campaign: Campaign, prospect: Prospect, firm: Firm): Promise<void> {
  const { req, ctx, recipient } = await buildDraftRequest(deps, campaign, prospect, firm);
  const template = campaign.config.email_mode !== "model";
  const practiceFact = req.facts.find((f) => f.id.startsWith("practice:"));
  const out = template
    ? renderEmailTemplate(req, ctx, practiceFact?.id ?? null)
    : await withRetry(
        () => metered(deps, { campaignId: campaign.id, prospectId: prospect.id, step: "draft" }, rt.providers.analyst.estimate("draft"), () => rt.providers.analyst.draftEmail(req)),
        { sleep: deps.sleep, random: deps.random },
      );
  out.sentences = frameVisibility(out.sentences, ctx);
  const body = renderBody(out.sentences);
  const values = {
    recipient,
    subject: out.subject,
    sentences: out.sentences,
    body,
    word_count: wordCount(body),
    fact_check: null,
    facts: req.facts,
    claim_context: ctx,
    rewrite_rounds: 0,
    blockers: [],
    content_hash: contentHash(out.subject, out.sentences, recipient),
    prompt_version: `${template ? EMAIL_TEMPLATE_VERSION : rt.providers.analyst.promptVersion}+${CLAIM_RULE_VERSION}`,
    edited_by_human: false,
    updated_at: deps.now(),
  };
  await deps.db.insert(schema.email_drafts).values({ prospect_id: prospect.id, ...values }).onConflictDoUpdate({ target: schema.email_drafts.prospect_id, set: values });
  await setState(deps, prospect, "DRAFT_READY");
}

/**
 * Boucle de contrôle factuel : chaque phrase est rattachée à une preuve ou refusée. Seules les phrases refusées
 * sont réécrites, deux tours au plus ; ensuite l'agent s'arrête et passe la main. Un texte modifié par un humain
 * n'est jamais réécrit par l'agent.
 */
export async function factcheckStep(deps: Deps, rt: Runtime, campaign: Campaign, prospect: Prospect, firm: Firm): Promise<void> {
  const D = schema.email_drafts;
  let [draft] = await deps.db.select().from(D).where(eq(D.prospect_id, prospect.id));
  const { req, ctx, recipient } = await buildDraftRequest(deps, campaign, prospect, firm);
  // Le constat reste la phrase encadrée, quoi qu'ait produit une réécriture. Un texte modifié à la main n'est pas retouché.
  let sentences = draft.edited_by_human ? (draft.sentences as DraftSentence[]) : frameVisibility(draft.sentences as DraftSentence[], ctx);
  let rounds = draft.rewrite_rounds;

  for (;;) {
    const check = checkDraft(draft.subject, sentences, req.facts, ctx);
    const body = renderBody(sentences);
    const blockers = [
      ...(recipient ? [] : ["Aucune adresse publique relevée : pas de destinataire."]),
    ];
    [draft] = await deps.db
      .update(D)
      .set({ sentences, body, word_count: check.wordCount, fact_check: check, rewrite_rounds: rounds, blockers, recipient, claim_context: ctx, facts: req.facts, content_hash: contentHash(draft.subject, sentences, recipient), updated_at: deps.now() })
      .where(eq(D.id, draft.id))
      .returning();
    if (check.ok) {
      await setState(deps, prospect, "READY_FOR_REVIEW");
      return;
    }
    const why = [...check.failed.map((f) => `« ${sentences.find((s) => s.id === f.id)?.text.slice(0, 80)} » : ${f.reason}`), ...check.global].join(" | ");
    // Le gabarit est un texte fixe : s'il échoue, c'est un fait manquant, pas une phrase à réécrire.
    if (draft.edited_by_human || campaign.config.email_mode !== "model" || rounds >= campaign.config.max_email_rewrite_rounds) {
      await sendToReview(deps, prospect, "UNSUPPORTED_CLAIM", why, "DRAFT_READY");
      return;
    }
    if (check.failed.length === 0) {
      // Défaut d'ensemble (longueur, objet, information absente) : aucune phrase à corriger seule, le brouillon est rédigé à nouveau avec la liste des défauts.
      const again = await withRetry(
        () => metered(deps, { campaignId: campaign.id, prospectId: prospect.id, step: "draft" }, rt.providers.analyst.estimate("draft"), () => rt.providers.analyst.draftEmail({ ...req, feedback: check.global })),
        { sleep: deps.sleep, random: deps.random },
      );
      sentences = frameVisibility(again.sentences, ctx);
      rounds += 1;
      [draft] = await deps.db.update(D).set({ subject: again.subject }).where(eq(D.id, draft.id)).returning();
      await logEvent(deps.db, { campaignId: campaign.id, prospectId: prospect.id, type: "EMAIL_REDRAFT_ROUND", data: { round: rounds, defects: check.global } });
      continue;
    }
    const failed = check.failed.map((c) => ({ sentence: sentences.find((s) => s.id === c.id)!, check: c }));
    const { rewrites } = await withRetry(
      () => metered(deps, { campaignId: campaign.id, prospectId: prospect.id, step: "rewrite" }, rt.providers.analyst.estimate("rewrite"), () => rt.providers.analyst.rewriteSentences(req, failed)),
      { sleep: deps.sleep, random: deps.random },
    );
    const failedIds = new Set(failed.map((f) => f.sentence.id));
    // Seules les phrases refusées peuvent changer ; une réécriture visant une autre phrase est ignorée.
    const byId = new Map(rewrites.filter((r) => failedIds.has(r.id)).map((r) => [r.id, r]));
    sentences = sentences.flatMap((s) => {
      const r = byId.get(s.id);
      if (!r) return [s];
      return r.text === null ? [] : [{ ...s, text: r.text, evidence_ids: r.evidence_ids }];
    });
    rounds += 1;
    await logEvent(deps.db, { campaignId: campaign.id, prospectId: prospect.id, type: "EMAIL_REWRITE_ROUND", data: { round: rounds, refused: failed.map((f) => ({ id: f.sentence.id, reason: f.check.reason })) } });
  }
}
