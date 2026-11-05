import Anthropic from "@anthropic-ai/sdk";
import { zodOutputFormat } from "@anthropic-ai/sdk/helpers/zod";
import { z } from "zod";
import type { DraftSentence } from "../core/claims";
import { AppError } from "../core/errors";
import type { KeywordCandidate } from "../core/keywords";
import { CLAUDE_SEARCH_SYSTEM, DRAFT_SYSTEM, KEYWORDS_SYSTEM, PROFILE_SYSTEM, PROMPT_VERSION, REWRITE_SYSTEM } from "../prompts";
import { KeywordZ, ProfileZ, SentenceZ } from "./schemas";
import type { Analyst, CallEstimate, DraftRequest, KeywordRequest, ProfileRequest, Providers, SearchCandidate, SearchProvider, SiteProfile, Usage, VisibilityAnswer, VisibilityProvider } from "./types";

/** Intégration Claude (Messages API). Le modèle vient de CLAUDE_MODEL, par défaut claude-opus-5-5. */
const FALLBACK_BETA = "server-side-fallback-2026-07-01";
const MAX_PAUSES = 3;
// Variante de base de la recherche web : sur les essais du 2026-10-01 (claude-opus-5-5), elle a renvoyé des citations dans le texte.
// La variante 20260209 n'en a renvoyé aucune sur deux appels. Deux appels ne prouvent pas qu'elle n'en renvoie jamais : à revérifier.
const SEARCH_TOOL = "web_search_20250305" as const;

type Message = Anthropic.Beta.Messages.BetaMessage;

function usageOf(res: Message, extra: Usage | null = null): Usage {
  const u = res.usage;
  // Lectures et écritures de cache comptées au prix de l'entrée : majorant simple, jamais une sous-estimation.
  const input = u.input_tokens + (u.cache_creation_input_tokens ?? 0) + (u.cache_read_input_tokens ?? 0);
  return {
    // Modèle qui a réellement répondu : il diffère du modèle demandé si un repli a eu lieu.
    model: res.model,
    input_tokens: input + (extra?.input_tokens ?? 0),
    output_tokens: u.output_tokens + (extra?.output_tokens ?? 0),
    web_search_calls: (u.server_tool_use?.web_search_requests ?? 0) + (extra?.web_search_calls ?? 0),
    reported: extra ? [extra.reported, u].flat() : u,
  };
}

function assertUsable(res: Message, what: string): void {
  if (res.stop_reason === "refusal") throw new AppError("INVALID_INPUT", `${what} : requête refusée par le modèle (${res.stop_details?.category ?? "motif non précisé"})`);
  if (res.stop_reason === "max_tokens") throw new AppError("INVALID_OUTPUT", `${what} : réponse tronquée (max_tokens)`);
}

export interface ClaudeConfig {
  apiKey: string;
  model: string;
}

class Base {
  protected client: Anthropic;
  constructor(protected cfg: ClaudeConfig) {
    // maxRetries: 0 — les relances sont décidées par le moteur, bornées et journalisées.
    this.client = new Anthropic({ apiKey: cfg.apiKey, maxRetries: 0, timeout: 300_000 });
  }
  get model() {
    return this.cfg.model;
  }

  /** Appel avec recherche web. Un tour mis en pause par l'outil serveur est repris, trois fois au plus. */
  protected async searchTurn(prompt: string, system: string | undefined, city: string | null, maxUses: number): Promise<{ message: Message; usage: Usage }> {
    const messages: Anthropic.Beta.Messages.BetaMessageParam[] = [{ role: "user", content: prompt }];
    let usage: Usage | null = null;
    for (let i = 0; ; i++) {
      const res = await this.client.beta.messages.create({
        model: this.model,
        max_tokens: 16000,
        betas: [FALLBACK_BETA],
        fallbacks: "default",
        ...(system ? { system } : {}),
        tools: [{ type: SEARCH_TOOL, name: "web_search", max_uses: maxUses, user_location: { type: "approximate", country: "FR", timezone: "Europe/Paris", ...(city ? { city } : {}) } }],
        messages,
      });
      usage = usageOf(res, usage);
      if (res.stop_reason === "pause_turn" && i < MAX_PAUSES) {
        messages.push({ role: "assistant", content: res.content as Anthropic.Beta.Messages.BetaContentBlockParam[] });
        continue;
      }
      assertUsable(res, "Recherche web");
      return { message: res, usage };
    }
  }

