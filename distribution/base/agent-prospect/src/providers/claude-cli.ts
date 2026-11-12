import { spawn } from "node:child_process";
import { mkdtempSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { z } from "zod";
import type { DraftSentence } from "../core/claims";
import { AppError } from "../core/errors";
import type { KeywordCandidate } from "../core/keywords";
import { CLAUDE_SEARCH_SYSTEM, DRAFT_SYSTEM, KEYWORDS_SYSTEM, PROFILE_SYSTEM, PROMPT_VERSION, REWRITE_SYSTEM } from "../prompts";
import { KeywordZ, ProfileZ, SentenceZ } from "./schemas";
import type { Analyst, CallEstimate, DraftRequest, KeywordRequest, ProfileRequest, SearchCandidate, SearchProvider, SiteProfile, Usage } from "./types";

/**
 * Claude par la ligne de commande `claude -p`, sur le forfait Max de l'opérateur : aucun coût à l'appel.
 * La clé ANTHROPIC_API_KEY est retirée de l'environnement du process, sinon l'appel serait facturé à l'API.
 * Chaque appel tourne dans un dossier vide, sans réglages utilisateur (donc sans hooks), sans MCP, sans session gardée.
 */
export interface CliResult {
  is_error?: boolean;
  subtype?: string;
  result?: string;
  structured_output?: unknown;
  usage?: { input_tokens?: number; output_tokens?: number; cache_creation_input_tokens?: number; cache_read_input_tokens?: number; server_tool_use?: { web_search_requests?: number } };
  modelUsage?: Record<string, { inputTokens?: number; outputTokens?: number; cacheReadInputTokens?: number; cacheCreationInputTokens?: number; webSearchRequests?: number }>;
}

export function usageFromCli(model: string, r: CliResult): Usage {
  let input = 0;
  let output = 0;
  let searches = 0;
  for (const m of Object.values(r.modelUsage ?? {})) {
    input += (m.inputTokens ?? 0) + (m.cacheReadInputTokens ?? 0) + (m.cacheCreationInputTokens ?? 0);
    output += m.outputTokens ?? 0;
    searches += m.webSearchRequests ?? 0;
  }
  return { model, input_tokens: input, output_tokens: output, web_search_calls: searches, reported: r.modelUsage ?? r.usage ?? null };
}

export interface CliOptions {
  bin?: string;
  model: string;
  timeoutMs?: number;
}

export function runClaudeCli(opts: CliOptions, call: { system: string; prompt: string; schema: object; webSearch: boolean; effort?: string }): Promise<CliResult> {
  const args = [
    "-p", "--output-format", "json", "--no-session-persistence", "--setting-sources", "project", "--strict-mcp-config",
    "--model", opts.model, "--system-prompt", call.system, "--json-schema", JSON.stringify(call.schema),
    "--tools", call.webSearch ? "WebSearch" : "", ...(call.webSearch ? ["--allowedTools", "WebSearch"] : []),
    ...(call.effort ? ["--effort", call.effort] : []),
  ];
  const env = { ...process.env };
  for (const k of Object.keys(env)) if (k.startsWith("ANTHROPIC_") || k === "CLAUDECODE" || k.startsWith("CLAUDE_CODE_")) delete env[k];
  return new Promise((resolve, reject) => {
    const child = spawn(opts.bin ?? "claude", args, { cwd: mkdtempSync(join(tmpdir(), "agent-claude-")), env, stdio: ["pipe", "pipe", "pipe"] });
    let out = "";
    let err = "";
    const timer = setTimeout(() => child.kill("SIGTERM"), opts.timeoutMs ?? 600_000);
    child.stdout.on("data", (d) => (out += d));
    child.stderr.on("data", (d) => (err += d));
    child.on("error", (e) => {
      clearTimeout(timer);
      reject(new AppError("AUTH_ERROR", `claude introuvable ou non lancé : ${e.message}`));
    });
    child.on("close", (code, signal) => {
      clearTimeout(timer);
      if (signal === "SIGTERM") return reject(new AppError("TIMEOUT", "claude -p : délai dépassé"));
      let parsed: CliResult;
      try {
        parsed = JSON.parse(out) as CliResult;
      } catch {
        return reject(new AppError("TEMPORARY_API_ERROR", `claude -p a quitté (code ${code}) sans JSON : ${(err || out).slice(0, 300)}`));
      }
      // Limite du forfait atteinte, authentification perdue… : l'erreur est rendue telle quelle, jamais maquillée en réponse vide.
      if (parsed.is_error) {
        const msg = `claude -p : ${parsed.subtype ?? "erreur"} ${String(parsed.result ?? "").slice(0, 300)}`;
        return reject(new AppError(/limit|quota|usage/i.test(msg) ? "RATE_LIMIT" : /auth|login|log in/i.test(msg) ? "AUTH_ERROR" : "TEMPORARY_API_ERROR", msg));
      }
      resolve(parsed);
    });
    child.stdin.end(call.prompt);
  });
}

/** Schéma JSON pour --json-schema : la CLI refuse la clé $schema (draft 2020-12) que zod ajoute. */
export function cliSchema(schema: z.ZodType): object {
  const { $schema: _drop, ...rest } = z.toJSONSchema(schema) as Record<string, unknown>;
  return rest;
}

abstract class CliBase {
  constructor(protected opts: CliOptions) {}
  get model() {
    return `max:${this.opts.model}`;
  }
  protected async json<S extends z.ZodType>(system: string, user: unknown, schema: S, what: string, webSearch = false, effort?: string): Promise<{ data: z.infer<S>; usage: Usage }> {
    const r = await runClaudeCli(this.opts, { system, prompt: typeof user === "string" ? user : JSON.stringify(user), schema: cliSchema(schema), webSearch, effort });
    const parsed = schema.safeParse(r.structured_output);
    if (!parsed.success) throw new AppError("INVALID_OUTPUT", `${what} : sortie hors schéma`);
    return { data: parsed.data, usage: usageFromCli(this.model, r) };
  }
}

const SitesZ = z.object({ sites: z.array(z.object({ name: z.string().nullable(), website: z.string(), source_url: z.string(), snippet: z.string() })) });

export class CliSearch extends CliBase implements SearchProvider {
  name = "CLAUDE_MAX_WEB_SEARCH";
  estimate(): CallEstimate {
    return { model: this.model, input_tokens: 0, output_tokens: 0, web_search_calls: 0 };
  }
  async search(query: string, limit: number, excludeDomains: string[]): Promise<{ candidates: SearchCandidate[]; usage: Usage }> {
    const prompt = `Requête : ${query}\nNombre de sites officiels recherchés : ${limit}.${excludeDomains.length ? `\nDomaines déjà connus, à ne pas reproposer : ${excludeDomains.slice(0, 80).join(", ")}` : ""}\nRends chaque site avec l'URL de la page où tu l'as trouvé et une phrase de cette page.`;
    // Ici la liste est rédigée par le modèle à partir de ses recherches. Chaque site est ensuite lu par l'agent :
    // une URL inventée échoue à la qualification et sort de la liste.
    const { data, usage } = await this.json(CLAUDE_SEARCH_SYSTEM, prompt, SitesZ, "Recherche", true);
    const seen = new Set<string>();
    const candidates: SearchCandidate[] = [];
    for (const s of data.sites) {
      let host: string;
      try {
        host = new URL(s.website).hostname.replace(/^www\./, "");
      } catch {
        continue;
      }
      if (seen.has(host) || excludeDomains.includes(host)) continue;
      seen.add(host);
      candidates.push({ name: s.name, website: `https://${new URL(s.website).hostname}/`, source_url: s.source_url, snippet: s.snippet });
    }
    return { candidates: candidates.slice(0, limit), usage };
  }
}

export class CliAnalyst extends CliBase implements Analyst {
  name = "CLAUDE_MAX";
  promptVersion = PROMPT_VERSION;
  estimate(): CallEstimate {
    return { model: this.model, input_tokens: 0, output_tokens: 0, web_search_calls: 0 };
  }
  async extractProfile(req: ProfileRequest): Promise<{ profile: SiteProfile; usage: Usage }> {
    const user = {
      target_practice: req.practice,
      target_subspecialties: req.subspecialties,
      target_city: req.city,
      pages: req.pages.map((p) => `<source url="${p.url}">\n${p.title ?? ""}\n${p.h1s.join(" | ")}\n${p.text.slice(0, 8000)}\n</source>`),
    };
    const { data, usage } = await this.json(PROFILE_SYSTEM, user, ProfileZ, "Profil du site", false, "high");
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
