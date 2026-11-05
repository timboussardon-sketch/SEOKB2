import type { Segment } from "./benchmark";

export const QUERY_RULE_VERSION = "queries-v1";

export interface DiscoveryQuery {
  family: string;
  query: string;
}

const CLIENT_TERMS: Record<Segment["clientType"], string[]> = {
  entreprise: ["entreprise", "employeur"],
  particulier: ["particulier"],
  mixte: [""],
};

/**
 * Familles de formulations pour trouver des candidats. Elles servent à découvrir :
 * la pratique et la clientèle sont ensuite vérifiées sur le site, jamais déduites de la requête.
 */
export function buildDiscoveryQueries(input: { practice: string; subspecialties: string[]; clientType: Segment["clientType"]; city: string }): DiscoveryQuery[] {
  const out: DiscoveryQuery[] = [];
  const terms = CLIENT_TERMS[input.clientType];
  const topics = [input.practice, ...input.subspecialties];
  const add = (family: string, query: string) => {
    const q = query.replace(/\s+/g, " ").trim();
    if (!out.some((o) => o.query === q)) out.push({ family, query: q });
  };
  for (const topic of topics) {
    for (const term of terms) {
      add("avocat+pratique+ville", `avocat ${topic} ${term} ${input.city}`);
      add("cabinet+pratique+ville", `cabinet d'avocats ${topic} ${term} ${input.city}`);
    }
  }
  for (const topic of topics) {
    add("contentieux", `avocat contentieux ${topic} ${terms[0]} ${input.city}`);
    add("conseil", `avocat conseil ${topic} ${terms[0]} ${input.city}`);
    add("annuaire", `liste avocats ${topic} barreau de ${input.city}`);
  }
  return out;
}
