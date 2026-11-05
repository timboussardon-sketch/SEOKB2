import type { Db } from "../db/client";
import { schema } from "../db/client";

export async function logEvent(db: Db | Parameters<Parameters<Db["transaction"]>[0]>[0], e: { campaignId?: string | null; prospectId?: string | null; type: string; data?: unknown }): Promise<void> {
  await db.insert(schema.event_log).values({ campaign_id: e.campaignId ?? null, prospect_id: e.prospectId ?? null, type: e.type, data: (e.data ?? null) as object | null });
}
