import { eq } from "drizzle-orm";
import Link from "next/link";
import { notFound } from "next/navigation";
import { getDb, schema } from "@/db/client";
import { manualPrompts } from "@/engine/manual";
import { importChatgptAction } from "@/server/actions";

export const dynamic = "force-dynamic";

export default async function ChatgptEntry({ params, searchParams }: { params: Promise<{ id: string }>; searchParams: Promise<{ reps?: string }> }) {
  const { id } = await params;
  const { reps: repsRaw } = await searchParams;
  const reps = Math.min(3, Math.max(1, Number(repsRaw) || 1));
  const [c] = await getDb().select().from(schema.campaigns).where(eq(schema.campaigns.id, id)).catch(() => []);
  if (!c) notFound();
  const prompts = manualPrompts(c);
  const today = new Date().toISOString().slice(0, 10);
  return (
    <>
      <h1>Réponses relevées dans ChatGPT</h1>
      <p className="muted">
        Campagne <Link href={`/campaigns/${c.id}`}>{c.name}</Link>. Posez chaque question dans une conversation neuve de ChatGPT, puis collez la réponse entière, liens compris. L'application ne se connecte pas à ChatGPT.
      </p>
      <p style={{ marginTop: 12 }}>
        Passages par question : {[1, 2, 3].map((n) => (n === reps ? <strong key={n}> {n} </strong> : <Link key={n} href={`/campaigns/${c.id}/chatgpt?reps=${n}`}> {n} </Link>))}
        <span className="muted"> ({prompts.length * reps} réponses à coller)</span>
      </p>
      <form action={importChatgptAction} style={{ marginTop: 28 }}>
        <input type="hidden" name="campaign_id" value={c.id} />
        <input type="hidden" name="questions" value={prompts.length} />
        <input type="hidden" name="reps" value={reps} />
        {prompts.map((prompt, p) => (
          <div className="card" key={p}>
            <h3>Question {p + 1}</h3>
            <p><code>{prompt}</code></p>
            {Array.from({ length: reps }, (_, r) => (
              <div key={r} style={{ marginTop: 12 }}>
                <label htmlFor={`r-${p}-${r}`}>Réponse de ChatGPT{reps > 1 ? `, passage ${r + 1}` : ""}</label>
                <textarea id={`r-${p}-${r}`} name={`r:${p}:${r}`} required style={{ minHeight: 140 }} />
              </div>
            ))}
          </div>
        ))}
        <div className="card">
          <div className="form">
            <div><label>Date des réponses</label><input type="text" name="observed_at" defaultValue={today} /></div>
            <div><label>Modèle affiché dans ChatGPT (vide si non noté)</label><input type="text" name="model" /></div>
            <div><label>Recherche web utilisée</label>
              <select name="web_search" defaultValue="inconnu"><option value="inconnu">Je ne sais pas</option><option value="oui">Oui</option><option value="non">Non</option></select>
            </div>
          </div>
          <p className="muted" style={{ marginTop: 16 }}>À l'enregistrement, les cabinets déjà qualifiés repassent par la mesure sur ces réponses et leurs emails sont rédigés à nouveau. Les réponses de l'API restent conservées.</p>
          <div className="row" style={{ marginTop: 16 }}><button>Enregistrer et recalculer</button></div>
        </div>
      </form>
    </>
  );
}
