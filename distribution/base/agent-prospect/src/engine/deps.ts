import type { Db } from "../db/client";
import type { schema } from "../db/client";
import type { Fetcher } from "../net/fetcher";
import type { Providers } from "../providers/types";
import type { PriceTable } from "./pricing";

export const JOB_NAMES = ["campaign-tick", "discovery-round", "prospect-advance"] as const;
export type JobName = (typeof JOB_NAMES)[number];
export interface JobData {
  campaignId: string;
  prospectId?: string;
}

export interface Queue {
  send(name: JobName, data: JobData): Promise<void>;
}

export type Campaign = typeof schema.campaigns.$inferSelect;
export type Prospect = typeof schema.prospects.$inferSelect;
export type Firm = typeof schema.firms.$inferSelect;
export type SitePage = typeof schema.site_pages.$inferSelect;

export interface Runtime {
  providers: Providers;
  fetcher: Fetcher;
  /** true / false si le DNS a répondu, null si le contrôle n'a pas pu être fait. */
  resolveMx: (domain: string) => Promise<boolean | null>;
}

export interface Deps {
  db: Db;
  queue: Queue;
  prices: PriceTable;
  /** Plafond de dépense quotidien, toutes campagnes confondues. */
  globalDailyUsd: number;
  /** URL publique https de l'application, pour les liens de pré-audit. null = pas de lien externe. */
  publicUrl: string | null;
  runtimeFor: (campaign: Campaign) => Runtime;
  /** Verrou de session PostgreSQL : rendu si la clé est libre, null sinon. Il tombe de lui-même si le process meurt. */
  tryLock: (key: string) => Promise<(() => Promise<void>) | null>;
  sleep: (ms: number) => Promise<void>;
  now: () => Date;
  random: () => number;
}
