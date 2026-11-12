import * as cheerio from "cheerio";
import { squash } from "../core/text";

export interface ParsedPage {
  title: string | null;
  h1s: string[];
  canonical: string | null;
  metaRobots: string | null;
  text: string;
  links: { href: string; anchor: string }[];
  mailtos: { email: string; context: string }[];
  jsonLdTypes: string[];
}

function collectTypes(node: unknown, out: Set<string>): void {
  if (Array.isArray(node)) return node.forEach((n) => collectTypes(n, out));
  if (!node || typeof node !== "object") return;
  const o = node as Record<string, unknown>;
  const t = o["@type"];
  if (typeof t === "string") out.add(t);
  if (Array.isArray(t)) t.forEach((x) => typeof x === "string" && out.add(x));
  if (o["@graph"]) collectTypes(o["@graph"], out);
}

/** Extraction déterministe. Le HTML d'une source n'est jamais exécuté ni réaffiché : seuls ces champs texte sont conservés. */
export function parsePage(pageUrl: string, html: string): ParsedPage {
  const $ = cheerio.load(html);
  const types = new Set<string>();
  $('script[type="application/ld+json"]').each((_, el) => {
    try {
      collectTypes(JSON.parse($(el).text()), types);
    } catch {
      // JSON-LD illisible : ignoré, rien n'est supposé.
    }
  });

  const links: ParsedPage["links"] = [];
  const mailtos: ParsedPage["mailtos"] = [];
  $("a[href]").each((_, el) => {
    const raw = ($(el).attr("href") ?? "").trim();
    if (/^mailto:/i.test(raw)) {
      const email = decodeURIComponent(raw.slice(7).split("?")[0]).trim();
      const context = squash($(el).closest("p,li,div,address,section,footer,td").first().text()).slice(0, 300);
      if (email) mailtos.push({ email, context });
      return;
    }
    if (!raw || /^(tel:|javascript:|#|data:)/i.test(raw)) return;
    try {
      const u = new URL(raw, pageUrl);
      u.hash = "";
      links.push({ href: u.toString(), anchor: squash($(el).text()).slice(0, 120) });
    } catch {
      // lien illisible
    }
  });

  const title = squash($("head > title").first().text()) || null;
  const h1s = $("h1").map((_, el) => squash($(el).text())).get().filter(Boolean);
  const canonicalRaw = $('link[rel="canonical"]').attr("href");
  let canonical: string | null = null;
  if (canonicalRaw) {
    try {
      canonical = new URL(canonicalRaw, pageUrl).toString();
    } catch {
      canonical = canonicalRaw;
    }
  }
  const metaRobots = $('meta[name="robots" i]').attr("content")?.toLowerCase() ?? null;
  $("script,style,noscript,template,svg,iframe").remove();
  $("br,p,div,li,h1,h2,h3,h4,h5,h6,tr,section,article,header,footer,address").each((_, el) => {
    $(el).append(" ");
  });
  const text = squash($("body").text()).slice(0, 60000);
  return { title, h1s, canonical, metaRobots, text, links, mailtos, jsonLdTypes: [...types] };
}

export function parseSitemap(xml: string): { urls: string[]; children: string[] } {
  const locs = [...xml.matchAll(/<loc>\s*(?:<!\[CDATA\[)?\s*([^<\]\s]+)\s*(?:\]\]>)?\s*<\/loc>/gi)].map((m) => m[1].replace(/&amp;/g, "&"));
  const isIndex = /<sitemapindex/i.test(xml);
  return isIndex ? { urls: [], children: locs } : { urls: locs, children: [] };
}
