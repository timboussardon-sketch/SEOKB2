import { and, eq, inArray, ne } from "drizzle-orm";
import { schema } from "../../db/client";
import { classify, withRetry } from "../../core/errors";
import type { QualificationReason } from "../../core/states";
import { normalize } from "../../core/text";
import type { Quote, SiteProfile } from "../../providers/types";
import { metered } from "../budget";
import type { Campaign, Deps, Firm, Prospect, Runtime, SitePage } from "../deps";
import { ensureSitePages, okPages, pageKey } from "../site";
import { logEvent } from "../events";
import { sendToReview, setState } from "../transitions";

const PROFILE_KINDS = ["FIRM_NAME", "IDENTITY", "LOCATION", "PRACTICE_AREA", "OTHER_PRACTICE", "CLIENT_TYPE", "SERVICE", "CERTIFICATION_CLAIM"];

/** Un extrait proposé par l'analyste n'est retenu que s'il figure mot pour mot dans la page citée. */
export function groundProfile(profile: SiteProfile, pages: SitePage[]): SiteProfile {
  const byUrl = new Map<string, string>();
  for (const p of pages) {
    const hay = normalize(`${p.title ?? ""} ${p.h1s.join(" ")} ${p.text ?? ""}`);
    byUrl.set(p.url, hay);
    if (p.final_url) byUrl.set(p.final_url, hay);
    byUrl.set(p.url.replace(/\/$/, ""), hay);
    byUrl.set(`${p.url}/`, hay);
  }
  const ok = (q: { source_url: string; excerpt: string }, mustContain: string[] = []) => {
    const hay = byUrl.get(q.source_url);
    const ex = normalize(q.excerpt);
    return !!hay && ex.length >= 3 && hay.includes(ex) && mustContain.every((m) => ex.includes(normalize(m)));
  };
  return {
    firm_name: profile.firm_name && ok(profile.firm_name, [profile.firm_name.value]) ? profile.firm_name : null,
    lawyers: profile.lawyers.filter((l) => ok(l, [l.first_name, l.last_name])),
    cities: profile.cities.filter((c) => ok(c, [c.value])),
    practice_areas: profile.practice_areas.filter((p) => ok(p)),
    // L'extrait doit nommer lui-même la clientèle : un extrait réel qui parle d'autre chose ne prouve pas le type proposé.
    client_types: profile.client_types.filter((c) => ok(c) && CLIENT_ANCHOR[c.value].test(normalize(c.excerpt))),
    services: profile.services.filter((s) => ok(s)),
    certification_claims: profile.certification_claims.filter((c) => ok(c)),
  };
}

const CLIENT_ANCHOR = { entreprise: /employeur|entreprise|dirigeant|societe|drh|\btpe\b|\bpme\b/, particulier: /salarie|particulier|\bcadres?\b/ } as const;

/** Phrases des pages lues qui nomment une clientèle, citées telles quelles avec leur page. Aucune conclusion n'en est tirée. */
export function clientHints(pages: Pick<SitePage, "url" | "text">[], max = 3): string[] {
  const out: string[] = [];
  for (const p of pages) {
    for (const sentence of (p.text ?? "").split(/(?<=[.!?])\s+/)) {
      const n = normalize(sentence);
      if (sentence.length > 30 && sentence.length < 320 && (CLIENT_ANCHOR.entreprise.test(n) || CLIENT_ANCHOR.particulier.test(n)) && /clientele|accompagn|conseill|defen|assist|intervien|au service|pour (les|des|une)/.test(n)) {
        out.push(`« ${sentence.trim()} » (${p.url})`);
        break;
      }
    }
    if (out.length >= max) break;
  }
  return out;
}

export type Decision =
  | { status: "QUALIFIED"; lawyerIndex: number | null; note: string | null }
  | { status: "REJECTED"; reason: QualificationReason; detail: string }
  | { status: "NEEDS_REVIEW" | "AMBIGUOUS"; reason: QualificationReason; detail: string; lawyerIndex: number | null };

