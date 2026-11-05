import { and, asc, desc, eq, sql } from "drizzle-orm";
import { schema } from "../../db/client";
import { BENCHMARK_PROMPT_VERSION, benchmarkConfigHash, buildBenchmarkPrompts, VISIBILITY_MODE_LABELS, type Segment } from "../../core/benchmark";
import { AppError, classify, POLICIES } from "../../core/errors";
import { assessRun, computeVerdict, matchEntity, type EntityRef } from "../../core/verdict";
import { metered } from "../budget";
import type { Campaign, Deps, Firm, Prospect, Runtime } from "../deps";
import { logEvent } from "../events";
import { sendToReview, setState } from "../transitions";

type Benchmark = typeof schema.visibility_benchmarks.$inferSelect;

export function segmentOf(campaign: Campaign): Segment {
  return { practice: campaign.config.practice_area, clientType: campaign.config.client_type, city: campaign.config.location };
}

/**
 * Benchmark partagé d'un segment : cinq formulations, N répétitions, chacune dans une conversation neuve.
 * L'objectif est N×5 réponses VALIDES, pas N×5 appels : une erreur, un refus ou une réponse inutilisable est relancé
 * dans la limite fixée, et n'est jamais compté comme une absence. Reprenable : chaque tentative occupe un créneau unique.
 */
export async function ensureBenchmark(deps: Deps, rt: Runtime, campaign: Campaign): Promise<Benchmark> {
  const cfg = campaign.config;
  const v = rt.providers.visibility;
  // Des réponses relevées à la main dans ChatGPT, si elles existent, priment sur la mesure par API.
  const [manual] = await deps.db.select().from(schema.visibility_benchmarks).where(and(eq(schema.visibility_benchmarks.campaign_id, campaign.id), eq(schema.visibility_benchmarks.provider, "CHATGPT_MANUAL_OBSERVATION"))).orderBy(desc(schema.visibility_benchmarks.started_at)).limit(1);
  if (manual) return manual;
  const segment = segmentOf(campaign);
  const prompts = buildBenchmarkPrompts(segment).slice(0, cfg.visibility_prompts);
  const hash = benchmarkConfigHash({ segment, provider: v.name, model: v.model, params: v.params, prompts: prompts.length, repetitions: cfg.visibility_repetitions });
  const B = schema.visibility_benchmarks;
  const R = schema.visibility_runs;
  await deps.db
    .insert(B)
    .values({ campaign_id: campaign.id, config_hash: hash, segment, provider: v.name, model: v.model, params: v.params, prompt_version: BENCHMARK_PROMPT_VERSION, prompts, repetitions: cfg.visibility_repetitions, expected_valid_runs: prompts.length * cfg.visibility_repetitions })
    .onConflictDoNothing();
  let [bench] = await deps.db.select().from(B).where(and(eq(B.campaign_id, campaign.id), eq(B.config_hash, hash)));
  if (bench.status !== "RUNNING") return bench;

  // Un seul worker mène le benchmark ; les autres attendent son résultat au lieu de payer les mêmes appels.
  let release: (() => Promise<void>) | null = null;
  for (let waited = 0; !(release = await deps.tryLock(`benchmark:${bench.id}`)); waited++) {
    if (waited > 1800) throw new AppError("TIMEOUT", "Benchmark de visibilité toujours en cours ailleurs");
    await deps.sleep(1000);
  }
  try {
    [bench] = await deps.db.select().from(B).where(eq(B.id, bench.id));
    if (bench.status !== "RUNNING") return bench;
    // Le verrou est à nous : une tentative restée en attente vient d'un worker interrompu. Issue inconnue, donc ni valide ni absence.
    await deps.db.update(R).set({ validity: "ERROR", validity_note: "Tentative interrompue, issue inconnue" }).where(and(eq(R.benchmark_id, bench.id), eq(R.validity, "PENDING")));

    const maxAttempts = 1 + cfg.max_visibility_retries_per_run;
    for (let p = 0; p < prompts.length; p++) {
      for (let rep = 1; rep <= cfg.visibility_repetitions; rep++) {
        for (;;) {
          const attempts = await deps.db.select().from(R).where(and(eq(R.benchmark_id, bench.id), eq(R.prompt_index, p), eq(R.repetition, rep))).orderBy(asc(R.attempt));
          if (attempts.some((a) => a.validity === "VALID") || attempts.length >= maxAttempts) break;
          const [slot] = await deps.db.insert(R).values({ benchmark_id: bench.id, prompt_index: p, repetition: rep, attempt: attempts.length + 1, prompt: prompts[p], validity: "PENDING" }).returning();
          try {
            const answer = await metered(deps, { campaignId: campaign.id, benchmarkId: bench.id, step: "visibility" }, v.estimate(), () => v.ask(prompts[p], segment.city));
            const verdict = assessRun({ text: answer.text, webSearchUsed: answer.webSearchUsed, requireWebSearch: v.requireWebSearch });
            await deps.db
              .update(R)
              .set({ response_text: answer.text, citations: answer.citations, web_search_used: answer.webSearchUsed, model: answer.usage.model, provider_response_id: answer.responseId, usage: answer.usage.reported as object | null, validity: verdict.validity, validity_note: verdict.note })
              .where(eq(R.id, slot.id));
          } catch (err) {
            const c = classify(err);
            await deps.db.update(R).set({ validity: "ERROR", validity_note: c.message.slice(0, 300), error: c }).where(eq(R.id, slot.id));
            // Clé invalide, budget épuisé, tarif inconnu : inutile d'insister, l'étape remonte l'erreur.
            if (!POLICIES[c.category].retryable) throw err instanceof AppError ? err : new AppError(c.category, c.message);
            if (c.retryAfterMs) await deps.sleep(Math.min(c.retryAfterMs, POLICIES[c.category].maxDelayMs));
          }
        }
      }
    }
    const [{ n }] = await deps.db
      .select({ n: sql<number>`count(distinct (${R.prompt_index}, ${R.repetition}))::int` })
      .from(R)
      .where(and(eq(R.benchmark_id, bench.id), eq(R.validity, "VALID")));
    [bench] = await deps.db
      .update(B)
      .set({ valid_runs: n, status: n >= bench.expected_valid_runs ? "COMPLETE" : "INCOMPLETE", finished_at: deps.now() })
      .where(eq(B.id, bench.id))
      .returning();
    await logEvent(deps.db, { campaignId: campaign.id, type: "BENCHMARK_FINISHED", data: { benchmark_id: bench.id, valid_runs: n, expected: bench.expected_valid_runs } });
    return bench;
  } finally {
    await release();
  }
}

