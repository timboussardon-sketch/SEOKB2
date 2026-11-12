import { eq } from "drizzle-orm";
import { afterAll, beforeEach, describe, expect, test } from "vitest";
import { replyState, statusAfterDelivery, type InboxMessage } from "../src/core/outreach";
import { schema, type Db } from "../src/db/client";
import { createCampaign, startCampaign } from "../src/engine/campaign";
import { markReply, sendApprovedEmail, sendFollowup, syncDelivery, syncReplies } from "../src/engine/outreach";
import { approveDraft, editDraft } from "../src/engine/review";
import type { Inbox } from "../src/net/gmail";
import type { Mailer, OutgoingEmail } from "../src/net/resend";
import { baseConfig, closeDb, drain, testDb, testEnv } from "./helpers";

const SENT_AT = new Date(Date.UTC(2026, 9, 2, 9));
const msg = (from: string, day: number, snippet = ""): InboxMessage => ({ id: `${from}${day}`, from, date: new Date(Date.UTC(2026, 9, day, 10)), snippet });
const CFG = { from: "Camille Test <camille@exemple.test>", replyTo: "reponses@exemple.test", maxPerDay: 20 };

describe("règles du suivi", () => {
  test("réponse, opposition, autre adresse du cabinet, message antérieur ignoré", () => {
    const to = "x@cabinet.test";
    expect(replyState([], to, SENT_AT)).toBeNull();
    expect(replyState([msg(to, 1, "ancien")], to, SENT_AT)).toBeNull();
    expect(replyState([msg(`Me X <${to}>`, 3, "Oui, envoyez-le")], to, SENT_AT)).toMatchObject({ status: "REPLIED", excerpt: "Oui, envoyez-le", received: 1 });
    expect(replyState([msg("secretariat@cabinet.test", 3, "Transmis à Maître X")], to, SENT_AT)?.status).toBe("REPLIED");
    expect(replyState([msg(to, 3, "STOP")], to, SENT_AT)?.status).toBe("OPTED_OUT");
    expect(replyState([msg(to, 3, "Merci de ne plus nous solliciter")], to, SENT_AT)?.status).toBe("OPTED_OUT");
    // « stop » à l'intérieur d'un mot ne vaut pas opposition
    expect(replyState([msg(to, 3, "Nous sommes à Stopford")], to, SENT_AT)?.status).toBe("REPLIED");
    expect(replyState([msg("y@autre.test", 3, "stop")], to, SENT_AT)).toBeNull();
  });

  test("évènements Resend : une réponse n'est jamais écrasée", () => {
    expect(statusAfterDelivery("SENT", "delivered")).toBe("DELIVERED");
    expect(statusAfterDelivery("SENT", "bounced")).toBe("BOUNCED");
    expect(statusAfterDelivery("DELIVERED", "complained")).toBe("OPTED_OUT");
    expect(statusAfterDelivery("DELIVERED", "sent")).toBe("DELIVERED");
    expect(statusAfterDelivery("REPLIED", "bounced")).toBe("REPLIED");
  });
});

class FakeMailer implements Mailer {
  sent: OutgoingEmail[] = [];
  events = new Map<string, string>();
  fail = false;
  async send(e: OutgoingEmail) {
    if (this.fail) throw new Error("domaine refusé");
    this.sent.push(e);
    const id = `em_${this.sent.length}`;
    this.events.set(id, "sent");
    return { id };
  }
  async lastEvent(id: string) {
    return this.events.get(id) ?? "sent";
  }
}

class FakeInbox implements Inbox {
  messages: InboxMessage[] = [];
  queries: string[] = [];
  async search(q: string) {
    this.queries.push(q);
    return this.messages;
  }
}

let db: Db;
beforeEach(async () => {
  db = await testDb();
});
afterAll(closeDb);

/** Campagne simulée, puis marquée réelle pour pouvoir tester l'envoi avec un faux Resend. */
async function ready() {
  const env = testEnv(db);
  const c = await createCampaign(env.deps, { name: "t", objectiveText: null, config: { ...baseConfig, target_count: 2, max_discovery_rounds: 1 } as never, simulation: true });
  await startCampaign(env.deps, c.id);
  await drain(env);
  await db.update(schema.campaigns).set({ simulation: false }).where(eq(schema.campaigns.id, c.id));
  const ps = (await db.select().from(schema.prospects).where(eq(schema.prospects.campaign_id, c.id))).filter((x) => x.state === "READY_FOR_REVIEW" && x.email_status === "FOUND");
  return { env, p: ps[0], ps };
}
const outreachRow = async () => (await db.select().from(schema.outreach))[0];