/** Règles de qualification appliquées par le code sur le profil vérifié. Le modèle propose, il ne décide pas. */
export function decideQualification(profile: SiteProfile, config: Campaign["config"]): Decision {
  const single = profile.lawyers.length === 1 ? 0 : null;
  if (!profile.firm_name && profile.lawyers.length === 0) {
    return { status: "REJECTED", reason: "INSUFFICIENT_EVIDENCE", detail: "Ni cabinet ni avocat identifiable sur les pages lues." };
  }
  const city = normalize(config.location);
  if (profile.cities.length && !profile.cities.some((c) => normalize(c.value) === city)) {
    return { status: "REJECTED", reason: "WRONG_LOCATION", detail: `Localisation relevée : ${profile.cities.map((c) => c.value).join(", ")}. Cible : ${config.location}.` };
  }
  if (!profile.practice_areas.some((p) => p.matches_target)) {
    const others = profile.practice_areas.map((p) => p.value);
    if (others.length) return { status: "REJECTED", reason: "WRONG_PRACTICE", detail: `Pratiques relevées : ${others.join(", ")}. Cible : ${config.practice_area}.` };
    return { status: "NEEDS_REVIEW", reason: "INSUFFICIENT_EVIDENCE", detail: "Aucun domaine de pratique relevé avec un extrait vérifiable.", lawyerIndex: single };
  }
  if (config.client_type !== "mixte") {
    const types = profile.client_types.map((c) => c.value);
    if (types.length && !types.includes(config.client_type)) {
      return { status: "REJECTED", reason: "WRONG_CLIENT_TYPE", detail: `Clientèle relevée : ${types.join(", ")}. Cible : ${config.client_type}.` };
    }
    if (!types.length) return { status: "NEEDS_REVIEW", reason: "INSUFFICIENT_EVIDENCE", detail: "Clientèle non établie par le site.", lawyerIndex: single };
  }
  if (!profile.cities.length) return { status: "NEEDS_REVIEW", reason: "INSUFFICIENT_EVIDENCE", detail: "Localisation non établie par le site.", lawyerIndex: single };
  if (config.target_type === "LAWYER") {
    if (profile.lawyers.length === 0) return { status: "NEEDS_REVIEW", reason: "INSUFFICIENT_EVIDENCE", detail: "Campagne ciblée sur un avocat : aucun avocat nommé sur le site.", lawyerIndex: null };
    if (profile.lawyers.length > 1) {
      return { status: "AMBIGUOUS", reason: "AMBIGUOUS_ENTITY", detail: `Plusieurs avocats dans ce cabinet (${profile.lawyers.map((l) => `${l.first_name} ${l.last_name}`).join(", ")}) : lequel viser ?`, lawyerIndex: null };
    }
  }
  if (config.certified_specialization_required) {
    return {
      status: "NEEDS_REVIEW",
      reason: "INSUFFICIENT_EVIDENCE",
      detail: profile.certification_claims.length ? "Le site revendique une spécialisation : à confirmer dans l'annuaire officiel, l'application ne la vérifie pas." : "Aucune mention de spécialisation certifiée sur le site.",
      lawyerIndex: single,
    };
  }
  const types = new Set(profile.client_types.map((c) => c.value));
  // La présence d'un extrait « entreprises » n'établit pas que le cabinet travaille surtout pour elles.
  const note = config.client_type !== "mixte" && types.size > 1 ? `Clientèle mixte relevée (${[...types].join(", ")}). La part de la clientèle ${config.client_type} n'est pas établie par le site.` : null;
  return { status: "QUALIFIED", lawyerIndex: single, note };
}

async function reject(deps: Deps, prospect: Prospect, reason: QualificationReason, detail: string): Promise<void> {
  await setState(deps, prospect, "REJECTED", { qualification_status: "REJECTED", qualification_reason: reason, qualification_detail: detail });
}

