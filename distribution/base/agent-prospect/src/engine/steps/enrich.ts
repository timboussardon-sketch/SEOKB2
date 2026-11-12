import { and, eq, inArray } from "drizzle-orm";
import { schema } from "../../db/client";
import { extractEmails, type EmailFinding } from "../../core/email-extract";
import { canonicalDomain, normalize } from "../../core/text";
import type { Campaign, Deps, Firm, Prospect, Runtime, SitePage } from "../deps";
import { ensureSitePages, okPages } from "../site";
import { setState } from "../transitions";

function collect(pages: SitePage[], domain: string): EmailFinding[] {
  const all = new Map<string, EmailFinding>();
  for (const p of okPages(pages)) {
    for (const f of extractEmails({ url: p.url, text: p.text ?? "", mailtos: p.mailtos }, domain)) {
      const prev = all.get(f.email);
      // On garde la publication la plus probante : lien mailto, puis page de contact.
      if (!prev || (prev.source_type !== "MAILTO" && f.source_type === "MAILTO") || (/contact/.test(f.source_url) && !/contact/.test(prev.source_url) && prev.source_type === f.source_type)) all.set(f.email, f);
    }
  }
  return [...all.values()];
}

function rank(f: EmailFinding, domain: string, lawyerLast: string | null): number {
  const [local, host] = f.email.split("@");
  let score = 0;
  if (canonicalDomain(host) === domain) score += 4;
  if (f.source_type === "MAILTO") score += 2;
  if (/contact/.test(f.source_url)) score += 2;
  if (/^(contact|cabinet|avocats?|accueil|secretariat)$/.test(local)) score += 1;
  if (lawyerLast && normalize(local).includes(normalize(lawyerLast))) score += 3;
  return score;
}

/**
 * Boucle d'enrichissement : lire les pages utiles, extraire, et tant qu'aucune adresse exploitable n'est trouvée,
 * lire les pages suivantes du site jusqu'au plafond. Aucune adresse n'est devinée.
 */
export async function enrichStep(deps: Deps, rt: Runtime, campaign: Campaign, prospect: Prospect, firmIn: Firm): Promise<void> {
  const max = campaign.config.max_crawl_pages_per_site;
  let found: EmailFinding[] = [];
  let firm = firmIn;
  let previous = -1;
  for (let wanted = Math.min(12, max); ; wanted = Math.min(max, wanted + 4)) {
    const res = await ensureSitePages(deps, rt.fetcher, firm, wanted, max);
    firm = res.firm;
    found = collect(res.pages, firm.canonical_domain);
    // Sortie : une adresse exploitable, le plafond de pages, ou plus aucune page nouvelle à lire.
    if (found.some((f) => !f.excluded) || wanted >= max || res.pages.length === previous) break;
    previous = res.pages.length;
  }

  const eligible = found.filter((f) => !f.excluded);
  if (eligible.length) {
    const hits = await deps.db.select().from(schema.suppressions).where(inArray(schema.suppressions.value, eligible.map((f) => f.email)));
    if (hits.length) {
      await setState(deps, prospect, "SUPPRESSED", { qualification_reason: "SUPPRESSED_CONTACT", qualification_detail: "Adresse inscrite sur la liste d'opposition." });
      return;
    }
  }

  const [lawyer] = prospect.lawyer_id ? await deps.db.select().from(schema.lawyers).where(eq(schema.lawyers.id, prospect.lawyer_id)) : [];
  const best = [...eligible].sort((a, b) => rank(b, firm.canonical_domain, lawyer?.last_name ?? null) - rank(a, firm.canonical_domain, lawyer?.last_name ?? null) || a.email.localeCompare(b.email))[0];
  const routable = new Map<string, boolean | null>();
  for (const f of eligible) {
    const host = f.email.split("@")[1];
    if (!routable.has(host)) routable.set(host, await rt.resolveMx(host).catch(() => null));
  }

  await deps.db.transaction(async (tx) => {
    await tx.update(schema.contacts).set({ selected: false }).where(eq(schema.contacts.firm_id, firm.id));
    for (const f of found) {
      const values = {
        firm_id: firm.id,
        email: f.email,
        source_url: f.source_url,
        source_type: f.source_type,
        context: f.context,
        excluded_reason: f.excluded,
        syntax_valid: true,
        domain_routable: f.excluded ? null : (routable.get(f.email.split("@")[1]) ?? null),
        selected: f.email === best?.email,
        observed_at: deps.now(),
      };
      await tx.insert(schema.contacts).values(values).onConflictDoUpdate({ target: [schema.contacts.firm_id, schema.contacts.email], set: { ...values } });
    }
  });
  // Sans adresse publiée, la fiche est conservée et le reste du travail continue.
  await setState(deps, prospect, "ENRICHED", { email_status: best ? "FOUND" : "NO_PUBLIC_EMAIL" });
}

export async function selectedContact(deps: Deps, firmId: string) {
  const [c] = await deps.db.select().from(schema.contacts).where(and(eq(schema.contacts.firm_id, firmId), eq(schema.contacts.selected, true)));
  return c ?? null;
}
