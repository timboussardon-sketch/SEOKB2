import { eq, sql } from "drizzle-orm";
import { afterAll, beforeEach, describe, expect, test } from "vitest";
import { businessDaysBetween, canSendNow, MISSION_SEGMENTS, missionSettings, nextSegment, parisClock } from "../src/core/mission";
import { schema, type Db } from "../src/db/client";
import { followupsDue, missionTick, sendableProspects } from "../src/engine/missions";
import type { Mailer, OutgoingEmail } from "../src/net/resend";
import { usageFromCli } from "../src/providers/claude-cli";
import { closeDb, drain, testDb, testEnv } from "./helpers";

// Mardi 6 octobre 2026, heure de Paris (UTC+2)
const at = (h: number, min = 0) => new Date(Date.UTC(2026, 9, 6, h - 2, min));
const S = { ...missionSettings({}), enabled: true, autoSend: true, dailySends: 2 };

describe("règles des missions", () => {
  test("heure de Paris, quel que soit le fuseau de la machine", () => {
    expect(parisClock(at(9, 30))).toEqual({ day: "2026-10-06", hour: 9, minute: 30, weekday: 2 });
    expect(parisClock(new Date(Date.UTC(2026, 9, 6, 22, 30))).day).toBe("2026-10-07");
  });

  test("fenêtre d'envoi : semaine, plage horaire, quota, espacement", () => {
    expect(canSendNow(S, at(10), 0, null).ok).toBe(true);
    expect(canSendNow({ ...S, autoSend: false }, at(10), 0, null).ok).toBe(false);
    expect(canSendNow(S, at(8), 0, null).why).toBe("hors plage horaire");
    expect(canSendNow(S, at(17), 0, null).why).toBe("hors plage horaire");
    expect(canSendNow(S, new Date(Date.UTC(2026, 9, 10, 8)), 0, null).why).toBe("week-end");
    expect(canSendNow(S, at(10), 2, null).why).toBe("quota du jour atteint");
    expect(canSendNow(S, at(10, 10), 1, at(10)).why).toBe("espacement");
    expect(canSendNow(S, at(10, 20), 1, at(10)).ok).toBe(true);
  });

  test("rotation : la cible jamais lancée passe d'abord, puis la plus ancienne", () => {
    const last = new Map([["droit du travail|Lyon", 5]]);
    expect(nextSegment(["Lyon"], last).segment.key).toBe("urssaf");
    const all = new Map(MISSION_SEGMENTS.map((s, i) => [`${s.practice_area}|Lyon`, 10 - i]));
    expect(nextSegment(["Lyon"], all).segment.key).toBe(MISSION_SEGMENTS.at(-1)!.key);
    // Clientèle de particuliers ou mixte : hors du message type, jamais ciblée par les missions.
    expect(MISSION_SEGMENTS.map((s) => s.key)).toEqual(["travail", "urssaf"]);
  });

  test("usage du forfait Max relevé sur tous les modèles appelés", () => {
    const u = usageFromCli("max:claude-opus-5-5", { modelUsage: { "claude-opus-5-5": { inputTokens: 6, outputTokens: 465, cacheReadInputTokens: 4548, cacheCreationInputTokens: 4062 }, "claude-haiku-4-5": { inputTokens: 20599, outputTokens: 929, webSearchRequests: 2 } } });
    expect(u).toMatchObject({ model: "max:claude-opus-5-5", input_tokens: 6 + 4548 + 4062 + 20599, output_tokens: 465 + 929, web_search_calls: 2 });
  });
});

class FakeMailer implements Mailer {
  sent: OutgoingEmail[] = [];
  async send(e: OutgoingEmail) {
    this.sent.push(e);
    return { id: `em_${this.sent.length}` };
  }
  async lastEvent() {
    return "delivered";
  }
}
const CFG = { from: "Camille Test <camille@exemple.test>", replyTo: "reponses@exemple.test", maxPerDay: 20 };

