import { and, eq } from "drizzle-orm";
import { schema } from "../../db/client";
import { withRetry } from "../../core/errors";
import { filterKeywords, KEYWORD_SCORING_VERSION, pickTopKeywords, underCoveredServices, type ScoredKeyword, type ServiceRef } from "../../core/keywords";
import { metered } from "../budget";
import type { Campaign, Deps, Firm, Prospect, Runtime } from "../deps";
import { logEvent } from "../events";
import { setState } from "../transitions";
import { assessRun, matchEntity } from "../../core/verdict";
import { classify, POLICIES } from "../../core/errors";
import { saveReport } from "./audit";
import { entityFor } from "./visibility";

const LIMIT = 20;

async function kept(deps: Deps, prospectId: string): Promise<ScoredKeyword[]> {
  const rows = await deps.db.select().from(schema.keywords).where(eq(schema.keywords.prospect_id, prospectId));
  return rows.map((r) => ({ normalized: r.normalized, service_evidence_id: r.service_evidence_id, keyword: r.keyword }) as ScoredKeyword);
}

/**
 * Boucle mots-clés : partir des prestations vérifiées, faire proposer 30 à 40 candidats, filtrer par le code
 * (offre, intention, clientèle, doublons), garder 20 au plus. S'il en manque, un second tour vise les prestations
 * peu couvertes. Deux tours au plus ; ce qui manque reste manquant.
 */
export async function keywordsStep(deps: Deps, rt: Runtime, campaign: Campaign, prospect: Prospect, firm: Firm): Promise<void> {
  const cfg = campaign.config;
  const ev = await deps.db.select().from(schema.evidence).where(eq(schema.evidence.prospect_id, prospect.id));
  const services: ServiceRef[] = ev.filter((e) => e.kind === "SERVICE").map((e) => ({ evidenceId: e.id, label: e.value, url: e.source_url }));
  const clientTypes = [...new Set(ev.filter((e) => e.kind === "CLIENT_TYPE").map((e) => e.value as "entreprise" | "particulier"))];
  const E = schema.event_log;
  const done = new Set(
    (await deps.db.select({ data: E.data }).from(E).where(and(eq(E.prospect_id, prospect.id), eq(E.type, "KEYWORD_ROUND_DONE")))).map((r) => (r.data as { round: number }).round),
  );

  if (services.length) {
    for (let round = 1; round <= cfg.max_keyword_rounds; round++) {
      const already = await kept(deps, prospect.id);
      if (already.length >= LIMIT) break;
      if (done.has(round)) continue;
      const scope = round === 1 ? services : underCoveredServices(services, already);
      if (!scope.length) break;
      const { candidates } = await withRetry(
        () =>
          metered(deps, { campaignId: campaign.id, prospectId: prospect.id, step: "keywords" }, rt.providers.analyst.estimate("keywords"), () =>
            rt.providers.analyst.proposeKeywords({ services: scope, city: cfg.location, clientTypes, count: round === 1 ? 40 : 20, round, alreadyKept: already.map((k) => k.keyword) }),
          ),
        { sleep: deps.sleep, random: deps.random },
      );
      const result = filterKeywords({ candidates, services, city: cfg.location, clientTypes, alreadyKept: already, limit: LIMIT });
      await deps.db.transaction(async (tx) => {
        for (const k of result.kept) {
          await tx
            .insert(schema.keywords)
            .values({
              prospect_id: prospect.id,
              round,
              normalized: k.normalized,
              keyword: k.keyword,
              cluster: k.cluster,
              search_intent: k.search_intent,
              client_type: k.client_type,
              relevant_service: k.relevant_service,
              service_evidence_id: k.service_evidence_id,
              geography: k.geography,
              existing_page_url: k.existing_page_url,
              recommended_page_type: k.recommended_page_type,
              business_rationale: k.business_rationale,
              recommendation_status: k.recommendation,
              offer_proximity_score: k.offer_proximity_score,
              business_intent_score: k.business_intent_score,
              scoring_version: KEYWORD_SCORING_VERSION,
            })
            .onConflictDoNothing();
        }
        const reasons: Record<string, number> = {};
        for (const r of result.rejected) reasons[r.reason] = (reasons[r.reason] ?? 0) + 1;
        await logEvent(tx, { campaignId: campaign.id, prospectId: prospect.id, type: "KEYWORD_ROUND_DONE", data: { round, proposed: candidates.length, kept: result.kept.length, rejected: reasons } });
      });
    }
  }

  await checkTopKeywords(deps, rt, campaign, prospect, firm);
  const count = (await kept(deps, prospect.id)).length;
  const updated = await setState(deps, prospect, "KEYWORDS_DONE", { keyword_count: count, keyword_status: count >= LIMIT ? "COMPLETE" : "INSUFFICIENT_EVIDENCE" });
  await saveReport(deps, campaign, updated, firm);
}