  protected async json<S extends z.ZodType>(system: string, user: unknown, schema: S, what: string, effort?: "low" | "medium" | "high"): Promise<{ data: z.infer<S>; usage: Usage }> {
    const res = await this.client.beta.messages.parse({
      model: this.model,
      max_tokens: 16000,
      betas: [FALLBACK_BETA],
      fallbacks: "default",
      system,
      messages: [{ role: "user", content: JSON.stringify(user) }],
      output_config: { format: zodOutputFormat(schema), ...(effort ? { effort } : {}) },
    });
    assertUsable(res as unknown as Message, what);
    if (res.parsed_output == null) throw new AppError("INVALID_OUTPUT", `${what} : sortie hors schéma`);
    return { data: res.parsed_output as z.infer<S>, usage: usageOf(res as unknown as Message) };
  }
}

function textAndCitations(message: Message): { text: string; citations: { url: string; title?: string }[]; results: { url: string; title: string }[]; searchErrors: string[] } {
  const searchErrors: string[] = [];
  const texts: string[] = [];
  const citations = new Map<string, { url: string; title?: string }>();
  const results = new Map<string, { url: string; title: string }>();
  for (const block of message.content) {
    if (block.type === "text") {
      texts.push(block.text);
      // Seuls les liens affichés comme citations comptent ; une source seulement consultée n'en est pas une.
      for (const c of block.citations ?? []) if (c.type === "web_search_result_location") citations.set(c.url, { url: c.url, title: c.title ?? undefined });
    } else if (block.type === "web_search_tool_result") {
      // Une erreur d'outil arrive dans une réponse HTTP 200 : le contenu est alors un objet d'erreur, pas une liste.
      if (Array.isArray(block.content)) for (const r of block.content) if (r.type === "web_search_result") results.set(r.url, { url: r.url, title: r.title });
      else searchErrors.push((block.content as { error_code?: string }).error_code ?? "erreur de recherche");
    }
  }
  return { text: texts.join(""), citations: [...citations.values()], results: [...results.values()], searchErrors };
}

export class ClaudeSearch extends Base implements SearchProvider {
  name = "CLAUDE_WEB_SEARCH";
  estimate(): CallEstimate {
    return { model: this.model, input_tokens: 60_000, output_tokens: 6_000, web_search_calls: 5 };
  }
  async search(query: string, limit: number, excludeDomains: string[]): Promise<{ candidates: SearchCandidate[]; usage: Usage }> {
    const prompt = `Requête : ${query}\nNombre de sites officiels recherchés : ${limit}.${excludeDomains.length ? `\nDomaines déjà connus, à ne pas reproposer : ${excludeDomains.slice(0, 80).join(", ")}` : ""}`;
    const { message, usage } = await this.searchTurn(prompt, CLAUDE_SEARCH_SYSTEM, null, 5);
    const { citations, results } = textAndCitations(message);
    // Les candidats viennent des résultats de recherche eux-mêmes (URL et intitulé), pas d'une liste rédigée par le modèle.
    const seen = new Set<string>();
    const candidates: SearchCandidate[] = [];
    for (const r of [...citations.map((c) => ({ url: c.url, title: c.title ?? "" })), ...results]) {
      let host: string;
      try {
        host = new URL(r.url).hostname.replace(/^www\./, "");
      } catch {
        continue;
      }
      if (seen.has(host) || excludeDomains.includes(host)) continue;
      seen.add(host);
      candidates.push({ name: r.title || null, website: `https://${new URL(r.url).hostname}/`, source_url: r.url, snippet: r.title });
    }
    return { candidates: candidates.slice(0, limit), usage };
  }
}

