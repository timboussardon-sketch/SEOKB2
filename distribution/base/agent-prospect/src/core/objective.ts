import { z } from "zod";
import { GOAL_TYPES } from "./states";

export const CampaignConfigSchema = z.object({
  practice_area: z.string().min(3),
  subspecialties: z.array(z.string().min(2)).default([]),
  location: z.string().min(2),
  client_type: z.enum(["entreprise", "particulier", "mixte"]).default("mixte"),
  target_type: z.enum(["LAWYER", "FIRM"]).default("FIRM"),
  certified_specialization_required: z.boolean().default(false),
  goal_type: z.enum(GOAL_TYPES).default("EMAIL_READY_PROSPECTS"),
  target_count: z.number().int().min(1).max(200).default(10),
  visibility_mode: z.enum(["CLAUDE_API_WEB_SEARCH", "OPENAI_API_WEB_SEARCH", "OPENAI_CODEX_WEB_SEARCH", "SIMULATION"]).default("CLAUDE_API_WEB_SEARCH"),
  visibility_prompts: z.number().int().min(1).max(5).default(5),
  visibility_repetitions: z.number().int().min(1).max(5).default(3),
  max_visibility_retries_per_run: z.number().int().min(0).max(3).default(2),
  generate_audit_if: z.enum(["NOT_OBSERVED_IN_SAMPLE", "NEVER"]).default("NOT_OBSERVED_IN_SAMPLE"),
  generate_keywords: z.boolean().default(true),
  generate_email: z.boolean().default(true),
  /** template : message type fixe rempli avec les faits. model : rédaction par le modèle, puis contrôle factuel. */
  email_mode: z.enum(["template", "model"]).default("template"),
  /** Aucun envoi dans cette version : la valeur ne peut être que false. */
  send_email: z.literal(false).default(false),
  max_discovery_rounds: z.number().int().min(1).max(20).default(6),
  max_candidates_per_round: z.number().int().min(1).max(50).default(20),
  max_total_discovery_results: z.number().int().min(1).max(600).default(120),
  max_empty_rounds: z.number().int().min(1).max(5).default(2),
  // 10 pages par site : assez pour qualifier et auditer, sans solliciter le site plus que nécessaire.
  max_crawl_pages_per_site: z.number().int().min(1).max(20).default(10),
  max_keyword_rounds: z.number().int().min(1).max(2).default(2),
  max_email_rewrite_rounds: z.number().int().min(0).max(2).default(2),
  max_campaign_cost_usd: z.number().min(0).max(500).default(10),
  max_prospect_cost_usd: z.number().min(0).max(20).default(2),
  excluded_domains: z.array(z.string()).default([]),
});
export type CampaignConfig = z.infer<typeof CampaignConfigSchema>;

export interface ParsedObjective {
  draft: Partial<CampaignConfig>;
  missing: string[];
  notes: string[];
}

const NUMBER_WORDS: Record<string, number> = { cinq: 5, dix: 10, quinze: 15, vingt: 20, trente: 30, quarante: 40, cinquante: 50 };

/**
 * Lecture déterministe d'une commande en texte libre. Elle propose une configuration à confirmer ;
 * elle ne peut ni activer l'envoi ni toucher aux budgets, quel que soit le texte.
 */
export function parseObjective(text: string): ParsedObjective {
  const draft: Partial<CampaignConfig> = {};
  const missing: string[] = [];
  const notes: string[] = [];
  const t = text.replace(/\s+/g, " ").trim();

  const num = t.match(/(\d{1,3})\s+(avocats?|cabinets?)/i);
  const word = t.match(new RegExp(`\\b(${Object.keys(NUMBER_WORDS).join("|")})\\s+(avocats?|cabinets?)`, "i"));
  if (num) draft.target_count = Number(num[1]);
  else if (word) draft.target_count = NUMBER_WORDS[word[1].toLowerCase()];
  else missing.push("target_count");
  const unit = (num?.[2] ?? word?.[2] ?? "").toLowerCase();
  if (unit) draft.target_type = unit.startsWith("cabinet") ? "FIRM" : "LAWYER";

  const practice = t.match(/\b(droit (?:du |de la |de l['’]|des |d['’])?[a-zàâçéèêëîïôûùüœ' -]+?)(?=\s+(?:à|a|sur|qui|et|pour)\s|[.,;]|$)/i);
  if (practice) draft.practice_area = practice[1].trim().toLowerCase();
  else missing.push("practice_area");

  const city = t.match(/(?:^|\s)(?:à|sur)\s+((?:[A-ZÉÈ][\wéèêàçîïôû'’-]+)(?:[ -](?:[A-ZÉÈ][\wéèêàçîïôû'’-]+|sur|en|la|le|les|de))*)/);
  if (city) draft.location = city[1].trim();
  else missing.push("location");

  const business = /employeurs?|entreprises?|dirigeants?|sociétés?/i.test(t);
  const individual = /salariés?|particuliers?|justiciables?/i.test(t);
  draft.client_type = business && !individual ? "entreprise" : individual && !business ? "particulier" : "mixte";

  draft.generate_keywords = /mots?[- ]cl[ée]s?/i.test(t);
  draft.generate_email = /e-?mails?|courriels?|messages?/i.test(t);
  draft.generate_audit_if = /audit/i.test(t) || draft.generate_keywords || draft.generate_email ? "NOT_OBSERVED_IN_SAMPLE" : "NEVER";
  draft.goal_type = draft.generate_email ? "EMAIL_READY_PROSPECTS" : draft.generate_audit_if === "NEVER" ? "QUALIFIED_PROSPECTS" : "AUDITED_PROSPECTS";
  draft.send_email = false;

  if (/\benvo(ie|yer|i)\b/i.test(t) && !/ne (rien|pas|les) .{0,20}envo|sans .{0,10}envo|n['’]envoie/i.test(t)) {
    notes.push("La commande évoque un envoi. Aucun envoi n'est activé par un texte libre : la campagne s'arrête aux brouillons.");
  }
  if (/budget|plafond|\$|€|usd|euros?/i.test(t)) {
    notes.push("Les budgets ne se règlent pas par texte libre : les plafonds par défaut s'appliquent et se modifient dans le formulaire.");
  }
  return { draft, missing, notes };
}
