import dns from "node:dns/promises";
import type pg from "pg";
import { lockerFor, type Db } from "../db/client";
import { HttpFetcher } from "../net/fetcher";
import { claudeProviders } from "../providers/claude";
import { CodexVisibility } from "../providers/codex";
import { openaiProviders } from "../providers/openai";
import { simulationProviders } from "../providers/simulation";
import type { Campaign, Deps, Queue, Runtime } from "./deps";
import { loadPriceTable } from "./pricing";

async function resolveMx(domain: string): Promise<boolean | null> {
  try {
    return (await dns.resolveMx(domain)).length > 0;
  } catch (err) {
    const code = (err as { code?: string }).code;
    // Domaine sans MX : non routable. Toute autre erreur : contrôle non concluant.
    return code === "ENOTFOUND" || code === "ENODATA" ? false : null;
  }
}

/** Assemble les dépendances réelles depuis l'environnement. Une intégration non configurée échoue à l'usage, avec son motif. */
export function buildDeps(db: Db, pool: pg.Pool, queue: Queue, env: Record<string, string | undefined> = process.env): Deps {
  const cache = new Map<string, Runtime>();
  let real: Runtime | null = null;
  let codex: Runtime | null = null;
  const publicUrl = env.APP_PUBLIC_URL && /^https:\/\//.test(env.APP_PUBLIC_URL) ? env.APP_PUBLIC_URL : null;
  return {
    db,
    queue,
    prices: loadPriceTable(env.PRICING_JSON),
    globalDailyUsd: Number(env.MAX_DAILY_COST_USD ?? 10),
    publicUrl,
    tryLock: lockerFor(pool),
    runtimeFor(campaign: Campaign): Runtime {
      if (campaign.simulation) {
        let rt = cache.get(campaign.id);
        if (!rt) {
          const cfg = campaign.config;
          const sim = simulationProviders({ practice: cfg.practice_area, clientType: cfg.client_type, city: cfg.location }, Number(env.SIMULATION_WORLD_SIZE ?? 60));
          rt = { providers: sim.providers, fetcher: sim.fetcher, resolveMx: async () => null };
          cache.set(campaign.id, rt);
        }
        return rt;
      }
      // Claude d'abord ; OpenAI seulement si c'est la seule intégration configurée.
      real ??= { providers: env.ANTHROPIC_API_KEY || !env.OPENAI_API_KEY ? claudeProviders(env) : openaiProviders(env), fetcher: new HttpFetcher(), resolveMx };
      // La mesure de présence peut passer par Codex (modèle d'OpenAI) quand la campagne le demande ; découverte et analyse restent inchangées.
      if (campaign.config.visibility_mode === "OPENAI_CODEX_WEB_SEARCH") {
        codex ??= { ...real, providers: { ...real.providers, visibility: new CodexVisibility({ model: env.CODEX_MODEL || undefined }) } };
        return codex;
      }
      return real;
    },
    sleep: (ms) => new Promise((r) => setTimeout(r, ms)),
    now: () => new Date(),
    random: Math.random,
  };
}
