import type { Segment } from "../core/benchmark";
import type { Fetcher } from "../net/fetcher";
import { FixtureFetcher } from "../net/fetcher";
import { AppError } from "../core/errors";
import { HeuristicAnalyst } from "./heuristic-analyst";
import type { CallEstimate, Providers, SearchCandidate, SearchProvider, Usage, VisibilityAnswer, VisibilityProvider } from "./types";

const ZERO: Usage = { model: "simulation", input_tokens: 0, output_tokens: 0, web_search_calls: 0, reported: null };
const EST: CallEstimate = { model: "simulation", input_tokens: 0, output_tokens: 0, web_search_calls: 0 };

const FIRST = ["Claire", "Hugo", "Inès", "Paul", "Nora", "Louis", "Jeanne", "Malo", "Élise", "Théo"];
const KINDS = ["GOOD", "GOOD", "GOOD_MULTI", "WRONG_LOCATION", "OBSERVED", "WRONG_PRACTICE", "NO_EMAIL", "WRONG_CLIENT", "FIRM_ONLY", "UNREACHABLE"] as const;
type Kind = (typeof KINDS)[number] | "ROBOTS_BLOCKED";

export interface SimFirm {
  kind: Kind;
  domain: string;
  website: string;
  firmName: string;
  first: string;
  last: string;
}

const slug = (s: string) => s.normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");

/** Monde fictif : cabinets, sites et réponses inventés, sous le domaine réservé .test. Rien ne décrit un cabinet réel. */
export function buildSimWorld(seg: Segment, size: number): { firms: SimFirm[]; pages: Map<string, { status?: number; body: string; contentType?: string; error?: AppError }> } {
  const firms: SimFirm[] = [];
  const pages = new Map<string, { status?: number; body: string; contentType?: string; error?: AppError }>();
  const otherClient = seg.clientType === "particulier" ? "entreprise" : "particulier";
  const clientSentence = (c: string, practice: string) =>
    c === "entreprise" ? `Le cabinet accompagne les employeurs et les dirigeants en ${practice}.` : `Le cabinet défend les salariés et les particuliers en ${practice}.`;

  for (let i = 0; i < size; i++) {
    let kind: Kind = KINDS[i % 10];
    if (kind === "UNREACHABLE" && i % 20 === 9) kind = "ROBOTS_BLOCKED";
    if (kind === "WRONG_CLIENT" && seg.clientType === "mixte") kind = "GOOD";
    const code = `${String.fromCharCode(97 + (i % 26))}${i + 1}`;
    const first = FIRST[i % FIRST.length];
    const last = `Exemple-${code.toUpperCase()}`;
    const firmName = `Cabinet Fictif ${code.toUpperCase()}`;
    const domain = `cabinet-fictif-${code}.exemple-fictif.test`;
    const base = `https://${domain}`;
    firms.push({ kind, domain, website: `${base}/`, firmName, first, last });
    if (kind === "UNREACHABLE") continue;

    const city = kind === "WRONG_LOCATION" ? "Villefictive" : seg.city;
    const practice = kind === "WRONG_PRACTICE" ? "droit de la famille" : seg.practice;
    const client = kind === "WRONG_CLIENT" ? otherClient : seg.clientType === "mixte" ? "entreprise" : seg.clientType;
    const services = [`Contentieux en ${practice}`, `Conseil en ${practice}`, `Audit de conformité en ${practice}`, `Formation en ${practice}`, `Négociation en ${practice}`];
    const nav = [
      `<a href="/cabinet">Le cabinet</a>`,
      ...services.map((s) => `<a href="/expertises/${slug(s)}">${s}</a>`),
      `<a href="/honoraires">Honoraires</a>`,
      `<a href="/contact">Contact</a>`,
      `<a href="/mentions-legales">Mentions légales</a>`,
      ...(i % 3 === 0 ? [`<a href="/actualites">Actualités</a>`] : []),
    ].join(" ");
    const page = (path: string, title: string | null, h1: string | null, body: string, extraHead = "") =>
      pages.set(`${base}${path}`, {
        body: `<!doctype html><html lang="fr"><head>${title ? `<title>${title}</title>` : ""}<link rel="canonical" href="${base}${path}">${extraHead}</head><body>${h1 ? `<h1>${h1}</h1>` : ""}<p>Site fictif de démonstration.</p>${body}<nav>${nav}</nav></body></html>`,
      });
    const second = kind === "GOOD_MULTI" ? ` Maître ${FIRST[(i + 3) % FIRST.length]} Exemple-${code.toUpperCase()}B exerce à ses côtés.` : "";

    pages.set(`${base}/robots.txt`, { body: kind === "ROBOTS_BLOCKED" ? "User-agent: *\nDisallow: /\n" : `User-agent: *\nDisallow: /admin\nSitemap: ${base}/sitemap.xml\n`, contentType: "text/plain" });
    pages.set(`${base}/sitemap.xml`, {
      contentType: "application/xml",
      body: `<?xml version="1.0"?><urlset>${["/", "/cabinet", "/contact", ...services.slice(0, 3).map((s) => `/expertises/${slug(s)}`)].map((p) => `<url><loc>${base}${p}</loc></url>`).join("")}</urlset>`,
    });
    page("/", `${firmName} - Avocat en ${practice} à ${city}`, firmName, `<p>Maître ${first} ${last}, avocat au barreau de ${city}, exerce en ${practice}.${second}</p><p>${clientSentence(client, practice)}</p>`);
    page("/cabinet", `Le cabinet - ${firmName}`, "Le cabinet", `<p>${firmName} est un cabinet à ${city}.</p><p>${clientSentence(client, practice)}</p>`);
    services.forEach((s, j) =>
      page(`/expertises/${slug(s)}`, j === 3 ? null : `${s} - ${firmName}`, s, `<p>${s} : le cabinet intervient à ${city} pour ses clients.</p>`, j === 4 ? `<meta name="robots" content="noindex">` : ""),
    );
    page("/honoraires", `Honoraires - ${firmName}`, i % 2 === 0 ? "Honoraires" : null, `<p>Les honoraires sont fixés par convention après un premier rendez-vous.</p>`);
    page(
      "/contact",
      `Contact - ${firmName}`,
      "Contact",
      kind === "NO_EMAIL"
        ? `<p>Pour joindre le cabinet, utilisez le formulaire de cette page.</p>`
        : `<p>Écrire au cabinet : <a href="mailto:contact@${domain}">contact@${domain}</a></p><p>Recrutement : <a href="mailto:recrutement@${domain}">recrutement@${domain}</a></p>`,
    );
    page("/mentions-legales", `Mentions légales - ${firmName}`, "Mentions légales", `<p>Site réalisé par une agence fictive : webmaster@agence-fictive.test</p>`);
  }
  return { firms, pages };
}

