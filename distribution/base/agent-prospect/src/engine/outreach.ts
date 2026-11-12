import { and, desc, eq, gte, inArray, isNull, ne } from "drizzle-orm";
import { schema } from "../db/client";
import { AppError } from "../core/errors";
import { bannerCid, presentEmail } from "../core/email-presentation";
import { replyState, statusAfterDelivery, type OutreachStatus } from "../core/outreach";
import { exchangeCode, httpInbox, oauthApp, profileEmail, refreshAccess, type Inbox, type OAuthApp } from "../net/gmail";
import { mailConfig, resendMailer, type MailConfig, type Mailer } from "../net/resend";
import type { Deps } from "./deps";
import { logEvent } from "./events";
import { suppressProspect } from "./review";

type Row = typeof schema.outreach.$inferSelect;

async function prospectOf(deps: Deps, row: Row) {
  return (await deps.db.select().from(schema.prospects).where(eq(schema.prospects.id, row.prospect_id)))[0];
}

async function setStatus(deps: Deps, row: Row, status: OutreachStatus, patch: Partial<Row> = {}) {
  await deps.db.update(schema.outreach).set({ ...patch, status, synced_at: deps.now() }).where(eq(schema.outreach.id, row.id));
  if (status === row.status) return;
  const p = await prospectOf(deps, row);
  await logEvent(deps.db, { campaignId: p.campaign_id, prospectId: p.id, type: `OUTREACH_${status}`, data: patch.delivery_event ? { event: patch.delivery_event } : null });
  // Opposition ou plainte : le cabinet sort de toutes les campagnes et ne sera plus sollicité.
  if (status === "OPTED_OUT" && p.state !== "SUPPRESSED") await suppressProspect(deps, p.id, "Opposition reçue après l'email");
}

/**
 * Envoie par Resend la version approuvée de l'email. Refusé si l'approbation ne porte plus sur cette version,
 * si le destinataire s'est opposé, si l'email est déjà parti ou si le plafond du jour est atteint.
 */
export async function sendApprovedEmail(deps: Deps, mailer: Mailer, cfg: MailConfig, prospectId: string): Promise<void> {
  const [prospect] = await deps.db.select().from(schema.prospects).where(eq(schema.prospects.id, prospectId));
  if (!prospect || prospect.state !== "APPROVED") throw new AppError("INVALID_INPUT", "Seul un email approuvé peut partir");
  const [campaign] = await deps.db.select().from(schema.campaigns).where(eq(schema.campaigns.id, prospect.campaign_id));
  if (campaign.simulation) throw new AppError("INVALID_INPUT", "Campagne de simulation : aucun envoi");
  const [draft] = await deps.db.select().from(schema.email_drafts).where(eq(schema.email_drafts.prospect_id, prospectId));
  const [approval] = await deps.db.select().from(schema.approvals)
    .where(and(eq(schema.approvals.draft_id, draft.id), isNull(schema.approvals.invalidated_at)))
    .orderBy(desc(schema.approvals.approved_at)).limit(1);
  if (!approval || approval.content_hash !== draft.content_hash || !approval.recipient) throw new AppError("INVALID_INPUT", "L'approbation ne porte pas sur cette version de l'email");
  const [firm] = await deps.db.select().from(schema.firms).where(eq(schema.firms.id, prospect.firm_id));
  const recipient = approval.recipient.toLowerCase();
  const blocked = await deps.db.select().from(schema.suppressions).where(inArray(schema.suppressions.value, [recipient, recipient.split("@")[1], firm.canonical_domain]));
  if (blocked.length) throw new AppError("INVALID_INPUT", "Destinataire en opposition : aucun envoi");
  const dayStart = new Date(deps.now());
  dayStart.setHours(0, 0, 0, 0);
  const today = await deps.db.select({ id: schema.outreach.id }).from(schema.outreach).where(and(gte(schema.outreach.created_at, dayStart), ne(schema.outreach.status, "FAILED")));
  if (today.length >= cfg.maxPerDay) throw new AppError("INVALID_INPUT", `Plafond de ${cfg.maxPerDay} envois par jour atteint`);

  const values = { draft_id: draft.id, approval_id: approval.id, sender: cfg.from, reply_to: cfg.replyTo, recipient: approval.recipient, subject: draft.subject, status: "SENDING", error: null, created_at: deps.now() };
  const [existing] = await deps.db.select().from(schema.outreach).where(eq(schema.outreach.prospect_id, prospectId));
  if (existing && existing.status !== "FAILED") throw new AppError("INVALID_INPUT", "Cet email est déjà parti");
  // La ligne SENDING est posée avant l'appel : l'index unique empêche un second envoi lancé en parallèle.
  const [row] = existing
    ? await deps.db.update(schema.outreach).set(values).where(and(eq(schema.outreach.id, existing.id), eq(schema.outreach.status, "FAILED"))).returning()
    : await deps.db.insert(schema.outreach).values({ prospect_id: prospectId, ...values }).onConflictDoNothing().returning();
  if (!row) throw new AppError("INVALID_INPUT", "Envoi déjà en cours");

  try {
    const { id } = await mailer.send({
      from: cfg.from, replyTo: cfg.replyTo, to: approval.recipient, subject: draft.subject, ...presentEmail(draft.body, bannerCid()),
      headers: { "List-Unsubscribe": `<mailto:${cfg.replyTo}?subject=stop>` },
      idempotencyKey: `agent-prospection-${approval.id}`,
    });
    const now = deps.now();
    await deps.db.update(schema.outreach).set({ status: "SENT", provider_message_id: id, delivery_event: "sent", messages_sent: 1, first_sent_at: now, last_sent_at: now }).where(eq(schema.outreach.id, row.id));
    await logEvent(deps.db, { campaignId: prospect.campaign_id, prospectId, type: "OUTREACH_SENT", data: { id, to: approval.recipient } });
  } catch (err) {
    const message = err instanceof Error ? err.message : String(err);
    await deps.db.update(schema.outreach).set({ status: "FAILED", error: message }).where(eq(schema.outreach.id, row.id));
    throw new AppError("INVALID_INPUT", `Envoi refusé : ${message}`);
  }
}

