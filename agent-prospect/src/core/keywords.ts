import { normalize, tokens } from "./text";

export const KEYWORD_SCORING_VERSION = "kw-score-v1";

export interface ServiceRef {
  evidenceId: string;
  label: string;
  url: string;
}

export interface KeywordCandidate {
  keyword: string;
  cluster: string;
  service_evidence_id: string;
  client_type: "entreprise" | "particulier" | "mixte";
  search_intent: string;
  business_rationale: string;
  existing_page_url: string | null;
  recommended_page_type: string;
  recommendation: "POUSSER" | "CRÉER" | "CONSOLIDER" | "ÉCARTER" | "À_VALIDER";
}

export interface ScoredKeyword extends KeywordCandidate {
  relevant_service: string;
  geography: string | null;
  offer_proximity_score: number;
  business_intent_score: number;
  feasibility_score: null;
  search_volume: null;
  cpc: null;
  keyword_difficulty: null;
  position: null;
  normalized: string;
}

export interface Rejected {
  keyword: string;
  reason: "UNKNOWN_SERVICE" | "WRONG_CLIENT_TYPE" | "LOW_OFFER_PROXIMITY" | "LOW_BUSINESS_INTENT" | "DUPLICATE" | "DISCARDED_BY_PROPOSAL" | "OVER_LIMIT";
}

const STOP = new Set(["de", "du", "des", "la", "le", "les", "un", "une", "en", "a", "au", "aux", "pour", "et", "d", "l", "sur", "par", "avec", "droit"]);
const significant = (s: string) => tokens(s).filter((w) => !STOP.has(w) && w.length > 2);

const BUSINESS_WORDS = /\b(employeurs?|entreprises?|dirigeants?|societes?|drh|pme)\b/;
const INDIVIDUAL_WORDS = /\b(salaries?|particuliers?|locataires?)\b/;

/** Grille interne 0–5 : proximité entre la requête et l'offre vérifiée sur le site. Ce n'est pas une mesure Google. */
export function offerProximity(k: KeywordCandidate, service: ServiceRef, city: string, clientTypes: string[]): number {
  let score = 2; // la prestation citée existe et porte une preuve
  const kw = new Set(significant(k.keyword));
  if (significant(service.label).some((w) => kw.has(w))) score += 1;
  if (normalize(k.keyword).includes(normalize(city))) score += 1;
  if (k.client_type === "mixte" || clientTypes.includes(k.client_type)) score += 1;
  return score;
}

/** Grille interne 0–5 : la recherche peut-elle mener à une prise de contact ? */
export function businessIntent(keyword: string, city: string): number {
  const k = normalize(keyword);
  if (/\b(definition|c est quoi|qu est ce|signification|exemple de|modele de)\b/.test(k)) return 1;
  const provider = /\b(avocats?|cabinets?)\b/.test(k);
  const local = k.includes(normalize(city));
  if (provider && local) return 5;
  if (provider || /\b(consultation|honoraires|tarifs?|prix|devis|rendez vous)\b/.test(k)) return 4;
  if (/\b(contester|procedure|assigner|saisir|negocier|rediger|securiser|accompagnement|conseil|defense|litige|contentieux|recours)\b/.test(k)) return 3;
  return 2;
}

export interface FilterInput {
  candidates: KeywordCandidate[];
  services: ServiceRef[];
  city: string;
  /** Clientèles vérifiées sur le site. */
  clientTypes: ("entreprise" | "particulier")[];
  alreadyKept: ScoredKeyword[];
  limit: number;
}

