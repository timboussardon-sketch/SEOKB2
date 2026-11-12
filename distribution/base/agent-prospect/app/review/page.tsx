import { asc, eq, inArray } from "drizzle-orm";
import Link from "next/link";
import { getDb, schema } from "@/db/client";
import { REVIEW_ACTIONS } from "@/engine/review";
import { reviewAction } from "@/server/actions";
import { ACTION_LABEL, REVIEW_LABEL } from "@/server/labels";

export const dynamic = "force-dynamic";

export default async function Review() {
  const db = getDb();
  const items = await db.select().from(schema.review_items).where(eq(schema.review_items.status, "OPEN")).orderBy(asc(schema.review_items.created_at));
  const prospects = items.length ? await db.select().from(schema.prospects).where(inArray(schema.prospects.id, items.map((i) => i.prospect_id))) : [];
  const firms = prospects.length ? await db.select().from(schema.firms).where(inArray(schema.firms.id, prospects.map((p) => p.firm_id))) : [];
  return (
    <>
      <h1>Revue humaine</h1>
      <p className="muted">Les cas où l'agent s'est arrêté plutôt que de trancher seul.</p>
      {items.length === 0 && <p style={{ marginTop: 28 }}>Rien à relire.</p>}
      <div style={{ marginTop: 28 }}>
        {items.map((item) => {
          const p = prospects.find((x) => x.id === item.prospect_id);
          const firm = firms.find((f) => f.id === p?.firm_id);
          return (
            <div className="card" key={item.id}>
              <div className="row" style={{ justifyContent: "space-between" }}>
                <h3><Link href={`/prospects/${item.prospect_id}`}>{firm?.name ?? firm?.canonical_domain}</Link> · {REVIEW_LABEL[item.reason] ?? item.reason}</h3>
                <div className="row">
                  {item.reason === "UNSUPPORTED_CLAIM" && <Link className="btn ghost" href={`/prospects/${item.prospect_id}#brouillon`}>Corriger le brouillon</Link>}
                  {REVIEW_ACTIONS[item.reason]?.map((a) => (
                    <form action={reviewAction} key={a}>
                      <input type="hidden" name="id" value={item.id} />
                      <input type="hidden" name="action" value={a} />
                      <button className={a === "REJECT" ? "danger" : a === "RETRY" ? "ghost" : ""}>{ACTION_LABEL[a]}</button>
                    </form>
                  ))}
                </div>
              </div>
              <p>{item.detail}</p>
            </div>
          );
        })}
      </div>
    </>
  );
}
