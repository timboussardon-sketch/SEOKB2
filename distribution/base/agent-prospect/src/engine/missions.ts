import { and, asc, eq, gte, inArray, sql } from "drizzle-orm";
import { schema } from "../db/client";
import { businessDaysBetween, canSendNow, nextSegment, parisClock, type MissionSettings } from "../core/mission";
import { FOLLOWUP_DELAY_BUSINESS_DAYS, FOLLOWUPS } from "../prompts/followups";
import type { MailConfig, Mailer } from "../net/resend";
import { createCampaign, startCampaign } from "./campaign";
import type { Deps } from "./deps";
import { sendApprovedEmail, sendFollowup } from "./outreach";
import { approveDraft } from "./review";

type Mission = typeof schema.missions.$inferSelect;

async function note(deps: Deps, m: Mission, step: string, message: string, patch: Partial<Mission> = {}) {
  const entry = { at: deps.now().toISOString(), step, message };
  await deps.db.update(schema.missions).set({ ...patch, log: sql`${schema.missions.log} || ${JSON.stringify([entry])}::jsonb` }).where(eq(schema.missions.id, m.id));
}

async function missionOfDay(deps: Deps, s: MissionSettings, day: string): Promise<Mission> {
  await deps.db.insert(schema.missions).values({ day, target_sends: s.dailySends }).onConflictDoNothing();
  return (await deps.db.select().from(schema.missions).where(eq(schema.missions.day, day)))[0];
}

/** Échec réseau avant toute réponse de Resend : l'email n'est pas parti, il repasse au prochain créneau. La clé d'idempotence empêche un doublon. */
const NETWORK_FAILURE = /Unable to fetch data|could not be resolved|fetch failed|ECONNRESET|ECONNREFUSED|ETIMEDOUT|ENOTFOUND|EAI_AGAIN/i;

/**
 * Emails prêts à partir : campagne réelle, contrôle factuel vert, destinataire, aucun blocage, jamais envoyés (ou échoués sur le réseau).
 * Les plus anciens d'abord.
 */
export async function sendableProspects(deps: Deps): Promise<string[]> {
  const rows = await deps.db
    .select({ id: schema.prospects.id, fact_check: schema.email_drafts.fact_check, blockers: schema.email_drafts.blockers, recipient: schema.email_drafts.recipient, outreach: schema.outreach.id, outreachStatus: schema.outreach.status, outreachError: schema.outreach.error })
    .from(schema.prospects)
    .innerJoin(schema.campaigns, eq(schema.campaigns.id, schema.prospects.campaign_id))
    .innerJoin(schema.email_drafts, eq(schema.email_drafts.prospect_id, schema.prospects.id))
    .leftJoin(schema.outreach, eq(schema.outreach.prospect_id, schema.prospects.id))
    .where(and(eq(schema.campaigns.simulation, false), inArray(schema.prospects.state, ["READY_FOR_REVIEW", "APPROVED"])))
    .orderBy(asc(schema.prospects.updated_at));
  return rows
    .filter((r) => !r.outreach || (r.outreachStatus === "FAILED" && NETWORK_FAILURE.test(r.outreachError ?? "")))
    .filter((r) => (r.fact_check as { ok?: boolean } | null)?.ok && !r.blockers.length && r.recipient)
    .map((r) => r.id);
}

/** Garde un stock d'emails prêts pour aujourd'hui et demain. Une seule campagne de mission tourne à la fois. */
async function pipeline(deps: Deps, s: MissionSettings, m: Mission, opts: { simulation: boolean }): Promise<void> {
  const real = await deps.db.select().from(schema.campaigns).where(eq(schema.campaigns.simulation, opts.simulation));
  const running = real.filter((c) => c.status === "RUNNING");
  const stock = (await sendableProspects(deps)).length;
  const need = Math.max(0, s.dailySends - m.sent) + s.dailySends - stock;
  if (running.length) return;
  if (need <= 0) return note(deps, m, "stock", `${stock} emails prêts, aucune campagne à lancer`, { last_pipeline_at: deps.now() });
  const lastRun = new Map<string, number>();
  for (const c of real) lastRun.set(`${c.config.practice_area}|${c.config.location}`, Math.max(lastRun.get(`${c.config.practice_area}|${c.config.location}`) ?? -1, c.created_at.getTime()));
  const { segment, city } = nextSegment(s.cities, lastRun);
  const target = Math.min(30, need);
  const c = await createCampaign(deps, {
    name: `Mission ${m.day} : ${segment.label}, ${city}`,
    objectiveText: `Mission du ${m.day} : ${target} emails prêts`,
    simulation: opts.simulation,
    config: {
      practice_area: segment.practice_area, subspecialties: segment.subspecialties, location: city, client_type: segment.client_type,
      target_count: target, goal_type: "EMAIL_READY_PROSPECTS", visibility_mode: "OPENAI_CODEX_WEB_SEARCH",
      max_discovery_rounds: 8, max_candidates_per_round: 20, max_total_discovery_results: 200,
    },
  });
  await startCampaign(deps, c.id);
  await note(deps, m, "campagne", `${stock} emails prêts : campagne lancée sur ${segment.label}, ${city}, objectif ${target}`, { last_pipeline_at: deps.now(), campaign_ids: [...m.campaign_ids, c.id] });
}

