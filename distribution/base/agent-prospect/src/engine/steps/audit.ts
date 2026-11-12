import { randomBytes } from "node:crypto";
import { asc, eq } from "drizzle-orm";
import { schema } from "../../db/client";
import { AUDIT_LIMITS, AUDIT_RULE_VERSION, buildFindings, renderHtml, renderMarkdown, type AuditReport, type Finding } from "../../core/audit";
import { frDate } from "../../core/text";
import type { Campaign, Deps, Firm, Prospect, Runtime } from "../deps";
import { ensureSitePages } from "../site";
import { setState } from "../transitions";

const SHARE_DAYS = 30;

interface VisibilitySummary {
  verdict: string;
  reason: string;
  validRuns: number;
  mode_label: string;
  model: string;
  window_end: string;
}

export function visibilityStatement(s: VisibilitySummary | null): string {
  if (!s) return "Aucun test de présence dans les réponses IA n'a été réalisé.";
  const tail = `Mode : ${s.mode_label}, modèle ${s.model}.`;
  if (s.verdict === "NOT_OBSERVED_IN_SAMPLE") {
    return `Le cabinet n'a pas été observé dans les ${s.validRuns} réponses de l'échantillon généré le ${frDate(new Date(s.window_end))}. ${tail} Le constat vaut pour cet échantillon et ces formulations ; ce n'est pas une observation de l'interface ChatGPT.`;
  }
  return `Résultat de l'échantillon du ${frDate(new Date(s.window_end))} : ${s.reason}. ${tail} Aucune conclusion d'absence n'est tirée.`;
}

/** Recalcule le rapport depuis la base (pages lues, constats, requêtes retenues) et l'enregistre en JSON, Markdown et HTML. */
export async function saveReport(deps: Deps, campaign: Campaign, prospect: Prospect, firm: Firm): Promise<void> {
  // L'audit porte sur les pages lues dans la limite de la campagne, dans l'ordre où elles ont été lues (accueil, puis pages les plus utiles).
  const pages = (await deps.db.select().from(schema.site_pages).where(eq(schema.site_pages.firm_id, firm.id)).orderBy(asc(schema.site_pages.fetched_at), asc(schema.site_pages.url))).slice(0, campaign.config.max_crawl_pages_per_site);
  const services = (await deps.db.select().from(schema.evidence).where(eq(schema.evidence.prospect_id, prospect.id))).filter((e) => e.kind === "SERVICE");
  const kws = await deps.db.select().from(schema.keywords).where(eq(schema.keywords.prospect_id, prospect.id)).orderBy(asc(schema.keywords.cluster), asc(schema.keywords.keyword));
  const findings = buildFindings(pages, { sitemapFound: firm.sitemap_urls.length > 0, serviceUrls: services.map((s) => s.source_url) });
  const confirmed = findings.filter((f) => f.confidence_status === "CONFIRMED");
  const priorities: Finding[] = [...confirmed].sort((a, b) => a.priority - b.priority).slice(0, 3);
  const analyzed = pages.filter((p) => p.status === 200).length;
  const [fresh] = await deps.db.select().from(schema.prospects).where(eq(schema.prospects.id, prospect.id));
  const visibility = visibilityStatement(fresh.visibility_summary as VisibilitySummary | null);
  const keywordNote = !campaign.config.generate_keywords
    ? "Requêtes non demandées pour cette campagne."
    : fresh.keyword_status === null
      ? "Requêtes en cours de préparation."
      : fresh.keyword_status === "COMPLETE"
        ? `${kws.length} requêtes retenues, rattachées aux prestations vérifiées sur le site.`
        : `${kws.length} ${kws.length > 1 ? "requêtes retenues" : "requête retenue"} seulement : les prestations vérifiées sur le site ne permettent pas d'en proposer vingt solides. La liste n'est pas complétée artificiellement.`;
  const report: AuditReport = {
    generated_at: deps.now().toISOString(),
    rule_version: AUDIT_RULE_VERSION,
    simulation: campaign.simulation,
    firm_name: firm.name,
    summary: [
      `${analyzed} pages analysées le ${frDate(deps.now())}, sur ${pages.length} URL tentées.`,
      visibility.split(". ")[0] + ".",
      `${confirmed.length} constats confirmés, ${findings.filter((f) => f.confidence_status === "HYPOTHESIS").length} hypothèses, ${findings.filter((f) => f.confidence_status === "INSUFFICIENT_DATA").length} contrôles sans donnée suffisante.`,
      priorities[0] ? `Premier point : ${priorities[0].finding}` : "Aucun constat confirmé sur les pages lues.",
      keywordNote,
    ],
    scope: { pages_analyzed: analyzed, urls: pages.map((p) => ({ url: p.url, status: p.status })), robots: firm.robots_status === "FOUND" ? "lu" : "absent ou illisible", sitemap_urls: firm.sitemap_urls.length },
    visibility,
    priorities,
    findings,
    keywords: kws.map((k) => ({ keyword: k.keyword, cluster: k.cluster, search_intent: k.search_intent, existing_page_url: k.existing_page_url, recommendation_status: k.recommendation_status, offer_proximity_score: k.offer_proximity_score, business_intent_score: k.business_intent_score })),
    keyword_note: keywordNote,
    limits: AUDIT_LIMITS,
  };
  const values = { pages_analyzed: analyzed, findings, report, report_md: renderMarkdown(report), report_html: renderHtml(report) };
  await deps.db
    .insert(schema.audits)
    .values({ prospect_id: prospect.id, ...values, share_token: randomBytes(24).toString("base64url"), share_expires_at: new Date(deps.now().getTime() + SHARE_DAYS * 86_400_000) })
    .onConflictDoUpdate({ target: schema.audits.prospect_id, set: values });
}

export async function auditStep(deps: Deps, rt: Runtime, campaign: Campaign, prospect: Prospect, firmIn: Firm): Promise<void> {
  const max = campaign.config.max_crawl_pages_per_site;
  const { firm } = await ensureSitePages(deps, rt.fetcher, firmIn, max, max);
  await saveReport(deps, campaign, prospect, firm);
  await setState(deps, prospect, "AUDIT_DONE");
}