export async function qualifyStep(deps: Deps, rt: Runtime, campaign: Campaign, prospect: Prospect, firmIn: Firm): Promise<void> {
  const cfg = campaign.config;
  const [suppressed] = await deps.db.select().from(schema.suppressions).where(eq(schema.suppressions.value, firmIn.canonical_domain));
  if (suppressed) return reject(deps, prospect, "SUPPRESSED_CONTACT", "Domaine inscrit sur la liste d'opposition.");

  const [elsewhere] = await deps.db
    .select({ id: schema.prospects.id })
    .from(schema.prospects)
    .where(and(eq(schema.prospects.firm_id, firmIn.id), ne(schema.prospects.campaign_id, campaign.id), ne(schema.prospects.state, "REJECTED")));
  if (elsewhere) return reject(deps, prospect, "DUPLICATE", "Cabinet déjà suivi dans une autre campagne : pas de sollicitation parallèle.");

  let firm = firmIn;
  let pages: SitePage[];
  try {
    ({ firm, pages } = await ensureSitePages(deps, rt.fetcher, firmIn, 12, cfg.max_crawl_pages_per_site));
  } catch (err) {
    const c = classify(err);
    if (c.category === "BLOCKED_SOURCE") return reject(deps, prospect, "BLOCKED_SOURCE", c.message);
    if (c.category === "DNS_ERROR") return reject(deps, prospect, "NO_OFFICIAL_SITE", "Domaine introuvable.");
    throw err;
  }
  const readable = okPages(pages);
  const home = pages.find((p) => p.url === pageKey(firm.website));
  if (!readable.length || !home || home.status !== 200) {
    return reject(deps, prospect, "NO_OFFICIAL_SITE", `Page d'accueil inexploitable (${home?.status ?? home?.error_category ?? "aucune réponse"}).`);
  }

  const charge = { campaignId: campaign.id, prospectId: prospect.id, step: "qualify" };
  const { profile: proposed } = await withRetry(
    () =>
      metered(deps, charge, rt.providers.analyst.estimate("profile"), () =>
        rt.providers.analyst.extractProfile({
          pages: readable.slice(0, 12).map((p) => ({ url: p.url, title: p.title, h1s: p.h1s, text: p.text ?? "" })),
          practice: cfg.practice_area,
          subspecialties: cfg.subspecialties,
          city: cfg.location,
        }),
      ),
    { sleep: deps.sleep, random: deps.random },
  );
  const profile = groundProfile(proposed, readable);
  // Trace de ce que le contrôle a écarté : sans elle, on ne sait pas si le modèle n'a rien proposé ou si l'extrait a été refusé.
  const kinds = ["lawyers", "cities", "practice_areas", "client_types", "services", "certification_claims"] as const;
  await logEvent(deps.db, {
    campaignId: campaign.id,
    prospectId: prospect.id,
    type: "PROFILE_GROUNDING",
    data: Object.fromEntries(kinds.map((k) => [k, { proposed: proposed[k].length, kept: profile[k].length, rejected: proposed[k].filter((x) => !(profile[k] as unknown[]).includes(x)).map((x) => ({ source_url: x.source_url, excerpt: x.excerpt.slice(0, 200) })) }])),
  });
  const method = `${rt.providers.analyst.name}:${rt.providers.analyst.promptVersion}+extrait vérifié dans la page`;
  const ev = (kind: string, q: Quote) => ({ prospect_id: prospect.id, kind, value: q.value, source_url: q.source_url, excerpt: q.excerpt.slice(0, 500), extraction_method: method, verification_status: "OBSERVED", observed_at: deps.now() });
  const rows = [
    ...(profile.firm_name ? [ev("FIRM_NAME", profile.firm_name)] : []),
    ...profile.lawyers.map((l) => ev("IDENTITY", { value: `${l.first_name} ${l.last_name}`, source_url: l.source_url, excerpt: l.excerpt })),
    ...profile.cities.map((c) => ev("LOCATION", c)),
    ...profile.practice_areas.map((p) => ev(p.matches_target ? "PRACTICE_AREA" : "OTHER_PRACTICE", p)),
    ...profile.client_types.map((c) => ev("CLIENT_TYPE", c)),
    ...profile.services.map((s) => ev("SERVICE", s)),
    // Revendication relevée sur le site, distincte d'une certification vérifiée.
    ...profile.certification_claims.map((c) => ev("CERTIFICATION_CLAIM", c)),
  ];

  const decision = decideQualification(profile, cfg);
  let lawyerId: string | null = null;
  await deps.db.transaction(async (tx) => {
    const hasKeywords = await tx.select({ id: schema.keywords.id }).from(schema.keywords).where(eq(schema.keywords.prospect_id, prospect.id)).limit(1);
    if (!hasKeywords.length) {
      await tx.delete(schema.evidence).where(and(eq(schema.evidence.prospect_id, prospect.id), inArray(schema.evidence.kind, PROFILE_KINDS)));
      if (rows.length) await tx.insert(schema.evidence).values(rows);
    }
    if (profile.firm_name || profile.cities[0]) {
      await tx.update(schema.firms).set({ name: profile.firm_name?.value ?? firm.name, city: profile.cities[0]?.value ?? firm.city }).where(eq(schema.firms.id, firm.id));
    }
    for (const [i, l] of profile.lawyers.entries()) {
      const normalized = normalize(`${l.first_name} ${l.last_name}`);
      await tx
        .insert(schema.lawyers)
        .values({ firm_id: firm.id, first_name: l.first_name, last_name: l.last_name, normalized_name: normalized, source_url: l.source_url, certified_specialization_status: profile.certification_claims.length ? "CLAIMED_ON_SITE" : "NOT_VERIFIED" })
        .onConflictDoNothing();
      if ("lawyerIndex" in decision && decision.lawyerIndex === i) {
        const [row] = await tx.select({ id: schema.lawyers.id }).from(schema.lawyers).where(and(eq(schema.lawyers.firm_id, firm.id), eq(schema.lawyers.normalized_name, normalized)));
        lawyerId = row.id;
      }
    }
  });

  if (decision.status === "REJECTED") return reject(deps, prospect, decision.reason, decision.detail);
  if (decision.status === "QUALIFIED") {
    await setState(deps, prospect, "QUALIFIED", { qualification_status: "QUALIFIED", qualification_reason: null, qualification_detail: decision.note, lawyer_id: lawyerId });
    return;
  }
  // Pour une clientèle non établie, le code joint les phrases du site qui en parlent : la décision reste humaine, la recherche est faite.
  const hints = decision.detail.startsWith("Clientèle non établie") ? clientHints(readable) : [];
  const detail = hints.length ? `${decision.detail} Phrases du site à lire : ${hints.join(" ")}` : decision.detail;
  await sendToReview(deps, prospect, decision.status === "AMBIGUOUS" ? "AMBIGUOUS_ENTITY" : "UNCERTAIN_PRACTICE", detail, "QUALIFIED", {
    qualification_status: decision.status,
    qualification_reason: decision.reason,
    qualification_detail: detail,
    lawyer_id: lawyerId,
  });
}
