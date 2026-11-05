import { and, eq, inArray, sql } from "drizzle-orm";
import { schema } from "../db/client";
import { AppError, classify } from "../core/errors";
import type { CallEstimate, Usage } from "../providers/types";
import type { Deps } from "./deps";
import { priceOf } from "./pricing";

const COUNTED = ["RESERVED", "RECONCILED", "UNCONFIRMED"];
const BUDGET_LOCK = 742_001;
const counted = sql`coalesce(sum(coalesce(${schema.budget_ledger.actual_usd}, ${schema.budget_ledger.estimated_usd})), 0)::float8`;

export interface Charge {
  campaignId: string;
  prospectId?: string | null;
  benchmarkId?: string | null;
  step: string;
}

/**
 * Réserve le coût majoré d'un appel avant de l'émettre. Les réservations sont sérialisées par un verrou
 * transactionnel : plusieurs workers ne peuvent pas dépasser un plafond à eux tous.
 */
export async function reserve(deps: Deps, charge: Charge, estimate: CallEstimate): Promise<string> {
  const amount = priceOf(deps.prices, estimate);
  return deps.db.transaction(async (tx) => {
    await tx.execute(sql`select pg_advisory_xact_lock(${BUDGET_LOCK})`);
    const [campaign] = await tx.select().from(schema.campaigns).where(eq(schema.campaigns.id, charge.campaignId));
    if (!campaign) throw new AppError("INVALID_INPUT", "Campagne introuvable");
    const L = schema.budget_ledger;
    const [{ total: campaignTotal }] = await tx.select({ total: counted }).from(L).where(and(eq(L.campaign_id, charge.campaignId), inArray(L.status, COUNTED)));
    const [{ total: dayTotal }] = await tx.select({ total: counted }).from(L).where(and(sql`${L.day} = current_date`, inArray(L.status, COUNTED)));
    const over = (label: string, used: number, cap: number) =>
      new AppError("BUDGET_EXCEEDED", `Plafond ${label} atteint : ${used.toFixed(4)} $ engagés + ${amount.toFixed(4)} $ demandés > ${cap.toFixed(2)} $ (étape ${charge.step}).`);
    if (Number(campaignTotal) + amount > campaign.config.max_campaign_cost_usd + 1e-9) throw over("de campagne", Number(campaignTotal), campaign.config.max_campaign_cost_usd);
    if (Number(dayTotal) + amount > deps.globalDailyUsd + 1e-9) throw over("quotidien", Number(dayTotal), deps.globalDailyUsd);
    if (charge.prospectId) {
      const used = await prospectCost(tx, charge.prospectId);
      if (used.total + amount > campaign.config.max_prospect_cost_usd + 1e-9) throw over("par prospect", used.total, campaign.config.max_prospect_cost_usd);
    }
    const [row] = await tx
      .insert(L)
      .values({ campaign_id: charge.campaignId, prospect_id: charge.prospectId ?? null, benchmark_id: charge.benchmarkId ?? null, step: charge.step, model: estimate.model, estimated_usd: amount.toFixed(6), status: "RESERVED" })
      .returning({ id: L.id });
    return row.id;
  });
}

/** Coût recalculé depuis l'usage rapporté par le fournisseur. Il reste un calcul local, pas une facture. */
export async function reconcile(deps: Deps, ledgerId: string, usage: Usage): Promise<void> {
  const actual = priceOf(deps.prices, usage);
  await deps.db
    .update(schema.budget_ledger)
    .set({ status: "RECONCILED", actual_usd: actual.toFixed(6), usage: { input_tokens: usage.input_tokens, output_tokens: usage.output_tokens, web_search_calls: usage.web_search_calls, reported: usage.reported } })
    .where(eq(schema.budget_ledger.id, ledgerId));
}

async function settle(deps: Deps, ledgerId: string, status: "RELEASED" | "UNCONFIRMED"): Promise<void> {
  await deps.db.update(schema.budget_ledger).set({ status, actual_usd: status === "RELEASED" ? "0" : null }).where(eq(schema.budget_ledger.id, ledgerId));
}

/** Enchaîne réservation, appel et rapprochement. Après une erreur d'issue inconnue, la réservation reste comptée. */
export async function metered<T extends { usage: Usage }>(deps: Deps, charge: Charge, estimate: CallEstimate, call: () => Promise<T>): Promise<T> {
  const id = await reserve(deps, charge, estimate);
  try {
    const result = await call();
    await reconcile(deps, id, result.usage);
    return result;
  } catch (err) {
    const c = classify(err).category;
    // Refus avant traitement : rien n'a été consommé.
    await settle(deps, id, c === "AUTH_ERROR" || c === "RATE_LIMIT" || c === "INVALID_INPUT" ? "RELEASED" : "UNCONFIRMED");
    throw err;
  }
}

type Reader = Pick<Deps["db"], "select">;

/** Coût d'un prospect : ses appels propres + sa part du benchmark partagé, divisé entre les prospects qui s'y adossent. */
export async function prospectCost(db: Reader, prospectId: string): Promise<{ direct: number; benchmarkShare: number; total: number }> {
  const L = schema.budget_ledger;
  const [{ total: direct }] = await db.select({ total: counted }).from(L).where(and(eq(L.prospect_id, prospectId), inArray(L.status, COUNTED)));
  const [p] = await db.select({ benchmark_id: schema.prospects.benchmark_id }).from(schema.prospects).where(eq(schema.prospects.id, prospectId));
  let share = 0;
  if (p?.benchmark_id) {
    const [{ total }] = await db.select({ total: counted }).from(L).where(and(eq(L.benchmark_id, p.benchmark_id), inArray(L.status, COUNTED)));
    const [{ n }] = await db.select({ n: sql<number>`count(*)::int` }).from(schema.prospects).where(eq(schema.prospects.benchmark_id, p.benchmark_id));
    share = n > 0 ? Number(total) / n : 0;
  }
  return { direct: Number(direct), benchmarkShare: share, total: Number(direct) + share };
}

export async function campaignCost(db: Reader, campaignId: string): Promise<{ engaged: number; reconciled: number; unconfirmed: number; reserved: number }> {
  const L = schema.budget_ledger;
  const rows = await db.select({ status: L.status, total: counted }).from(L).where(eq(L.campaign_id, campaignId)).groupBy(L.status);
  const by = (s: string) => Number(rows.find((r) => r.status === s)?.total ?? 0);
  return { reconciled: by("RECONCILED"), unconfirmed: by("UNCONFIRMED"), reserved: by("RESERVED"), engaged: by("RECONCILED") + by("UNCONFIRMED") + by("RESERVED") };
}