async function sendOne(deps: Deps, s: MissionSettings, m: Mission, mail: { mailer: Mailer; cfg: MailConfig }): Promise<void> {
  const gate = canSendNow(s, deps.now(), m.sent, m.last_send_at);
  if (!gate.ok) return;
  const [next] = await sendableProspects(deps);
  if (!next) return;
  const [p] = await deps.db.select().from(schema.prospects).where(eq(schema.prospects.id, next));
  const [firm] = await deps.db.select().from(schema.firms).where(eq(schema.firms.id, p.firm_id));
  try {
    // L'agent approuve lui-même la version contrôlée (décision de l'opérateur du 2026-10-02), puis l'envoie.
    if (p.state === "READY_FOR_REVIEW") await approveDraft(deps, p.id);
    await sendApprovedEmail(deps, mail.mailer, mail.cfg, p.id);
    await note(deps, m, "envoi", `Envoyé à ${firm.name ?? firm.canonical_domain}`, { sent: m.sent + 1, last_send_at: deps.now() });
  } catch (err) {
    // L'échec compte dans l'espacement : un destinataire refusé ne bloque pas la file, il n'est pas retenté en boucle.
    await note(deps, m, "erreur", `${firm.name ?? firm.canonical_domain} : ${err instanceof Error ? err.message : String(err)}`, { last_send_at: deps.now() });
  }
}

/**
 * Relances dues : email parti (remis ou envoyé), sans réponse, moins de 1 + FOLLOWUPS.length messages, dernier envoi il y a au moins
 * FOLLOWUP_DELAY_BUSINESS_DAYS jours ouvrés, et texte de cette relance fourni. Les plus anciennes d'abord.
 */
export async function followupsDue(deps: Deps, followups: (string | null)[] = FOLLOWUPS): Promise<{ id: string; n: number; text: string }[]> {
  const rows = await deps.db.select().from(schema.outreach).where(inArray(schema.outreach.status, ["SENT", "DELIVERED"])).orderBy(asc(schema.outreach.last_sent_at));
  const now = deps.now();
  return rows
    .filter((o) => !o.replied_at && o.last_sent_at && o.messages_sent >= 1 && o.messages_sent <= followups.length)
    .filter((o) => businessDaysBetween(o.last_sent_at!, now) >= FOLLOWUP_DELAY_BUSINESS_DAYS)
    .map((o) => ({ id: o.id, n: o.messages_sent, text: followups[o.messages_sent - 1] }))
    .filter((x): x is { id: string; n: number; text: string } => !!x.text);
}

/** Les réponses sont-elles relevées ? Sans relevé Gmail réussi depuis 30 min, une relance risquerait de partir chez quelqu'un qui a déjà répondu. */
async function repliesTracked(deps: Deps): Promise<boolean> {
  const [g] = await deps.db.select().from(schema.gmail_account);
  return !!g?.last_sync_at && !g.last_sync_error && deps.now().getTime() - g.last_sync_at.getTime() < 30 * 60_000;
}

/** Une relance par créneau, quand aucun premier email n'est parti à ce créneau. */
async function followupOne(deps: Deps, s: MissionSettings, m: Mission, mail: { mailer: Mailer; cfg: MailConfig }, followups: (string | null)[]): Promise<void> {
  const gate = canSendNow({ ...s, dailySends: Number.MAX_SAFE_INTEGER }, deps.now(), m.sent, m.last_send_at);
  if (!gate.ok || !(await repliesTracked(deps))) return;
  const [due] = await followupsDue(deps, followups);
  if (!due) return;
  try {
    await sendFollowup(deps, mail.mailer, mail.cfg, due.id, due.n, due.text);
    await note(deps, m, "relance", `Relance ${due.n} envoyée`, { last_send_at: deps.now() });
  } catch (err) {
    await note(deps, m, "erreur", `Relance ${due.n} : ${err instanceof Error ? err.message : String(err)}`, { last_send_at: deps.now() });
  }
}

