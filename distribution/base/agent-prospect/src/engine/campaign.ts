import { eq, sql } from "drizzle-orm";
import { schema } from "../db/client";
import { classify, POLICIES, withRetry } from "../core/errors";
import { CampaignConfigSchema, type CampaignConfig } from "../core/objective";
import { buildDiscoveryQueries, QUERY_RULE_VERSION } from "../core/queries";
import { assertAllowedUrl } from "../core/ssrf";
import { canonicalDomain, stableHash } from "../core/text";
import { metered } from "./budget";
import type { Campaign, Deps } from "./deps";
import { logEvent } from "./events";
import { nextStep } from "./prospect";

// Annuaires, réseaux et médias : ce ne sont pas des sites de cabinet, et leurs conditions n'autorisent pas la collecte.
const NOT_A_FIRM_SITE = /(^|\.)(linkedin|facebook|instagram|x|twitter|youtube|pagesjaunes|google|avocat|justifit|alexia|doctrine|village-justice|legalplace|captaincontrat|meilleursavocats|annuaire|wikipedia|trustpilot|mappy|societe|pappers|juritravail|starofservice|barreau[a-z-]*|cnb|legal500|chambers|decideurs|magazine-decideurs|ordre-avocats|lemondedudroit|yelp|cylex|kompass|alexia|avostart|call-a-lawyer|ooreka|indeed|welcometothejungle)\.[a-z.]+$/;

export async function createCampaign(deps: Pick<Deps, "db">, input: { name: string; objectiveText?: string | null; config: unknown; simulation: boolean }): Promise<Campaign> {
  const config: CampaignConfig = CampaignConfigSchema.parse(input.config);
  if (input.simulation) config.visibility_mode = "SIMULATION";
  const [row] = await deps.db
    .insert(schema.campaigns)
    .values({ name: input.name, objective_text: input.objectiveText ?? null, config, config_hash: stableHash(config), goal_type: config.goal_type, target_count: config.target_count, simulation: input.simulation })
    .returning();
  await logEvent(deps.db, { campaignId: row.id, type: "CAMPAIGN_CREATED", data: { config } });
  return row;
}

async function setStatus(deps: Deps, id: string, status: string, reason: string | null): Promise<void> {
  await deps.db.update(schema.campaigns).set({ status, stop_reason: reason, updated_at: deps.now() }).where(eq(schema.campaigns.id, id));
  await logEvent(deps.db, { campaignId: id, type: "CAMPAIGN_STATUS", data: { status, reason } });
}

async function requeue(deps: Deps, c: Campaign): Promise<void> {
  const rows = await deps.db.select().from(schema.prospects).where(eq(schema.prospects.campaign_id, c.id));
  for (const p of rows) if (nextStep(p, c.config)) await deps.queue.send("prospect-advance", { campaignId: c.id, prospectId: p.id });
  await deps.queue.send("campaign-tick", { campaignId: c.id });
}

/** Démarre ou reprend : libère les prospects suspendus pour budget, relance ceux restés en cours, puis réévalue l'objectif. */
export async function startCampaign(deps: Deps, id: string): Promise<void> {
  const [c] = await deps.db.select().from(schema.campaigns).where(eq(schema.campaigns.id, id));
  if (!c || c.status === "STOPPED") return;
  await setStatus(deps, id, "RUNNING", null);
  const blocked = await deps.db.select().from(schema.prospects).where(sql`${schema.prospects.campaign_id} = ${id} and ${schema.prospects.state} = 'BUDGET_BLOCKED'`);
  for (const p of blocked) if (p.resume_state) await deps.db.update(schema.prospects).set({ state: p.resume_state, resume_state: null }).where(eq(schema.prospects.id, p.id));
  await requeue(deps, c);
}

const STALE_RESERVATION_MS = 10 * 60_000;

/**
 * Une réservation restée ouverte après l'arrêt d'un worker a une issue inconnue : l'appel a pu partir et être facturé.
 * Elle n'est donc pas libérée. Elle passe en « non confirmée » : toujours comptée dans les plafonds, affichée à part.
 */
export async function settleStaleReservations(deps: Pick<Deps, "db" | "now">, olderThanMs = STALE_RESERVATION_MS): Promise<number> {
  const L = schema.budget_ledger;
  const limit = new Date(deps.now().getTime() - olderThanMs);
  const rows = await deps.db.update(L).set({ status: "UNCONFIRMED" }).where(sql`${L.status} = 'RESERVED' and ${L.created_at} < ${limit}`).returning({ id: L.id });
  return rows.length;
}

