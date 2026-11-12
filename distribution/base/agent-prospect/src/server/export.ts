import { eq, inArray } from "drizzle-orm";
import { VISIBILITY_MODE_LABELS } from "../core/benchmark";
import type { Db } from "../db/client";
import { schema } from "../db/client";

export const PROSPECT_COLUMNS = [
  "prospect_id", "lawyer_name", "firm_name", "website", "city", "practice_area", "subspecialties", "client_type", "email", "email_source_url", "email_validation_status",
  "certification_status", "visibility_provider", "tested_at", "valid_runs", "mention_count", "firm_mention_count", "owned_domain_citation_count", "visibility_verdict",
  "audit_status", "audit_url", "keyword_count", "top_3_keywords", "email_subject", "draft_status", "delivery_status", "last_error", "simulation",
];
export const KEYWORD_COLUMNS = [
  "prospect_id", "keyword", "cluster", "search_intent", "client_type", "relevant_service", "service_evidence_id", "geography", "existing_page_url", "recommended_page_type",
  "business_rationale", "observed_demand_signals", "source_urls", "recommendation_status", "offer_proximity_score", "business_intent_score", "feasibility_score", "search_volume", "cpc", "keyword_difficulty", "position", "confidence_notes",
];

export async function exportProspects(db: Db, campaignId: string, publicUrl: string | null) {
  const [c] = await db.select().from(schema.campaigns).where(eq(schema.campaigns.id, campaignId));
  if (!c) return null;
  const prospects = await db.select().from(schema.prospects).where(eq(schema.prospects.campaign_id, campaignId));
  const ids = prospects.map((p) => p.id);
  const firmIds = prospects.map((p) => p.firm_id);
  const pick = async <T,>(q: Promise<T[]>) => (ids.length ? q : Promise.resolve([] as T[]));
  const firms = await pick(db.select().from(schema.firms).where(inArray(schema.firms.id, firmIds)));
  const lawyers = await pick(db.select().from(schema.lawyers).where(inArray(schema.lawyers.firm_id, firmIds)));
  const contacts = await pick(db.select().from(schema.contacts).where(inArray(schema.contacts.firm_id, firmIds)));
  const audits = await pick(db.select().from(schema.audits).where(inArray(schema.audits.prospect_id, ids)));
  const drafts = await pick(db.select().from(schema.email_drafts).where(inArray(schema.email_drafts.prospect_id, ids)));
  const kws = await pick(db.select().from(schema.keywords).where(inArray(schema.keywords.prospect_id, ids)));
  const ev = await pick(db.select().from(schema.evidence).where(inArray(schema.evidence.prospect_id, ids)));

  const rows = prospects.map((p) => {
    const firm = firms.find((f) => f.id === p.firm_id);
    const lawyer = lawyers.find((l) => l.id === p.lawyer_id);
    const contact = contacts.find((x) => x.firm_id === p.firm_id && x.selected);
    const audit = audits.find((a) => a.prospect_id === p.id);
    const draft = drafts.find((d) => d.prospect_id === p.id);
    const mine = kws.filter((k) => k.prospect_id === p.id).sort((a, b) => b.business_intent_score + b.offer_proximity_score - a.business_intent_score - a.offer_proximity_score);
    const s = p.visibility_summary as { provider: string; window_end: string; validRuns: number; lawyerMentions: number; firmMentions: number; ownDomainCitations: number } | null;
    const validation = contact ? ["publié", "syntaxe valide", contact.domain_routable === true ? "domaine routable" : contact.domain_routable === false ? "domaine non routable" : "routage non contrôlé", "réception non vérifiée"].join(" ; ") : "";
    return {
      prospect_id: p.id,
      lawyer_name: lawyer ? `${lawyer.first_name} ${lawyer.last_name}` : "",
      firm_name: firm?.name ?? p.candidate_name ?? "",
      website: firm?.website ?? "",
      city: firm?.city ?? "",
      practice_area: ev.filter((e) => e.prospect_id === p.id && e.kind === "PRACTICE_AREA").map((e) => e.value),
      subspecialties: ev.filter((e) => e.prospect_id === p.id && e.kind === "SERVICE").map((e) => e.value),
      client_type: ev.filter((e) => e.prospect_id === p.id && e.kind === "CLIENT_TYPE").map((e) => e.value),
      email: contact?.email ?? (p.email_status === "NO_PUBLIC_EMAIL" ? "NO_PUBLIC_EMAIL" : ""),
      email_source_url: contact?.source_url ?? "",
      email_validation_status: validation,
      certification_status: lawyer?.certified_specialization_status ?? "NOT_VERIFIED",
      visibility_provider: s ? VISIBILITY_MODE_LABELS[s.provider] : "",
      tested_at: s?.window_end ?? "",
      valid_runs: s?.validRuns ?? "",
      mention_count: s?.lawyerMentions ?? "",
      firm_mention_count: s?.firmMentions ?? "",
      owned_domain_citation_count: s?.ownDomainCitations ?? "",
      visibility_verdict: p.visibility_verdict ?? "",
      audit_status: audit ? "DONE" : "",
      audit_url: audit && publicUrl && !audit.share_revoked ? `${publicUrl.replace(/\/$/, "")}/r/${audit.share_token}` : "",
      keyword_count: p.keyword_count ?? "",
      top_3_keywords: mine.slice(0, 3).map((k) => k.keyword),
      email_subject: draft?.subject ?? "",
      draft_status: p.state,
      // Aucun envoi n'existe dans cette version.
      delivery_status: "NOT_SENT",
      last_error: p.last_error ? JSON.stringify(p.last_error) : (p.qualification_detail ?? ""),
      simulation: c.simulation ? "SIMULATION" : "",
    };
  });
  const keywords = kws.map((k) => ({ ...k, observed_demand_signals: "", source_urls: k.existing_page_url ?? "", confidence_notes: "Grille interne, pas une mesure Google. Aucune demande démontrée." }));
  return { campaign: c, rows, keywords };
}
