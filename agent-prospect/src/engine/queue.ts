import { PgBoss } from "pg-boss";
import { JOB_NAMES, type JobData, type JobName, type Queue } from "./deps";

export async function createBoss(url: string): Promise<PgBoss> {
  const boss = new PgBoss({ connectionString: url, schema: "pgboss" });
  boss.on("error", (err: unknown) => console.error("[pg-boss]", err));
  await boss.start();
  for (const name of JOB_NAMES) {
    // Un job interrompu (arrêt du process, expiration) est rejoué, trois fois au plus, avec un délai croissant.
    await boss.createQueue(name, { retryLimit: 3, retryDelay: 5, retryBackoff: true, retryDelayMax: 300, expireInSeconds: 1800 });
  }
  return boss;
}

export function bossQueue(boss: PgBoss): Queue {
  return {
    async send(name: JobName, data: JobData) {
      await boss.send(name, data);
    },
  };
}
