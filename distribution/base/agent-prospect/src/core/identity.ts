/** Identité de l'expéditeur, lue dans .env.local : rien n'est écrit en dur dans le code. */
export type Identity = { name: string; company: string; url: string; presentation: string };

export function identity(env: Record<string, string | undefined> = process.env): Identity {
  const name = env.SENDER_NAME?.trim() || "[SENDER_NAME à renseigner]";
  const company = env.SENDER_COMPANY?.trim() || "";
  const rawUrl = env.SENDER_URL?.trim() || "";
  const url = /^https?:\/\//i.test(rawUrl) ? rawUrl.replace(/\/+$/, "") : "";
  return { name, company, url, presentation: `${name} (${company ? `${company}, ` : ""}consultant SEO)` };
}
