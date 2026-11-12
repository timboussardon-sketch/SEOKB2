import OpenAI from "openai";
import { z } from "zod";
import type { DraftSentence } from "../core/claims";
import { AppError } from "../core/errors";
import type { KeywordCandidate } from "../core/keywords";
import { DRAFT_SYSTEM, KEYWORDS_SYSTEM, PROFILE_SYSTEM, PROMPT_VERSION, REWRITE_SYSTEM, SEARCH_SYSTEM } from "../prompts";
import { KINDS, KeywordZ, ProfileZ, SentenceZ } from "./schemas";
import type { Analyst, CallEstimate, DraftRequest, KeywordRequest, ProfileRequest, Providers, SearchCandidate, SearchProvider, SiteProfile, Usage, VisibilityAnswer, VisibilityProvider } from "./types";

/**
 * Intégration OpenAI (API Responses). Non exercée par les tests de ce dépôt : elle exige une clé et des appels facturés.
 * Les identifiants de modèles viennent de la configuration ; aucun n'est supposé.
 */
type Res = OpenAI.Responses.Response;

function usageOf(model: string, res: Res): Usage {
  return {
    model,
    input_tokens: res.usage?.input_tokens ?? 0,
    output_tokens: res.usage?.output_tokens ?? 0,
    web_search_calls: res.output.filter((o) => o.type === "web_search_call").length,
    reported: res.usage ?? null,
  };
}

function citationsOf(res: Res): { url: string; title?: string }[] {
  const out: { url: string; title?: string }[] = [];
  for (const item of res.output) {
    if (item.type !== "message") continue;
    for (const part of item.content) {
      if (part.type !== "output_text") continue;
      for (const a of part.annotations) if (a.type === "url_citation") out.push({ url: a.url, title: a.title });
    }
  }
  return out;
}

const quote = { type: "object", additionalProperties: false, required: ["value", "source_url", "excerpt"], properties: { value: { type: "string" }, source_url: { type: "string" }, excerpt: { type: "string" } } } as const;
const arr = (items: unknown) => ({ type: "array", items });
const obj = (properties: Record<string, unknown>) => ({ type: "object", additionalProperties: false, required: Object.keys(properties), properties });

export interface OpenAIConfig {
  apiKey: string;
  searchModel: string;
  visibilityModel: string;
  analystModel: string;
}

class Base {
  protected client: OpenAI;
  constructor(protected cfg: OpenAIConfig) {
    // maxRetries: 0 — les relances sont décidées par le moteur, bornées et journalisées.
    this.client = new OpenAI({ apiKey: cfg.apiKey, maxRetries: 0, timeout: 120_000 });
  }

  protected async json<T>(model: string, system: string, user: unknown, name: string, schema: unknown, parser: z.ZodType<T>, webSearch = false): Promise<{ data: T; usage: Usage }> {
    const res = await this.client.responses.create({
      model,
      instructions: system,
      input: JSON.stringify(user),
      ...(webSearch ? { tools: [{ type: "web_search" as const, user_location: { type: "approximate" as const, country: "FR" } }] } : {}),
      text: { format: { type: "json_schema", name, strict: true, schema: schema as Record<string, unknown> } },
    });
    let parsed: unknown;
    try {
      parsed = JSON.parse(res.output_text);
    } catch {
      throw new AppError("INVALID_OUTPUT", `Sortie ${name} illisible`);
    }
    const checked = parser.safeParse(parsed);
    if (!checked.success) throw new AppError("INVALID_OUTPUT", `Sortie ${name} hors schéma`);
    return { data: checked.data, usage: usageOf(model, res) };
  }
}

export class OpenAISearch extends Base implements SearchProvider {
  name = "OPENAI_WEB_SEARCH";
  get model() {
    return this.cfg.searchModel;
  }
  estimate(): CallEstimate {
    return { model: this.model, input_tokens: 20_000, output_tokens: 3_000, web_search_calls: 5 };
  }
  async search(query: string, limit: number, excludeDomains: string[]): Promise<{ candidates: SearchCandidate[]; usage: Usage }> {
    const item = obj({ name: { type: ["string", "null"] }, website: { type: "string" }, source_url: { type: "string" }, snippet: { type: "string" } });
    const parser = z.object({ candidates: z.array(z.object({ name: z.string().nullable(), website: z.string(), source_url: z.string(), snippet: z.string() })) });
    const { data, usage } = await this.json(this.model, SEARCH_SYSTEM, { query, max_results: limit, already_known_domains: excludeDomains.slice(0, 80) }, "candidates", obj({ candidates: arr(item) }), parser, true);
    return { candidates: data.candidates.slice(0, limit), usage };
  }
}

export class OpenAIVisibility extends Base implements VisibilityProvider {
  name = "OPENAI_API_WEB_SEARCH" as const;
  requireWebSearch = true;
  get model() {
    return this.cfg.visibilityModel;
  }
  get params() {
    return { tool: "web_search", country: "FR", tool_choice: "auto", store: false };
  }
  estimate(): CallEstimate {
    return { model: this.model, input_tokens: 15_000, output_tokens: 2_000, web_search_calls: 3 };
  }
  async ask(prompt: string, city: string): Promise<VisibilityAnswer> {
    // Requête seule : pas d'instructions, pas d'historique, pas de liste de cabinets.
    const res = await this.client.responses.create({
      model: this.model,
      input: prompt,
      store: false,
      tools: [{ type: "web_search", user_location: { type: "approximate", country: "FR", city } }],
    });
    const usage = usageOf(this.model, res);
    return { text: res.output_text, citations: citationsOf(res), webSearchUsed: usage.web_search_calls > 0, responseId: res.id, usage };
  }
}

