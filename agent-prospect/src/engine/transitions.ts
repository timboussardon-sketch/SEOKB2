import { and, eq } from "drizzle-orm";
import { schema } from "../db/client";
import { assertTransition, type ProspectState, type ReviewReason } from "../core/states";
import type { Deps, Prospect } from "./deps";
import { logEvent } from "./events";

type Patch = Partial<typeof schema.prospects.$inferInsert>;

/** Seul point de changement d'état d'un prospect : la transition est validée, persistée et journalisée. */
export async function setState(deps: Deps, prospect: Prospect, to: ProspectState, patch: Patch = {}): Promise<Prospect> {
  if (prospect.state !== to) assertTransition(prospect.state, to);
  const [updated] = await deps.db
    .update(schema.prospects)
    .set({ ...patch, state: to, updated_at: deps.now() })
    .where(eq(schema.prospects.id, prospect.id))
    .returning();
  if (prospect.state !== to) await logEvent(deps.db, { campaignId: prospect.campaign_id, prospectId: prospect.id, type: "STATE_CHANGED", data: { from: prospect.state, to } });
  return updated;
}

/** L'agent s'arrête sur ce prospect et dit pourquoi. `resume` est l'état repris si un humain valide. */
export async function sendToReview(deps: Deps, prospect: Prospect, reason: ReviewReason, detail: string, resume: ProspectState, patch: Patch = {}): Promise<Prospect> {
  const R = schema.review_items;
  const [open] = await deps.db.select({ id: R.id }).from(R).where(and(eq(R.prospect_id, prospect.id), eq(R.reason, reason), eq(R.status, "OPEN")));
  if (open) await deps.db.update(R).set({ detail }).where(eq(R.id, open.id));
  else await deps.db.insert(R).values({ campaign_id: prospect.campaign_id, prospect_id: prospect.id, reason, detail });
  return setState(deps, prospect, "HUMAN_REVIEW_REQUIRED", { ...patch, review_reason: reason, resume_state: resume });
}