describe("envoi par Resend", () => {
  test("version approuvée envoyée une fois, depuis le domaine configuré, réponses vers Gmail", async () => {
    const { env, p } = await ready();
    const mailer = new FakeMailer();
    await expect(sendApprovedEmail(env.deps, mailer, CFG, p.id)).rejects.toThrow(/approuvé/);
    await approveDraft(env.deps, p.id);
    await sendApprovedEmail(env.deps, mailer, CFG, p.id);
    await expect(sendApprovedEmail(env.deps, mailer, CFG, p.id)).rejects.toThrow(/déjà parti/);
    expect(mailer.sent).toHaveLength(1);
    const [draft] = await db.select().from(schema.email_drafts).where(eq(schema.email_drafts.prospect_id, p.id));
    expect(mailer.sent[0]).toMatchObject({ from: CFG.from, replyTo: CFG.replyTo, to: draft.recipient, subject: draft.subject, text: draft.body });
    expect(mailer.sent[0].headers["List-Unsubscribe"]).toBe("<mailto:reponses@exemple.test?subject=stop>");
    expect(mailer.sent[0].html).toContain('href="https://exemple.test"');
    expect(mailer.sent[0].html).toContain('alt="Cabinet Test"');
    expect(mailer.sent[0].html).toContain('src="cid:email-banner"');
    expect(await outreachRow()).toMatchObject({ status: "SENT", messages_sent: 1, provider_message_id: "em_1" });
  });

  test("relance : même bannière embarquée, lien et signature sans ligne d'entreprise", async () => {
    const { env, p } = await ready();
    const mailer = new FakeMailer();
    await approveDraft(env.deps, p.id);
    await sendApprovedEmail(env.deps, mailer, CFG, p.id);
    await sendFollowup(env.deps, mailer, CFG, (await outreachRow()).id, 1, "Bonjour,\n\nCamille Test\nCabinet Test");
    expect(mailer.sent[1].html).toContain('src="cid:email-banner"');
    expect(mailer.sent[1].text).toContain("https://exemple.test");
    expect(mailer.sent[1].text).not.toMatch(/^Cabinet Test$/m);
  });

  test("refus : simulation, version modifiée, opposition, plafond du jour", async () => {
    const { env, p, ps } = await ready();
    const mailer = new FakeMailer();
    await approveDraft(env.deps, p.id);
    await editDraft(env.deps, p.id, { subject: "Autre objet", texts: {} });
    await expect(sendApprovedEmail(env.deps, mailer, CFG, p.id)).rejects.toThrow();

    const q = ps[1];
    await approveDraft(env.deps, q.id);
    await expect(sendApprovedEmail(env.deps, mailer, { ...CFG, maxPerDay: 0 }, q.id)).rejects.toThrow(/Plafond/);
    const [draft] = await db.select().from(schema.email_drafts).where(eq(schema.email_drafts.prospect_id, q.id));
    await db.insert(schema.suppressions).values({ value: draft.recipient!.toLowerCase(), kind: "EMAIL", reason: "test" });
    await expect(sendApprovedEmail(env.deps, mailer, CFG, q.id)).rejects.toThrow(/opposition/);
    await db.delete(schema.suppressions);
    await db.update(schema.campaigns).set({ simulation: true });
    await expect(sendApprovedEmail(env.deps, mailer, CFG, q.id)).rejects.toThrow(/simulation/);
    expect(mailer.sent).toHaveLength(0);
  });

  test("échec Resend : noté, puis nouvel essai possible", async () => {
    const { env, p } = await ready();
    const mailer = new FakeMailer();
    await approveDraft(env.deps, p.id);
    mailer.fail = true;
    await expect(sendApprovedEmail(env.deps, mailer, CFG, p.id)).rejects.toThrow(/domaine refusé/);
    expect(await outreachRow()).toMatchObject({ status: "FAILED", error: "domaine refusé" });
    mailer.fail = false;
    await sendApprovedEmail(env.deps, mailer, CFG, p.id);
    expect((await outreachRow()).status).toBe("SENT");
    expect(await db.select().from(schema.outreach)).toHaveLength(1);
  });

  test("remise, réponse relevée dans Gmail, puis opposition : cabinet retiré", async () => {
    const { env, p } = await ready();
    const mailer = new FakeMailer();
    const inbox = new FakeInbox();
    await approveDraft(env.deps, p.id);
    await sendApprovedEmail(env.deps, mailer, CFG, p.id);
    mailer.events.set("em_1", "delivered");
    await syncDelivery(env.deps, mailer);
    expect((await outreachRow()).status).toBe("DELIVERED");

    const row = await outreachRow();
    inbox.messages = [{ id: "r1", from: row.recipient, date: new Date(row.first_sent_at!.getTime() + 3600_000), snippet: "Bonjour, oui merci" }];
    await syncReplies(env.deps, inbox);
    expect(inbox.queries[0]).toContain(`from:(${row.recipient} OR ${row.recipient.split("@")[1]})`);
    expect(await outreachRow()).toMatchObject({ status: "REPLIED", reply_source: "GMAIL", reply_excerpt: "Bonjour, oui merci" });

    inbox.messages.push({ id: "r2", from: row.recipient, date: new Date(row.first_sent_at!.getTime() + 7200_000), snippet: "Finalement stop" });
    await syncReplies(env.deps, inbox);
    expect((await outreachRow()).status).toBe("OPTED_OUT");
    expect((await db.select().from(schema.prospects).where(eq(schema.prospects.id, p.id)))[0].state).toBe("SUPPRESSED");
  });

  test("réponse marquée à la main", async () => {
    const { env, p } = await ready();
    await expect(markReply(env.deps, p.id, "REPLIED")).rejects.toThrow(/Aucun email/);
    await approveDraft(env.deps, p.id);
    await sendApprovedEmail(env.deps, new FakeMailer(), CFG, p.id);
    await markReply(env.deps, p.id, "REPLIED");
    expect(await outreachRow()).toMatchObject({ status: "REPLIED", reply_source: "MANUAL", messages_received: 1 });
  });
});
