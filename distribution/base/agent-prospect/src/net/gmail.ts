import type { InboxMessage } from "../core/outreach";

/**
 * Lecture de la boîte Gmail de MAIL_REPLY_TO, où arrivent les réponses.
 * OAuth avec un client « application de bureau » créé une fois dans la console Google Cloud. Portée en lecture seule.
 */
export const GMAIL_SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"];

export interface Inbox {
  search(query: string): Promise<InboxMessage[]>;
}

export interface OAuthApp {
  clientId: string;
  clientSecret: string;
}

export function oauthApp(env: Record<string, string | undefined> = process.env): OAuthApp | null {
  return env.GMAIL_CLIENT_ID && env.GMAIL_CLIENT_SECRET ? { clientId: env.GMAIL_CLIENT_ID, clientSecret: env.GMAIL_CLIENT_SECRET } : null;
}

export function authUrl(app: OAuthApp, redirectUri: string, state: string): string {
  const q = new URLSearchParams({ client_id: app.clientId, redirect_uri: redirectUri, response_type: "code", scope: GMAIL_SCOPES.join(" "), access_type: "offline", prompt: "consent", state });
  return `https://accounts.google.com/o/oauth2/v2/auth?${q}`;
}

async function tokenCall(body: Record<string, string>): Promise<{ access_token: string; expires_in: number; refresh_token?: string }> {
  const res = await fetch("https://oauth2.googleapis.com/token", { method: "POST", headers: { "content-type": "application/x-www-form-urlencoded" }, body: new URLSearchParams(body) });
  const json = await res.json();
  if (!res.ok) throw new Error(`Google OAuth ${res.status} : ${json.error_description ?? json.error ?? "erreur"}`);
  return json;
}

export const exchangeCode = (app: OAuthApp, code: string, redirectUri: string) =>
  tokenCall({ code, client_id: app.clientId, client_secret: app.clientSecret, redirect_uri: redirectUri, grant_type: "authorization_code" });

export const refreshAccess = (app: OAuthApp, refreshToken: string) =>
  tokenCall({ refresh_token: refreshToken, client_id: app.clientId, client_secret: app.clientSecret, grant_type: "refresh_token" });

const API = "https://gmail.googleapis.com/gmail/v1/users/me";

export async function profileEmail(accessToken: string): Promise<string> {
  const res = await fetch(`${API}/profile`, { headers: { authorization: `Bearer ${accessToken}` } });
  const json = await res.json();
  if (!res.ok) throw new Error(`Gmail ${res.status} : ${json.error?.message ?? "erreur"}`);
  return json.emailAddress;
}

const unescape = (s: string) => s.replace(/&#39;/g, "'").replace(/&quot;/g, '"').replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&amp;/g, "&");

export function httpInbox(getToken: () => Promise<string>): Inbox {
  const call = async (path: string) => {
    const res = await fetch(`${API}${path}`, { headers: { authorization: `Bearer ${await getToken()}` } });
    const json = await res.json();
    if (!res.ok) throw new Error(`Gmail ${res.status} : ${json.error?.message ?? "erreur"}`);
    return json;
  };
  return {
    async search(query) {
      const list = await call(`/messages?maxResults=20&q=${encodeURIComponent(query)}`);
      const out: InboxMessage[] = [];
      for (const { id } of list.messages ?? []) {
        const m = await call(`/messages/${id}?format=metadata&metadataHeaders=From`);
        out.push({ id, from: m.payload?.headers?.find((h: { name: string }) => h.name.toLowerCase() === "from")?.value ?? "", date: new Date(Number(m.internalDate)), snippet: unescape(m.snippet ?? "") });
      }
      return out;
    },
  };
}
