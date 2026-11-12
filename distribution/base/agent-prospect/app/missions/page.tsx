import { eq } from "drizzle-orm";
import { getDb, schema } from "@/db/client";
import { missionSettings, parisClock, SEGMENTS } from "@/core/mission";
import { recentMissions, sendableProspects } from "@/engine/missions";
import { getDeps } from "@/server/context";
import { mailConfig } from "@/net/resend";

export const dynamic = "force-dynamic";

export default async function Missions() {
  const db = getDb();
  const s = missionSettings();
  const mail = mailConfig();
  const missions = await recentMissions({ db });
  const today = parisClock(new Date()).day;
  const m = missions.find((x) => x.day === today);
  const out = await db.select().from(schema.outreach);
  const real = await db.select().from(schema.campaigns).where(eq(schema.campaigns.simulation, false));
  const stock = (await sendableProspects(await getDeps())).length;
  const signed = out.filter((o) => o.deal_stage === "SIGNED").length;
  const funnel: [string, number][] = [
    ["Cabinets contactés", out.filter((o) => o.first_sent_at).length],
    ["Réponses", out.filter((o) => o.replied_at).length],
    ["Rendez-vous", out.filter((o) => o.deal_stage === "MEETING").length],
    ["Propositions", out.filter((o) => o.deal_stage === "PROPOSAL").length],
    ["Contrats signés", signed],
  ];
  return (
    <>
      <h1>Missions</h1>
      <p className="muted">Objectif : des contrats de prestation SEO signés avec des avocats spécialisés. Chaque jour, l'agent garde un stock d'emails prêts, envoie {s.dailySends} emails en semaine entre {s.sendFrom} h et {s.sendUntil} h (heure de Paris), un toutes les {s.spacingMinutes} minutes au plus, et t'envoie le rapport à {s.reportAt} h.</p>
      {!s.enabled && <div className="banner bad" style={{ marginTop: 20 }}>Missions désactivées : MISSIONS_ENABLED n'est pas à true.</div>}
      {s.enabled && !s.autoSend && <div className="banner" style={{ marginTop: 20 }}>Envoi automatique désactivé : AUTO_SEND n'est pas à true. L'agent prépare, tu envoies depuis Suivi.</div>}
      {s.enabled && !mail && <div className="banner bad" style={{ marginTop: 20 }}>Resend n'est pas configuré : aucun envoi, aucun rapport.</div>}

      <div className="grid" style={{ marginTop: 20 }}>
        {funnel.map(([label, v]) => <div className="stat" key={label}><b>{v}</b><span>{label}</span></div>)}
      </div>

      <h2 style={{ marginTop: 36 }}>Aujourd'hui, {today}</h2>
      <div className="grid" style={{ marginTop: 12 }}>
        <div className="stat"><b>{m?.sent ?? 0} / {s.dailySends}</b><span>Envoyés</span></div>
        <div className="stat"><b>{stock}</b><span>Emails prêts en stock</span></div>
        <div className="stat"><b>{real.filter((c) => c.status === "RUNNING").length}</b><span>Campagne en cours</span></div>
        <div className="stat"><b>{m?.report_sent_at ? "envoyé" : "à venir"}</b><span>Rapport du soir</span></div>
      </div>
      {m && m.log.length > 0 ? (
        <div className="table" style={{ marginTop: 16 }}>
          <table><thead><tr><th>Heure (Paris)</th><th>Étape</th><th>Détail</th></tr></thead>
            <tbody>{[...m.log].reverse().map((e, i) => (
              <tr key={i}><td>{new Date(e.at).toLocaleTimeString("fr-FR", { timeZone: "Europe/Paris", hour: "2-digit", minute: "2-digit" })}</td><td>{e.step}</td><td>{e.message}</td></tr>
            ))}</tbody>
          </table>
        </div>
      ) : <p className="muted" style={{ marginTop: 12 }}>Rien au journal aujourd'hui.</p>}

      <h2 style={{ marginTop: 36 }}>Cibles en rotation</h2>
      <div className="table" style={{ marginTop: 12 }}>
        <table><thead><tr><th>Spécialité</th><th>Ville</th><th className="num">Campagnes</th><th>Dernière</th></tr></thead>
          <tbody>{SEGMENTS.flatMap((seg) => s.cities.map((city) => {
            const cs = real.filter((c) => c.config.practice_area === seg.practice_area && c.config.location === city);
            const last = cs.sort((a, b) => b.created_at.getTime() - a.created_at.getTime())[0];
            return <tr key={seg.key + city}><td>{seg.label}</td><td>{city}</td><td className="num">{cs.length}</td><td>{last ? last.created_at.toLocaleDateString("fr-FR") : "jamais"}</td></tr>;
          }))}</tbody>
        </table>
      </div>

      <h2 style={{ marginTop: 36 }}>14 derniers jours</h2>
      <div className="table" style={{ marginTop: 12 }}>
        <table><thead><tr><th>Jour</th><th className="num">Envoyés</th><th className="num">Campagnes lancées</th><th>Rapport</th></tr></thead>
          <tbody>{missions.map((x) => <tr key={x.id}><td>{x.day}</td><td className="num">{x.sent} / {x.target_sends}</td><td className="num">{x.campaign_ids.length}</td><td>{x.report_sent_at ? "envoyé" : ""}</td></tr>)}</tbody>
        </table>
      </div>
    </>
  );
}