/**
 * Relance n°`n` (1 ou 2) d'un email parti sans réponse. Même destinataire, objet « Re: », texte fourni par l'opérateur.
 * La clé d'idempotence par relance empêche un doublon chez Resend.
 */
export async function sendFollowup(deps: Deps, mailer: Mailer, cfg: MailConfig, outreachId: string, n: number, text: string): Promise<void> {
  const [o] = await deps.db.select().from(schema.outreach).where(eq(schema.outreach.id, outreachId));
  if (!o || !["SENT", "DELIVERED"].includes(o.status) || o.replied_at || o.messages_sent !== n) throw new AppError("INVALID_INPUT", "Relance non permise sur cet envoi");
  const blocked = await deps.db.select().from(schema.suppressions).where(inArray(schema.suppressions.value, [o.recipient.toLowerCase(), o.recipient.toLowerCase().split("@")[1]]));
  if (blocked.length) throw new AppError("INVALID_INPUT", "Destinataire en opposition : aucune relance");
  const { id } = await mailer.send({
    from: cfg.from, replyTo: cfg.replyTo, to: o.recipient, subject: `Re: ${o.subject}`, ...presentEmail(text, bannerCid()),
    headers: { "List-Unsubscribe": `<mailto:${cfg.replyTo}?subject=stop>` },
    idempotencyKey: `agent-prospection-relance-${o.id}-${n}`,
  });
  await deps.db.update(schema.outreach).set({ messages_sent: n + 1, last_sent_at: deps.now() }).where(eq(schema.outreach.id, o.id));
  await logEvent(deps.db, { prospectId: o.prospect_id, type: "FOLLOWUP_SENT", data: { id, n, to: o.recipient } });
}

/** Relit chez Resend le dernier évènement de chaque email parti : remis, rebond, plainte. */
export async function syncDelivery(deps: Deps, mailer: Mailer): Promise<number> {
  const rows = await deps.db.select().from(schema.outreach).where(inArray(schema.outreach.status, ["SENT", "DELIVERED"]));
  for (const row of rows) {
    if (!row.provider_message_id) continue;
    const event = await mailer.lastEvent(row.provider_message_id);
    await setStatus(deps, row, statusAfterDelivery(row.status as OutreachStatus, event), { delivery_event: event });
  }
  return rows.length;
}

