import { spawn } from "node:child_process";
import { mkdtempSync, readFileSync } from "node:fs";
import { homedir, tmpdir } from "node:os";
import { join } from "node:path";
import { AppError } from "../core/errors";
import type { CallEstimate, Usage, VisibilityAnswer, VisibilityProvider } from "./types";

/**
 * Mesure par Codex, l'outil en ligne de commande d'OpenAI, connecté au compte ChatGPT de l'utilisateur (`codex login`).
 * C'est un modèle d'OpenAI avec recherche web en direct. Ce n'est PAS l'interface ChatGPT : l'email ne doit pas dire « dans ChatGPT ».
 * Aucun appel n'est facturé à l'unité : la consommation est imputée au forfait ChatGPT.
 */
export interface CodexEvent {
  type?: string;
  item?: { type?: string; text?: string; query?: string; action?: { type?: string; queries?: string[] } };
  usage?: { input_tokens?: number; output_tokens?: number };
}

export function parseCodexEvents(jsonl: string): { text: string; searches: number; citations: { url: string; title?: string }[]; usage: { input: number; output: number }; reported: unknown } {
  let text = "";
  let searches = 0;
  let usage = { input: 0, output: 0 };
  let reported: unknown = null;
  for (const line of jsonl.split("\n")) {
    let e: CodexEvent;
    try {
      e = JSON.parse(line) as CodexEvent;
    } catch {
      continue;
    }
    if (e.type === "item.completed" && e.item?.type === "agent_message" && e.item.text) text = e.item.text; // le dernier message est la réponse
    if (e.type === "item.completed" && e.item?.type === "web_search" && e.item.action?.type === "search") searches++;
    if (e.type === "turn.completed" && e.usage) {
      usage = { input: e.usage.input_tokens ?? 0, output: e.usage.output_tokens ?? 0 };
      reported = e.usage;
    }
  }
  // Liens affichés dans la réponse : liens Markdown, puis URL nues.
  const found = new Map<string, { url: string; title?: string }>();
  for (const m of text.matchAll(/\[([^\]]+)\]\((https?:\/\/[^\s)]+)\)/g)) found.set(m[2], { url: m[2], title: m[1] });
  for (const m of text.matchAll(/https?:\/\/[^\s)\]»"']+/g)) {
    const url = m[0].replace(/[.,;:]+$/, "");
    if (!found.has(url)) found.set(url, { url });
  }
  return { text, searches, citations: [...found.values()], usage, reported };
}

function configuredModel(): string {
  try {
    return readFileSync(join(homedir(), ".codex", "config.toml"), "utf8").match(/^model\s*=\s*"([^"]+)"/m)?.[1] ?? "inconnu";
  } catch {
    return "inconnu";
  }
}

export class CodexVisibility implements VisibilityProvider {
  name = "OPENAI_CODEX_WEB_SEARCH" as const;
  requireWebSearch = true;
  private modelName: string;
  constructor(private options: { bin?: string; model?: string; timeoutMs?: number } = {}) {
    this.modelName = options.model || configuredModel();
  }
  get model() {
    return `codex:${this.modelName}`;
  }
  get params() {
    return { outil: "codex exec", web_search: "live", sandbox: "read-only", effort: "low", compte: "forfait ChatGPT" };
  }
  estimate(): CallEstimate {
    return { model: this.model, input_tokens: 0, output_tokens: 0, web_search_calls: 0 };
  }

  ask(prompt: string): Promise<VisibilityAnswer> {
    return new Promise((resolve, reject) => {
      const args = ["exec", "--skip-git-repo-check", "--ephemeral", "-s", "read-only", "-c", 'web_search="live"', "-c", 'model_reasoning_effort="low"', "--json"];
      if (this.options.model) args.push("-m", this.options.model);
      // Conversation neuve à chaque appel, dans un dossier vide, sans historique ni instruction ajoutée : la question seule.
      const child = spawn(this.options.bin ?? "codex", [...args, prompt], { cwd: mkdtempSync(join(tmpdir(), "codex-mesure-")), stdio: ["ignore", "pipe", "pipe"] });
      let out = "";
      let err = "";
      const timer = setTimeout(() => {
        child.kill("SIGKILL");
        reject(new AppError("TIMEOUT", "Codex n'a pas répondu dans le délai"));
      }, this.options.timeoutMs ?? 900_000);
      child.stdout.on("data", (d) => (out += d));
      child.stderr.on("data", (d) => (err += d));
      child.on("error", (e) => {
        clearTimeout(timer);
        reject(new AppError("AUTH_ERROR", `Codex introuvable ou non exécutable : ${e.message}`));
      });
      child.on("close", (code) => {
        clearTimeout(timer);
        const parsed = parseCodexEvents(out);
        if (code !== 0 && !parsed.text) {
          const auth = /login|unauthorized|401|not logged/i.test(err);
          return reject(new AppError(auth ? "AUTH_ERROR" : "TEMPORARY_API_ERROR", `Codex a échoué (code ${code}) : ${err.trim().slice(-200)}`));
        }
        const usage: Usage = { model: this.model, input_tokens: parsed.usage.input, output_tokens: parsed.usage.output, web_search_calls: parsed.searches, reported: parsed.reported };
        resolve({ text: parsed.text, citations: parsed.citations, webSearchUsed: parsed.searches > 0, responseId: null, usage });
      });
    });
  }
}
