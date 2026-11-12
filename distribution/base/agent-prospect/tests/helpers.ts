import { sql } from "drizzle-orm";
import { createDb, lockerFor, schema, type Db } from "../src/db/client";
import { runMigrations } from "../src/db/migrate";
import { discoveryRound, tickCampaign } from "../src/engine/campaign";
import type { Campaign, Deps, JobData, JobName, Runtime } from "../src/engine/deps";
import { SIMULATION_PRICES, type PriceTable } from "../src/engine/pricing";
import { advanceProspect } from "../src/engine/prospect";
import { simulationProviders } from "../src/providers/simulation";

export const TEST_DB_URL = process.env.DATABASE_URL_TEST ?? "postgresql://agent@127.0.0.1:5545/agent_prospection_test";

let shared: ReturnType<typeof createDb> | null = null;
let migrated = false;

export async function testDb(): Promise<Db> {
  if (!migrated) {
    await runMigrations(TEST_DB_URL);
    migrated = true;
  }
  shared ??= createDb(TEST_DB_URL);
  const tables = Object.values(schema).map((t) => (t as unknown as { [k: symbol]: string })[Symbol.for("drizzle:Name")]);
  await shared.db.execute(sql.raw(`truncate ${tables.map((t) => `"${t}"`).join(", ")} cascade`));
  return shared.db;
}

export async function closeDb(): Promise<void> {
  await shared?.pool.end();
  shared = null;
}

export class MemoryQueue {
  jobs: { name: JobName; data: JobData }[] = [];
  log: JobName[] = [];
  async send(name: JobName, data: JobData) {
    this.jobs.push({ name, data });
  }
}

export interface TestEnv {
  deps: Deps;
  queue: MemoryQueue;
  runtime: Runtime;
}

export function testEnv(db: Db, opts: { runtime?: (c: Campaign) => Runtime; prices?: PriceTable; publicUrl?: string | null; globalDailyUsd?: number; worldSize?: number } = {}): TestEnv {
  const queue = new MemoryQueue();
  const cache = new Map<string, Runtime>();
  const runtimeFor =
    opts.runtime ??
    ((c: Campaign) => {
      let rt = cache.get(c.id);
      if (!rt) {
        const sim = simulationProviders({ practice: c.config.practice_area, clientType: c.config.client_type, city: c.config.location }, opts.worldSize ?? 60);
        rt = { providers: sim.providers, fetcher: sim.fetcher, resolveMx: async () => null };
        cache.set(c.id, rt);
      }
      return rt;
    });
  const deps: Deps = {
    db,
    queue,
    prices: opts.prices ?? SIMULATION_PRICES,
    globalDailyUsd: opts.globalDailyUsd ?? 10,
    publicUrl: opts.publicUrl === undefined ? "https://agent.exemple-fictif.test" : opts.publicUrl,
    runtimeFor,
    tryLock: lockerFor(shared!.pool),
    sleep: async () => {},
    now: () => new Date(),
    random: () => 0.5,
  };
  return { deps, queue, runtime: null as unknown as Runtime };
}

/** Exécute les jobs en file jusqu'à épuisement, comme le ferait le worker, mais dans le test. */
export async function drain(env: TestEnv, max = 5000): Promise<number> {
  let n = 0;
  while (env.queue.jobs.length) {
    if (++n > max) throw new Error("File de jobs sans fin : boucle infinie probable");
    const job = env.queue.jobs.shift()!;
    env.queue.log.push(job.name);
    if (job.name === "campaign-tick") await tickCampaign(env.deps, job.data.campaignId);
    else if (job.name === "discovery-round") await discoveryRound(env.deps, job.data.campaignId);
    else if (job.data.prospectId) await advanceProspect(env.deps, job.data.prospectId);
  }
  return n;
}

export const baseConfig = {
  practice_area: "droit du travail",
  location: "Lyon",
  client_type: "entreprise" as const,
  target_count: 5,
  goal_type: "EMAIL_READY_PROSPECTS" as const,
  max_candidates_per_round: 10,
};
