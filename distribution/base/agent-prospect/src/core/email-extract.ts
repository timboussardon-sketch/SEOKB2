import { canonicalDomain, normalize } from "./text";

const EMAIL_RE = /[a-z0-9._%+-]+@[a-z0-9-]+(?:\.[a-z0-9-]+)*\.[a-z]{2,}/gi;

// Adresses publiées mais sans rapport avec la prise de contact du cabinet.
const EXCLUDED_LOCAL = /^(dpo|rgpd|privacy|cnil|recrutement|rh|jobs?|careers?|candidatures?|stages?|presse|press|media|webmaster|postmaster|abuse|hostmaster|noreply|no-reply|support|admin|technique|comptabilite|compta|facturation)([._+-]|$)/;
// Tiers, clients, victimes, recrutement, DPO, presse, prestataires techniques : jamais des destinataires.
const EXCLUDED_CONTEXT = /\b(dpo|delegue a la protection|recrutement|candidatures?|presse|hebergeur|heberge par|webmaster|directeur de la publication|editeur du site|conception du site|site realise|realisation du site|clients?|clientes?|temoign\w*|victimes?|partie adverse)\b/;
const OWN_DOMAIN_EXCLUDED_CONTEXT = /\b(dpo|delegue a la protection|recrutement|candidatures?|presse)\b/;
const COMMON_LABELS = new Set(["avocat", "avocats", "avocate", "cabinet", "lyon", "paris", "conseil", "conseils", "associes", "law", "legal", "juridique", "droit", "selarl", "scp", "office"]);

/** Deux domaines au même nom distinctif (durand-demo.example, durand-demo-lyon.example) : même titulaire. */
export function sameOwner(domain: string, firmDomain: string): boolean {
  const tokens = (d: string) => (canonicalDomain(d) ?? d).split(".")[0].split(/[-_]/).filter((t) => t.length >= 5 && !COMMON_LABELS.has(t));
  const mine = new Set(tokens(firmDomain));
  return tokens(domain).some((t) => mine.has(t));
}
const ASSET = /\.(png|jpe?g|gif|svg|webp|css|js)$/i;

export interface EmailFinding {
  email: string;
  source_url: string;
  source_type: "MAILTO" | "TEXT";
  context: string;
  excluded: string | null;
}

export function normalizeEmail(e: string): string {
  return e.trim().toLowerCase().replace(/^mailto:/, "").split("?")[0];
}

export function isSyntaxValid(email: string): boolean {
  return /^[a-z0-9._%+-]+@[a-z0-9-]+(\.[a-z0-9-]+)*\.[a-z]{2,}$/.test(email) && !email.includes("..") && email.length <= 254;
}

/** Extrait les adresses réellement publiées sur une page, avec leur contexte. N'en fabrique aucune. */
export function extractEmails(page: { url: string; text: string; mailtos: { email: string; context: string }[] }, firmDomain: string | null): EmailFinding[] {
  const found = new Map<string, EmailFinding>();
  const judge = (email: string, context: string): string | null => {
    const local = email.split("@")[0];
    const domain = email.split("@")[1];
    if (ASSET.test(email)) return "nom de fichier, pas une adresse";
    if (EXCLUDED_LOCAL.test(local)) return `boîte hors prise de contact (${local})`;
    const own = !!firmDomain && (canonicalDomain(domain) === firmDomain || sameOwner(domain, firmDomain));
    // Sur le domaine du cabinet, « mentions légales », « clients » ou « hébergeur » autour de l'adresse ne la rendent pas tierce :
    // l'agence ou l'hébergeur publient sous leur propre domaine. Seuls DPO, recrutement et presse restent écartés.
    if ((own ? OWN_DOMAIN_EXCLUDED_CONTEXT : EXCLUDED_CONTEXT).test(normalize(context))) return "contexte hors prise de contact (DPO, presse, hébergeur, recrutement)";
    // Une adresse d'un autre domaine nommé (agence web, hébergeur, tiers) n'est pas celle du cabinet.
    // Les messageries grand public restent admises si le cabinet les publie comme contact.
    const generic = /^(gmail|outlook|hotmail|yahoo|orange|wanadoo|free|laposte|icloud|live|sfr|avocat-conseil|avocatline)\./.test(domain) || /\.avocat\.fr$|barreau/.test(domain);
    if (firmDomain && !own && !generic) return `domaine tiers (${domain})`;
    return null;
  };
  for (const m of page.mailtos) {
    const email = normalizeEmail(m.email);
    if (!isSyntaxValid(email)) continue;
    found.set(email, { email, source_url: page.url, source_type: "MAILTO", context: m.context.slice(0, 240), excluded: judge(email, m.context) });
  }
  for (const m of page.text.matchAll(EMAIL_RE)) {
    const email = normalizeEmail(m[0]);
    if (found.has(email) || !isSyntaxValid(email)) continue;
    const i = m.index ?? 0;
    // Le libellé qui précède l'adresse dit à qui elle appartient.
    const context = page.text.slice(Math.max(0, i - 80), i + email.length).replace(/\s+/g, " ");
    found.set(email, { email, source_url: page.url, source_type: "TEXT", context, excluded: judge(email, context) });
  }
  return [...found.values()];
}
