import { toCsv } from "@/core/csv";
import { getDb } from "@/db/client";
import { integrations } from "@/server/context";
import { exportProspects, KEYWORD_COLUMNS, PROSPECT_COLUMNS } from "@/server/export";

export const dynamic = "force-dynamic";

export async function GET(request: Request, { params }: { params: Promise<{ kind: string }> }) {
  const { kind } = await params;
  const campaignId = new URL(request.url).searchParams.get("campaign") ?? "";
  if (!/^[0-9a-f-]{36}$/.test(campaignId)) return new Response("Campagne invalide", { status: 400 });
  const data = await exportProspects(getDb(), campaignId, integrations().publicUrl);
  if (!data) return new Response("Campagne introuvable", { status: 404 });
  const file = (name: string, type: string, body: string) => new Response(body, { headers: { "content-type": `${type}; charset=utf-8`, "content-disposition": `attachment; filename="${name}"`, "cache-control": "no-store" } });
  if (kind === "prospects") return file("prospects.csv", "text/csv", toCsv(PROSPECT_COLUMNS, data.rows));
  if (kind === "keywords") return file("mots-cles.csv", "text/csv", toCsv(KEYWORD_COLUMNS, data.keywords as unknown as Record<string, unknown>[]));
  if (kind === "json") return file("campagne.json", "application/json", JSON.stringify({ campaign: { id: data.campaign.id, name: data.campaign.name, config: data.campaign.config, simulation: data.campaign.simulation }, prospects: data.rows, keywords: data.keywords }, null, 2));
  return new Response("Export inconnu", { status: 404 });
}
