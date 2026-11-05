import { CampaignConfigSchema, parseObjective } from "@/core/objective";
import { createCampaignAction } from "@/server/actions";
import { integrations } from "@/server/context";

export const dynamic = "force-dynamic";

const FIELD: Record<string, string> = { target_count: "le nombre de prospects visé", practice_area: "le domaine de pratique", location: "la ville" };

export default async function NewCampaign({ searchParams }: { searchParams: Promise<{ q?: string }> }) {
  const { q } = await searchParams;
  const parsed = q ? parseObjective(q) : null;
  const defaults = CampaignConfigSchema.parse({ practice_area: "à renseigner", location: "à renseigner" });
  const d = { ...defaults, practice_area: "", location: "", ...(parsed?.draft ?? {}) };
  const integ = integrations();
  return (
    <>
      <h1>Nouvelle campagne</h1>
      <p className="muted">Décrivez l'objectif en une phrase. L'application en propose une lecture, que vous corrigez avant de créer la campagne.</p>
      <form method="get" className="card" style={{ marginTop: 28 }}>
        <label htmlFor="q">Objectif</label>
        <textarea id="q" name="q" defaultValue={q ?? ""} placeholder="Trouve-moi 30 avocats en droit du travail à Lyon qui accompagnent les employeurs. Vérifie leur visibilité dans les réponses IA, prépare pré-audit, mots-clés et email. Ne rien envoyer." />
        <div className="row" style={{ marginTop: 12 }}><button className="ghost">Interpréter</button></div>
      </form>

      {parsed && (
        <>
          <h2>Lecture de la commande</h2>
          {parsed.missing.length > 0 && <div className="banner">Non trouvé dans le texte : {parsed.missing.map((m) => FIELD[m] ?? m).join(", ")}. À renseigner ci-dessous.</div>}
          {parsed.notes.map((n) => <div key={n} className="banner">{n}</div>)}
        </>
      )}

      <h2>Configuration</h2>
      <form action={createCampaignAction} className="card">
        <input type="hidden" name="objective_text" value={q ?? ""} />
        <div className="form">
          <div><label>Nom de la campagne</label><input type="text" name="name" placeholder="Droit du travail, Lyon, employeurs" /></div>
          <div><label>Domaine de pratique</label><input type="text" name="practice_area" required defaultValue={d.practice_area} /></div>
          <div><label>Sous-spécialités (séparées par des virgules)</label><input type="text" name="subspecialties" defaultValue={d.subspecialties.join(", ")} /></div>
          <div><label>Ville</label><input type="text" name="location" required defaultValue={d.location} /></div>
          <div><label>Clientèle</label>
            <select name="client_type" defaultValue={d.client_type}><option value="entreprise">Entreprises, employeurs</option><option value="particulier">Particuliers, salariés</option><option value="mixte">Mixte</option></select>
          </div>
          <div><label>Ciblage</label>
            <select name="target_type" defaultValue={d.target_type}><option value="FIRM">Cabinet</option><option value="LAWYER">Avocat individuel</option></select>
          </div>
          <div><label>Nombre visé</label><input type="number" name="target_count" min={1} max={200} required defaultValue={d.target_count} /></div>
          <div><label>Ce nombre compte</label>
            <select name="goal_type" defaultValue={d.goal_type}><option value="EMAIL_READY_PROSPECTS">les prospects avec email prêt à relire</option><option value="AUDITED_PROSPECTS">les prospects audités</option><option value="QUALIFIED_PROSPECTS">les prospects qualifiés</option></select>
          </div>
        </div>
        <div className="row" style={{ marginTop: 20, gap: 24 }}>
          <label className="check"><input type="checkbox" name="generate_audit" defaultChecked={d.generate_audit_if !== "NEVER"} /> Pré-audit si non observé</label>
          <label className="check"><input type="checkbox" name="generate_keywords" defaultChecked={d.generate_keywords} /> Mots-clés</label>
          <label className="check"><input type="checkbox" name="generate_email" defaultChecked={d.generate_email} /> Brouillon d'email</label>
          <label className="check"><input type="checkbox" name="certified" defaultChecked={d.certified_specialization_required} /> Spécialisation certifiée exigée</label>
        </div>
        <h2 style={{ marginTop: 32 }}>Limites et budget</h2>
        <div className="form">
          <div><label>Tours de découverte au plus</label><input type="number" name="max_discovery_rounds" min={1} max={20} defaultValue={d.max_discovery_rounds} /></div>
          <div><label>Candidats par tour</label><input type="number" name="max_candidates_per_round" min={1} max={50} defaultValue={d.max_candidates_per_round} /></div>
          <div><label>Résultats de découverte au plus</label><input type="number" name="max_total_discovery_results" min={1} max={600} defaultValue={d.max_total_discovery_results} /></div>
          <div><label>Budget de la campagne ($)</label><input type="number" name="max_campaign_cost_usd" min={0} max={500} step="0.5" defaultValue={d.max_campaign_cost_usd} /></div>
          <div><label>Budget par prospect ($)</label><input type="number" name="max_prospect_cost_usd" min={0} max={20} step="0.1" defaultValue={d.max_prospect_cost_usd} /></div>
          <div><label>Domaines exclus (séparés par des virgules)</label><input type="text" name="excluded_domains" /></div>
          <div><label>Mode</label>
            <select name="mode" defaultValue="simulation">
              <option value="simulation">Simulation (données fictives, aucun appel)</option>
              <option value="real" disabled={integ.openaiMissing.length > 0}>Réel, via l'API Claude{integ.openaiMissing.length > 0 ? " (non configurée)" : ""}</option>
            </select>
          </div>
        </div>
        <p className="muted" style={{ marginTop: 20 }}>Aucun envoi d'email n'existe dans cette version : la campagne s'arrête aux brouillons à relire.</p>
        <div className="row" style={{ marginTop: 20 }}><button>Créer la campagne</button></div>
      </form>
    </>
  );
}
