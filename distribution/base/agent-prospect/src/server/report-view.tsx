import type { AuditReport, Finding } from "../core/audit";

const STATUS: Record<string, string> = { CONFIRMED: "Confirmé", HYPOTHESIS: "Hypothèse", INSUFFICIENT_DATA: "Donnée insuffisante" };

function FindingCard({ f }: { f: Finding }) {
  return (
    <div className="card">
      <h3>{f.finding}</h3>
      <p><span className={`tag ${f.confidence_status === "CONFIRMED" ? "ok" : "warn"}`}>{STATUS[f.confidence_status]}</span></p>
      <p><strong>Preuve.</strong> {f.evidence}</p>
      <p><strong>Méthode.</strong> {f.method}</p>
      <p><strong>Conséquence possible.</strong> {f.impact}</p>
      <p><strong>Action proposée.</strong> {f.recommended_action}</p>
    </div>
  );
}

/** Rendu du rapport depuis ses données : aucun HTML de source externe n'est injecté. */
export function ReportView({ report }: { report: AuditReport }) {
  const others = report.findings.filter((f) => !report.priorities.some((p) => p.id === f.id));
  return (
    <>
      <h2>Synthèse</h2>
      <ul style={{ paddingLeft: 18 }}>{report.summary.map((s) => <li key={s}>{s}</li>)}</ul>
      <h2>Réponses des assistants IA</h2>
      <p>{report.visibility}</p>
      <h2>Priorités</h2>
      {report.priorities.length === 0 && <p className="muted">Aucun constat confirmé sur les pages lues.</p>}
      {report.priorities.map((f) => <FindingCard key={f.id} f={f} />)}
      {others.length > 0 && <><h2>Autres constats</h2>{others.map((f) => <FindingCard key={f.id} f={f} />)}</>}
      <h2>Requêtes</h2>
      <p>{report.keyword_note}</p>
      {report.keywords.length > 0 && (
        <div className="table" style={{ marginTop: 16 }}><table>
          <thead><tr><th>Requête</th><th>Groupe</th><th>Intention</th><th>Recommandation</th><th className="num">Proximité offre</th><th className="num">Intention business</th></tr></thead>
          <tbody>{report.keywords.map((k) => (<tr key={k.keyword}><td>{k.keyword}</td><td>{k.cluster}</td><td>{k.search_intent}</td><td>{k.recommendation_status}</td><td className="num">{k.offer_proximity_score}/5</td><td className="num">{k.business_intent_score}/5</td></tr>))}</tbody>
        </table></div>
      )}
      <h2>Périmètre exploré</h2>
      <p>{report.scope.pages_analyzed} pages analysées. robots.txt : {report.scope.robots}. Sitemap : {report.scope.sitemap_urls} URL lues.</p>
      <ul style={{ paddingLeft: 18, marginTop: 12 }} className="muted">{report.scope.urls.map((u) => <li key={u.url}>{u.url} ({u.status ?? "sans réponse"})</li>)}</ul>
      <h2>Limites</h2>
      <ul style={{ paddingLeft: 18 }}>{report.limits.map((l) => <li key={l}>{l}</li>)}</ul>
    </>
  );
}
