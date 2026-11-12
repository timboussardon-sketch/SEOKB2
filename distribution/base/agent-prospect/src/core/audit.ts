export const AUDIT_RULE_VERSION = "audit-v1";

export interface AuditPage {
  url: string;
  status: number | null;
  error_category: string | null;
  title: string | null;
  h1s: string[];
  canonical: string | null;
  meta_robots: string | null;
  x_robots: string | null;
  links: { href: string; anchor: string }[];
  json_ld_types: string[];
  in_sitemap: boolean | null;
}

export type Confidence = "CONFIRMED" | "HYPOTHESIS" | "INSUFFICIENT_DATA";

export interface Finding {
  id: string;
  finding: string;
  urls: string[];
  evidence: string;
  method: string;
  impact: string;
  recommended_action: string;
  priority: 1 | 2 | 3;
  confidence_status: Confidence;
}

const key = (u: string) => u.replace(/[#?].*$/, "").replace(/\/$/, "");
const plural = (n: number, one: string, many: string) => (n > 1 ? many : one);

/**
 * Constats tirés des seules pages lues. Chaque décompte est rapporté au nombre de pages analysées,
 * jamais étendu au site entier. Ce qui n'est pas mesurable ici est dit non mesuré.
 */
export function buildFindings(pages: AuditPage[], opts: { sitemapFound: boolean; serviceUrls: string[] }): Finding[] {
  const ok = pages.filter((p) => p.status === 200);
  const n = ok.length;
  const out: Finding[] = [];
  const scope = `${n} ${plural(n, "page analysée", "pages analysées")}`;
  const add = (f: Finding) => out.push(f);

  const errors = pages.filter((p) => p.status === 404 || p.status === 410);
  if (errors.length) {
    const sources = ok.filter((p) => p.links.some((l) => errors.some((e) => key(e.url) === key(l.href))));
    add({
      id: "INTERNAL_LINK_TO_ERROR",
      finding: `${errors.length} ${plural(errors.length, "URL liée depuis le site répond", "URL liées depuis le site répondent")} en erreur 404 ou 410.`,
      urls: errors.map((e) => e.url),
      evidence: `Statut HTTP relevé : ${errors.map((e) => `${e.url} → ${e.status}`).join(" ; ")}. ${sources.length ? `Lien présent sur : ${sources.map((s) => s.url).slice(0, 5).join(", ")}.` : "URL issue du sitemap."}`,
      method: "Requête HTTP sur les URL trouvées dans le maillage et le sitemap",
      impact: "Un visiteur qui suit ce lien n'arrive nulle part.",
      recommended_action: "Corriger le lien ou rediriger l'URL vers la page qui la remplace.",
      priority: 1,
      confidence_status: "CONFIRMED",
    });
  }

  const noindex = ok.filter((p) => /noindex/.test(`${p.meta_robots ?? ""} ${p.x_robots ?? ""}`));
  const noindexServices = noindex.filter((p) => opts.serviceUrls.map(key).includes(key(p.url)));
  if (noindex.length) {
    add({
      id: "NOINDEX_DIRECTIVE",
      finding: `${noindex.length} des ${scope} ${plural(noindex.length, "porte", "portent")} une directive noindex${noindexServices.length ? `, dont ${noindexServices.length} ${plural(noindexServices.length, "page de prestation", "pages de prestation")}` : ""}.`,
      urls: noindex.map((p) => p.url),
      evidence: noindex.map((p) => `${p.url} : ${p.meta_robots ?? p.x_robots}`).join(" ; "),
      method: "Lecture de la balise meta robots et de l'en-tête X-Robots-Tag",
      impact: "La directive demande aux moteurs de ne pas indexer ces pages. Leur indexation réelle n'est pas connue sans la Search Console.",
      recommended_action: "Vérifier que la directive est voulue ; la retirer des pages de prestation qui doivent être trouvées.",
      priority: noindexServices.length ? 1 : 2,
      confidence_status: "CONFIRMED",
    });
  }

  const noTitle = ok.filter((p) => !p.title);
  if (noTitle.length) {
    add({
      id: "MISSING_TITLE",
      finding: `${noTitle.length} des ${scope} ${plural(noTitle.length, "n'a", "n'ont")} pas de balise title.`,
      urls: noTitle.map((p) => p.url),
      evidence: "Balise <title> absente ou vide dans le HTML reçu.",
      method: "Analyse du HTML",
      impact: "Le moteur choisit seul l'intitulé affiché dans ses résultats.",
      recommended_action: "Rédiger une balise title qui nomme la prestation et la ville.",
      priority: 1,
      confidence_status: "CONFIRMED",
    });
  }

  const byTitle = new Map<string, string[]>();
  for (const p of ok) if (p.title) byTitle.set(p.title, [...(byTitle.get(p.title) ?? []), p.url]);
  const dup = [...byTitle.entries()].filter(([, urls]) => urls.length > 1);
  if (dup.length) {
    add({
      id: "DUPLICATE_TITLE",
      finding: `${dup.reduce((a, [, u]) => a + u.length, 0)} des ${scope} partagent une balise title identique à celle d'une autre page.`,
      urls: dup.flatMap(([, u]) => u),
      evidence: dup.map(([t, u]) => `« ${t} » : ${u.join(", ")}`).join(" ; "),
      method: "Comparaison des balises title",
      impact: "Deux pages se présentent de la même façon. Cela ne suffit pas à conclure qu'elles se font de l'ombre dans les résultats.",
      recommended_action: "Donner à chaque page un title qui dit ce qu'elle a de propre.",
      priority: 2,
      confidence_status: "CONFIRMED",
    });
  }

  const noH1 = ok.filter((p) => p.h1s.length === 0);
  if (noH1.length) {
    add({
      id: "MISSING_H1",
      finding: `${noH1.length} des ${scope} ${plural(noH1.length, "n'a", "n'ont")} pas de H1.`,
      urls: noH1.map((p) => p.url),
      evidence: "Aucune balise <h1> dans le HTML reçu.",
      method: "Analyse du HTML (sans exécution de JavaScript : un H1 injecté par script n'est pas vu)",
      impact: "Le sujet de la page n'est pas annoncé dans sa structure.",
      recommended_action: "Ajouter un H1 qui nomme la prestation.",
      priority: 2,
      confidence_status: "CONFIRMED",
    });
  }

  const canon = ok.filter((p) => p.canonical && key(p.canonical) !== key(p.url));
  if (canon.length) {
    add({
      id: "CANONICAL_ELSEWHERE",
      finding: `${canon.length} des ${scope} ${plural(canon.length, "désigne", "désignent")} une autre URL comme canonique.`,
      urls: canon.map((p) => p.url),
      evidence: canon.map((p) => `${p.url} → ${p.canonical}`).join(" ; "),
      method: "Lecture de la balise link rel=canonical",
      impact: "Le site indique aux moteurs de retenir l'autre URL à la place de celle-ci.",
      recommended_action: "Vérifier que ce renvoi est voulu.",
      priority: 2,
      confidence_status: "CONFIRMED",
    });
  }

  if (!opts.sitemapFound) {
    add({
      id: "SITEMAP_NOT_RETRIEVED",
      finding: "Aucun sitemap n'a pu être récupéré.",
      urls: [],
      evidence: "Ni déclaration dans robots.txt lisible, ni /sitemap.xml exploitable.",
      method: "Lecture de robots.txt puis de /sitemap.xml",
      impact: "La présence des pages dans un sitemap n'a pas pu être contrôlée.",
      recommended_action: "Confirmer si un sitemap existe à une autre adresse.",
      priority: 3,
      confidence_status: "INSUFFICIENT_DATA",
    });
  } else {
    const missing = ok.filter((p) => p.in_sitemap === false);
    if (missing.length) {
      add({
        id: "NOT_IN_SITEMAP",
        finding: `${missing.length} des ${scope} ${plural(missing.length, "est absente", "sont absentes")} du sitemap récupéré.`,
        urls: missing.map((p) => p.url),
        evidence: "URL non listée dans le sitemap lu.",
        method: "Comparaison des URL analysées avec le sitemap récupéré",
        impact: "Ces pages ne sont pas signalées aux moteurs par ce sitemap. Elles peuvent l'être par un autre fichier non lu.",
        recommended_action: "Ajouter au sitemap les pages qui doivent être trouvées.",
        priority: 2,
        confidence_status: "CONFIRMED",
      });
    }
  }

  const legalTypes = ["LegalService", "Attorney", "LocalBusiness", "Organization", "ProfessionalService"];
  const withLd = ok.filter((p) => p.json_ld_types.some((t) => legalTypes.includes(t)));
  if (n && withLd.length === 0) {
    add({
      id: "NO_STRUCTURED_DATA",
      finding: `Aucune des ${scope} ne contient de données structurées décrivant le cabinet.`,
      urls: [],
      evidence: `Types JSON-LD recherchés : ${legalTypes.join(", ")}. Types trouvés : ${[...new Set(ok.flatMap((p) => p.json_ld_types))].join(", ") || "aucun"}.`,
      method: "Lecture des blocs JSON-LD du HTML reçu",
      impact: "Nom, adresse et activité du cabinet ne sont pas décrits dans un format lisible par les moteurs sur ces pages.",
      recommended_action: "Ajouter un balisage LegalService sur la page d'accueil et la page de contact.",
      priority: 3,
      confidence_status: "CONFIRMED",
    });
  }

  const contact = ok.find((p) => /contact|rendez-vous|rdv/.test(p.url));
  const services = ok.filter((p) => opts.serviceUrls.map(key).includes(key(p.url)));
  if (contact && services.length) {
    const without = services.filter((p) => !p.links.some((l) => key(l.href) === key(contact.url)));
    if (without.length) {
      add({
        id: "SERVICE_WITHOUT_CONTACT_LINK",
        finding: `${without.length} des ${services.length} pages de prestation analysées n'ont pas de lien vers la page de contact.`,
        urls: without.map((p) => p.url),
        evidence: `Aucun lien vers ${contact.url} dans le HTML reçu.`,
        method: "Analyse des liens internes",
        impact: "Le lecteur d'une prestation n'a pas de chemin direct vers la prise de contact.",
        recommended_action: "Placer un lien vers le contact ou la prise de rendez-vous sur chaque page de prestation.",
        priority: 2,
        confidence_status: "CONFIRMED",
      });
    }
  }

  if (!pages.some((p) => /honoraires|tarifs/.test(p.url))) {
    add({
      id: "FEES_PAGE_NOT_FOUND",
      finding: "Aucune page sur les honoraires parmi les URL explorées.",
      urls: [],
      evidence: `Aucune URL contenant « honoraires » ou « tarifs » parmi les ${pages.length} URL tentées.`,
      method: "Examen des URL du maillage et du sitemap",
      impact: "La page peut exister sous un autre nom ou hors des pages explorées.",
      recommended_action: "Confirmer si les honoraires sont présentés quelque part sur le site.",
      priority: 3,
      confidence_status: "HYPOTHESIS",
    });
  }

  add({
    id: "PERFORMANCE_NOT_MEASURED",
    finding: "Performance de chargement : non mesurée.",
    urls: [],
    evidence: "Aucun outil de mesure n'a été exécuté.",
    method: "Aucune",
    impact: "Rien ne peut être dit sur la vitesse du site.",
    recommended_action: "Mesurer avec un outil dédié si le sujet se pose.",
    priority: 3,
    confidence_status: "INSUFFICIENT_DATA",
  });
  return out;
}

export interface AuditReport {
  generated_at: string;
  rule_version: string;
  simulation: boolean;
  firm_name: string | null;
  summary: string[];
  scope: { pages_analyzed: number; urls: { url: string; status: number | null }[]; robots: string; sitemap_urls: number };
  visibility: string;
  priorities: Finding[];
  findings: Finding[];
  keywords: { keyword: string; cluster: string; search_intent: string; existing_page_url: string | null; recommendation_status: string; offer_proximity_score: number; business_intent_score: number }[];
  keyword_note: string;
  limits: string[];
}

export const AUDIT_LIMITS = [
  "Analyse limitée aux pages listées : un constat vaut pour ces pages, pas pour le site entier.",
  "Aucun accès à la Search Console : indexation, trafic, impressions et positions ne sont pas connus.",
  "HTML lu sans exécuter JavaScript : un contenu injecté par script n'est pas vu.",
  "Une URL absente de l'exploration peut exister ; une page sans lien dans l'échantillon peut être liée ailleurs.",
  "Les notes des requêtes sont une grille interne de proximité avec l'offre et d'intention ; ce ne sont pas des mesures Google. Aucun volume, CPC ni position n'a été obtenu.",
];

const esc = (s: string) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");

export function renderMarkdown(r: AuditReport): string {
  const f = (x: Finding) => `### ${x.finding}\n\n- Statut : ${x.confidence_status}\n- Preuve : ${x.evidence}\n- Méthode : ${x.method}\n- Conséquence possible : ${x.impact}\n- Action proposée : ${x.recommended_action}\n${x.urls.length ? `- URL : ${x.urls.join(", ")}\n` : ""}`;
  return [
    `# Pré-audit${r.firm_name ? ` : ${r.firm_name}` : ""}`,
    r.simulation ? "> SIMULATION : site et résultats fictifs." : "",
    "## Synthèse",
    r.summary.map((s) => `- ${s}`).join("\n"),
    "## Périmètre exploré",
    `${r.scope.pages_analyzed} pages analysées. robots.txt : ${r.scope.robots}. Sitemap : ${r.scope.sitemap_urls} URL lues.`,
    r.scope.urls.map((u) => `- ${u.url} (${u.status ?? "sans réponse"})`).join("\n"),
    "## Réponses des assistants IA",
    r.visibility,
    "## Priorités",
    r.priorities.map(f).join("\n") || "Aucun constat confirmé.",
    "## Autres constats",
    r.findings.filter((x) => !r.priorities.includes(x)).map(f).join("\n") || "Aucun.",
    "## Requêtes",
    r.keyword_note,
    r.keywords.length ? `| Requête | Groupe | Intention | Page | Recommandation | Proximité offre | Intention business |\n|---|---|---|---|---|---|---|\n${r.keywords.map((k) => `| ${k.keyword} | ${k.cluster} | ${k.search_intent} | ${k.existing_page_url ?? ""} | ${k.recommendation_status} | ${k.offer_proximity_score}/5 | ${k.business_intent_score}/5 |`).join("\n")}` : "",
    "## Limites",
    r.limits.map((l) => `- ${l}`).join("\n"),
  ]
    .filter(Boolean)
    .join("\n\n");
}

export function renderHtml(r: AuditReport): string {
  const f = (x: Finding) =>
    `<article><h3>${esc(x.finding)}</h3><p><strong>Statut :</strong> ${x.confidence_status}</p><p><strong>Preuve :</strong> ${esc(x.evidence)}</p><p><strong>Méthode :</strong> ${esc(x.method)}</p><p><strong>Conséquence possible :</strong> ${esc(x.impact)}</p><p><strong>Action proposée :</strong> ${esc(x.recommended_action)}</p></article>`;
  return `<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="robots" content="noindex"><title>Pré-audit</title></head><body>
<h1>Pré-audit${r.firm_name ? ` : ${esc(r.firm_name)}` : ""}</h1>${r.simulation ? "<p><strong>SIMULATION : site et résultats fictifs.</strong></p>" : ""}
<h2>Synthèse</h2><ul>${r.summary.map((s) => `<li>${esc(s)}</li>`).join("")}</ul>
<h2>Périmètre exploré</h2><p>${r.scope.pages_analyzed} pages analysées. robots.txt : ${esc(r.scope.robots)}. Sitemap : ${r.scope.sitemap_urls} URL lues.</p><ul>${r.scope.urls.map((u) => `<li>${esc(u.url)} (${u.status ?? "sans réponse"})</li>`).join("")}</ul>
<h2>Réponses des assistants IA</h2><p>${esc(r.visibility)}</p>
<h2>Priorités</h2>${r.priorities.map(f).join("") || "<p>Aucun constat confirmé.</p>"}
<h2>Autres constats</h2>${r.findings.filter((x) => !r.priorities.includes(x)).map(f).join("")}
<h2>Requêtes</h2><p>${esc(r.keyword_note)}</p>${r.keywords.length ? `<table><thead><tr><th>Requête</th><th>Groupe</th><th>Intention</th><th>Recommandation</th><th>Proximité offre</th><th>Intention business</th></tr></thead><tbody>${r.keywords.map((k) => `<tr><td>${esc(k.keyword)}</td><td>${esc(k.cluster)}</td><td>${esc(k.search_intent)}</td><td>${esc(k.recommendation_status)}</td><td>${k.offer_proximity_score}/5</td><td>${k.business_intent_score}/5</td></tr>`).join("")}</tbody></table>` : ""}
<h2>Limites</h2><ul>${r.limits.map((l) => `<li>${esc(l)}</li>`).join("")}</ul>
</body></html>`;
}