export async function entityFor(deps: Deps, prospect: Prospect, firm: Firm): Promise<EntityRef> {
  const [lawyer] = prospect.lawyer_id ? await deps.db.select().from(schema.lawyers).where(eq(schema.lawyers.id, prospect.lawyer_id)) : [];
  return {
    targetType: lawyer ? "LAWYER" : "FIRM",
    lawyer: lawyer ? { firstName: lawyer.first_name, lastName: lawyer.last_name } : undefined,
    firmNames: [firm.name, ...firm.aliases].filter((n): n is string => !!n),
    domain: firm.canonical_domain,
  };
}

export async function visibilityStep(deps: Deps, rt: Runtime, campaign: Campaign, prospect: Prospect, firm: Firm): Promise<void> {
  const bench = await ensureBenchmark(deps, rt, campaign);
  const R = schema.visibility_runs;
  const valid = await deps.db.select().from(R).where(and(eq(R.benchmark_id, bench.id), eq(R.validity, "VALID"))).orderBy(asc(R.prompt_index), asc(R.repetition));
  // La correspondance avec l'entité est faite après coup, sur les réponses déjà produites.
  const entity = await entityFor(deps, prospect, firm);
  const perRun = valid.map((run) => ({ run, obs: matchEntity(entity, run.response_text ?? "", run.citations) }));
  await deps.db.transaction(async (tx) => {
    await tx.delete(schema.entity_observations).where(eq(schema.entity_observations.prospect_id, prospect.id));
    const rows = perRun.flatMap(({ run, obs }) => obs.map((o) => ({ prospect_id: prospect.id, run_id: run.id, type: o.type, detail: o.detail })));
    if (rows.length) await tx.insert(schema.entity_observations).values(rows);
  });
  const result = computeVerdict({ targetType: entity.targetType, expectedValidRuns: bench.expected_valid_runs, validRuns: perRun.map((x) => x.obs) });
  const summary = {
    ...result,
    expected_valid_runs: bench.expected_valid_runs,
    provider: bench.provider,
    mode_label: VISIBILITY_MODE_LABELS[bench.provider],
    model: bench.model,
    window_start: bench.started_at.toISOString(),
    window_end: (bench.finished_at ?? deps.now()).toISOString(),
    target_type: entity.targetType,
    question_count: bench.prompts.length,
    // Vrai seulement pour des réponses relevées à la main dans ChatGPT ; un résultat d'API ne l'est jamais.
    chatgpt_observed: bench.provider === "CHATGPT_MANUAL_OBSERVATION",
  };
  const patch = { visibility_verdict: result.verdict, visibility_summary: summary, benchmark_id: bench.id };

  if (result.verdict === "NOT_OBSERVED_IN_SAMPLE") {
    await setState(deps, prospect, "VISIBILITY_DONE", patch);
  } else if (result.verdict === "OBSERVED") {
    await setState(deps, prospect, prospect.force_audit ? "VISIBILITY_DONE" : "ARCHIVED_OBSERVED", patch);
  } else if (prospect.force_audit) {
    await setState(deps, prospect, "VISIBILITY_DONE", patch);
  } else if (result.verdict === "FIRM_ONLY") {
    await sendToReview(deps, prospect, "FIRM_ONLY", `${result.reason}. Un audit reste possible, sans discours d'absence.`, "VISIBILITY_DONE", patch);
  } else {
    await sendToReview(deps, prospect, "VISIBILITY_INCONCLUSIVE", `${result.reason}. Aucune conclusion d'absence n'est tirée.`, "VISIBILITY_DONE", patch);
  }
}
