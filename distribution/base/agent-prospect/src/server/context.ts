import type { PgBoss } from "pg-boss";
import { getDb, getPool } from "../db/client";
import type { Deps } from "../engine/deps";
import { bossQueue, createBoss } from "../engine/queue";
import { buildDeps } from "../engine/runtime";

const g = globalThis as unknown as { __agentBoss?: Promise<PgBoss> };

/** Dépendances côté serveur web : il met des jobs en file, le worker séparé les exécute. */
export async function getDeps(): Promise<Deps> {
  const url = process.env.DATABASE_URL;
  if (!url) throw new Error("DATABASE_URL absente : la base PostgreSQL n'est pas configurée.");
  g.__agentBoss ??= createBoss(url);
  return buildDeps(getDb(), getPool(), bossQueue(await g.__agentBoss));
}

export function integrations() {
  const env = process.env;
  const openai = env.ANTHROPIC_API_KEY || ["OPENAI_API_KEY", "OPENAI_MODEL_SEARCH", "OPENAI_MODEL_VISIBILITY", "OPENAI_MODEL_ANALYST"].every((k) => env[k]) ? [] : ["ANTHROPIC_API_KEY"];
  return {
    openaiMissing: openai,
    pricing: !!env.PRICING_JSON,
    publicUrl: env.APP_PUBLIC_URL && /^https:\/\//.test(env.APP_PUBLIC_URL) ? env.APP_PUBLIC_URL : null,
    password: !!env.DASHBOARD_PASSWORD,
  };
}
