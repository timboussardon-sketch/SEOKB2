// Importe les avocats relevés dans l'annuaire du CNB (~/Code/prospection/avocats/cnb/fiches.jsonl) comme prospects.
// Une campagne par segment × ville du cabinet ; l'agent qualifie, cherche l'adresse, mesure, rédige. Idempotent : un domaine déjà connu n'est pas réimporté.
// npx tsx --env-file=.env.local scripts/import-cnb.ts [chemin.jsonl] [--dry]
import { readFileSync } from "node:fs";
import { and, eq } from "drizzle-orm";
import { MISSION_SEGMENTS } from "../src/core/mission";
import { canonicalDomain } from "../src/core/text";
import { createDb, schema } from "../src/db/client";
import { createCampaign, startCampaign } from "../src/engine/campaign";
import { bossQueue, createBoss } from "../src/engine/queue";
import { buildDeps } from "../src/engine/runtime";

interface Fiche { url_cnb: string; nom: string | null; cabinet: string | null; site: string | null; listes: string[]; code_postal: string | null }

const path = process.argv.find((a) => a.endsWith(".jsonl")) ?? `${process.env.HOME}/Code/prospection/avocats/cnb/fiches.jsonl`;
const dry = process.argv.includes("--dry");
const SECU = ["comp-54", "comp-52", "comp-53", "specialistes-securite-sociale"];
const TRAVAIL = ["comp-49", "comp-50", "comp-51"];
// Plateformes et annuaires : pas le site du cabinet.
const NOT_OWN_SITE = /(^|\.)(avocat\.fr|linkedin\.com|facebook\.com|doctrine\.fr|justifit\.fr|alexia\.fr|pagesjaunes\.fr|google\.com|sites\.google\.com)$/i;

function ville(cabinet: string | null): string | null {
  const m = cabinet?.match(/\b\d{5}\s+(.+?)(?:\s+CEDEX.*)?$/i);
  if (!m) return null;
  const v = m[1].replace(/\s+\d+$/, "").trim().toLowerCase().replace(/(^|[\s-])\p{L}/gu, (c) => c.toUpperCase());
  return v.replace(/^Paris.*/, "Paris").replace(/^(Lyon|Marseille)\s.*/, "$1");
}

const fiches: Fiche[] = readFileSync(path, "utf-8").split("\n").filter(Boolean).map((l) => JSON.parse(l));
const url = process.env.DATABASE_URL!;
const { db, pool } = createDb(url);
const boss = await createBoss(url);
const deps = buildDeps(db, pool, bossQueue(boss));

const known = new Set((await db.select({ d: schema.firms.canonical_domain }).from(schema.firms)).map((r) => r.d));
const groups = new Map<string, { segment: (typeof MISSION_SEGMENTS)[number]; city: string; items: { f: Fiche; domain: string; website: string }[] }>();
let sansSite = 0, connus = 0, sansVille = 0;
for (const f of fiches) {
  if (!f.site) { sansSite++; continue; }
  const website = /^https?:\/\//.test(f.site) ? f.site : `https://${f.site}`;
  const domain = canonicalDomain(website);
  if (!domain || NOT_OWN_SITE.test(domain)) { sansSite++; continue; }
  if (known.has(domain)) { connus++; continue; }
  const city = ville(f.cabinet);
  if (!city) { sansVille++; continue; }
  const key = f.listes.some((l) => SECU.includes(l)) && !f.listes.every((l) => TRAVAIL.includes(l)) ? "urssaf" : "travail";
  const segment = MISSION_SEGMENTS.find((s) => s.key === key)!;
  const g = groups.get(`${key}|${city}`) ?? { segment, city, items: [] };
  g.items.push({ f, domain, website: new URL("/", website).toString() });
  groups.set(`${key}|${city}`, g);
  known.add(domain);
}
console.log({ fiches: fiches.length, sansSite, connus, sansVille, campagnes: groups.size, prospects: [...groups.values()].reduce((n, g) => n + g.items.length, 0) });

if (!dry) {
  for (const g of groups.values()) {
    const c = await createCampaign(deps, {
      name: `Annuaire CNB : ${g.segment.label}, ${g.city}`,
      objectiveText: `Avocats de l'annuaire du CNB, compétences côté employeur, ${g.city}`,
      simulation: false,
      config: {
        practice_area: g.segment.practice_area, subspecialties: g.segment.subspecialties, location: g.city, client_type: g.segment.client_type,
        target_count: g.items.length, goal_type: "EMAIL_READY_PROSPECTS", visibility_mode: "OPENAI_CODEX_WEB_SEARCH",
        // Les prospects viennent de l'annuaire : la découverte par recherche web reste au minimum.
        max_discovery_rounds: 1, max_candidates_per_round: 1, max_total_discovery_results: 1,
      },
    });
    for (const { f, domain, website } of g.items) {
      await db.insert(schema.firms).values({ canonical_domain: domain, website }).onConflictDoNothing();
      const [firm] = await db.select().from(schema.firms).where(eq(schema.firms.canonical_domain, domain));
      const exists = await db.select().from(schema.prospects).where(and(eq(schema.prospects.campaign_id, c.id), eq(schema.prospects.firm_id, firm.id)));
      if (!exists.length) await db.insert(schema.prospects).values({ campaign_id: c.id, firm_id: firm.id, candidate_name: (f.nom ?? f.cabinet ?? "").slice(0, 200) || null, source_url: f.url_cnb });
    }
    await startCampaign(deps, c.id);
    console.log(`${c.name} : ${g.items.length} prospects`);
  }
}
await boss.stop();
await pool.end();