export function filterKeywords(input: FilterInput): { kept: ScoredKeyword[]; rejected: Rejected[] } {
  const byId = new Map(input.services.map((s) => [s.evidenceId, s]));
  const seen = new Set(input.alreadyKept.map((k) => k.normalized));
  const scored: ScoredKeyword[] = [];
  const rejected: Rejected[] = [];

  for (const c of input.candidates) {
    const service = byId.get(c.service_evidence_id);
    if (!service) {
      rejected.push({ keyword: c.keyword, reason: "UNKNOWN_SERVICE" });
      continue;
    }
    if (c.recommendation === "ÉCARTER") {
      rejected.push({ keyword: c.keyword, reason: "DISCARDED_BY_PROPOSAL" });
      continue;
    }
    const k = normalize(c.keyword);
    const onlyBusiness = input.clientTypes.length > 0 && !input.clientTypes.includes("particulier");
    const onlyIndividual = input.clientTypes.length > 0 && !input.clientTypes.includes("entreprise");
    if ((onlyBusiness && (INDIVIDUAL_WORDS.test(k) || c.client_type === "particulier")) || (onlyIndividual && (BUSINESS_WORDS.test(k) || c.client_type === "entreprise"))) {
      rejected.push({ keyword: c.keyword, reason: "WRONG_CLIENT_TYPE" });
      continue;
    }
    const proximity = offerProximity(c, service, input.city, input.clientTypes);
    const intent = businessIntent(c.keyword, input.city);
    if (proximity < 3) {
      rejected.push({ keyword: c.keyword, reason: "LOW_OFFER_PROXIMITY" });
      continue;
    }
    if (intent < 3) {
      rejected.push({ keyword: c.keyword, reason: "LOW_BUSINESS_INTENT" });
      continue;
    }
    const normalized = significant(c.keyword).sort().join(" ");
    if (!normalized || seen.has(normalized)) {
      rejected.push({ keyword: c.keyword, reason: "DUPLICATE" });
      continue;
    }
    seen.add(normalized);
    scored.push({
      ...c,
      relevant_service: service.label,
      geography: k.includes(normalize(input.city)) ? input.city : null,
      // Les variantes d'une même intention partagent la page de la prestation.
      existing_page_url: c.existing_page_url ?? service.url,
      offer_proximity_score: proximity,
      business_intent_score: intent,
      feasibility_score: null,
      search_volume: null,
      cpc: null,
      keyword_difficulty: null,
      position: null,
      normalized,
    });
  }

  scored.sort((a, b) => b.business_intent_score + b.offer_proximity_score - (a.business_intent_score + a.offer_proximity_score) || a.keyword.localeCompare(b.keyword));
  const room = Math.max(0, input.limit - input.alreadyKept.length);
  for (const s of scored.slice(room)) rejected.push({ keyword: s.keyword, reason: "OVER_LIMIT" });
  return { kept: scored.slice(0, room), rejected };
}

/** Prestations encore peu couvertes, pour cibler un second tour au lieu de tout régénérer. */
export function underCoveredServices(services: ServiceRef[], kept: ScoredKeyword[], minPerService = 2): ServiceRef[] {
  return services.filter((s) => kept.filter((k) => k.service_evidence_id === s.evidenceId).length < minPerService);
}

export interface RankableKeyword {
  keyword: string;
  cluster: string;
  relevant_service: string;
  geography: string | null;
  offer_proximity_score: number;
  business_intent_score: number;
}

/**
 * Les deux requêtes à mettre en avant : intention business d'abord, puis proximité avec la spécialité visée
 * (mots de la pratique dans la requête ou dans la prestation), clientèle visée, ville. Deux groupes différents si possible.
 * Classement déterministe : mêmes données, même choix.
 */
export function pickTopKeywords<K extends RankableKeyword>(rows: K[], practices: string[], clientType: "entreprise" | "particulier" | "mixte", count = 2): K[] {
  const terms = [...new Set(practices.flatMap(significant))];
  const score = (k: K) => {
    const kw = normalize(k.keyword);
    const inKeyword = terms.some((t) => kw.includes(t));
    const inService = terms.some((t) => normalize(k.relevant_service).includes(t));
    const client = clientType === "entreprise" ? BUSINESS_WORDS.test(kw) : clientType === "particulier" ? INDIVIDUAL_WORDS.test(kw) : false;
    return k.business_intent_score * 10 + k.offer_proximity_score * 5 + (inKeyword ? 8 : inService ? 4 : 0) + (client ? 3 : 0) + (k.geography ? 2 : 0);
  };
  const ranked = [...rows].sort((a, b) => score(b) - score(a) || a.keyword.length - b.keyword.length || a.keyword.localeCompare(b.keyword));
  const out: K[] = [];
  for (const k of ranked) if (out.length < count && !out.some((o) => o.cluster === k.cluster)) out.push(k);
  for (const k of ranked) if (out.length < count && !out.includes(k)) out.push(k);
  return out;
}