export class ClaudeVisibility extends Base implements VisibilityProvider {
  name = "CLAUDE_API_WEB_SEARCH" as const;
  requireWebSearch = true;
  get params() {
    return { tool: SEARCH_TOOL, country: "FR", max_uses: 3, system: null, fallbacks: "default" };
  }
  estimate(): CallEstimate {
    return { model: this.model, input_tokens: 45_000, output_tokens: 4_000, web_search_calls: 3 };
  }
  async ask(prompt: string, city: string): Promise<VisibilityAnswer> {
    // Requête seule, dans une conversation neuve : ni consigne système, ni historique, ni liste de cabinets.
    const { message, usage } = await this.searchTurn(prompt, undefined, city, 3);
    const { text, citations, results } = textAndCitations(message);
    // Recherche « utilisée » = au moins une recherche a rendu des résultats. Une recherche en erreur ne valide pas la réponse.
    return { text, citations, webSearchUsed: results.length > 0, responseId: message.id, usage };
  }
}

export class ClaudeAnalyst extends Base implements Analyst {
  name = "CLAUDE";
  promptVersion = PROMPT_VERSION;
  estimate(kind: "profile" | "keywords" | "draft" | "rewrite"): CallEstimate {
    // La réflexion du modèle est facturée en tokens de sortie : les majorants en tiennent compte.
    const table = { profile: [60_000, 12_000], keywords: [6_000, 10_000], draft: [6_000, 6_000], rewrite: [5_000, 4_000] } as const;
    return { model: this.model, input_tokens: table[kind][0], output_tokens: table[kind][1], web_search_calls: 0 };
  }

  async extractProfile(req: ProfileRequest): Promise<{ profile: SiteProfile; usage: Usage }> {
    const user = {
      target_practice: req.practice,
      target_subspecialties: req.subspecialties,
      target_city: req.city,
      pages: req.pages.map((p) => `<source url="${p.url}">\n${p.title ?? ""}\n${p.h1s.join(" | ")}\n${p.text.slice(0, 8000)}\n</source>`),
    };
    // Effort élevé : au réglage par défaut, le modèle a rendu des listes vides sur des sites qui nomment leur clientèle (essai du 2026-10-02).
    const { data, usage } = await this.json(PROFILE_SYSTEM, user, ProfileZ, "Profil du site", "high");
    return { profile: data, usage };
  }

  async proposeKeywords(req: KeywordRequest): Promise<{ candidates: KeywordCandidate[]; usage: Usage }> {
    const { data, usage } = await this.json(KEYWORDS_SYSTEM, req, z.object({ candidates: z.array(KeywordZ) }), "Mots-clés");
    return { candidates: data.candidates, usage };
  }

  async draftEmail(req: DraftRequest): Promise<{ subject: string; sentences: DraftSentence[]; usage: Usage }> {
    const { data, usage } = await this.json(DRAFT_SYSTEM, req, z.object({ subject: z.string(), sentences: z.array(SentenceZ) }), "Brouillon");
    return { subject: data.subject, sentences: data.sentences.map((s, i) => ({ ...s, id: `s${i + 1}` })), usage };
  }

  async rewriteSentences(req: DraftRequest, failed: Parameters<Analyst["rewriteSentences"]>[1]) {
    const schema = z.object({ rewrites: z.array(z.object({ id: z.string(), text: z.string().nullable(), evidence_ids: z.array(z.string()) })) });
    const user = { context: req, refused: failed.map((f) => ({ id: f.sentence.id, kind: f.sentence.kind, text: f.sentence.text, reason: f.check.reason })) };
    const { data, usage } = await this.json(REWRITE_SYSTEM, user, schema, "Réécriture");
    return { rewrites: data.rewrites, usage };
  }
}

/** Une clé absente bloque cette intégration avec une erreur explicite ; elle ne devient jamais une fausse réussite. */
export function claudeProviders(env: Record<string, string | undefined>): Providers {
  if (!env.ANTHROPIC_API_KEY) throw new AppError("AUTH_ERROR", "Intégration Claude non configurée : ANTHROPIC_API_KEY manquante.");
  const cfg: ClaudeConfig = { apiKey: env.ANTHROPIC_API_KEY, model: env.CLAUDE_MODEL || "claude-opus-5-5" };
  return { search: new ClaudeSearch(cfg), visibility: new ClaudeVisibility(cfg), analyst: new ClaudeAnalyst(cfg) };
}
