// Relit les adresses des prospects réels restés sans destinataire, après un changement des règles d'extraction.
// npx tsx --env-file=.env.local scripts/reprise-adresses.ts
import { and, eq, inArray, isNull } from "drizzle-orm";
import { createDb, schema } from "../src/db/client";
import { bossQueue, createBoss } from "../src/engine/queue";
import { buildDeps } from "../src/engine/runtime";
import { enrichStep } from "../src/engine/steps/enrich";
import { factcheckStep } from "../src/engine/steps/draft";

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
  .where(and(eq(schema.campaigns.simulation, false), isNull(schema.email_drafts.recipient), inArray(schema.prospects.state, ["READY_FOR_REVIEW", "HUMAN_REVIEW_REQUIRED"])));

for (const { prospect, campaign, firm } of rows) {
  const rt = deps.runtimeFor(campaign);
  // L'enrichissement fait passer le prospect par ENRICHED ; il est remis à son état d'avant pour le contrôle factuel.
  await enrichStep(deps, rt, campaign, { ...prospect, state: "ENRICHING" }, firm);
  await db.update(schema.prospects).set({ state: prospect.state }).where(eq(schema.prospects.id, prospect.id));
  const [p] = await db.select().from(schema.prospects).where(eq(schema.prospects.id, prospect.id));
  await factcheckStep(deps, rt, campaign, p, firm);
  const [d] = await db.select().from(schema.email_drafts).where(eq(schema.email_drafts.prospect_id, prospect.id));
  const [after] = await db.select().from(schema.prospects).where(eq(schema.prospects.id, prospect.id));
  console.log(`${firm.canonical_domain} : ${d.recipient ?? "toujours sans adresse"} (${after.state})`);
}
await boss.stop();
await pool.end();
