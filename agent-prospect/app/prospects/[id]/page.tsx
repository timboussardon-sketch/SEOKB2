import { asc, eq } from "drizzle-orm";
import Link from "next/link";
import { notFound } from "next/navigation";
import type { AuditReport } from "@/core/audit";
import type { DraftCheck, DraftSentence } from "@/core/claims";
import { getDb, schema } from "@/db/client";
import { prospectCost } from "@/engine/budget";
import { approveDraftAction, editDraftAction, forceAuditAction, revokeShareAction, suppressAction } from "@/server/actions";
import { integrations } from "@/server/context";
import { REASON_LABEL, REVIEW_LABEL, STATE_LABEL, VERDICT_LABEL } from "@/server/labels";
import { ReportView } from "@/server/report-view";
import { SimBanner, Tag, usd } from "@/server/ui";
import { AutoRefresh } from "../../refresh";

export const dynamic = "force-dynamic";

const KIND: Record<string, string> = { FIRM_NAME: "Nom du cabinet", IDENTITY: "Avocat", LOCATION: "Localisation", PRACTICE_AREA: "Pratique déclarée (cible)", OTHER_PRACTICE: "Autre pratique déclarée", CLIENT_TYPE: "Clientèle", SERVICE: "Prestation avec page dédiée", CERTIFICATION_CLAIM: "Spécialisation revendiquée sur le site (non vérifiée)" };
const SENTENCE: Record<string, string> = { GREETING: "Salutation", OBSERVATION: "Observation", VISIBILITY: "Constat IA", KEYWORDS: "Mots-clés", AUDIT_LINK: "Lien du pré-audit", CTA: "Appel à l'action", TRANSPARENCY: "Transparence et opposition", SIGNATURE: "Signature" };
const CLAIM: Record<string, [string, string]> = { SUPPORTED: ["Étayée", "ok"], INFERRED: ["Déduite, au conditionnel", "warn"], UNSUPPORTED: ["Non étayée", "bad"], PROMOTIONAL: ["Promotionnelle", "bad"], NOT_A_CLAIM: ["Sans affirmation", ""] };
const OBS: Record<string, string> = { LAWYER_MENTION: "Avocat nommé", FIRM_MENTION: "Cabinet nommé", OWN_DOMAIN_CITATION: "Site du cabinet cité", THIRD_PARTY_CITATION: "Source tierce qui nomme l'entité", AMBIGUOUS_MATCH: "Correspondance ambiguë" };