/** Au démarrage d'un worker : remet en file le travail des campagnes en cours. Sans effet si tout est déjà en file. */
export async function recoverRunning(deps: Deps): Promise<number> {
  await settleStaleReservations(deps);
  const running = await deps.db.select().from(schema.campaigns).where(eq(schema.campaigns.status, "RUNNING"));
  for (const c of running) await requeue(deps, c);
  return running.length;
}

export const pauseCampaign = (deps: Deps, id: string) => setStatus(deps, id, "PAUSED", "Mise en pause par l'utilisateur");
export const stopCampaign = (deps: Deps, id: string) => setStatus(deps, id, "STOPPED", "Arrêt demandé par l'utilisateur");

export interface Progress {
  goal: number;
  target: number;
  inFlight: number;
  inReview: number;
  budgetBlocked: number;
  funnel: { discovered: number; qualified: number; rejected: number; enriched: number; visibilityDone: number; audited: number; keywordsDone: number; drafts: number; ready: number; observed: number; noEmail: number; failed: number };
  rejections: Record<string, number>;
}

export async function campaignProgress(deps: Pick<Deps, "db">, c: Campaign): Promise<Progress> {
  const rows = await deps.db.select().from(schema.prospects).where(eq(schema.prospects.campaign_id, c.id));
  const audited = new Set((await deps.db.select({ id: schema.audits.prospect_id }).from(schema.audits).innerJoin(schema.prospects, eq(schema.audits.prospect_id, schema.prospects.id)).where(eq(schema.prospects.campaign_id, c.id))).map((r) => r.id));
  const drafts = new Set((await deps.db.select({ id: schema.email_drafts.prospect_id }).from(schema.email_drafts).innerJoin(schema.prospects, eq(schema.email_drafts.prospect_id, schema.prospects.id)).where(eq(schema.prospects.campaign_id, c.id))).map((r) => r.id));
  const gone = ["REJECTED", "SUPPRESSED"];
  const qualified = rows.filter((p) => p.qualification_status === "QUALIFIED" && !gone.includes(p.state));
  const ready = rows.filter((p) => (p.state === "READY_FOR_REVIEW" || p.state === "APPROVED") && p.email_status === "FOUND");
  const goal = c.goal_type === "QUALIFIED_PROSPECTS" ? qualified.length : c.goal_type === "AUDITED_PROSPECTS" ? rows.filter((p) => audited.has(p.id) && !gone.includes(p.state)).length : ready.length;
  const rejections: Record<string, number> = {};
  for (const p of rows) if (p.state === "REJECTED") rejections[p.qualification_reason ?? "MANUAL"] = (rejections[p.qualification_reason ?? "MANUAL"] ?? 0) + 1;
  return {
    goal,
    target: c.target_count,
    inFlight: rows.filter((p) => nextStep(p, c.config)).length,
    inReview: rows.filter((p) => p.state === "HUMAN_REVIEW_REQUIRED").length,
    budgetBlocked: rows.filter((p) => p.state === "BUDGET_BLOCKED").length,
    funnel: {
      discovered: rows.length,
      qualified: qualified.length,
      rejected: rows.filter((p) => p.state === "REJECTED").length,
      enriched: rows.filter((p) => p.email_status !== null).length,
      visibilityDone: rows.filter((p) => p.visibility_verdict !== null).length,
      audited: rows.filter((p) => audited.has(p.id)).length,
      keywordsDone: rows.filter((p) => p.keyword_status !== null).length,
      drafts: rows.filter((p) => drafts.has(p.id)).length,
      ready: ready.length,
      observed: rows.filter((p) => p.state === "ARCHIVED_OBSERVED").length,
      noEmail: rows.filter((p) => p.email_status === "NO_PUBLIC_EMAIL").length,
      failed: rows.filter((p) => p.state === "FAILED").length,
    },
    rejections,
  };
}

/** Raison pour laquelle la découverte ne peut plus repartir, ou null s'il reste des moyens. */
export function discoveryStop(c: Campaign): string | null {
  const cfg = c.config;
  if (c.discovery_rounds_done >= cfg.max_discovery_rounds) return `nombre maximal de tours de découverte atteint (${cfg.max_discovery_rounds})`;
  if (c.discovery_results_total >= cfg.max_total_discovery_results) return `plafond de résultats de découverte atteint (${cfg.max_total_discovery_results})`;
  if (c.empty_rounds >= cfg.max_empty_rounds) return `sources épuisées dans le périmètre défini (${c.empty_rounds} tours de recherche sans nouveau candidat)`;
  return null;
}

