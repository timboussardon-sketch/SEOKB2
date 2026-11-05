import { stableHash } from "./text";

export const BENCHMARK_PROMPT_VERSION = "bench-v1";

export interface Segment {
  practice: string;
  clientType: "entreprise" | "particulier" | "mixte";
  city: string;
}

const CLIENT = {
  entreprise: { self: "dirigeant d'entreprise", plural: "les entreprises", side: "côté employeur ou entreprise" },
  particulier: { self: "un particulier", plural: "les particuliers", side: "côté particulier" },
  mixte: { self: "à la recherche d'un conseil", plural: "les entreprises et les particuliers", side: "" },
} as const;

/** Cinq formulations de recherche de prestataire. Aucun nom, domaine ou détail distinctif d'un prospect n'y figure. */
export function buildBenchmarkPrompts(s: Segment): string[] {
  const c = CLIENT[s.clientType];
  return [
    `Quel avocat contacter à ${s.city} pour un dossier de ${s.practice}${c.side ? ` ${c.side}` : ""} ?`,
    `Je suis ${c.self} et je cherche un avocat en ${s.practice} à ${s.city}. Quels cabinets examiner ?`,
    `Quels cabinets d'avocats accompagnent ${c.plural} en ${s.practice} à ${s.city} ?`,
    `Je dois choisir un avocat en ${s.practice} à ${s.city}. Qui consulter quand on est ${c.self} ?`,
    `Peux-tu me citer des avocats en ${s.practice} à ${s.city} qui travaillent avec ${c.plural} ?`,
  ];
}

export function benchmarkConfigHash(input: {
  segment: Segment;
  provider: string;
  model: string;
  params: unknown;
  prompts: number;
  repetitions: number;
}): string {
  return stableHash({ ...input, promptVersion: BENCHMARK_PROMPT_VERSION });
}

export const VISIBILITY_MODE_LABELS: Record<string, string> = {
  CLAUDE_API_WEB_SEARCH: "Test via l’API Claude avec recherche web",
  OPENAI_API_WEB_SEARCH: "Test via l’API OpenAI avec recherche web",
  OPENAI_CODEX_WEB_SEARCH: "Test via Codex (modèle d’OpenAI, compte ChatGPT) avec recherche web",
  CHATGPT_MANUAL_OBSERVATION: "Réponses relevées à la main dans ChatGPT",
  SIMULATION: "Simulation locale (données fictives, aucun appel réel)",
};