export async function topKeywords(deps: Deps, campaign: Campaign, prospectId: string) {
  const rows = await deps.db.select().from(schema.keywords).where(eq(schema.keywords.prospect_id, prospectId));
  const ev = await deps.db.select().from(schema.evidence).where(eq(schema.evidence.prospect_id, prospectId));
  const practices = [campaign.config.practice_area, ...campaign.config.subspecialties, ...ev.filter((e) => e.kind === "PRACTICE_AREA").map((e) => e.value)];
  return pickTopKeywords(rows, practices, campaign.config.client_type);
}

/**
 * Pour chacune des deux requêtes mises en avant : la requête est posée telle quelle à l'IA (conversation neuve, sans nom de cabinet),
 * puis le code cherche le site et le nom du cabinet dans la réponse. Une réponse invalide, une erreur ou une correspondance ambiguë
 * donne « non vérifié » : rien n'est affirmé dans ce cas. Une vérification déjà faite n'est pas repayée.
 */
export async function checkTopKeywords(deps: Deps, rt: Runtime, campaign: Campaign, prospect: Prospect, firm: Firm): Promise<void> {
  const K = schema.keyword_checks;
  const v = rt.providers.visibility;
  const top = await topKeywords(deps, campaign, prospect.id);
  if (!top.length) return;
  const done = new Set((await deps.db.select().from(K).where(and(eq(K.prospect_id, prospect.id), eq(K.provider, v.name)))).map((r) => r.keyword));
  const entity = await entityFor(deps, prospect, firm);
  for (const k of top) {
    if (done.has(k.keyword)) continue;
    let row: { response_text: string | null; citations: { url: string; title?: string }[]; result: string; detail: string };
    try {
      const answer = await metered(deps, { campaignId: campaign.id, prospectId: prospect.id, step: "keyword_check" }, v.estimate(), () => v.ask(k.keyword, campaign.config.location));
      const validity = assessRun({ text: answer.text, webSearchUsed: answer.webSearchUsed, requireWebSearch: v.requireWebSearch });
      const obs = matchEntity(entity, answer.text, answer.citations);
      const cited = obs.filter((o) => ["OWN_DOMAIN_CITATION", "FIRM_MENTION", "LAWYER_MENTION"].includes(o.type));
      const unsure = obs.filter((o) => ["AMBIGUOUS_MATCH", "THIRD_PARTY_CITATION"].includes(o.type));
      row = {
        response_text: answer.text,
        citations: answer.citations,
        result: validity.validity !== "VALID" ? "UNVERIFIED" : cited.length ? "CITED" : unsure.length ? "UNVERIFIED" : "NOT_CITED",
        detail: validity.validity !== "VALID" ? validity.note : [...cited, ...unsure].map((o) => `${o.type} : ${o.detail}`).join(" | "),
      };
    } catch (err) {
      const c = classify(err);
      // Budget, clé ou tarif : l'étape s'arrête. Autre erreur : la requête reste « non vérifiée », sans rien affirmer.
      if (["BUDGET_BLOCK", "STOP_INTEGRATION"].includes(POLICIES[c.category].recovery)) throw err;
      row = { response_text: null, citations: [], result: "UNVERIFIED", detail: `${c.category} : ${c.message}`.slice(0, 300) };
    }
    await deps.db.insert(K).values({ prospect_id: prospect.id, keyword: k.keyword, provider: v.name, model: v.model, ...row, checked_at: deps.now() }).onConflictDoNothing();
  }
}
