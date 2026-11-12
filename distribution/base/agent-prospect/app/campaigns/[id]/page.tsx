import { and, desc, eq } from "drizzle-orm";
import Link from "next/link";
import { notFound } from "next/navigation";
import { VISIBILITY_MODE_LABELS } from "@/core/benchmark";
import { getDb, schema } from "@/db/client";
import { campaignCost } from "@/engine/budget";
import { campaignLearning, campaignProgress } from "@/engine/campaign";
import { campaignControlAction } from "@/server/actions";
import { CAMPAIGN_STATUS, GOAL_LABEL, REASON_LABEL } from "@/server/labels";
import { SimBanner, Tag, usd } from "@/server/ui";
import { AutoRefresh } from "../../refresh";

export const dynamic = "force-dynamic";

function Control({ id, op, label, kind = "" }: { id: string; op: string; label: string; kind?: string }) {
  return (
    <form action={campaignControlAction}>
      <input type="hidden" name="id" value={id} />
      <input type="hidden" name="op" value={op} />
      <button className={kind}>{label}</button>
    </form>
  );
}

export default async function CampaignPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const db = getDb();
  const [c] = await db.select().from(schema.campaigns).where(eq(schema.campaigns.id, id)).catch(() => []);
  if (!c) notFound();
  const pr = await campaignProgress({ db }, c);
  const cost = await campaignCost(db, c.id);
  const learning = await campaignLearning({ db }, c.id);
  const benchmarks = await db.select().from(schema.visibility_benchmarks).where(eq(schema.visibility_benchmarks.campaign_id, c.id));
  const errors = await db.select().from(schema.event_log).where(and(eq(schema.event_log.campaign_id, c.id), eq(schema.event_log.type, "STEP_ERROR"))).orderBy(desc(schema.event_log.created_at)).limit(15);
  const cfg = c.config;
  const f = pr.funnel;
  const steps: [string, number, string][] = [
    ["Découverte", f.discovered, "candidats"],
    ["Qualification", f.qualified, "qualifiés"],
    ["Enrichissement", f.enriched, "traités"],
    ["Mesure IA", f.visibilityDone, "terminés"],
    ["Pré-audits", f.audited, ""],
    ["Mots-clés", f.keywordsDone, ""],
    ["Brouillons", f.drafts, ""],
  ];
  return (
    <>
      <AutoRefresh active={c.status === "RUNNING"} />
      <SimBanner simulation={c.simulation} />
      <div className="row" style={{ justifyContent: "space-between" }}>
        <div className="row"><h1>{c.name}</h1><Tag pair={CAMPAIGN_STATUS[c.status]} /></div>
        <div className="row">
          {(c.status === "DRAFT") && <Control id={c.id} op="start" label="Lancer" />}
          {(c.status === "PAUSED" || c.status === "BLOCKED" || c.status === "PARTIAL") && <Control id={c.id} op="start" label="Reprendre" />}
          {c.status === "RUNNING" && <Control id={c.id} op="pause" label="Mettre en pause" kind="ghost" />}
          {!["STOPPED", "COMPLETED", "DRAFT"].includes(c.status) && <Control id={c.id} op="stop" label="Arrêter" kind="danger" />}
        </div>
      </div>
      {c.stop_reason && <p style={{ marginTop: 28 }}>{c.stop_reason}</p>}
      {c.status === "DRAFT" && <p className="muted" style={{ marginTop: 28 }}>La campagne est créée mais ne tourne pas. Le worker doit être démarré (<code>npm run worker</code>) pour qu'elle avance.</p>}

      <h2>Objectif</h2>
      <div className="card">
        <p><strong>{pr.goal} / {pr.target}</strong> {GOAL_LABEL[c.goal_type]}{pr.inFlight > 0 && <span className="muted"> · {pr.inFlight} en cours de traitement</span>}</p>
        <div className="bar" style={{ marginTop: 12 }}><i style={{ width: `${Math.min(100, (pr.goal / pr.target) * 100)}%` }} /></div>
        <p className="muted" style={{ marginTop: 12 }}>
          {cfg.practice_area}{cfg.subspecialties.length ? ` (${cfg.subspecialties.join(", ")})` : ""}, {cfg.location}, clientèle {cfg.client_type}, ciblage {cfg.target_type === "FIRM" ? "cabinet" : "avocat individuel"}.
          Découverte : tour {c.discovery_rounds_done} sur {cfg.max_discovery_rounds} au plus, {c.discovery_results_total} résultats sur {cfg.max_total_discovery_results} au plus.
        </p>
        {c.objective_text && <blockquote style={{ marginTop: 12 }}>{c.objective_text}</blockquote>}
      </div>

      <h2>Avancement</h2>
      <div className="grid">
        {steps.map(([label, n, unit]) => (<div className="stat" key={label}><b>{n}</b><span>{label}{unit ? ` · ${unit}` : ""}</span></div>))}
        <div className="stat"><b>{f.ready} / {pr.target}</b><span>Prêts à relire</span></div>
      </div>
      <div className="grid" style={{ marginTop: 12 }}>
        <div className="stat"><b>{f.rejected}</b><span>Écartés</span></div>
        <div className="stat"><b>{f.observed}</b><span>Déjà observés, archivés</span></div>
        <div className="stat"><b>{f.noEmail}</b><span>Sans adresse publiée</span></div>
        <div className="stat"><b>{pr.inReview}</b><span><Link href="/review">En revue humaine</Link></span></div>
        <div className="stat"><b>{pr.budgetBlocked}</b><span>Suspendus : budget</span></div>
      </div>
      {Object.keys(pr.rejections).length > 0 && (
        <p className="muted" style={{ marginTop: 16 }}>Motifs d'écart : {Object.entries(pr.rejections).map(([k, v]) => `${REASON_LABEL[k] ?? k} (${v})`).join(", ")}.</p>
      )}
      <p style={{ marginTop: 16 }}><Link href={`/prospects?campaign=${c.id}`}>Voir les prospects</Link> · <Link href={`/campaigns/${c.id}/chatgpt`}>Saisir des réponses de ChatGPT</Link> · <a href={`/api/export/prospects?campaign=${c.id}`}>Export CSV</a> · <a href={`/api/export/keywords?campaign=${c.id}`}>Mots-clés CSV</a> · <a href={`/api/export/json?campaign=${c.id}`}>Export JSON</a></p>

      <h2>Coûts</h2>
      <div className="grid">
        <div className="stat"><b>{usd(cost.engaged)}</b><span>Engagé sur {usd(cfg.max_campaign_cost_usd)}</span></div>
        <div className="stat"><b>{usd(cost.reconciled)}</b><span>Recalculé depuis l'usage rapporté</span></div>
        <div className="stat"><b>{usd(cost.unconfirmed + cost.reserved)}</b><span>Réservé, issue non confirmée</span></div>
      </div>
      <p className="muted" style={{ marginTop: 16 }}>Montants calculés à partir des tarifs saisis dans la configuration et de l'usage rapporté par le fournisseur. Ce n'est pas une facture.</p>

      {benchmarks.length > 0 && (
        <>
          <h2>Mesure de présence IA</h2>
          <div className="table"><table>
            <thead><tr><th>Mode</th><th>Modèle</th><th>Segment</th><th className="num">Réponses valides</th><th>État</th><th>Fenêtre</th></tr></thead>
            <tbody>{benchmarks.map((b) => (
              <tr key={b.id}>
                <td>{VISIBILITY_MODE_LABELS[b.provider]}</td><td>{b.model}</td>
                <td>{(b.segment as { practice: string; city: string }).practice}, {(b.segment as { city: string }).city}</td>
                <td className="num">{b.valid_runs} / {b.expected_valid_runs}</td>
                <td>{b.status === "COMPLETE" ? "Complet" : b.status === "INCOMPLETE" ? "Incomplet : aucun constat d'absence" : "En cours"}</td>
                <td>{b.started_at.toLocaleString("fr-FR")}{b.finished_at ? ` → ${b.finished_at.toLocaleTimeString("fr-FR")}` : ""}</td>
              </tr>))}</tbody>
          </table></div>
        </>
      )}

      <h2>Recherches de découverte</h2>
      <div className="table"><table>
        <thead><tr><th>Formulation</th><th>Famille</th><th className="num">Résultats</th><th className="num">Nouveaux</th><th className="num">Qualifiés</th><th className="num">Écartés</th></tr></thead>
        <tbody>
          {learning.length === 0 && <tr><td colSpan={6} className="muted">Aucune recherche lancée.</td></tr>}
          {learning.map((l, i) => (<tr key={i}><td>{l.query}</td><td>{l.family}</td><td className="num">{l.results}</td><td className="num">{l.created}</td><td className="num">{l.qualified}</td><td className="num">{l.rejected}</td></tr>))}
        </tbody>
      </table></div>
      <p className="muted" style={{ marginTop: 16 }}>Relevé en lecture seule. Aucune règle de campagne n'est modifiée à partir de ces chiffres sans votre décision.</p>

      {errors.length > 0 && (
        <>
          <h2>Incidents</h2>
          <div className="table"><table>
            <thead><tr><th>Heure</th><th>Étape</th><th>Catégorie</th><th>Message</th><th>Suite donnée</th></tr></thead>
            <tbody>{errors.map((e) => { const d = e.data as { step: string; category: string; message: string; recovery: string }; return (
              <tr key={e.id}><td>{e.created_at.toLocaleTimeString("fr-FR")}</td><td>{d.step}</td><td>{d.category}</td><td>{d.message}</td><td>{d.recovery}</td></tr>); })}</tbody>
          </table></div>
        </>
      )}
    </>
  );
}