export default async function ProspectPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const db = getDb();
  const [p] = await db.select().from(schema.prospects).where(eq(schema.prospects.id, id)).catch(() => []);
  if (!p) notFound();
  const [c] = await db.select().from(schema.campaigns).where(eq(schema.campaigns.id, p.campaign_id));
  const [firm] = await db.select().from(schema.firms).where(eq(schema.firms.id, p.firm_id));
  const lawyers = await db.select().from(schema.lawyers).where(eq(schema.lawyers.firm_id, firm.id));
  const contacts = await db.select().from(schema.contacts).where(eq(schema.contacts.firm_id, firm.id));
  const evidence = await db.select().from(schema.evidence).where(eq(schema.evidence.prospect_id, p.id)).orderBy(asc(schema.evidence.kind));
  const [audit] = await db.select().from(schema.audits).where(eq(schema.audits.prospect_id, p.id));
  const [draft] = await db.select().from(schema.email_drafts).where(eq(schema.email_drafts.prospect_id, p.id));
  const reviews = await db.select().from(schema.review_items).where(eq(schema.review_items.prospect_id, p.id));
  const runs = p.benchmark_id ? await db.select().from(schema.visibility_runs).where(eq(schema.visibility_runs.benchmark_id, p.benchmark_id)).orderBy(asc(schema.visibility_runs.prompt_index), asc(schema.visibility_runs.repetition), asc(schema.visibility_runs.attempt)) : [];
  const observations = await db.select().from(schema.entity_observations).where(eq(schema.entity_observations.prospect_id, p.id));
  const cost = await prospectCost(db, p.id);
  const summary = p.visibility_summary as { reason: string; validRuns: number; expected_valid_runs: number; mode_label: string; model: string } | null;
  const check = draft?.fact_check as DraftCheck | null;
  const publicUrl = integrations().publicUrl;
  const editable = ["READY_FOR_REVIEW", "APPROVED", "HUMAN_REVIEW_REQUIRED"].includes(p.state);
  const working = c.status === "RUNNING" && /ING$|^DISCOVERED$|^QUALIFIED$|^ENRICHED$|_DONE$|^DRAFT_READY$/.test(p.state);

  return (
    <>
      <AutoRefresh active={working} />
      <SimBanner simulation={c.simulation} />
      <div className="row" style={{ justifyContent: "space-between" }}>
        <div className="row"><h1>{firm.name ?? p.candidate_name ?? firm.canonical_domain}</h1><Tag pair={STATE_LABEL[p.state]} /></div>
        <div className="row">
          {p.state === "ARCHIVED_OBSERVED" && <form action={forceAuditAction}><input type="hidden" name="prospect_id" value={p.id} /><button className="ghost">Auditer quand même</button></form>}
          {!["SUPPRESSED"].includes(p.state) && <form action={suppressAction}><input type="hidden" name="prospect_id" value={p.id} /><button className="danger">Supprimer le contact (opposition)</button></form>}
        </div>
      </div>
      <p className="muted">Campagne <Link href={`/campaigns/${c.id}`}>{c.name}</Link> · <a href={firm.website} rel="noreferrer noopener" target="_blank">{firm.canonical_domain}</a> · trouvé via {p.source_url ?? "source inconnue"}</p>

      {p.qualification_detail && <div className="banner" style={{ marginTop: 20 }}>{REASON_LABEL[p.qualification_reason ?? ""] ?? "Qualification"} : {p.qualification_detail}</div>}
      {reviews.filter((r) => r.status === "OPEN").map((r) => <div className="banner" key={r.id}>Revue demandée ({REVIEW_LABEL[r.reason]}) : {r.detail} <Link href="/review">Traiter</Link></div>)}
      {p.last_error != null && <div className="banner bad">Dernière erreur : {(p.last_error as { category: string; message: string }).category}. {(p.last_error as { message: string }).message}</div>}

      <div className="grid" style={{ marginTop: 28 }}>
        <div className="stat"><b>{lawyers.length}</b><span>{lawyers.map((l) => `${l.first_name} ${l.last_name}`).join(", ") || "Aucun avocat nommé"}</span></div>
        <div className="stat"><b>{p.visibility_verdict ? VERDICT_LABEL[p.visibility_verdict][0] : "Non mesurée"}</b><span>Présence IA</span></div>
        <div className="stat"><b>{p.keyword_count ?? 0}</b><span>Requêtes retenues</span></div>
        <div className="stat"><b>{usd(cost.total)}</b><span>Coût, dont {usd(cost.benchmarkShare)} de part du benchmark partagé</span></div>
        <div className="stat"><b>Bloqué</b><span>Envoi Resend : contact issu d'une collecte web, aucune permission documentée</span></div>
      </div>

      <h2>Coordonnées publiées</h2>
      <div className="table"><table>
        <thead><tr><th>Adresse</th><th>Publiée sur</th><th>Contexte</th><th>Contrôles</th><th>Retenue</th></tr></thead>
        <tbody>
          {contacts.length === 0 && <tr><td colSpan={5} className="muted">{p.email_status === "NO_PUBLIC_EMAIL" ? "Aucune adresse publiée sur les pages lues. Rien n'est deviné." : "Recherche non effectuée."}</td></tr>}
          {contacts.map((x) => (
            <tr key={x.id}>
              <td>{x.email}</td><td>{x.source_url}</td><td>{x.context}</td>
              <td>Publiée · syntaxe valide · {x.domain_routable === true ? "domaine routable" : x.domain_routable === false ? "domaine non routable" : "routage non contrôlé"} · réception non vérifiée</td>
              <td>{x.selected ? <span className="tag ok">Oui</span> : x.excluded_reason ? <span className="tag">Écartée : {x.excluded_reason}</span> : "Non"}</td>
            </tr>))}
        </tbody>
      </table></div>

      <h2>Preuves relevées sur le site</h2>
      <div className="table"><table>
        <thead><tr><th>Élément</th><th>Valeur</th><th>Extrait de la page</th><th>Source</th><th>Relevé le</th></tr></thead>
        <tbody>
          {evidence.length === 0 && <tr><td colSpan={5} className="muted">Aucune preuve enregistrée.</td></tr>}
          {evidence.map((e) => (<tr key={e.id}><td>{KIND[e.kind] ?? e.kind}</td><td>{e.value}</td><td>{e.excerpt}</td><td>{e.source_url}</td><td>{e.observed_at.toLocaleDateString("fr-FR")}</td></tr>))}
        </tbody>
      </table></div>
      <p className="muted" style={{ marginTop: 12 }}>Chaque extrait a été retrouvé mot pour mot dans la page citée. Méthode : {evidence[0]?.extraction_method ?? "sans objet"}.</p>

      <h2>Réponses IA</h2>
      {summary ? <p>{summary.mode_label}, modèle {summary.model}. {summary.validRuns} réponses valides sur {summary.expected_valid_runs} attendues. {summary.reason}.</p> : <p className="muted">Mesure non réalisée.</p>}
      {runs.length > 0 && (
        <div className="table" style={{ marginTop: 16 }}><table>
          <thead><tr><th>Question</th><th className="num">Rép.</th><th>Validité</th><th>Observation pour ce prospect</th><th>Réponse</th></tr></thead>
          <tbody>{runs.map((r) => {
            const obs = observations.filter((o) => o.run_id === r.id && o.type !== "NO_MATCH");
            return (
              <tr key={r.id}>
                <td>{r.prompt}</td><td className="num">{r.repetition}.{r.attempt}</td>
                <td>{r.validity === "VALID" ? <span className="tag ok">Valide</span> : <span className="tag warn">{r.validity} : {r.validity_note}</span>}</td>
                <td>{r.validity !== "VALID" ? <span className="muted">non comptée</span> : obs.length ? obs.map((o) => <div key={o.id}><span className="tag info">{OBS[o.type]}</span> {o.detail}</div>) : "Aucune"}</td>
                <td><details><summary>Lire</summary><pre>{r.response_text}</pre>{r.citations.length > 0 && <p className="muted">Liens cités : {r.citations.map((x) => x.url).join(", ")}</p>}</details></td>
              </tr>);
          })}</tbody>
        </table></div>
      )}

      {audit && (
        <>
          <h2>Pré-audit</h2>
          <p className="muted">
            {publicUrl && !audit.share_revoked ? <>Lien de partage, valable jusqu'au {audit.share_expires_at.toLocaleDateString("fr-FR")} : {publicUrl.replace(/\/$/, "")}/r/{audit.share_token}</> : audit.share_revoked ? "Lien de partage révoqué." : "Pas de lien externe : APP_PUBLIC_URL n'est pas configurée. Aperçu privé ci-dessous."}
          </p>
          {publicUrl && !audit.share_revoked && <form action={revokeShareAction} style={{ marginTop: 12 }}><input type="hidden" name="prospect_id" value={p.id} /><button className="ghost">Révoquer le lien</button></form>}
          <ReportView report={audit.report as AuditReport} />
        </>
      )}

      {draft && (
        <>
          <h2 id="brouillon">Brouillon d'email</h2>
          <p className="muted">Destinataire : {draft.recipient ?? "aucun"} · {draft.word_count} mots · {draft.rewrite_rounds} tour(s) de réécriture · {draft.edited_by_human ? "modifié à la main" : "non modifié"}</p>
          {draft.blockers.map((b) => <div className="banner" key={b} style={{ marginTop: 12 }}>{b}</div>)}
          {check && check.global.map((g) => <div className="banner bad" key={g} style={{ marginTop: 12 }}>{g}</div>)}
          <form action={editDraftAction} className="card" style={{ marginTop: 16 }}>
            <input type="hidden" name="prospect_id" value={p.id} />
            <label>Objet</label>
            <input type="text" name="subject" defaultValue={draft.subject} readOnly={!editable} />
            {(draft.sentences as DraftSentence[]).map((s) => {
              const sc = check?.sentences.find((x) => x.id === s.id);
              return (
                <div key={s.id} style={{ marginTop: 16 }}>
                  <label>{SENTENCE[s.kind]} {sc && <Tag pair={CLAIM[sc.status]} />} {sc?.reason && <span>{sc.reason}</span>}</label>
                  <textarea name={`s:${s.id}`} defaultValue={s.text} readOnly={!editable} />
                </div>);
            })}
            {editable && <div className="row" style={{ marginTop: 16 }}><button className="ghost">Enregistrer et recontrôler</button><span className="muted">Toute modification annule l'approbation et relance le contrôle factuel. Vider une phrase la supprime.</span></div>}
          </form>
          {p.state === "READY_FOR_REVIEW" && (
            <form action={approveDraftAction} style={{ marginTop: 16 }}>
              <input type="hidden" name="prospect_id" value={p.id} />
              <button disabled={!draft.recipient}>Approuver cette version</button>
              <span className="muted"> L'approbation n'envoie rien.</span>
            </form>
          )}
        </>
      )}
    </>
  );
}
