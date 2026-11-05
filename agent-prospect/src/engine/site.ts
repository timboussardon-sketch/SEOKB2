import { eq } from "drizzle-orm";
import { schema } from "../db/client";
import { AppError, classify, withRetry } from "../core/errors";
import { canonicalDomain, normalize } from "../core/text";
import type { Fetcher } from "../net/fetcher";
import { parsePage, parseSitemap } from "../net/parse";
import { isAllowed, parseRobots, type Robots } from "../net/robots";
import type { Deps, Firm, SitePage } from "./deps";

// Les pages de prestations d'abord : c'est d'elles que dépendent la qualification et les mots-clés.
const PRIORITY: [RegExp, number][] = [
  [/expertise|competence|domaine|prestation|droit-|activites|intervention/, 9],
  [/equipe|avocats?|associes|qui-sommes|a-propos|apropos|cabinet|presentation/, 8],
  [/contact|coordonnees|rendez-vous|rdv/, 7],
  [/honoraires|tarifs/, 6],
  [/mentions-legales/, 4],
  [/actualites?|blog|articles?|news/, 0],
];
const SKIP_EXT = /\.(pdf|jpe?g|png|gif|webp|svg|zip|docx?|xlsx?|mp4|mp3|css|js|ico|xml|json)$/i;

function priority(url: string, anchor: string): number {
  const hay = normalize(`${new URL(url).pathname} ${anchor}`).replace(/\s/g, "-");
  let best = 1;
  for (const [re, score] of PRIORITY) if (re.test(hay)) best = Math.max(best, score);
  return best - new URL(url).pathname.split("/").filter(Boolean).length * 0.1;
}

export const pageKey = (url: string) => {
  const u = new URL(url);
  u.hash = "";
  u.search = "";
  return u.toString().replace(/\/$/, "") || u.origin;
};

async function loadPages(deps: Deps, firmId: string): Promise<SitePage[]> {
  return deps.db.select().from(schema.site_pages).where(eq(schema.site_pages.firm_id, firmId));
}

async function fetchOne(deps: Deps, fetcher: Fetcher, url: string) {
  return withRetry(() => fetcher.fetch(url), { sleep: deps.sleep, random: deps.random });
}

/** Lit robots.txt et le sitemap une seule fois par cabinet (budget séparé des pages HTML). */
async function ensureSiteMeta(deps: Deps, fetcher: Fetcher, firm: Firm): Promise<Firm> {
  if (firm.robots_status) return firm;
  const origin = new URL(firm.website).origin;
  let robotsStatus = "NONE";
  let robotsTxt = "";
  let blocked: string | null = null;
  try {
    const res = await fetchOne(deps, fetcher, `${origin}/robots.txt`);
    if (res.status === 200 && !/<html/i.test(res.body.slice(0, 300))) {
      robotsStatus = "FOUND";
      robotsTxt = res.body.slice(0, 100_000);
    }
  } catch (err) {
    const c = classify(err);
    if (c.category === "BLOCKED_SOURCE") blocked = c.message;
    else if (c.category === "DNS_ERROR") throw err;
    robotsStatus = "UNREADABLE";
  }
  const robots = parseRobots(robotsTxt);
  if (!blocked && !isAllowed(robots, `${origin}/`)) blocked = "robots.txt interdit l'exploration du site";

  let sitemapUrls: string[] = [];
  if (!blocked) {
    const candidates = robots.sitemaps.length ? robots.sitemaps.slice(0, 1) : [`${origin}/sitemap.xml`];
    try {
      const res = await fetchOne(deps, fetcher, candidates[0]);
      if (res.status === 200) {
        let parsed = parseSitemap(res.body);
        if (parsed.children.length) {
          const child = await fetchOne(deps, fetcher, parsed.children[0]);
          if (child.status === 200) parsed = parseSitemap(child.body);
        }
        const domain = canonicalDomain(origin);
        sitemapUrls = parsed.urls.filter((u) => canonicalDomain(u) === domain).slice(0, 500);
      }
    } catch {
      // Sitemap illisible : le contrôle « présence dans le sitemap » restera sans donnée.
    }
  }
  const [updated] = await deps.db
    .update(schema.firms)
    .set({ robots_status: robotsStatus, robots_txt: robotsTxt, sitemap_urls: sitemapUrls, crawl_blocked_reason: blocked })
    .where(eq(schema.firms.id, firm.id))
    .returning();
  return updated;
}

