// Crée et lance une campagne réelle depuis la ligne de commande : npx tsx --env-file=.env.local scripts/run-campaign.ts '<config JSON>'
import { createDb } from "../src/db/client";
import { createCampaign, startCampaign } from "../src/engine/campaign";
import { bossQueue, createBoss } from "../src/engine/queue";
import { buildDeps } from "../src/engine/runtime";

const url = process.env.DATABASE_URL!;
const { db, pool } = createDb(url);
const boss = await createBoss(url);
const deps = buildDeps(db, pool, bossQueue(boss));
const config = JSON.parse(process.argv[2]);
const c = await createCampaign(deps, { name: process.argv[3] ?? "Campagne réelle", config, simulation: false });
await startCampaign(deps, c.id);
console.log(c.id);
await boss.stop();
await pool.end();
