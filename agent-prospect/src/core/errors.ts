export const ERROR_CATEGORIES = [
  "TEMPORARY_API_ERROR",
  "RATE_LIMIT",
  "TIMEOUT",
  "DNS_ERROR",
  "NOT_FOUND",
  "INVALID_HTML",
  "BLOCKED_SOURCE",
  "BUDGET_EXCEEDED",
  "PRICING_UNKNOWN",
  "AUTH_ERROR",
  "INVALID_INPUT",
  "INVALID_OUTPUT",
  "UNKNOWN",
] as const;
export type ErrorCategory = (typeof ERROR_CATEGORIES)[number];

export class AppError extends Error {
  constructor(
    public category: ErrorCategory,
    message: string,
    public retryAfterMs?: number,
  ) {
    super(message);
    this.name = "AppError";
  }
}

export type Recovery = "RETRY" | "ALTERNATIVE" | "STOP_SOURCE" | "STOP_INTEGRATION" | "BUDGET_BLOCK" | "FAIL";

export interface RetryPolicy {
  retryable: boolean;
  maxAttempts: number;
  baseDelayMs: number;
  maxDelayMs: number;
  recovery: Recovery;
}

export const POLICIES: Record<ErrorCategory, RetryPolicy> = {
  TEMPORARY_API_ERROR: { retryable: true, maxAttempts: 3, baseDelayMs: 1000, maxDelayMs: 20000, recovery: "RETRY" },
  RATE_LIMIT: { retryable: true, maxAttempts: 4, baseDelayMs: 2000, maxDelayMs: 60000, recovery: "RETRY" },
  TIMEOUT: { retryable: true, maxAttempts: 3, baseDelayMs: 1000, maxDelayMs: 20000, recovery: "RETRY" },
  DNS_ERROR: { retryable: true, maxAttempts: 2, baseDelayMs: 1000, maxDelayMs: 5000, recovery: "RETRY" },
  NOT_FOUND: { retryable: false, maxAttempts: 1, baseDelayMs: 0, maxDelayMs: 0, recovery: "ALTERNATIVE" },
  INVALID_HTML: { retryable: false, maxAttempts: 1, baseDelayMs: 0, maxDelayMs: 0, recovery: "ALTERNATIVE" },
  // Jamais de contournement : la source est abandonnée.
  BLOCKED_SOURCE: { retryable: false, maxAttempts: 1, baseDelayMs: 0, maxDelayMs: 0, recovery: "STOP_SOURCE" },
  BUDGET_EXCEEDED: { retryable: false, maxAttempts: 1, baseDelayMs: 0, maxDelayMs: 0, recovery: "BUDGET_BLOCK" },
  PRICING_UNKNOWN: { retryable: false, maxAttempts: 1, baseDelayMs: 0, maxDelayMs: 0, recovery: "BUDGET_BLOCK" },
  AUTH_ERROR: { retryable: false, maxAttempts: 1, baseDelayMs: 0, maxDelayMs: 0, recovery: "STOP_INTEGRATION" },
  INVALID_INPUT: { retryable: false, maxAttempts: 1, baseDelayMs: 0, maxDelayMs: 0, recovery: "FAIL" },
  INVALID_OUTPUT: { retryable: true, maxAttempts: 2, baseDelayMs: 0, maxDelayMs: 0, recovery: "RETRY" },
  UNKNOWN: { retryable: false, maxAttempts: 1, baseDelayMs: 0, maxDelayMs: 0, recovery: "FAIL" },
};

export interface Classified {
  category: ErrorCategory;
  message: string;
  retryAfterMs?: number;
}

function parseRetryAfter(value: unknown): number | undefined {
  if (typeof value !== "string" || !value) return undefined;
  const secs = Number(value);
  if (Number.isFinite(secs)) return Math.max(0, secs * 1000);
  const date = Date.parse(value);
  return Number.isNaN(date) ? undefined : Math.max(0, date - Date.now());
}