export class SimSearch implements SearchProvider {
  name = "SIMULATION";
  model = "simulation";
  constructor(private firms: SimFirm[]) {}
  estimate() {
    return EST;
  }
  async search(query: string, limit: number, excludeDomains: string[]): Promise<{ candidates: SearchCandidate[]; usage: Usage }> {
    // Sans état : la suite du monde fictif après les domaines déjà connus, plus deux résultats déjà vus pour exercer la déduplication.
    const firstNew = this.firms.findIndex((f) => !excludeDomains.includes(f.domain));
    if (firstNew === -1) return { candidates: [], usage: ZERO };
    const start = Math.max(0, firstNew - 2);
    const slice = this.firms.slice(start, start + limit);
    return {
      candidates: slice.map((f) => ({ name: f.firmName, website: f.website, source_url: `https://annuaire.exemple-fictif.test/recherche?q=${encodeURIComponent(query)}`, snippet: `${f.firmName} (fictif)` })),
      usage: ZERO,
    };
  }
}

export class SimVisibility implements VisibilityProvider {
  name = "SIMULATION" as const;
  model = "simulation";
  params = { world: "fictif" };
  requireWebSearch = false;
  constructor(private firms: SimFirm[]) {}
  estimate() {
    return EST;
  }
  async ask(prompt: string, city: string): Promise<VisibilityAnswer> {
    const observed = this.firms.filter((f) => f.kind === "OBSERVED");
    const cited = this.firms.filter((f) => f.kind === "FIRM_ONLY");
    const names = observed.slice(0, 3).map((f) => `Maître ${f.first} ${f.last} (${f.firmName})`);
    const text =
      `Réponse simulée à la question « ${prompt} ». Plusieurs cabinets d'avocats interviennent à ${city}. ` +
      `Vous pouvez examiner ${names.length ? names.join(", ") : "le Cabinet Générique Fictif"}, ainsi que le Cabinet Générique Fictif. ` +
      `Comparez leurs domaines d'intervention, leurs honoraires et leur disponibilité avant de prendre rendez-vous.`;
    return { text, citations: cited.slice(0, 2).map((f) => ({ url: `${f.website}cabinet`, title: "Page du cabinet" })), webSearchUsed: false, responseId: null, usage: ZERO };
  }
}

export function simulationProviders(seg: Segment, size: number): { providers: Providers; fetcher: Fetcher; world: ReturnType<typeof buildSimWorld> } {
  const world = buildSimWorld(seg, size);
  return {
    world,
    fetcher: new FixtureFetcher(world.pages),
    providers: { search: new SimSearch(world.firms), visibility: new SimVisibility(world.firms), analyst: new HeuristicAnalyst() },
  };
}