/** Rapport du soir envoyé à l'opérateur : ce qui est parti, ce qui a répondu, ce qui l'attend. */
export async function dailyReport(deps: Deps, m: Mission): Promise<{ subject: string; text: string }> {
  const today = (d: Date | null) => !!d && parisClock(d).day === m.day;
  const out = await deps.db.select().from(schema.outreach);
  const firmOf = async (prospectId: string) => {
    const [p] = await deps.db.select().from(schema.prospects).where(eq(schema.prospects.id, prospectId));
    const [f] = await deps.db.select().from(schema.firms).where(eq(schema.firms.id, p.firm_id));
    return f.name ?? f.canonical_domain;
  };
  const sentToday = out.filter((o) => today(o.first_sent_at));
  const repliesToday = out.filter((o) => today(o.replied_at));
  const reviews = await deps.db.select().from(schema.review_items).where(eq(schema.review_items.status, "OPEN"));
  const stock = (await sendableProspects(deps)).length;
  const signed = out.filter((o) => o.deal_stage === "SIGNED").length;
  const lines = [
    `Mission du ${m.day}`,
    "",
    `Envoyés aujourd'hui : ${sentToday.length} sur ${m.target_sends}`,
    ...(await Promise.all(sentToday.map(async (o) => `- ${await firmOf(o.prospect_id)} (${o.recipient})`))),
    "",
    `Réponses reçues aujourd'hui : ${repliesToday.length}`,
    ...(await Promise.all(repliesToday.map(async (o) => `- ${await firmOf(o.prospect_id)} : ${o.status === "OPTED_OUT" ? "opposition" : "à traiter"}. « ${o.reply_excerpt ?? ""} »`))),
    "",
    `Total : ${out.filter((o) => o.first_sent_at).length} cabinets contactés, ${out.filter((o) => o.replied_at).length} réponses, ${out.filter((o) => o.deal_stage === "MEETING").length} rendez-vous, ${out.filter((o) => o.deal_stage === "PROPOSAL").length} propositions, ${signed} contrats signés.`,
    `Stock : ${stock} emails prêts pour les prochains envois.`,
    `À trancher dans Revue : ${reviews.length}.`,
    "",
    "Journal :",
    ...m.log.slice(-30).map((e) => `- ${e.at.slice(11, 16)} UTC, ${e.step} : ${e.message}`),
  ];
  return { subject: `Agent avocats, ${m.day} : ${sentToday.length} envoyés, ${repliesToday.length} réponses`, text: lines.join("\n") };
}

/**
 * Un tour de mission, appelé chaque minute par le worker. Chaque action ne se fait qu'une fois au bon moment :
 * le stock au plus une fois par heure, un envoi par espacement, le rapport une fois le soir.
 */
export async function missionTick(deps: Deps, s: MissionSettings, mail: { mailer: Mailer; cfg: MailConfig } | null, opts: { simulation?: boolean; followups?: (string | null)[] } = {}): Promise<void> {
  if (!s.enabled) return;
  const clock = parisClock(deps.now());
  if (clock.hour < 7) return;
  let m = await missionOfDay(deps, s, clock.day);
  if (!m.last_pipeline_at || deps.now().getTime() - m.last_pipeline_at.getTime() >= 3600_000) {
    await pipeline(deps, s, m, { simulation: opts.simulation ?? false });
    await deps.db.update(schema.missions).set({ last_pipeline_at: deps.now() }).where(eq(schema.missions.id, m.id));
    m = (await deps.db.select().from(schema.missions).where(eq(schema.missions.id, m.id)))[0];
  }
  if (mail) {
    const before = m.last_send_at?.getTime() ?? 0;
    await sendOne(deps, s, m, mail);
    m = (await deps.db.select().from(schema.missions).where(eq(schema.missions.id, m.id)))[0];
    if ((m.last_send_at?.getTime() ?? 0) === before) await followupOne(deps, s, m, mail, opts.followups ?? FOLLOWUPS);
  }
  if (mail && clock.hour >= s.reportAt && !m.report_sent_at) {
    m = (await deps.db.select().from(schema.missions).where(eq(schema.missions.id, m.id)))[0];
    const r = await dailyReport(deps, m);
    await mail.mailer.send({ from: mail.cfg.from, replyTo: mail.cfg.replyTo, to: mail.cfg.replyTo, subject: r.subject, text: r.text, headers: {}, idempotencyKey: `agent-avocats-rapport-${m.day}` });
    await note(deps, m, "rapport", `Rapport envoyé à ${mail.cfg.replyTo}`, { report_sent_at: deps.now() });
  }
}

/** Suite commerciale notée par l'opérateur depuis /suivi. */
export async function setDealStage(deps: Deps, prospectId: string, stage: "MEETING" | "PROPOSAL" | "SIGNED" | "LOST" | null): Promise<void> {
  await deps.db.update(schema.outreach).set({ deal_stage: stage, deal_updated_at: deps.now() }).where(eq(schema.outreach.prospect_id, prospectId));
}

export async function recentMissions(deps: Pick<Deps, "db">, days = 14) {
  const from = new Date(Date.now() - days * 86_400_000).toISOString().slice(0, 10);
  return deps.db.select().from(schema.missions).where(gte(schema.missions.day, from)).orderBy(sql`${schema.missions.day} desc`);
}