export class OpenAIAnalyst extends Base implements Analyst {
  name = "OPENAI";
  promptVersion = PROMPT_VERSION;
  get model() {
    return this.cfg.analystModel;
  }
  estimate(kind: "profile" | "keywords" | "draft" | "rewrite"): CallEstimate {
    const table = { profile: [30_000, 3_000], keywords: [4_000, 5_000], draft: [4_000, 1_200], rewrite: [3_000, 600] } as const;
    return { model: this.model, input_tokens: table[kind][0], output_tokens: table[kind][1], web_search_calls: 0 };
  }

  async extractProfile(req: ProfileRequest): Promise<{ profile: SiteProfile; usage: Usage }> {
    const lawyer = obj({ first_name: { type: "string" }, last_name: { type: "string" }, source_url: { type: "string" }, excerpt: { type: "string" } });
    const schema = obj({
      firm_name: { anyOf: [quote, { type: "null" }] },
      lawyers: arr(lawyer),
      cities: arr(quote),
      practice_areas: arr(obj({ ...quote.properties, matches_target: { type: "boolean" } })),
      client_types: arr(obj({ ...quote.properties, value: { type: "string", enum: ["entreprise", "particulier"] } })),
      services: arr(quote),
      certification_claims: arr(quote),
    });
    const user = {
      target_practice: req.practice,
      target_subspecialties: req.subspecialties,
      target_city: req.city,
      pages: req.pages.map((p) => `<source url="${p.url}">\n${p.title ?? ""}\n${p.h1s.join(" | ")}\n${p.text.slice(0, 6000)}\n</source>`),
    };
    const { data, usage } = await this.json(this.model, PROFILE_SYSTEM, user, "profile", schema, ProfileZ);
    return { profile: data, usage };
  }

  async proposeKeywords(req: KeywordRequest): Promise<{ candidates: KeywordCandidate[]; usage: Usage }> {
    const item = obj({
      keyword: { type: "string" },
      cluster: { type: "string" },
      service_evidence_id: { type: "string" },
      client_type: { type: "string", enum: ["entreprise", "particulier", "mixte"] },
      search_intent: { type: "string" },
      business_rationale: { type: "string" },
      existing_page_url: { type: ["string", "null"] },
      recommended_page_type: { type: "string" },
      recommendation: { type: "string", enum: ["POUSSER", "CRÉER", "CONSOLIDER", "ÉCARTER", "À_VALIDER"] },
    });
    const { data, usage } = await this.json(this.model, KEYWORDS_SYSTEM, req, "keywords", obj({ candidates: arr(item) }), z.object({ candidates: z.array(KeywordZ) }));
    return { candidates: data.candidates, usage };
  }

  async draftEmail(req: DraftRequest): Promise<{ subject: string; sentences: DraftSentence[]; usage: Usage }> {
    const sentence = obj({ kind: { type: "string", enum: [...KINDS] }, text: { type: "string" }, evidence_ids: arr({ type: "string" }) });
    const { data, usage } = await this.json(this.model, DRAFT_SYSTEM, req, "draft", obj({ subject: { type: "string" }, sentences: arr(sentence) }), z.object({ subject: z.string(), sentences: z.array(SentenceZ) }));
    return { subject: data.subject, sentences: data.sentences.map((s, i) => ({ ...s, id: `s${i + 1}` })), usage };
  }

  async rewriteSentences(req: DraftRequest, failed: Parameters<Analyst["rewriteSentences"]>[1]) {
    const item = obj({ id: { type: "string" }, text: { type: ["string", "null"] }, evidence_ids: arr({ type: "string" }) });
    const parser = z.object({ rewrites: z.array(z.object({ id: z.string(), text: z.string().nullable(), evidence_ids: z.array(z.string()) })) });
    const user = { context: req, refused: failed.map((f) => ({ id: f.sentence.id, kind: f.sentence.kind, text: f.sentence.text, reason: f.check.reason })) };
    const { data, usage } = await this.json(this.model, REWRITE_SYSTEM, user, "rewrites", obj({ rewrites: arr(item) }), parser);
    return { rewrites: data.rewrites, usage };
  }
}

/** Un secret ou un modèle absent bloque cette intégration avec une erreur explicite ; il ne devient jamais une fausse réussite. */
export function openaiProviders(env: Record<string, string | undefined>): Providers {
  const missing = ["OPENAI_API_KEY", "OPENAI_MODEL_SEARCH", "OPENAI_MODEL_VISIBILITY", "OPENAI_MODEL_ANALYST"].filter((k) => !env[k]);
  if (missing.length) throw new AppError("AUTH_ERROR", `Intégration OpenAI non configurée : ${missing.join(", ")} manquant(s).`);
  const cfg: OpenAIConfig = { apiKey: env.OPENAI_API_KEY!, searchModel: env.OPENAI_MODEL_SEARCH!, visibilityModel: env.OPENAI_MODEL_VISIBILITY!, analystModel: env.OPENAI_MODEL_ANALYST! };
  return { search: new OpenAISearch(cfg), visibility: new OpenAIVisibility(cfg), analyst: new OpenAIAnalyst(cfg) };
}
