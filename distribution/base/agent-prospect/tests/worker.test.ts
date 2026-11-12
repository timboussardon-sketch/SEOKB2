import { eq, sql } from "drizzle-orm";
import { afterAll, expect, test } from "vitest";
import { createDb, schema } from "../src/db/client";
import { createCampaign, startCampaign } from "../src/engine/campaign";
import { startWorker } from "../worker/index";
import { baseConfig, closeDb, TEST_DB_URL, testDb } from "./helpers";

afterAll(closeDb);

const env = { SIMULATION_WORLD_SIZE: "40", MAX_CONCURRENT_DOMAINS: "3" };

async function waitFor<T>(fn: () => Promise<T | null | false | undefined>, ms: number): Promise<T> {
  const start = Date.now();
  for (;;) {
    const v = await fn();
    if (v) return v;
    if (Date.now() - start > ms) throw new Error("Délai d'attente dépassé");
    await new Promise((r) => setTimeout(r, 200));
  }
}

test("worker pg-boss : la campagne survit à un arrêt brutal et se termine sans doublon", async () => {
  const db = await testDb();
  const admin = createDb(TEST_DB_URL);
  await admin.db.execute(sql`drop schema if exists pgboss cascade`);

  const a = await startWorker(TEST_DB_URL, env);
  const c = await createCampaign(a.deps, { name: "worker", config: { ...baseConfig, target_count: 6, max_candidates_per_round: 8 }, simulation: true });
  await startCampaign(a.deps, c.id);
  // On laisse le travail s'engager, puis on coupe sans laisser finir les jobs en cours.
  await waitFor(async () => (await db.select().from(schema.prospects)).length > 0, 30_000);
  await a.boss.stop({ graceful: false, close: true });
  const mid = await db.select().from(schema.prospects);
  const midStatus = (await db.select().from(schema.campaigns).where(eq(schema.campaigns.id, c.id)))[0].status;
  expect(midStatus).toBe("RUNNING");

  // Un nouveau worker démarre : il reprend depuis l'état enregistré.
  const b = await startWorker(TEST_DB_URL, env);
  const done = await waitFor(async () => {
    const [row] = await db.select().from(schema.campaigns).where(eq(schema.campaigns.id, c.id));
    return row.status === "COMPLETED" || row.status === "PARTIAL" || row.status === "BLOCKED" ? row : null;
  }, 120_000);
  await b.stop();

  expect(done.status).toBe("COMPLETED");
  const prospects = await db.select().from(schema.prospects);
  expect(prospects.length).toBeGreaterThanOrEqual(mid.length);
  expect(new Set(prospects.map((p) => p.firm_id)).size).toBe(prospects.length);
  const ready = prospects.filter((p) => (p.state === "READY_FOR_REVIEW" || p.state === "APPROVED") && p.email_status === "FOUND");
  expect(ready.length).toBeGreaterThanOrEqual(6);
  // Un seul benchmark, quinze réponses valides, aucune tentative laissée en suspens.
  const benchmarks = await db.select().from(schema.visibility_benchmarks);
  const runs = await db.select().from(schema.visibility_runs);
  expect(benchmarks).toHaveLength(1);
  expect(benchmarks[0]).toMatchObject({ status: "COMPLETE", valid_runs: 15 });
  expect(runs.filter((r) => r.validity === "PENDING")).toHaveLength(0);
  expect(new Set(runs.filter((r) => r.validity === "VALID").map((r) => `${r.prompt_index}:${r.repetition}`)).size).toBe(15);
  // Aucune étape en double : un audit et un brouillon au plus par prospect.
  const audits = await db.select().from(schema.audits);
  const drafts = await db.select().from(schema.email_drafts);
  expect(new Set(audits.map((x) => x.prospect_id)).size).toBe(audits.length);
  expect(new Set(drafts.map((x) => x.prospect_id)).size).toBe(drafts.length);
  expect(prospects.filter((p) => p.state.endsWith("ING") && p.state !== "ARCHIVED_OBSERVED")).toHaveLength(0);
  await admin.pool.end();
}, 180_000);