/**
 * Boucle de campagne. L'objectif est un nombre de prospects aboutis, pas un nombre de résultats trouvés :
 * tant qu'il n'est pas atteint et qu'il reste des moyens (tours, résultats, budget), la découverte repart.
 * Sinon la campagne se termine en disant exactement pourquoi.
 */
export async function tickCampaign(deps: Deps, campaignId: string): Promise<void> {
  const [c] = await deps.db.select().from(schema.campaigns).where(eq(schema.campaigns.id, campaignId));
  if (!c || c.status !== "RUNNING") return;
  const pr = await campaignProgress(deps, c);

  if (pr.goal >= pr.target) {
    if (pr.inFlight === 0) await setStatus(deps, c.id, "COMPLETED", `Objectif atteint : ${pr.goal} / ${pr.target}.`);
    return;
  }
  // Les prospects en cours peuvent encore aboutir : on attend leur issue avant de chercher davantage.
  if (pr.goal + pr.inFlight >= pr.target) return;

  const tail = `Cible ${pr.target}, atteints ${pr.goal}${pr.inReview ? `, ${pr.inReview} en attente de revue humaine` : ""}${pr.funnel.rejected ? `, ${pr.funnel.rejected} écartés` : ""}.`;
  if (pr.budgetBlocked > 0) {
    if (pr.inFlight === 0) await setStatus(deps, c.id, "BLOCKED", `Budget épuisé : ${pr.budgetBlocked} prospects suspendus. ${tail}`);
    return;
  }
  const exhausted = discoveryStop(c);
  if (exhausted) {
    if (pr.inFlight === 0) await setStatus(deps, c.id, "PARTIAL", `Objectif non atteint : ${exhausted}. ${tail}`);
    return;
  }
  // Un tour déjà lancé il y a peu est en cours : on attend son résultat.
  const [running] = await deps.db.select().from(schema.discovery_queries).where(sql`${schema.discovery_queries.campaign_id} = ${c.id} and ${schema.discovery_queries.round} = ${c.discovery_rounds_done + 1}`);
  if (running && deps.now().getTime() - running.created_at.getTime() < 10 * 60_000) return;
  await deps.queue.send("discovery-round", { campaignId: c.id });
}