let db: Db;
beforeEach(async () => {
  db = await testDb();
});
afterAll(closeDb);

describe("journée de mission", () => {
  test("lance une campagne, envoie deux emails espacés, puis le rapport du soir", async () => {
    const env = testEnv(db);
    let now = at(8);
    env.deps.now = () => now;
    const mailer = new FakeMailer();
    const mail = { mailer, cfg: CFG };

    await missionTick(env.deps, S, mail, { simulation: true });
    const [c] = await db.select().from(schema.campaigns);
    expect(c.name).toContain("Droit du travail, Lyon");
    expect(c.config.target_count).toBe(4);
    await drain(env);
    // Campagne simulée rendue « réelle » pour que ses emails deviennent envoyables dans le test.
    await db.update(schema.campaigns).set({ simulation: false });
    expect((await sendableProspects(env.deps)).length).toBeGreaterThanOrEqual(2);

    await missionTick(env.deps, S, mail, { simulation: false });
    expect(mailer.sent).toHaveLength(0); // 8 h : hors plage

    now = at(9);
    await missionTick(env.deps, S, mail, { simulation: false });
    await missionTick(env.deps, S, mail, { simulation: false });
    expect(mailer.sent).toHaveLength(1); // espacement
    now = at(9, 25);
    await missionTick(env.deps, S, mail, { simulation: false });
    now = at(10);
    await missionTick(env.deps, S, mail, { simulation: false });
    expect(mailer.sent).toHaveLength(2); // quota de 2
    expect(mailer.sent.every((e) => e.from === CFG.from && e.replyTo === CFG.replyTo)).toBe(true);
    expect((await db.select().from(schema.outreach)).every((o) => o.status === "SENT")).toBe(true);

    now = at(18, 1);
    await missionTick(env.deps, S, mail, { simulation: false });
    await missionTick(env.deps, S, mail, { simulation: false });
    expect(mailer.sent).toHaveLength(3);
    const report = mailer.sent[2];
    expect(report.to).toBe("reponses@exemple.test");
    expect(report.subject).toBe("Agent avocats, 2026-10-06 : 2 envoyés, 0 réponses");
    expect(report.text).toContain("Envoyés aujourd'hui : 2 sur 2");
    const [m] = await db.select().from(schema.missions).where(eq(schema.missions.day, "2026-10-06"));
    expect(m.sent).toBe(2);
    expect(m.log.map((e) => e.step)).toEqual(expect.arrayContaining(["campagne", "envoi", "rapport"]));
  });

  test("échec réseau chez Resend : le même email repart au créneau suivant ; refus de Resend : jamais retenté", async () => {
    const env = testEnv(db);
    let now = at(8);
    env.deps.now = () => now;
    await missionTick(env.deps, S, { mailer: new FakeMailer(), cfg: CFG }, { simulation: true });
    await drain(env);
    await db.update(schema.campaigns).set({ simulation: false });
    const [first, second] = await sendableProspects(env.deps);

    let failure: string | null = "Unable to fetch data. The request could not be resolved.";
    const mailer = new FakeMailer();
    const flaky = { send: async (e: OutgoingEmail) => { if (failure) throw new Error(failure); return mailer.send(e); }, lastEvent: async () => "delivered" };
    const mail = { mailer: flaky as unknown as FakeMailer, cfg: CFG };

    now = at(9);
    await missionTick(env.deps, S, mail, { simulation: false });
    const [failed] = await db.select().from(schema.outreach).where(eq(schema.outreach.prospect_id, first));
    expect(failed.status).toBe("FAILED");
    expect(await sendableProspects(env.deps)).toContain(first);

    failure = "Invalid `to` field";
    now = at(9, 25);
    await missionTick(env.deps, S, mail, { simulation: false });
    expect(await sendableProspects(env.deps)).not.toContain(second);

    failure = null;
    for (let h = 10; h <= 13; h++) {
      now = at(h);
      await missionTick(env.deps, { ...S, dailySends: 10 }, mail, { simulation: false });
    }
    const [o] = await db.select().from(schema.outreach).where(eq(schema.outreach.prospect_id, first));
    expect(o.status).toBe("SENT");
    expect(mailer.sent.filter((e) => e.to === failed.recipient)).toHaveLength(1);
  });

  test("relances : 3 jours ouvrés, deux au plus, jamais sans texte, sans relevé Gmail ou après une réponse", async () => {
    // Vendredi 2 octobre → mercredi 7 octobre : 3 jours ouvrés (lundi, mardi, mercredi).
    const fri = new Date(Date.UTC(2026, 9, 2, 10));
    expect(businessDaysBetween(fri, new Date(Date.UTC(2026, 9, 6, 10)))).toBe(2);
    expect(businessDaysBetween(fri, new Date(Date.UTC(2026, 9, 7, 10)))).toBe(3);

    const env = testEnv(db);
    let now = at(8);
    env.deps.now = () => now;
    const mailer = new FakeMailer();
    const mail = { mailer, cfg: CFG };
    await missionTick(env.deps, S, mail, { simulation: true });
    await drain(env);
    await db.update(schema.campaigns).set({ simulation: false });
    now = at(9);
    await missionTick(env.deps, { ...S, dailySends: 1 }, mail);
    expect(mailer.sent).toHaveLength(1);
    const [o] = await db.select().from(schema.outreach);
    const texts = ["Relance 1", "Relance 2"];
    // Plus aucun premier email en stock : seules les relances peuvent partir ; les campagnes relancées restent simulées.
    await db.update(schema.prospects).set({ state: "REJECTED" }).where(sql`${schema.prospects.id} <> ${o.prospect_id}`);

    // Mardi 6 → vendredi 9 : 3 jours ouvrés.
    const day = (d: number, h: number) => new Date(Date.UTC(2026, 9, d, h - 2));
    now = day(8, 10);
    expect(await followupsDue(env.deps, texts)).toHaveLength(0); // 2 jours ouvrés
    now = day(9, 10);
    expect(await followupsDue(env.deps, [null, null])).toHaveLength(0); // texte absent
    expect(await followupsDue(env.deps, texts)).toEqual([{ id: o.id, n: 1, text: "Relance 1" }]);

    // Relevé Gmail absent : rien ne part.
    await missionTick(env.deps, { ...S, dailySends: 1 }, mail, { simulation: true, followups: texts });
    expect(mailer.sent).toHaveLength(1);

    await db.insert(schema.gmail_account).values({ email: "reponses@exemple.test", refresh_token: "x", last_sync_at: now });
    await missionTick(env.deps, { ...S, dailySends: 1 }, mail, { simulation: true, followups: texts });
    expect(mailer.sent).toHaveLength(2);
    expect(mailer.sent[1]).toMatchObject({ to: o.recipient, subject: `Re: ${o.subject}`, text: "Relance 1\n\nhttps://exemple.test" });

    // Deuxième relance 3 jours ouvrés plus tard, puis plus rien.
    now = day(14, 10);
    await db.update(schema.gmail_account).set({ last_sync_at: now });
    await missionTick(env.deps, { ...S, dailySends: 1 }, mail, { simulation: true, followups: texts });
    expect(mailer.sent).toHaveLength(3);
    expect(mailer.sent[2].text).toBe("Relance 2\n\nhttps://exemple.test");
    now = day(20, 10);
    expect(await followupsDue(env.deps, texts)).toHaveLength(0);

    // Une réponse arrête tout.
    await db.update(schema.outreach).set({ messages_sent: 1, replied_at: now });
    expect(await followupsDue(env.deps, texts)).toHaveLength(0);
  });

  test("missions désactivées : rien ne se passe", async () => {
    const env = testEnv(db);
    env.deps.now = () => at(10);
    await missionTick(env.deps, { ...S, enabled: false }, { mailer: new FakeMailer(), cfg: CFG });
    expect(await db.select().from(schema.missions)).toHaveLength(0);
  });
});
