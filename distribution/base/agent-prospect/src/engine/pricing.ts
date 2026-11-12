import { AppError } from "../core/errors";
import type { CallEstimate, Usage } from "../providers/types";

export interface ModelPrice {
  input_per_mtok: number;
  output_per_mtok: number;
  web_search_per_call: number;
}

export type PriceTable = Record<string, ModelPrice>;

/** Le mode simulation n'émet aucun appel facturé : son prix nul est déclaré, pas supposé. */
export const SIMULATION_PRICES: PriceTable = { simulation: { input_per_mtok: 0, output_per_mtok: 0, web_search_per_call: 0 } };

/**
 * Tarifs de l'API Claude relevés le 2026-10-01 sur platform.claude.com/docs/en/about-claude/pricing :
 * prix par million de tokens, et recherche web à 10 $ les 1 000 recherches. PRICING_JSON les remplace s'ils changent.
 * Opus 5 et Opus 4.8 y figurent parce qu'une requête refusée par Opus 5.5 peut être reprise par l'un d'eux.
 */
export const CLAUDE_PRICES: PriceTable = {
  "claude-opus-5-5": { input_per_mtok: 4, output_per_mtok: 20, web_search_per_call: 0.01 },
  "claude-opus-5": { input_per_mtok: 5, output_per_mtok: 25, web_search_per_call: 0.01 },
  "claude-opus-4-8": { input_per_mtok: 5, output_per_mtok: 25, web_search_per_call: 0.01 },
  "claude-sonnet-5-5": { input_per_mtok: 2, output_per_mtok: 10, web_search_per_call: 0.01 },
  "claude-haiku-4-5": { input_per_mtok: 1, output_per_mtok: 5, web_search_per_call: 0.01 },
};

export function loadPriceTable(json: string | undefined): PriceTable {
  if (!json) return { ...SIMULATION_PRICES, ...CLAUDE_PRICES };
  try {
    return { ...SIMULATION_PRICES, ...CLAUDE_PRICES, ...(JSON.parse(json) as PriceTable) };
  } catch {
    throw new AppError("INVALID_INPUT", "PRICING_JSON illisible");
  }
}

/** Tarif inconnu : on suspend. Un coût nul n'est jamais inventé. */
export function priceOf(table: PriceTable, u: CallEstimate | Usage): number {
  // Codex tourne sur le forfait ChatGPT : aucun coût à l'appel. La consommation du forfait n'est pas chiffrée ici.
  if (u.model.startsWith("codex:")) return 0;
  // Claude par `claude -p` tourne sur le forfait Max : aucun coût à l'appel non plus.
  if (u.model.startsWith("max:")) return 0;
  const p = table[u.model];
  if (!p || ![p.input_per_mtok, p.output_per_mtok, p.web_search_per_call].every((x) => typeof x === "number" && x >= 0)) {
    throw new AppError("PRICING_UNKNOWN", `Tarif inconnu pour le modèle « ${u.model} » : renseignez PRICING_JSON.`);
  }
  return (u.input_tokens * p.input_per_mtok + u.output_tokens * p.output_per_mtok) / 1_000_000 + u.web_search_calls * p.web_search_per_call;
}
