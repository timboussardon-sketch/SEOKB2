// Refait, avec le message type en vigueur, les brouillons réels pas encore partis, puis leur contrôle factuel.
// npx tsx --env-file=.env.local scripts/reprise-gabarit.ts
import { and, eq, inArray, isNull, or } from "drizzle-orm";
import { createDb, schema } from "../src/db/client";
import { bossQueue, createBoss } from "../src/engine/queue";
import { buildDeps } from "../src/engine/runtime";
import { draftStep, factcheckStep } from "../src/engine/steps/draft";

const url = process.env.DATABASE_URL!;
const { db, pool } = createDb(url);
const boss = await createBoss(url);
const deps = buildDeps(db, pool, bossQueue(boss));

const rows = await db
  .select({ prospect: schema.prospects, campaign: schema.campaigns, firm: schema.firms })
  .from(schema.prospects)
  .innerJoin(schema.campaigns, eq(schema.campaigns.id, schema.prospects.campaign_id))
  .innerJoin(schema.firms, eq(schema.firms.id, schema.prospects.firm_id))
  .innerJoin(schema.email_drafts, eq(schema.email_drafts.prospect_id, schema.prospects.id))
  .leftJoin(schema.outreach, eq(schema.outreach.prospect_id, schema.prospects.id))
  .where(and(eq(schema.campaigns.simulation, false), inArray(schema.prospects.state, ["READY_FOR_REVIEW", "APPROVED", "DRAFT_READY"]), or(isNull(schema.outreach.id), eq(schema.outreach.status, "FAILED"))));

for (const { prospect, campaign, firm } of rows) {
  const rt = deps.runtimeFor(campaign);
  await draftStep(deps, rt, campaign, { ...prospect, state: "DRAFTING" }, firm);
  const [p] = await db.select().from(schema.prospects).where(eq(schema.prospects.id, prospect.id));
  await factcheckStep(deps, rt, campaign, { ...p, state: "FACT_CHECKING" }, firm);
  const [d] = await db.select().from(schema.email_drafts).where(eq(schema.email_drafts.prospect_id, prospect.id));
  const [after] = await db.select().from(schema.prospects).where(eq(schema.prospects.id, prospect.id));
  const check = d.fact_check as { ok: boolean; failed: { reason: string }[]; global: string[] };
  console.log(`${firm.canonical_domain} : ${after.state}, ${check.ok ? "contrôle vert" : `bloqué (${[...check.failed.map((f) => f.reason), ...check.global].join(" ; ")})`}`);
}
await boss.stop();
await pool.end();
