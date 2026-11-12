import { desc, eq, inArray } from "drizzle-orm";
import Link from "next/link";
import { getDb, schema } from "@/db/client";
import { REASON_LABEL, STATE_LABEL, VERDICT_LABEL } from "@/server/labels";
import { Tag } from "@/server/ui";

export const dynamic = "force-dynamic";

export default async function Prospects({ searchParams }: { searchParams: Promise<{ campaign?: string; state?: string }> }) {
  const { campaign, state } = await searchParams;
  const db = getDb();
  const campaigns = await db.select().from(schema.campaigns).orderBy(desc(schema.campaigns.created_at));
  const valid = campaign && campaigns.some((c) => c.id === campaign) ? campaign : undefined;
  let rows = valid ? await db.select().from(schema.prospects).where(eq(schema.prospects.campaign_id, valid)).orderBy(desc(schema.prospects.updated_at)) : await db.select().from(schema.prospects).orderBy(desc(schema.prospects.updated_at)).limit(300);
  if (state) rows = rows.filter((p) => p.state === state);
  const firmIds = [...new Set(rows.map((p) => p.firm_id))];
  const firms = firmIds.length ? await db.select().from(schema.firms).where(inArray(schema.firms.id, firmIds)) : [];
  const lawyers = firmIds.length ? await db.select().from(schema.lawyers).where(inArray(schema.lawyers.firm_id, firmIds)) : [];
  const contacts = firmIds.length ? await db.select().from(schema.contacts).where(inArray(schema.contacts.firm_id, firmIds)) : [];
  const states = [...new Set(rows.map((p) => p.state))];
  return (
    <>
      <h1>Prospects</h1>
      <form method="get" className="row" style={{ marginTop: 28 }}>
        <select name="campaign" defaultValue={valid ?? ""} style={{ width: 280 }}>
          <option value="">Toutes les campagnes</option>
          {campaigns.map((c) => <option key={c.id} value={c.id}>{c.name}</option>)}
        </select>
        <select name="state" defaultValue={state ?? ""} style={{ width: 240 }}>
          <option value="">Tous les états</option>
          {Object.entries(STATE_LABEL).map(([k, v]) => <option key={k} value={k}>{v[0]}</option>)}
        </select>
        <button className="ghost">Filtrer</button>
        <span className="muted">{rows.length} prospects{states.length > 1 ? "" : ""}</span>
      </form>
      <div className="table" style={{ marginTop: 20 }}>
        <table>
          <thead><tr><th>Cabinet</th><th>Avocat</th><th>Ville</th><th>Email</th><th>Qualification</th><th>Présence IA</th><th className="num">Mots-clés</th><th>État</th></tr></thead>
          <tbody>
            {rows.length === 0 && <tr><td colSpan={8} className="muted">Aucun prospect.</td></tr>}
            {rows.map((p) => {
              const firm = firms.find((f) => f.id === p.firm_id);
              const lawyer = lawyers.find((l) => l.id === p.lawyer_id);
              const contact = contacts.find((c) => c.firm_id === p.firm_id && c.selected);
              return (
                <tr key={p.id}>
                  <td><Link href={`/prospects/${p.id}`}>{firm?.name ?? p.candidate_name ?? firm?.canonical_domain}</Link><br /><span className="muted">{firm?.canonical_domain}</span></td>
                  <td>{lawyer ? `${lawyer.first_name} ${lawyer.last_name}` : <span className="muted">non identifié</span>}</td>
                  <td>{firm?.city ?? <span className="muted">inconnue</span>}</td>
                  <td>{contact?.email ?? (p.email_status === "NO_PUBLIC_EMAIL" ? <span className="tag warn">Aucune adresse publiée</span> : <span className="muted">non cherché</span>)}</td>
                  <td>{p.qualification_status === "QUALIFIED" ? <span className="tag ok">Qualifié</span> : p.qualification_reason ? <span className="tag">{REASON_LABEL[p.qualification_reason] ?? p.qualification_reason}</span> : <span className="muted">en attente</span>}</td>
                  <td>{p.visibility_verdict ? <Tag pair={VERDICT_LABEL[p.visibility_verdict]} /> : <span className="muted">non mesurée</span>}</td>
                  <td className="num">{p.keyword_count ?? ""}{p.keyword_status === "INSUFFICIENT_EVIDENCE" ? " (liste courte)" : ""}</td>
                  <td><Tag pair={STATE_LABEL[p.state]} /></td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </>
  );
}
