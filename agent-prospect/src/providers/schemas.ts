import { z } from "zod";

export const QuoteZ = z.object({ value: z.string(), source_url: z.string(), excerpt: z.string() });
export const ProfileZ = z.object({
  firm_name: QuoteZ.nullable(),
  lawyers: z.array(z.object({ first_name: z.string(), last_name: z.string(), source_url: z.string(), excerpt: z.string() })),
  cities: z.array(QuoteZ),
  practice_areas: z.array(QuoteZ.extend({ matches_target: z.boolean() })),
  client_types: z.array(QuoteZ.extend({ value: z.enum(["entreprise", "particulier"]) })),
  services: z.array(QuoteZ),
  certification_claims: z.array(QuoteZ),
});
export const KeywordZ = z.object({
  keyword: z.string(),
  cluster: z.string(),
  service_evidence_id: z.string(),
  client_type: z.enum(["entreprise", "particulier", "mixte"]),
  search_intent: z.string(),
  business_rationale: z.string(),
  existing_page_url: z.string().nullable(),
  recommended_page_type: z.string(),
  recommendation: z.enum(["POUSSER", "CRÉER", "CONSOLIDER", "ÉCARTER", "À_VALIDER"]),
});
export const KINDS = ["GREETING", "OBSERVATION", "VISIBILITY", "KEYWORDS", "AUDIT_LINK", "CTA", "TRANSPARENCY", "SIGNATURE"] as const;
export const SentenceZ = z.object({ kind: z.enum(KINDS), text: z.string(), evidence_ids: z.array(z.string()) });