export function categoryForHttpStatus(status: number): ErrorCategory {
  if (status === 401) return "AUTH_ERROR";
  if (status === 403) return "BLOCKED_SOURCE";
  if (status === 404 || status === 410) return "NOT_FOUND";
  if (status === 408) return "TIMEOUT";
  if (status === 429) return "RATE_LIMIT";
  if (status >= 500) return "TEMPORARY_API_ERROR";
  return "UNKNOWN";
}

/** Classe une erreur à partir de champs structurés (catégorie, statut HTTP, code système), jamais du texte du message. */
export function classify(err: unknown): Classified {
  if (err instanceof AppError) return { category: err.category, message: err.message, retryAfterMs: err.retryAfterMs };
  const e = err as { status?: unknown; code?: unknown; name?: unknown; message?: unknown; headers?: unknown; cause?: unknown };
  const message = typeof e?.message === "string" ? e.message : String(err);
  if (typeof e?.status === "number") {
    // Erreurs d'un SDK d'API : 403 = clé sans droit, pas une source bloquée.
    const category = e.status === 403 ? "AUTH_ERROR" : categoryForHttpStatus(e.status);
    const headers = e.headers as { get?: (k: string) => string | null } | Record<string, string> | undefined;
    const ra = typeof headers?.get === "function" ? headers.get("retry-after") : (headers as Record<string, string> | undefined)?.["retry-after"];
    return { category, message, retryAfterMs: parseRetryAfter(ra) };
  }
  // Erreurs de connexion des SDK (Anthropic, OpenAI) : pas de statut HTTP, mais un nom de classe stable.
  const ctor = (err as { constructor?: { name?: string } })?.constructor?.name;
  if (ctor === "APIConnectionTimeoutError") return { category: "TIMEOUT", message };
  if (ctor === "APIConnectionError") return { category: "TEMPORARY_API_ERROR", message };
  const code = typeof e?.code === "string" ? e.code : typeof (e?.cause as { code?: unknown })?.code === "string" ? ((e.cause as { code: string }).code) : undefined;
  if (code === "ENOTFOUND" || code === "EAI_AGAIN") return { category: "DNS_ERROR", message };
  if (code === "ETIMEDOUT" || code === "UND_ERR_CONNECT_TIMEOUT" || e?.name === "TimeoutError" || e?.name === "AbortError") return { category: "TIMEOUT", message };
  if (code === "ECONNRESET" || code === "ECONNREFUSED" || code === "EPIPE") return { category: "TEMPORARY_API_ERROR", message };
  return { category: "UNKNOWN", message };
}

export function backoffDelay(attempt: number, policy: RetryPolicy, random: () => number = Math.random): number {
  const exp = Math.min(policy.maxDelayMs, policy.baseDelayMs * 2 ** (attempt - 1));
  return Math.round(exp / 2 + (exp / 2) * random());
}

export interface RetryEnv {
  sleep: (ms: number) => Promise<void>;
  random?: () => number;
  maxAttempts?: number;
  onRetry?: (c: Classified, attempt: number, delayMs: number) => void;
}

/** Retries bornés avec backoff et jitter ; respecte Retry-After ; aucune relance d'une erreur non rejouable. */
export async function withRetry<T>(fn: (attempt: number) => Promise<T>, env: RetryEnv): Promise<T> {
  for (let attempt = 1; ; attempt++) {
    try {
      return await fn(attempt);
    } catch (err) {
      const c = classify(err);
      const policy = POLICIES[c.category];
      const max = Math.min(policy.maxAttempts, env.maxAttempts ?? policy.maxAttempts);
      if (!policy.retryable || attempt >= max) throw err instanceof AppError ? err : new AppError(c.category, c.message, c.retryAfterMs);
      const delay = Math.min(policy.maxDelayMs, Math.max(c.retryAfterMs ?? 0, backoffDelay(attempt, policy, env.random)));
      env.onRetry?.(c, attempt, delay);
      await env.sleep(delay);
    }
  }
}
