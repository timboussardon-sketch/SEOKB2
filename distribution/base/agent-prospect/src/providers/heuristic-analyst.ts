import type { DraftSentence } from "../core/claims";
import type { KeywordCandidate } from "../core/keywords";
import { identity } from "../core/identity";
import { normalize } from "../core/text";
import type { Analyst, CallEstimate, DraftRequest, KeywordRequest, ProfileRequest, Quote, SiteProfile, Usage } from "./types";

const ZERO: Usage = { model: "simulation", input_tokens: 0, output_tokens: 0, web_search_calls: 0, reported: null };
const sentencesOf = (text: string) => text.split(/(?<=[.!?])\s+/).map((s) => s.trim()).filter((s) => s.length > 8 && s.length < 400);

/**
 * Analyste par règles, sans appel externe. Il sert au mode simulation et aux tests.
 * Ses lectures restent des propositions : le moteur revérifie chaque extrait dans la page source.
 */
export class HeuristicAnalyst implements Analyst {
  name = "heuristic";
  model = "simulation";
  promptVersion = "heuristic-v1";

  estimate(): CallEstimate {
    return { model: this.model, input_tokens: 0, output_tokens: 0, web_search_calls: 0 };
  }

  async extractProfile(req: ProfileRequest): Promise<{ profile: SiteProfile; usage: Usage }> {
    const profile: SiteProfile = { firm_name: null, lawyers: [], cities: [], practice_areas: [], client_types: [], services: [], certification_claims: [] };
    const targets = [req.practice, ...req.subspecialties].map(normalize);
    const seen = new Set<string>();
    const once = (key: string) => (seen.has(key) ? false : (seen.add(key), true));

    for (const page of req.pages) {
      const path = new URL(page.url).pathname;
      if (path === "/" && page.h1s[0] && !profile.firm_name) profile.firm_name = { value: page.h1s[0], source_url: page.url, excerpt: page.h1s[0] };
      if (/expertise|competence|domaine|prestation/.test(path) && path.split("/").filter(Boolean).length >= 2 && page.h1s[0] && once(`s:${normalize(page.h1s[0])}`)) {
        profile.services.push({ value: page.h1s[0], source_url: page.url, excerpt: page.h1s[0] });
      }
      for (const s of sentencesOf(page.text)) {
        const n = normalize(s);
        for (const m of s.matchAll(/Ma[îi]tre\s+([A-ZÉÈ][\p{L}-]+)\s+([A-ZÉÈ][\p{L}\d-]+)/gu)) {
          if (once(`l:${normalize(m[1])} ${normalize(m[2])}`)) profile.lawyers.push({ first_name: m[1], last_name: m[2], source_url: page.url, excerpt: s });
        }
        for (const m of s.matchAll(/(?:barreau de|situé à|installé à|cabinet à|avocats? à)\s+([A-ZÉÈ][\p{L}-]+(?:[ -][A-ZÉÈ][\p{L}-]+)*)/gu)) {
          if (once(`c:${normalize(m[1])}`)) profile.cities.push({ value: m[1], source_url: page.url, excerpt: s });
        }
        const target = targets.find((t) => n.includes(t));
        if (target && once(`p:${target}`)) profile.practice_areas.push({ value: target, source_url: page.url, excerpt: s, matches_target: true });
        if (!target) {
          const other = s.match(/droit (?:du |de la |des |de l['’]|d['’])[\p{L}' -]{3,40}/u);
          if (other && once(`p:${normalize(other[0])}`)) profile.practice_areas.push({ value: other[0].trim(), source_url: page.url, excerpt: s, matches_target: false });
        }
        if (/(accompagn|defen|conseill|assist)\w*\s+(?:les |des )?(employeurs|entreprises|dirigeants)/.test(n) && once("t:entreprise")) {
          profile.client_types.push({ value: "entreprise", source_url: page.url, excerpt: s });
        }
        if (/(accompagn|defen|conseill|assist)\w*\s+(?:les |des )?(salaries|particuliers)/.test(n) && once("t:particulier")) {
          profile.client_types.push({ value: "particulier", source_url: page.url, excerpt: s });
        }
        if (/specialiste en|certificat de specialisation|mention de specialisation/.test(n) && once(`x:${n.slice(0, 60)}`)) {
          profile.certification_claims.push({ value: s, source_url: page.url, excerpt: s } satisfies Quote);
        }
      }
    }
    return { profile, usage: ZERO };
  }

  async proposeKeywords(req: KeywordRequest): Promise<{ candidates: KeywordCandidate[]; usage: Usage }> {
    const client = req.clientTypes.length === 1 ? req.clientTypes[0] : "mixte";
    const who = client === "entreprise" ? "employeur" : client === "particulier" ? "particulier" : "";
    const patterns: [(s: string) => string, string, string][] =
      req.round === 1
        ? [
            [(s) => `avocat ${s} ${req.city}`, "choix d'un cabinet", "page de prestation"],
            [(s) => `cabinet d'avocats ${s} ${who} ${req.city}`, "choix d'un cabinet", "page de prestation"],
            [(s) => `consultation avocat ${s} ${who}`, "consultation", "page de prestation"],
            [(s) => `honoraires avocat ${s}`, "honoraires", "page honoraires"],
            [(s) => `${s} définition`, "information", "article"],
            [(s) => `avocat ${s} salarié ${req.city}`, "choix d'un cabinet", "page de prestation"],
          ]
        : [
            [(s) => `accompagnement ${who} ${s} ${req.city}`, "accompagnement", "page de prestation"],
            [(s) => `devis avocat ${s} ${req.city}`, "honoraires", "page honoraires"],
          ];
    const candidates: KeywordCandidate[] = [];
    for (const service of req.services) {
      const label = service.label.toLowerCase();
      for (const [build, intent, pageType] of patterns) {
        candidates.push({
          keyword: build(label).replace(/\s+/g, " ").trim(),
          cluster: service.label,
          service_evidence_id: service.evidenceId,
          client_type: client,
          search_intent: intent,
          business_rationale: `Recherche d'un prestataire pour « ${service.label} », prestation présentée sur ${service.url}.`,
          existing_page_url: service.url,
          recommended_page_type: pageType,
          recommendation: "POUSSER",
        });
      }
    }
    return { candidates: candidates.slice(0, Math.max(req.count, 0) || candidates.length), usage: ZERO };
  }

  async draftEmail(req: DraftRequest): Promise<{ subject: string; sentences: DraftSentence[]; usage: Usage }> {
    const service = req.facts.find((f) => f.id.startsWith("service:"));
    const out: DraftSentence[] = [];
    const push = (kind: DraftSentence["kind"], text: string, evidence_ids: string[] = []) => out.push({ id: `s${out.length + 1}`, kind, text, evidence_ids });

    push("GREETING", req.lawyerLastName ? `Bonjour Maître ${req.lawyerLastName},` : "Bonjour,");
    if (service) {
      push("OBSERVATION", `En consultant le site ${req.firmName ? `de ${req.firmName}` : "de votre cabinet"}, j’ai relevé votre page « ${service.values[0]} ».`, [service.id]);
    }
    if (req.keywords.length >= 2) {
      push("KEYWORDS", `J’ai aussi listé ${req.keywordCount} recherches proches de vos prestations, par exemple « ${req.keywords[0]} » et « ${req.keywords[1]} ».`);
    }
    if (req.auditPages && req.auditFactId) {
      push("OBSERVATION", `Le pré-audit porte sur ${req.auditPages} pages de votre site.`, [req.auditFactId]);
    }
    if (req.auditUrl) push("AUDIT_LINK", `Il est consultable ici : ${req.auditUrl}`);
    push("CTA", "Souhaitez-vous que je vous présente ces points lors d’un échange de vingt minutes ?");
    push(
      "TRANSPARENCY",
      `${req.contactSourceUrl ? `J’ai trouvé votre adresse sur ${req.contactSourceUrl}. ` : ""}Si vous ne souhaitez plus recevoir de message de ma part, répondez « stop » et je supprime vos coordonnées.`,
    );
    push("SIGNATURE", [identity().name, identity().url].filter(Boolean).join("\n"));
    return { subject: "Pré-audit de votre site et réponses des assistants IA", sentences: out, usage: ZERO };
  }

  async rewriteSentences(_req: DraftRequest, failed: Parameters<Analyst["rewriteSentences"]>[1]) {
    // Sans modèle de langage, la seule correction sûre est de retirer l'affirmation refusée.
    return { rewrites: failed.map((f) => ({ id: f.sentence.id, text: null, evidence_ids: [] })), usage: ZERO };
  }
}
