import { desc } from "drizzle-orm";
import Link from "next/link";
import { getDb, schema } from "@/db/client";
import { campaignCost } from "@/engine/budget";
import { campaignProgress } from "@/engine/campaign";
import { integrations } from "@/server/context";
import { CAMPAIGN_STATUS, GOAL_LABEL } from "@/server/labels";
import { Tag, usd } from "@/server/ui";
import { AutoRefresh } from "../refresh";

export const dynamic = "force-dynamic";

export default async function Campaigns() {
  const db = getDb();
  const rows = await db.select().from(schema.campaigns).orderBy(desc(schema.campaigns.created_at));
  const data = await Promise.all(rows.map(async (c) => ({ c, pr: await campaignProgress({ db }, c), cost: await campaignCost(db, c.id) })));
  const integ = integrations();
  return (
    <>
      <AutoRefresh active={rows.some((c) => c.status === "RUNNING")} />
      <div className="row" style={{ justifyContent: "space-between" }}>
        <h1>Campagnes</h1>
        <Link className="btn" href="/campaigns/new">Nouvelle campagne</Link>
      </div>
      {integ.openaiMissing.length > 0 && (
        <p className="muted" style={{ marginTop: 28 }}>
          Intégration Claude non configurée ({integ.openaiMissing.join(", ")}) : seules les campagnes en simulation peuvent tourner.
        </p>
      )}
      <div className="table" style={{ marginTop: 28 }}>
        <table>
          <thead>
            <tr>
              <th>Campagne</th><th>Statut</th><th>Objectif</th><th className="num">Trouvés</th><th className="num">Qualifiés</th><th className="num">Audits</th><th className="num">Brouillons</th><th className="num">En revue</th><th className="num">Coût engagé</th>
            </tr>
          </thead>
          <tbody>
            {data.length === 0 && <tr><td colSpan={9} className="muted">Aucune campagne.</td></tr>}
            {data.map(({ c, pr, cost }) => (
              <tr key={c.id}>
                <td><Link href={`/campaigns/${c.id}`}>{c.name}</Link>{c.simulation && <> <span className="tag warn">Simulation</span></>}</td>
                <td><Tag pair={CAMPAIGN_STATUS[c.status]} /></td>
                <td>{pr.goal} / {pr.target} {GOAL_LABEL[c.goal_type]}</td>
                <td className="num">{pr.funnel.discovered}</td>
                <td className="num">{pr.funnel.qualified}</td>
                <td className="num">{pr.funnel.audited}</td>
                <td className="num">{pr.funnel.drafts}</td>
                <td className="num">{pr.inReview}</td>
                <td className="num">{usd(cost.engaged)}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </>
  );
}
