import { and, eq, inArray, isNotNull } from "drizzle-orm";
import { BENCHMARK_PROMPT_VERSION, buildBenchmarkPrompts } from "../core/benchmark";
import { AppError } from "../core/errors";
import { stableHash } from "../core/text";
import { assessRun } from "../core/verdict";
import { schema } from "../db/client";
import { startCampaign } from "./campaign";
import type { Campaign, Deps } from "./deps";
import { logEvent } from "./events";
import { segmentOf } from "./steps/visibility";

export interface ManualObservations {
  /** responses[question][répétition] : texte de la réponse copiée depuis ChatGPT. */
  responses: string[][];
  /** Modèle affiché dans ChatGPT, ou null s'il n'a pas été noté. */
  modelShown: string | null;
  webSearch: "oui" | "non" | "inconnu";
  observedAt: Date;
}

export const manualPrompts = (campaign: Campaign) => buildBenchmarkPrompts(segmentOf(campaign)).slice(0, campaign.config.visibility_prompts);

const urlsOf = (text: string) => [...new Set([...text.matchAll(/https?:\/\/[^\s)\]»"']+/g)].map((m) => m[0].replace(/[.,;:]+$/, "")))].map((url) => ({ url }));

/**
 * Enregistre des réponses réellement obtenues dans ChatGPT, collées à la main. Rien n'est automatisé côté ChatGPT.
 * Ce qui n'a pas été noté (modèle, recherche web, localisation, personnalisation) est enregistré comme inconnu.
 * Les prospects déjà enrichis repassent ensuite par la mesure, sur ces réponses.
 */
export async function importManualObservations(deps: Deps, campaignId: string, input: ManualObservations): Promise<{ benchmarkId: string; valid: number; expected: number; invalid: string[]; reset: number }> {
  const [campaign] = await deps.db.select().from(schema.campaigns).where(eq(schema.campaigns.id, campaignId));
  if (!campaign) throw new AppError("INVALID_INPUT", "Campagne introuvable");
  const prompts = manualPrompts(campaign);
  const reps = input.responses[0]?.length ?? 0;
  if (input.responses.length !== prompts.length || reps < 1 || reps > 3 || input.responses.some((r) => r.length !== reps || r.some((t) => !t.trim()))) {
    throw new AppError("INVALID_INPUT", `Il faut une réponse par question et par passage : ${prompts.length} questions, le même nombre de réponses pour chacune (1 à 3).`);
  }
  const B = schema.visibility_benchmarks;
  const R = schema.visibility_runs;
  const params = { saisie: "manuelle", recherche_web: input.webSearch, localisation: "inconnue", personnalisation: "inconnue" };
  const [bench] = await deps.db
    .insert(B)
    .values({
      campaign_id: campaign.id,
      config_hash: stableHash({ manual: true, at: input.observedAt.toISOString(), n: deps.now().getTime() }),
      segment: segmentOf(campaign),
      provider: "CHATGPT_MANUAL_OBSERVATION",
      model: input.modelShown?.trim() || "inconnu",
      params,
      prompt_version: BENCHMARK_PROMPT_VERSION,
      prompts,
      repetitions: reps,
      expected_valid_runs: prompts.length * reps,
      started_at: input.observedAt,
    })
    .returning();
  let valid = 0;
  const invalid: string[] = [];
  for (const [p, texts] of input.responses.entries()) {
    for (const [i, text] of texts.entries()) {
      // La recherche web n'est pas exigée : dans ChatGPT, on ne sait pas toujours si elle a servi.
      const v = assessRun({ text, webSearchUsed: input.webSearch === "oui", requireWebSearch: false });
      if (v.validity === "VALID") valid++;
      else invalid.push(`Question ${p + 1}, réponse ${i + 1} : ${v.note}`);
      await deps.db.insert(R).values({ benchmark_id: bench.id, prompt_index: p, repetition: i + 1, attempt: 1, prompt: prompts[p], response_text: text.trim(), citations: urlsOf(text), web_search_used: input.webSearch === "inconnu" ? null : input.webSearch === "oui", model: bench.model, validity: v.validity, validity_note: v.note });
    }
  }
  await deps.db.update(B).set({ valid_runs: valid, status: valid >= bench.expected_valid_runs ? "COMPLETE" : "INCOMPLETE", finished_at: input.observedAt }).where(eq(B.id, bench.id));

  // Les prospects qualifiés et enrichis repartent de la mesure. Audit et mots-clés déjà faits ne sont pas refaits ; le brouillon est rédigé à nouveau.
  const P = schema.prospects;
  const rows = await deps.db.select().from(P).where(and(eq(P.campaign_id, campaign.id), eq(P.qualification_status, "QUALIFIED"), isNotNull(P.email_status)));
  const ids = rows.filter((p) => !["REJECTED", "SUPPRESSED"].includes(p.state)).map((p) => p.id);
  if (ids.length) {
    await deps.db.update(P).set({ state: "ENRICHED", review_reason: null, resume_state: null, force_audit: false, updated_at: deps.now() }).where(inArray(P.id, ids));
    await deps.db
      .update(schema.review_items)
      .set({ status: "RESOLVED", resolution: "RETRY", resolved_at: deps.now() })
      .where(and(inArray(schema.review_items.prospect_id, ids), eq(schema.review_items.status, "OPEN"), inArray(schema.review_items.reason, ["FIRM_ONLY", "VISIBILITY_INCONCLUSIVE", "UNSUPPORTED_CLAIM"])));
  }
  await logEvent(deps.db, { campaignId: campaign.id, type: "MANUAL_OBSERVATIONS_IMPORTED", data: { benchmark_id: bench.id, valid, expected: bench.expected_valid_runs, prospects_reset: ids.length, ...params, model: bench.model } });
  await startCampaign(deps, campaign.id);
  return { benchmarkId: bench.id, valid, expected: bench.expected_valid_runs, invalid, reset: ids.length };
}
