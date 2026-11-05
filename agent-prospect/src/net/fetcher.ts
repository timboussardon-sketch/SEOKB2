import dns from "node:dns";
import http from "node:http";
import https from "node:https";
import type { LookupFunction } from "node:net";
import { AppError, categoryForHttpStatus } from "../core/errors";
import { assertAllowedUrl, isBlockedAddress } from "../core/ssrf";
import { AGENT_UA } from "./robots";

export interface FetchResult {
  url: string;
  finalUrl: string;
  status: number;
  contentType: string;
  headers: Record<string, string>;
  body: string;
  redirectChain: string[];
  truncated: boolean;
}

export interface Fetcher {
  fetch(url: string, opts?: { maxBytes?: number }): Promise<FetchResult>;
}

/** Résolution DNS contrôlée au moment de la connexion : l'adresse validée est celle qui est jointe. */
export const guardedLookup: LookupFunction = (hostname, options, callback) => {
  const opts = typeof options === "object" ? options : {};
  dns.lookup(hostname, { ...opts, all: true }, (err, addresses) => {
    if (err) return callback(err, "", 0);
    const list = addresses as dns.LookupAddress[];
    const bad = list.find((a) => isBlockedAddress(a.address));
    if (bad) {
      const e = new AppError("BLOCKED_SOURCE", `Adresse interne refusée pour ${hostname} : ${bad.address}`);
      return callback(e as unknown as NodeJS.ErrnoException, "", 0);
    }
    if ((opts as { all?: boolean }).all) return (callback as unknown as (e: null, a: dns.LookupAddress[]) => void)(null, list);
    callback(null, list[0].address, list[0].family);
  });
};

export interface HttpFetcherOptions {
  timeoutMs?: number;
  maxRedirects?: number;
  minIntervalMs?: number;
  sleep?: (ms: number) => Promise<void>;
  /** Tests uniquement : remplace la résolution DNS. */
  lookup?: LookupFunction;
}

export class HttpFetcher implements Fetcher {
  private nextSlot = new Map<string, number>();
  constructor(private options: HttpFetcherOptions = {}) {}

  private async throttle(host: string): Promise<void> {
    const interval = this.options.minIntervalMs ?? 2000; // 0,5 requête par seconde et par domaine
    const now = Date.now();
    const at = Math.max(now, this.nextSlot.get(host) ?? 0);
    this.nextSlot.set(host, at + interval);
    if (at > now) await (this.options.sleep ?? ((ms) => new Promise((r) => setTimeout(r, ms))))(at - now);
  }

  private once(url: URL, maxBytes: number): Promise<{ status: number; headers: http.IncomingHttpHeaders; body: Buffer; truncated: boolean }> {
    return new Promise((resolve, reject) => {
      const lib = url.protocol === "https:" ? https : http;
      const req = lib.request(
        url,
        {
          method: "GET",
          lookup: this.options.lookup ?? guardedLookup,
          timeout: this.options.timeoutMs ?? 10000,
          headers: { "user-agent": AGENT_UA, accept: "text/html,application/xhtml+xml,text/plain,application/xml;q=0.8", "accept-encoding": "identity" },
        },
        (res) => {
          const chunks: Buffer[] = [];
          let size = 0;
          let truncated = false;
          res.on("data", (c: Buffer) => {
            size += c.length;
            if (size > maxBytes) {
              truncated = true;
              res.destroy();
              return;
            }
            chunks.push(c);
          });
          const done = () => resolve({ status: res.statusCode ?? 0, headers: res.headers, body: Buffer.concat(chunks), truncated });
          res.on("end", done);
          res.on("close", done);
          res.on("error", reject);
        },
      );
      req.on("timeout", () => req.destroy(new AppError("TIMEOUT", `Délai dépassé : ${url.host}`)));
      req.on("error", reject);
      req.end();
    });
  }

  async fetch(rawUrl: string, opts: { maxBytes?: number } = {}): Promise<FetchResult> {
    const maxBytes = opts.maxBytes ?? 2_000_000;
    let url = assertAllowedUrl(rawUrl);
    const chain: string[] = [];
    for (let hop = 0; ; hop++) {
      await this.throttle(url.host);
      const res = await this.once(url, maxBytes);
      const location = res.headers.location;
      if (res.status >= 300 && res.status < 400 && location) {
        if (hop >= (this.options.maxRedirects ?? 5)) throw new AppError("BLOCKED_SOURCE", "Trop de redirections");
        const next = assertAllowedUrl(new URL(location, url).toString());
        if (url.protocol === "https:" && next.protocol === "http:") throw new AppError("BLOCKED_SOURCE", "Redirection de https vers http refusée");
        chain.push(url.toString());
        url = next;
        continue;
      }
      if (res.status === 429) {
        const ra = Number(res.headers["retry-after"]);
        throw new AppError("RATE_LIMIT", `429 sur ${url.host}`, Number.isFinite(ra) ? ra * 1000 : undefined);
      }
      // 401 / 403 : accès protégé. On s'arrête, sans contournement.
      if (res.status === 401 || res.status === 403) throw new AppError("BLOCKED_SOURCE", `Accès refusé (${res.status}) sur ${url.host}`);
      if (res.status >= 500) throw new AppError(categoryForHttpStatus(res.status), `Erreur ${res.status} sur ${url.host}`);
      const contentType = String(res.headers["content-type"] ?? "").toLowerCase();
      const textual = /text\/|xml|json/.test(contentType) || contentType === "";
      const latin = /iso-8859-1|latin1|windows-1252/.test(contentType);
      const headers: Record<string, string> = {};
      for (const [k, v] of Object.entries(res.headers)) if (typeof v === "string") headers[k] = v;
      return {
        url: rawUrl,
        finalUrl: url.toString(),
        status: res.status,
        contentType,
        headers,
        body: textual ? res.body.toString(latin ? "latin1" : "utf8") : "",
        redirectChain: chain,
        truncated: res.truncated,
      };
    }
  }
}

/** Sites fictifs servis depuis la mémoire : tests et mode simulation. Aucun accès réseau. */
export class FixtureFetcher implements Fetcher {
  public calls: string[] = [];
  constructor(private pages: Map<string, { status?: number; body: string; contentType?: string; error?: AppError }>) {}
  async fetch(url: string): Promise<FetchResult> {
    assertAllowedUrl(url);
    this.calls.push(url);
    const page = this.pages.get(url) ?? this.pages.get(`${url}/`) ?? this.pages.get(url.replace(/\/$/, ""));
    if (page?.error) throw page.error;
    const status = page ? (page.status ?? 200) : 404;
    return { url, finalUrl: url, status, contentType: page?.contentType ?? "text/html", headers: {}, body: page?.body ?? "", redirectChain: [], truncated: false };
  }
}
