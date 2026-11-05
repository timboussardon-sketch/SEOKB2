import { canonicalDomain, containsPhrase, escapeRegExp, normalize } from "./text";
import type { Verdict } from "./states";

export type ObservationType =
  | "LAWYER_MENTION"
  | "FIRM_MENTION"
  | "OWN_DOMAIN_CITATION"
  | "THIRD_PARTY_CITATION"
  | "AMBIGUOUS_MATCH"
  | "NO_MATCH";

export interface EntityRef {
  targetType: "LAWYER" | "FIRM";
  lawyer?: { firstName: string; lastName: string };
  /** Nom vérifié du cabinet et alias vérifiés. */
  firmNames: string[];
  domain: string | null;
}

export interface Citation {
  url: string;
  title?: string;
}

export interface Observation {
  type: ObservationType;
  detail: string;
}

/** Analyse une réponse déjà produite. L'entité n'entre jamais dans la requête de mesure. */
export function matchEntity(entity: EntityRef, text: string, citations: Citation[]): Observation[] {
  const out: Observation[] = [];
  const t = normalize(text);

  if (entity.lawyer) {
    const first = normalize(entity.lawyer.firstName);
    const last = normalize(entity.lawyer.lastName);
    const full = containsPhrase(t, `${first} ${last}`) || containsPhrase(t, `${last} ${first}`);
    if (full) {
      out.push({ type: "LAWYER_MENTION", detail: `Nom complet « ${entity.lawyer.firstName} ${entity.lawyer.lastName} » présent dans la réponse` });
    } else {
      const l = escapeRegExp(last);
      const other = t.match(new RegExp(`(?:^|[^a-z0-9])(?:maitre|me)\\s+([a-z-]+)\\s+${l}(?:[^a-z0-9]|$)`));
      const bare = new RegExp(`(?:^|[^a-z0-9])(?:maitre|me|cabinet)\\s+${l}(?:[^a-z0-9]|$)`).test(t);
      const firmCovers = entity.firmNames.some((n) => containsPhrase(t, n));
      if (other && other[1] !== first) {
        // Même nom, autre prénom : un homonyme, pas la personne ciblée.
      } else if (bare && !firmCovers) {
        out.push({ type: "AMBIGUOUS_MATCH", detail: `Nom « ${entity.lawyer.lastName} » sans prénom ni cabinet vérifié` });
      }
    }
  }

  for (const name of entity.firmNames) {
    if (name.trim().length >= 4 && containsPhrase(t, name)) {
      out.push({ type: "FIRM_MENTION", detail: `Cabinet « ${name} » présent dans la réponse` });
      break;
    }
  }

  for (const c of citations) {
    const host = canonicalDomain(c.url);
    if (!host) continue;
    if (entity.domain && (host === entity.domain || host.endsWith(`.${entity.domain}`))) {
      out.push({ type: "OWN_DOMAIN_CITATION", detail: c.url });
      continue;
    }
    const title = normalize(c.title ?? "");
    const named =
      (entity.lawyer && containsPhrase(title, `${entity.lawyer.firstName} ${entity.lawyer.lastName}`)) ||
      entity.firmNames.some((n) => n.trim().length >= 4 && containsPhrase(title, n));
    // Une page tierce citée ne vaut présence que si elle nomme l'entité ; reste à vérifier par un humain.
    if (named) out.push({ type: "THIRD_PARTY_CITATION", detail: c.url });
  }

  const seen = new Set<string>();
  const unique = out.filter((o) => (seen.has(o.type) ? false : (seen.add(o.type), true)));
  return unique.length ? unique : [{ type: "NO_MATCH", detail: "" }];
}

export interface VerdictInput {
  targetType: "LAWYER" | "FIRM";
  expectedValidRuns: number;
  /** Observations des seules réponses valides, une entrée par réponse. */
  validRuns: Observation[][];
}

export interface VerdictResult {
  verdict: Verdict;
  validRuns: number;
  lawyerMentions: number;
  firmMentions: number;
  ownDomainCitations: number;
  thirdPartyCitations: number;
  ambiguous: number;
  reason: string;
}

export function computeVerdict(input: VerdictInput): VerdictResult {
  const count = (type: ObservationType) => input.validRuns.filter((obs) => obs.some((o) => o.type === type)).length;
  const base = {
    validRuns: input.validRuns.length,
    lawyerMentions: count("LAWYER_MENTION"),
    firmMentions: count("FIRM_MENTION"),
    ownDomainCitations: count("OWN_DOMAIN_CITATION"),
    thirdPartyCitations: count("THIRD_PARTY_CITATION"),
    ambiguous: count("AMBIGUOUS_MATCH"),
  };
  const firmPresence = base.firmMentions + base.ownDomainCitations > 0;

  if (input.targetType === "LAWYER" && base.lawyerMentions > 0) {
    return { ...base, verdict: "OBSERVED", reason: "Avocat nommé dans au moins une réponse valide" };
  }
  if (input.targetType === "FIRM" && firmPresence) {
    return { ...base, verdict: "OBSERVED", reason: "Cabinet nommé ou site cité dans au moins une réponse valide" };
  }
  if (input.targetType === "LAWYER" && firmPresence) {
    return { ...base, verdict: "FIRM_ONLY", reason: "Cabinet ou site observé, avocat non identifié" };
  }
  if (base.ambiguous > 0) return { ...base, verdict: "INCONCLUSIVE", reason: "Correspondance ambiguë à départager" };
  if (base.thirdPartyCitations > 0) {
    return { ...base, verdict: "INCONCLUSIVE", reason: "Source tierce citée qui nomme l'entité, à vérifier" };
  }
  if (base.validRuns < input.expectedValidRuns) {
    return { ...base, verdict: "INCONCLUSIVE", reason: `Échantillon incomplet : ${base.validRuns} réponses valides sur ${input.expectedValidRuns}` };
  }
  return { ...base, verdict: "NOT_OBSERVED_IN_SAMPLE", reason: `Aucune présence dans ${base.validRuns} réponses valides` };
}

export type RunValidity = "VALID" | "ERROR" | "REFUSED" | "UNUSABLE" | "NO_WEB_SEARCH";

/** Critères de validité fixés avant exécution. Une réponse non valide n'est jamais comptée comme une absence. */
export function assessRun(r: { text: string; webSearchUsed: boolean; requireWebSearch: boolean }): { validity: RunValidity; note: string } {
  const t = normalize(r.text);
  if (t.length < 200) return { validity: "UNUSABLE", note: "Réponse vide ou trop courte" };
  if (/^(je ne peux pas|je ne suis pas en mesure|desole|je regrette)/.test(t) && !/cabinet|maitre/.test(t)) {
    return { validity: "REFUSED", note: "Refus de répondre" };
  }
  if (!/avocat|cabinet/.test(t)) return { validity: "UNUSABLE", note: "Réponse hors sujet : aucun prestataire évoqué" };
  if (r.requireWebSearch && !r.webSearchUsed) return { validity: "NO_WEB_SEARCH", note: "Recherche web non utilisée" };
  return { validity: "VALID", note: "" };
}