/** Cherche dans Gmail les messages reçus du cabinet depuis l'envoi. */
export async function syncReplies(deps: Deps, inbox: Inbox): Promise<number> {
  const rows = await deps.db.select().from(schema.outreach).where(inArray(schema.outreach.status, ["SENT", "DELIVERED", "REPLIED"]));
  let found = 0;
  for (const row of rows) {
    if (!row.first_sent_at || row.reply_source === "MANUAL") continue;
    const domain = row.recipient.split("@")[1];
    const messages = await inbox.search(`from:(${row.recipient} OR ${domain}) after:${Math.floor(row.first_sent_at.getTime() / 1000)}`);
    const r = replyState(messages, row.recipient, row.first_sent_at);
    if (!r) continue;
    found++;
    await setStatus(deps, row, r.status, { replied_at: r.repliedAt, reply_excerpt: r.excerpt, messages_received: r.received, reply_source: "GMAIL" });
  }
  return found;
}

/** Réponse notée à la main, quand Gmail n'est pas connecté ou qu'elle est arrivée ailleurs. */
export async function markReply(deps: Deps, prospectId: string, kind: "REPLIED" | "OPTED_OUT"): Promise<void> {
  const [row] = await deps.db.select().from(schema.outreach).where(eq(schema.outreach.prospect_id, prospectId));
  if (!row?.first_sent_at) throw new AppError("INVALID_INPUT", "Aucun email parti pour ce cabinet");
  await setStatus(deps, row, kind, { replied_at: row.replied_at ?? deps.now(), reply_source: "MANUAL", messages_received: Math.max(row.messages_received, 1) });
}

export async function connectedInbox(deps: Deps, app: OAuthApp | null = oauthApp()): Promise<{ inbox: Inbox; email: string } | null> {
  if (!app) return null;
  const [acc] = await deps.db.select().from(schema.gmail_account);
  if (!acc) return null;
  const getToken = async () => {
    const [cur] = await deps.db.select().from(schema.gmail_account);
    if (cur.access_token && cur.access_expires_at && cur.access_expires_at.getTime() - 60_000 > deps.now().getTime()) return cur.access_token;
    const t = await refreshAccess(app, cur.refresh_token);
    await deps.db.update(schema.gmail_account).set({ access_token: t.access_token, access_expires_at: new Date(deps.now().getTime() + t.expires_in * 1000) });
    return t.access_token;
  };
  return { inbox: httpInbox(getToken), email: acc.email };
}

export async function connectGmail(deps: Deps, app: OAuthApp, code: string, redirectUri: string): Promise<string> {
  const t = await exchangeCode(app, code, redirectUri);
  if (!t.refresh_token) throw new AppError("INVALID_INPUT", "Google n'a pas rendu de jeton de rafraîchissement : retire l'accès de l'app dans ton compte Google et recommence");
  const email = await profileEmail(t.access_token);
  const values = { email, refresh_token: t.refresh_token, access_token: t.access_token, access_expires_at: new Date(deps.now().getTime() + t.expires_in * 1000), connected_at: deps.now(), last_sync_error: null };
  await deps.db.insert(schema.gmail_account).values({ id: "default", ...values }).onConflictDoUpdate({ target: schema.gmail_account.id, set: values });
  return email;
}

export function mailerFromEnv(env: Record<string, string | undefined> = process.env): { mailer: Mailer; cfg: MailConfig } | null {
  const cfg = mailConfig(env);
  return cfg ? { mailer: resendMailer(env.RESEND_API_KEY!), cfg } : null;
}

/** Relevé complet : remise chez Resend, réponses dans Gmail. L'erreur Gmail est gardée pour /suivi. */
export async function runSync(deps: Deps, env: Record<string, string | undefined> = process.env): Promise<void> {
  const m = mailerFromEnv(env);
  if (m) await syncDelivery(deps, m.mailer);
  const conn = await connectedInbox(deps, oauthApp(env));
  if (!conn) return;
  try {
    await syncReplies(deps, conn.inbox);
    await deps.db.update(schema.gmail_account).set({ last_sync_at: deps.now(), last_sync_error: null });
  } catch (err) {
    await deps.db.update(schema.gmail_account).set({ last_sync_error: err instanceof Error ? err.message : String(err) });
  }
}
