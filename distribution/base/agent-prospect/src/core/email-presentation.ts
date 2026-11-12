/** Présentation commune à l'aperçu et aux envois Resend, indépendante du brouillon. */
import { identity } from "./identity";

export const BANNER_CID = "email-banner";

/** Nom d'un PNG déposé dans public/email/ (EMAIL_BANNER_FILE). Vide : aucun bandeau sous l'email. */
export function bannerFile(env: Record<string, string | undefined> = process.env): string | null {
  const name = env.EMAIL_BANNER_FILE?.trim();
  return name && /^[\w.-]+\.png$/i.test(name) ? name : null;
}
export const bannerPath = (): string | null => {
  const file = bannerFile();
  return file ? `/email/${file}` : null;
};
export const bannerCid = (): string | null => (bannerFile() ? `cid:${BANNER_CID}` : null);

const escapeHtml = (text: string) => text.replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]!);
const escapeRegex = (text: string) => text.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");

function linkify(text: string): string {
  return text.split(/(https?:\/\/[^\s<>"']+)/g).map((part, i) => {
    if (i % 2 === 0) return escapeHtml(part);
    const url = part.replace(/[.,;!?)]+$/, "");
    return `<a href="${escapeHtml(url)}" style="color:#2559DD;text-decoration:underline;overflow-wrap:anywhere;">${escapeHtml(url)}</a>${escapeHtml(part.slice(url.length))}`;
  }).join("");
}

export function presentEmail(body: string, bannerSrc: string | null = bannerPath()): { text: string; html: string } {
  const { name, company, url } = identity();
  if (company) body = body.replace(new RegExp(`(^|\\n)[ \\t]*${escapeRegex(company)}[ \\t]*(?=\\r?\\n|$)`, "g"), "");
  const text = !url || new RegExp(`${escapeRegex(url)}/?(?=\\s|$)`, "i").test(body) ? body : `${body.trimEnd()}\n\n${url}`;
  const paragraphs = body.replace(/\r\n?/g, "\n").split(/\n\s*\n/).map((p) => `<p style="margin:0 0 18px;font-size:16px;line-height:1.65;">${linkify(p).replace(/\n/g, "<br>")}</p>`).join("\n");
  const label = escapeHtml(company || name);
  // Bandeau facultatif : PNG affiché depuis le site dans l’aperçu et embarqué par CID dans Resend.
  const banner = bannerSrc
    ? `<tr><td style="padding-top:14px;">
${url ? `<a href="${escapeHtml(url)}" aria-label="${label}" style="display:block;text-decoration:none;">` : ""}
<img src="${escapeHtml(bannerSrc)}" width="600" alt="${label}" style="display:block;width:100%;max-width:600px;height:auto;border:0;border-radius:20px;">
${url ? "</a>" : ""}
</td></tr>`
    : "";
  const html = `<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Email</title></head>
<body style="margin:0;padding:0;background-color:#ffffff;color:#0A0F1E;font-family:Arial,Helvetica,sans-serif;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding:24px 16px;">
<!--[if mso]><table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0"><tr><td><![endif]-->
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="max-width:600px;"><tr><td>${paragraphs}</td></tr>
${banner}</table>
<!--[if mso]></td></tr></table><![endif]-->
</td></tr></table></body></html>`;
  return { text, html };
}
