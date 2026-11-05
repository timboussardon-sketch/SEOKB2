import { createDb } from "../src/db/client";
import { discoveryRound, recoverRunning, tickCampaign } from "../src/engine/campaign";
import type { JobData } from "../src/engine/deps";
import { advanceProspect } from "../src/engine/prospect";
import { bossQueue, createBoss } from "../src/engine/queue";
import { buildDeps } from "../src/engine/runtime";

/** Worker séparé : il exécute les traitements longs depuis la file persistante et peut être arrêté à tout moment. */
export async function startWorker(url: string, env: Record<string, string | undefined> = process.env) {
  const { db, pool } = createDb(url);
  const boss = await createBoss(url);
  const deps = buildDeps(db, pool, bossQueue(boss), env);
  const concurrency = Number(env.MAX_CONCURRENT_DOMAINS ?? 3);
  await boss.work<JobData>("campaign-tick", { pollingIntervalSeconds: 1 }, async (jobs) => {
    for (const job of jobs) await tickCampaign(deps, job.data.campaignId);
  });
  await boss.work<JobData>("discovery-round", { pollingIntervalSeconds: 1 }, async (jobs) => {
    for (const job of jobs) await discoveryRound(deps, job.data.campaignId);
  });
  await boss.work<JobData>("prospect-advance", { pollingIntervalSeconds: 1, localConcurrency: concurrency }, async (jobs) => {
    for (const job of jobs) {
      if (!job.data.prospectId) continue;
      // Prospect tenu par un autre process : l'échec du job déclenche la relance différée de pg-boss.
      if ((await advanceProspect(deps, job.data.prospectId)) === "busy") throw new Error(`Prospect ${job.data.prospectId} occupé, nouvelle tentative différée`);
    }
  });
  // Reprise après interruption : les campagnes en cours repartent de l'état enregistré.
  await recoverRunning(deps);
  return {
    deps,
    boss,
    async stop() {
      await boss.stop({ graceful: true, timeout: 10_000 });
      await pool.end();
    },
  };
}

if (process.argv[1]?.endsWith("worker/index.ts")) {
  const url = process.env.DATABASE_URL;
  if (!url) {
    console.error("DATABASE_URL absente : le worker ne démarre pas.");
    process.exit(1);
  }
  const worker = await startWorker(url);
  console.log("Worker démarré. Ctrl+C pour arrêter.");
  const shutdown = async () => {
    await worker.stop();
    process.exit(0);
  };
  process.on("SIGINT", shutdown);
  process.on("SIGTERM", shutdown);
}