async function storePage(deps: Deps, fetcher: Fetcher, firm: Firm, url: string, sitemap: Set<string>): Promise<void> {
  const base = { firm_id: firm.id, url, in_sitemap: sitemap.size ? sitemap.has(pageKey(url)) : null, fetched_at: deps.now() };
  try {
    const res = await fetchOne(deps, fetcher, url);
    const isHtml = res.contentType.includes("html") || /<html/i.test(res.body.slice(0, 500));
    const parsed = res.status === 200 && isHtml ? parsePage(res.finalUrl, res.body) : null;
    await deps.db
      .insert(schema.site_pages)
      .values({
        ...base,
        final_url: res.finalUrl,
        status: res.status,
        redirect_chain: res.redirectChain,
        x_robots: res.headers["x-robots-tag"]?.toLowerCase() ?? null,
        title: parsed?.title ?? null,
        h1s: parsed?.h1s ?? [],
        canonical: parsed?.canonical ?? null,
        meta_robots: parsed?.metaRobots ?? null,
        text: parsed?.text ?? null,
        links: parsed?.links ?? [],
        mailtos: parsed?.mailtos ?? [],
        json_ld_types: parsed?.jsonLdTypes ?? [],
      })
      .onConflictDoNothing();
  } catch (err) {
    const c = classify(err);
    if (c.category === "BLOCKED_SOURCE") throw err;
    await deps.db.insert(schema.site_pages).values({ ...base, error_category: c.category }).onConflictDoNothing();
  }
}

/**
 * Garantit qu'au moins `wanted` pages du site ont été tentées (dans la limite `max`), en reprenant là où l'on s'est arrêté.
 * Seules des URL réellement vues dans le maillage ou le sitemap sont visitées : aucun chemin n'est deviné.
 * Un blocage (403, robots.txt) arrête l'exploration, sans contournement.
 */
export async function ensureSitePages(deps: Deps, fetcher: Fetcher, firmIn: Firm, wanted: number, max: number): Promise<{ firm: Firm; pages: SitePage[] }> {
  const firm = await ensureSiteMeta(deps, fetcher, firmIn);
  if (firm.crawl_blocked_reason) throw new AppError("BLOCKED_SOURCE", firm.crawl_blocked_reason);
  const robots: Robots = parseRobots(firm.robots_txt ?? "");
  const domain = firm.canonical_domain;
  const sitemap = new Set(firm.sitemap_urls.map(pageKey));
  const home = pageKey(firm.website);
  const target = Math.min(wanted, max);

  let pages = await loadPages(deps, firm.id);
  if (!pages.some((p) => p.url === home)) {
    await storePage(deps, fetcher, firm, home, sitemap);
    pages = await loadPages(deps, firm.id);
  }
  while (pages.length < target) {
    const tried = new Set(pages.flatMap((p) => [p.url, p.final_url ? pageKey(p.final_url) : p.url]));
    const candidates = new Map<string, number>();
    const consider = (href: string, anchor: string) => {
      let key: string;
      try {
        key = pageKey(href);
      } catch {
        return;
      }
      if (tried.has(key) || canonicalDomain(key) !== domain || SKIP_EXT.test(new URL(key).pathname) || !isAllowed(robots, key)) return;
      candidates.set(key, Math.max(candidates.get(key) ?? 0, priority(key, anchor)));
    };
    for (const p of pages) for (const l of p.links) consider(l.href, l.anchor);
    for (const u of firm.sitemap_urls) consider(u, "");
    const next = [...candidates.entries()].sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]))[0];
    if (!next) break;
    await storePage(deps, fetcher, firm, next[0], sitemap);
    pages = await loadPages(deps, firm.id);
  }
  return { firm, pages };
}

export const okPages = (pages: SitePage[]) => pages.filter((p) => p.status === 200 && p.text);