/** Un tour de découverte : une formulation, des candidats, la déduplication, puis la qualification de chaque nouveau candidat. */
export async function discoveryRound(deps: Deps, campaignId: string): Promise<void> {
  const [c] = await deps.db.select().from(schema.campaigns).where(eq(schema.campaigns.id, campaignId));
  if (!c || c.status !== "RUNNING") return;
  const cfg = c.config;
  const round = c.discovery_rounds_done + 1;
  // Plusieurs demandes de découverte peuvent s'être accumulées : chacune revérifie les limites avant d'agir.
  if (discoveryStop(c)) return void (await deps.queue.send("campaign-tick", { campaignId }));
  // Un autre tour a pu suffire entre-temps : on ne cherche que s'il manque encore des prospects.
  const pr = await campaignProgress(deps, c);
  if (pr.goal + pr.inFlight >= pr.target) return void (await deps.queue.send("campaign-tick", { campaignId }));
  let rt: ReturnType<Deps["runtimeFor"]>;
  try {
    rt = deps.runtimeFor(c);
  } catch (err) {
    return setStatus(deps, c.id, "BLOCKED", `Recherche impossible : ${classify(err).message}`);
  }
  const queries = buildDiscoveryQueries({ practice: cfg.practice_area, subspecialties: cfg.subspecialties, clientType: cfg.client_type, city: cfg.location });
  const q = queries[(round - 1) % queries.length];
  const Q = schema.discovery_queries;
  // Rejouer ce job après un arrêt brutal reprend le même tour : les insertions suivantes sont idempotentes.
  await deps.db.insert(Q).values({ campaign_id: c.id, round, family: q.family, query: q.query, provider: rt.providers.search.name, rule_version: QUERY_RULE_VERSION }).onConflictDoNothing();
  const [row] = await deps.db.select().from(Q).where(sql`${Q.campaign_id} = ${c.id} and ${Q.round} = ${round}`);

  const known = await deps.db.select({ domain: schema.firms.canonical_domain }).from(schema.prospects).innerJoin(schema.firms, eq(schema.prospects.firm_id, schema.firms.id)).where(eq(schema.prospects.campaign_id, c.id));
  const suppressed = new Set((await deps.db.select().from(schema.suppressions)).map((s) => s.value));
  const excluded = new Set(cfg.excluded_domains.map((d) => canonicalDomain(d) ?? d));
  // Taille du tour réglée sur ce qui manque et sur le rendement observé, pour ne pas payer des candidats inutiles.
  const settled = pr.funnel.discovered - pr.inFlight;
  const yieldRate = settled >= 5 ? Math.max(0.2, pr.goal / settled) : 0.5;
  const wanted = Math.ceil((pr.target - pr.goal - pr.inFlight) / yieldRate) + 1;
  const room = Math.min(cfg.max_candidates_per_round, cfg.max_total_discovery_results - c.discovery_results_total, wanted);

  let results = 0;
  let created = 0;
  let duplicates = 0;
  let error: ReturnType<typeof classify> | null = null;
  const newIds: string[] = [];
  try {
    const { candidates } = await withRetry(
      () => metered(deps, { campaignId: c.id, step: "discovery" }, rt.providers.search.estimate(), () => rt.providers.search.search(q.query, room, known.map((k) => k.domain))),
      { sleep: deps.sleep, random: deps.random },
    );
    results = Math.min(candidates.length, room);
    for (const cand of candidates.slice(0, room)) {
      const domain = canonicalDomain(cand.website);
      if (!domain || NOT_A_FIRM_SITE.test(domain) || excluded.has(domain) || suppressed.has(domain)) continue;
      let website: string;
      try {
        website = assertAllowedUrl(new URL("/", cand.website).toString()).toString();
      } catch {
        continue;
      }
      await deps.db.insert(schema.firms).values({ canonical_domain: domain, website }).onConflictDoNothing();
      const [firm] = await deps.db.select().from(schema.firms).where(eq(schema.firms.canonical_domain, domain));
      const [p] = await deps.db
        .insert(schema.prospects)
        .values({ campaign_id: c.id, firm_id: firm.id, candidate_name: cand.name?.slice(0, 200) ?? null, source_url: cand.source_url, discovery_query_id: row.id })
        .onConflictDoNothing()
        .returning({ id: schema.prospects.id });
      if (p) {
        created++;
        newIds.push(p.id);
      } else duplicates++;
    }
  } catch (err) {
    error = classify(err);
  }

  await deps.db.transaction(async (tx) => {
    await tx.update(Q).set({ results_count: results, new_candidates: created, duplicates, error }).where(eq(Q.id, row.id));
    await tx
      .update(schema.campaigns)
      .set({ discovery_rounds_done: round, discovery_results_total: sql`${schema.campaigns.discovery_results_total} + ${results}`, empty_rounds: created === 0 ? sql`${schema.campaigns.empty_rounds} + 1` : 0, updated_at: deps.now() })
      .where(eq(schema.campaigns.id, c.id));
    await logEvent(tx, { campaignId: c.id, type: "DISCOVERY_ROUND", data: { round, query: q.query, results, new: created, duplicates, error } });
  });

  if (error) {
    const recovery = POLICIES[error.category].recovery;
    if (recovery === "STOP_INTEGRATION") return setStatus(deps, c.id, "BLOCKED", `Recherche impossible : ${error.message}`);
    if (recovery === "BUDGET_BLOCK") return setStatus(deps, c.id, "BLOCKED", `Budget : ${error.message}`);
  }
  for (const id of newIds) await deps.queue.send("prospect-advance", { campaignId: c.id, prospectId: id });
  await deps.queue.send("campaign-tick", { campaignId: c.id });
}

/** Enseignements de la campagne, en lecture seule : ils n'altèrent aucune règle sans validation humaine. */
export async function campaignLearning(deps: Pick<Deps, "db">, campaignId: string) {
  const Q = schema.discovery_queries;
  const P = schema.prospects;
  const rows = await deps.db
    .select({ family: Q.family, query: Q.query, results: Q.results_count, created: Q.new_candidates, qualified: sql<number>`count(*) filter (where ${P.qualification_status} = 'QUALIFIED')::int`, rejected: sql<number>`count(*) filter (where ${P.state} = 'REJECTED')::int` })
    .from(Q)
    .leftJoin(P, eq(P.discovery_query_id, Q.id))
    .where(eq(Q.campaign_id, campaignId))
    .groupBy(Q.id)
    .orderBy(Q.round);
  return rows;
}
