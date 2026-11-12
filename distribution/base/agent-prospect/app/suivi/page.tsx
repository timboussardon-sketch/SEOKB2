import { eq, inArray } from "drizzle-orm";
import Link from "next/link";
import { getDb, schema } from "@/db/client";
import { oauthApp } from "@/net/gmail";
import { dealStageAction, markReplyAction, sendEmailAction, syncAction } from "@/server/actions";
import { mailConfig } from "@/net/resend";
import { STATE_LABEL } from "@/server/labels";
import { Tag } from "@/server/ui";

export const dynamic = "force-dynamic";

const OUT: Record<string, [string, string]> = {
  SENDING: ["Envoi en cours", "info"],
  FAILED: ["Envoi refusé", "bad"],
  SENT: ["Envoyé", "info"],
  DELIVERED: ["Remis, sans réponse", "info"],
  REPLIED: ["A répondu", "ok"],
  OPTED_OUT: ["Opposition (stop)", "bad"],
  BOUNCED: ["Rebond", "bad"],
};
const day = (d: Date | null) => (d ? d.toLocaleDateString("fr-FR", { day: "2-digit", month: "2-digit" }) : "");
const DAY_MS = 86_400_000;

export default async function Suivi({ searchParams }: { searchParams: Promise<{ gmail?: string; notice?: string }> }) {
  const sp = await searchParams;
  const notice = sp.notice ?? sp.gmail;
  const db = getDb();
  const app = oauthApp();
  const mail = mailConfig();
  const [account] = await db.select().from(schema.gmail_account);
  const campaigns = await db.select().from(schema.campaigns).where(eq(schema.campaigns.simulation, false));
  const ids = campaigns.map((c) => c.id);
  const prospects = ids.length ? await db.select().from(schema.prospects).where(inArray(schema.prospects.campaign_id, ids)) : [];
  const pids = prospects.map((p) => p.id);
  const drafts = pids.length ? await db.select().from(schema.email_drafts).where(inArray(schema.email_drafts.prospect_id, pids)) : [];
  const outreach = pids.length ? await db.select().from(schema.outreach).where(inArray(schema.outreach.prospect_id, pids)) : [];
  const firms = prospects.length ? await db.select().from(schema.firms).where(inArray(schema.firms.id, prospects.map((p) => p.firm_id))) : [];

  const count = (s: string) => prospects.filter((p) => p.state === s).length;
  const contacted = outreach.filter((o) => o.first_sent_at);
  const replied = outreach.filter((o) => o.replied_at);
  const stats: [string, string | number][] = [
    ["Cabinets trouvés", prospects.length],
    ["Emails prêts à relire", count("READY_FOR_REVIEW")],
    ["Approuvés", count("APPROVED")],
    ["Cabinets contactés", contacted.length],
    ["Emails envoyés", outreach.reduce((n, o) => n + o.messages_sent, 0)],
    ["Réponses", replied.length],
    ["Oppositions", outreach.filter((o) => o.status === "OPTED_OUT").length],
    ["Rebonds", outreach.filter((o) => o.status === "BOUNCED").length],
    ["Rendez-vous", outreach.filter((o) => o.deal_stage === "MEETING").length],
    ["Propositions", outreach.filter((o) => o.deal_stage === "PROPOSAL").length],
    ["Contrats signés", outreach.filter((o) => o.deal_stage === "SIGNED").length],
    ["Taux de réponse", contacted.length ? `${Math.round((replied.length / contacted.length) * 100)} %` : "aucun envoi"],
  ];

  const rows = prospects
    .filter((p) => drafts.some((d) => d.prospect_id === p.id))
    .map((p) => ({ p, d: drafts.find((x) => x.prospect_id === p.id)!, o: outreach.find((x) => x.prospect_id === p.id), f: firms.find((x) => x.id === p.firm_id), c: campaigns.find((x) => x.id === p.campaign_id) }))
    .sort((a, b) => (b.o?.last_sent_at?.getTime() ?? 0) - (a.o?.last_sent_at?.getTime() ?? 0));
  const now = Date.now();

  return (
    <>
      <h1>Suivi des envois</h1>
      <p className="muted">Campagnes réelles seulement. Un email approuvé part par Resend quand tu cliques sur « Envoyer ». Les réponses arrivent sur {mail?.replyTo ?? "l'adresse de réponse"}.</p>

      {notice && <div className="banner" style={{ marginTop: 20 }}>{notice}</div>}
      <div className="card" style={{ marginTop: 20 }}>
        <p>Envoi : {mail ? <>de <strong>{mail.from}</strong>, réponses vers <strong>{mail.replyTo}</strong>, {mail.maxPerDay} envois par jour au plus</> : <>non configuré (<code>RESEND_API_KEY</code>, <code>MAIL_FROM</code>, <code>MAIL_REPLY_TO</code>, <code>SENDER_NAME</code>)</>}</p>
        <div className="row" style={{ justifyContent: "space-between", marginTop: 12 }}>
          {!app ? (
            <span className="muted">Réponses : relevé Gmail non configuré, marque-les à la main. Pour l'automatiser, crée un identifiant OAuth « application de bureau » (API Gmail, ton adresse en utilisateur test) et mets <code>GMAIL_CLIENT_ID</code> et <code>GMAIL_CLIENT_SECRET</code> dans <code>.env.local</code>.</span>
          ) : !account ? (
            <a className="btn ghost" href="/api/gmail/connect">Connecter Gmail pour relever les réponses</a>
          ) : (
            <span>Réponses relevées dans <strong>{account.email}</strong> · dernier relevé {account.last_sync_at ? account.last_sync_at.toLocaleString("fr-FR") : "jamais"}{account.last_sync_error && <span className="tag bad" style={{ marginLeft: 8 }}>{account.last_sync_error}</span>}</span>
          )}
          <form action={syncAction}><button className="ghost">Relever maintenant</button></form>
        </div>
      </div>

      <div className="grid" style={{ marginTop: 20 }}>
        {stats.map(([label, v]) => <div className="stat" key={label}><b>{v}</b><span>{label}</span></div>)}
      </div>

      <h2 style={{ marginTop: 36 }}>Qui a reçu quoi</h2>
      {rows.length === 0 ? <p className="muted">Aucun email rédigé dans une campagne réelle.</p> : (
        <div className="table" style={{ marginTop: 12 }}>
          <table>
            <thead><tr><th>Cabinet</th><th>Destinataire</th><th>État</th><th>Envoyé le</th><th className="num">Envoyés</th><th>Réponse</th><th className="num">Jours sans réponse</th><th>Suite</th><th></th></tr></thead>
            <tbody>
              {rows.map(({ p, d, o, f, c }) => (
                <tr key={p.id}>
                  <td><Link href={`/prospects/${p.id}`}>{f?.name ?? f?.canonical_domain}</Link><div className="muted" style={{ fontSize: 13 }}>{c?.name}</div></td>
                  <td>{o?.recipient ?? d.recipient ?? "aucun"}</td>
                  <td><Tag pair={o ? OUT[o.status] : STATE_LABEL[p.state]} /></td>
                  <td>{day(o?.first_sent_at ?? null)}</td>
                  <td className="num">{o?.messages_sent ?? 0}</td>
                  <td>{o?.replied_at && <>{day(o.replied_at)}<div className="muted" style={{ fontSize: 13, maxWidth: 280 }}>{o.reply_excerpt}</div></>}{o?.status === "FAILED" && <div className="muted" style={{ fontSize: 13, maxWidth: 280 }}>{o.error}</div>}</td>
                  <td className="num">{(o?.status === "SENT" || o?.status === "DELIVERED") && o.last_sent_at ? Math.floor((now - o.last_sent_at.getTime()) / DAY_MS) : ""}</td>
                  <td>{o?.first_sent_at && (
                    <form action={dealStageAction} className="row" style={{ gap: 6 }}>
                      <input type="hidden" name="prospect_id" value={p.id} />
                      <select name="stage" defaultValue={o.deal_stage ?? ""} style={{ width: "auto" }}>
                        <option value="">Aucune</option><option value="MEETING">Rendez-vous</option><option value="PROPOSAL">Proposition</option><option value="SIGNED">Signé</option><option value="LOST">Perdu</option>
                      </select>
                      <button className="ghost">OK</button>
                    </form>
                  )}</td>
                  <td>{p.state === "APPROVED" && mail && (!o || o.status === "FAILED") && (
                    <form action={sendEmailAction}><input type="hidden" name="prospect_id" value={p.id} /><button>Envoyer à {o?.recipient ?? d.recipient}</button></form>
                  )}{(o?.status === "SENT" || o?.status === "DELIVERED") && (
                    <div className="row" style={{ gap: 6 }}>
                      <form action={markReplyAction}><input type="hidden" name="prospect_id" value={p.id} /><input type="hidden" name="kind" value="REPLIED" /><button className="ghost">A répondu</button></form>
                      <form action={markReplyAction}><input type="hidden" name="prospect_id" value={p.id} /><input type="hidden" name="kind" value="OPTED_OUT" /><button className="ghost">Stop</button></form>
                    </div>
                  )}{p.state === "READY_FOR_REVIEW" && <Link href={`/prospects/${p.id}#brouillon`}>Relire</Link>}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </>
  );
}
