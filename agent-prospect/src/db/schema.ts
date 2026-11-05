import { sql } from "drizzle-orm";
import { boolean, date, index, integer, jsonb, numeric, pgTable, text, timestamp, uniqueIndex, uuid } from "drizzle-orm/pg-core";
import type { CampaignConfig } from "../core/objective";
import type { ProspectState } from "../core/states";

const id = () => uuid("id").primaryKey().defaultRandom();
const ts = (name: string) => timestamp(name, { withTimezone: true });
const createdAt = () => ts("created_at").notNull().defaultNow();
const usd = (name: string) => numeric(name, { precision: 12, scale: 6 });

export const campaigns = pgTable("campaigns", {
  id: id(),
  name: text("name").notNull(),
  objective_text: text("objective_text"),
  config: jsonb("config").$type<CampaignConfig>().notNull(),
  config_hash: text("config_hash").notNull(),
  goal_type: text("goal_type").notNull(),
  target_count: integer("target_count").notNull(),
  // DRAFT, RUNNING, PAUSED, STOPPED, COMPLETED, PARTIAL, BLOCKED
  status: text("status").notNull().default("DRAFT"),
  stop_reason: text("stop_reason"),
  simulation: boolean("simulation").notNull().default(false),
  discovery_rounds_done: integer("discovery_rounds_done").notNull().default(0),
  discovery_results_total: integer("discovery_results_total").notNull().default(0),
  empty_rounds: integer("empty_rounds").notNull().default(0),
  created_at: createdAt(),
  updated_at: ts("updated_at").notNull().defaultNow(),
});

export const firms = pgTable("firms", {
  id: id(),
  canonical_domain: text("canonical_domain").notNull().unique(),
  website: text("website").notNull(),
  name: text("name"),
  aliases: jsonb("aliases").$type<string[]>().notNull().default([]),
  city: text("city"),
  robots_status: text("robots_status"),
  robots_txt: text("robots_txt"),
  sitemap_urls: jsonb("sitemap_urls").$type<string[]>().notNull().default([]),
  crawl_blocked_reason: text("crawl_blocked_reason"),
  created_at: createdAt(),
});

export const lawyers = pgTable(
  "lawyers",
  {
    id: id(),
    firm_id: uuid("firm_id").notNull().references(() => firms.id),
    first_name: text("first_name").notNull(),
    last_name: text("last_name").notNull(),
    normalized_name: text("normalized_name").notNull(),
    // NOT_VERIFIED, CLAIMED_ON_SITE, VERIFIED. Une page sur un sujet ne vaut jamais VERIFIED.
    certified_specialization_status: text("certified_specialization_status").notNull().default("NOT_VERIFIED"),
    source_url: text("source_url"),
    created_at: createdAt(),
  },
  (t) => [uniqueIndex("lawyers_firm_name_uq").on(t.firm_id, t.normalized_name)],
);

export const discovery_queries = pgTable("discovery_queries", {
  id: id(),
  campaign_id: uuid("campaign_id").notNull().references(() => campaigns.id),
  round: integer("round").notNull(),
  family: text("family").notNull(),
  query: text("query").notNull(),
  provider: text("provider").notNull(),
  rule_version: text("rule_version").notNull(),
  results_count: integer("results_count").notNull().default(0),
  new_candidates: integer("new_candidates").notNull().default(0),
  duplicates: integer("duplicates").notNull().default(0),
  error: jsonb("error"),
  created_at: createdAt(),
}, (t) => [uniqueIndex("discovery_round_uq").on(t.campaign_id, t.round)]);

export const prospects = pgTable(
  "prospects",
  {
    id: id(),
    campaign_id: uuid("campaign_id").notNull().references(() => campaigns.id),
    firm_id: uuid("firm_id").notNull().references(() => firms.id),
    lawyer_id: uuid("lawyer_id").references(() => lawyers.id),
    candidate_name: text("candidate_name"),
    source_url: text("source_url"),
    discovery_query_id: uuid("discovery_query_id").references(() => discovery_queries.id),
    state: text("state").$type<ProspectState>().notNull().default("DISCOVERED"),
    resume_state: text("resume_state").$type<ProspectState>(),
    qualification_status: text("qualification_status").notNull().default("PENDING"),
    qualification_reason: text("qualification_reason"),
    qualification_detail: text("qualification_detail"),
    email_status: text("email_status"), // FOUND, NO_PUBLIC_EMAIL
    visibility_verdict: text("visibility_verdict"),
    visibility_summary: jsonb("visibility_summary"),
    benchmark_id: uuid("benchmark_id"),
    keyword_status: text("keyword_status"), // COMPLETE, INSUFFICIENT_EVIDENCE
    keyword_count: integer("keyword_count"),
    // L'envoi par Resend reste bloqué tant qu'aucune permission documentée n'existe.
    send_eligibility: text("send_eligibility").notNull().default("PROVIDER_BLOCKED"),
    force_audit: boolean("force_audit").notNull().default(false),
    review_reason: text("review_reason"),
    last_error: jsonb("last_error"),
    created_at: createdAt(),
    updated_at: ts("updated_at").notNull().defaultNow(),
  },
  // Un cabinet = un prospect par campagne : plusieurs avocats d'un même cabinet ne créent pas plusieurs sollicitations.
  (t) => [uniqueIndex("prospects_campaign_firm_uq").on(t.campaign_id, t.firm_id), index("prospects_state_idx").on(t.campaign_id, t.state)],
);

export const site_pages = pgTable(
  "site_pages",
  {
    id: id(),
    firm_id: uuid("firm_id").notNull().references(() => firms.id),
    url: text("url").notNull(),
    final_url: text("final_url"),
    status: integer("status"),
    error_category: text("error_category"),
    redirect_chain: jsonb("redirect_chain").$type<string[]>().notNull().default([]),
    title: text("title"),
    h1s: jsonb("h1s").$type<string[]>().notNull().default([]),
    canonical: text("canonical"),
    meta_robots: text("meta_robots"),
    x_robots: text("x_robots"),
    text: text("text"),
    links: jsonb("links").$type<{ href: string; anchor: string }[]>().notNull().default([]),
    mailtos: jsonb("mailtos").$type<{ email: string; context: string }[]>().notNull().default([]),
    json_ld_types: jsonb("json_ld_types").$type<string[]>().notNull().default([]),
    in_sitemap: boolean("in_sitemap"),
    fetched_at: ts("fetched_at").notNull().defaultNow(),
  },
  (t) => [uniqueIndex("site_pages_firm_url_uq").on(t.firm_id, t.url)],
);

export const evidence = pgTable(
  "evidence",
  {
    id: id(),
    prospect_id: uuid("prospect_id").notNull().references(() => prospects.id),
    // IDENTITY, FIRM_NAME, LOCATION, PRACTICE_AREA, CLIENT_TYPE, SERVICE, CERTIFICATION_CLAIM, ACTIVITY
    kind: text("kind").notNull(),
    value: text("value").notNull(),
    source_url: text("source_url").notNull(),
    excerpt: text("excerpt").notNull(),
    extraction_method: text("extraction_method").notNull(),
    // OBSERVED (extrait retrouvé mot pour mot dans la page), INFERRED, PROPOSED
    verification_status: text("verification_status").notNull(),
    observed_at: ts("observed_at").notNull().defaultNow(),
  },
  (t) => [index("evidence_prospect_idx").on(t.prospect_id)],
);

export const contacts = pgTable(
  "contacts",
  {
    id: id(),
    firm_id: uuid("firm_id").notNull().references(() => firms.id),
    email: text("email").notNull(),
    source_url: text("source_url").notNull(),
    source_type: text("source_type").notNull(),
    context: text("context").notNull(),
    excluded_reason: text("excluded_reason"),
    publicly_published: boolean("publicly_published").notNull().default(true),
    syntax_valid: boolean("syntax_valid").notNull(),
    domain_routable: boolean("domain_routable"), // null = non contrôlé
    // Aucun contrôle ne prouve l'existence de la boîte : toujours false ici.
    mailbox_verified: boolean("mailbox_verified").notNull().default(false),
    selected: boolean("selected").notNull().default(false),
    observed_at: ts("observed_at").notNull().defaultNow(),
  },
  (t) => [uniqueIndex("contacts_firm_email_uq").on(t.firm_id, t.email)],
);

export const visibility_benchmarks = pgTable(
  "visibility_benchmarks",
  {
    id: id(),
    campaign_id: uuid("campaign_id").notNull().references(() => campaigns.id),
    config_hash: text("config_hash").notNull(),
    segment: jsonb("segment").notNull(),
    provider: text("provider").notNull(),
    model: text("model").notNull(),
    params: jsonb("params").notNull(),
    prompt_version: text("prompt_version").notNull(),
    prompts: jsonb("prompts").$type<string[]>().notNull(),
    repetitions: integer("repetitions").notNull(),
    expected_valid_runs: integer("expected_valid_runs").notNull(),
    valid_runs: integer("valid_runs").notNull().default(0),
    status: text("status").notNull().default("RUNNING"), // RUNNING, COMPLETE, INCOMPLETE
    started_at: ts("started_at").notNull().defaultNow(),
    finished_at: ts("finished_at"),
  },
  (t) => [uniqueIndex("benchmarks_campaign_hash_uq").on(t.campaign_id, t.config_hash)],
);

export const visibility_runs = pgTable(
  "visibility_runs",
  {
    id: id(),
    benchmark_id: uuid("benchmark_id").notNull().references(() => visibility_benchmarks.id),
    prompt_index: integer("prompt_index").notNull(),
    repetition: integer("repetition").notNull(),
    attempt: integer("attempt").notNull(),
    prompt: text("prompt").notNull(),
    response_text: text("response_text"),
    citations: jsonb("citations").$type<{ url: string; title?: string }[]>().notNull().default([]),
    web_search_used: boolean("web_search_used"),
    model: text("model"),
    provider_response_id: text("provider_response_id"),
    usage: jsonb("usage"),
    validity: text("validity").notNull(),
    validity_note: text("validity_note"),
    error: jsonb("error"),
    created_at: createdAt(),
  },
  (t) => [uniqueIndex("runs_slot_uq").on(t.benchmark_id, t.prompt_index, t.repetition, t.attempt)],
);

export const entity_observations = pgTable(
  "entity_observations",
  {
    id: id(),
    prospect_id: uuid("prospect_id").notNull().references(() => prospects.id),
    run_id: uuid("run_id").notNull().references(() => visibility_runs.id),
    type: text("type").notNull(),
    detail: text("detail").notNull().default(""),
  },
  (t) => [uniqueIndex("observations_uq").on(t.prospect_id, t.run_id, t.type)],
);

export const audits = pgTable("audits", {
  id: id(),
  prospect_id: uuid("prospect_id").notNull().unique().references(() => prospects.id),
  pages_analyzed: integer("pages_analyzed").notNull(),
  findings: jsonb("findings").notNull(),
  report: jsonb("report").notNull(),
  report_md: text("report_md").notNull(),
  report_html: text("report_html").notNull(),
  share_token: text("share_token").notNull().unique(),
  share_expires_at: ts("share_expires_at").notNull(),
  share_revoked: boolean("share_revoked").notNull().default(false),
  created_at: createdAt(),
});

export const keywords = pgTable(
  "keywords",
  {
    id: id(),
    prospect_id: uuid("prospect_id").notNull().references(() => prospects.id),
    round: integer("round").notNull(),
    normalized: text("normalized").notNull(),
    keyword: text("keyword").notNull(),
    cluster: text("cluster").notNull(),
    search_intent: text("search_intent").notNull(),
    client_type: text("client_type").notNull(),
    relevant_service: text("relevant_service").notNull(),
    service_evidence_id: uuid("service_evidence_id").notNull().references(() => evidence.id),
    geography: text("geography"),
    existing_page_url: text("existing_page_url"),
    recommended_page_type: text("recommended_page_type").notNull(),
    business_rationale: text("business_rationale").notNull(),
    recommendation_status: text("recommendation_status").notNull(),
    offer_proximity_score: integer("offer_proximity_score").notNull(),
    business_intent_score: integer("business_intent_score").notNull(),
    // Sans donnée obtenue et sourcée, ces colonnes restent vides.
    feasibility_score: integer("feasibility_score"),
    search_volume: integer("search_volume"),
    cpc: numeric("cpc"),
    keyword_difficulty: integer("keyword_difficulty"),
    position: integer("position"),
    scoring_version: text("scoring_version").notNull(),
  },
  (t) => [uniqueIndex("keywords_prospect_norm_uq").on(t.prospect_id, t.normalized)],
);

/** Vérification d'une requête retenue : elle est posée telle quelle à l'IA, et le code relève si le cabinet figure dans la réponse. */
export const keyword_checks = pgTable(
  "keyword_checks",
  {
    id: id(),
    prospect_id: uuid("prospect_id").notNull().references(() => prospects.id),
    keyword: text("keyword").notNull(),
    provider: text("provider").notNull(),
    model: text("model").notNull(),
    response_text: text("response_text"),
    citations: jsonb("citations").$type<{ url: string; title?: string }[]>().notNull().default([]),
    // CITED (site cité ou cabinet nommé), NOT_CITED, UNVERIFIED (réponse invalide, erreur ou correspondance ambiguë : aucune affirmation possible)
    result: text("result").notNull(),
    detail: text("detail").notNull().default(""),
    checked_at: ts("checked_at").notNull().defaultNow(),
  },
  (t) => [uniqueIndex("keyword_checks_uq").on(t.prospect_id, t.keyword, t.provider)],
);

export const email_drafts = pgTable("email_drafts", {
  id: id(),
  prospect_id: uuid("prospect_id").notNull().unique().references(() => prospects.id),
  recipient: text("recipient"),
  subject: text("subject").notNull(),
  sentences: jsonb("sentences").notNull(),
  body: text("body").notNull(),
  word_count: integer("word_count").notNull(),
  fact_check: jsonb("fact_check"),
  facts: jsonb("facts").notNull(),
  claim_context: jsonb("claim_context").notNull(),
  rewrite_rounds: integer("rewrite_rounds").notNull().default(0),
  // Motifs qui interdisent l'approbation tant qu'ils existent.
  blockers: jsonb("blockers").$type<string[]>().notNull().default([]),
  content_hash: text("content_hash").notNull(),
  prompt_version: text("prompt_version").notNull(),
  edited_by_human: boolean("edited_by_human").notNull().default(false),
  updated_at: ts("updated_at").notNull().defaultNow(),
});

export const approvals = pgTable("approvals", {
  id: id(),
  draft_id: uuid("draft_id").notNull().references(() => email_drafts.id),
  content_hash: text("content_hash").notNull(),
  recipient: text("recipient"),
  approved_at: ts("approved_at").notNull().defaultNow(),
  invalidated_at: ts("invalidated_at"),
  invalidated_reason: text("invalidated_reason"),
});

export const review_items = pgTable(
  "review_items",
  {
    id: id(),
    campaign_id: uuid("campaign_id").notNull().references(() => campaigns.id),
    prospect_id: uuid("prospect_id").notNull().references(() => prospects.id),
    reason: text("reason").notNull(),
    detail: text("detail").notNull(),
    status: text("status").notNull().default("OPEN"),
    resolution: text("resolution"), // APPROVE, REJECT, RETRY, EDIT
    created_at: createdAt(),
    resolved_at: ts("resolved_at"),
  },
  (t) => [index("review_open_idx").on(t.status)],
);

export const budget_ledger = pgTable(
  "budget_ledger",
  {
    id: id(),
    campaign_id: uuid("campaign_id").notNull().references(() => campaigns.id),
    prospect_id: uuid("prospect_id"),
    benchmark_id: uuid("benchmark_id"),
    step: text("step").notNull(),
    model: text("model").notNull(),
    estimated_usd: usd("estimated_usd").notNull(),
    actual_usd: usd("actual_usd"),
    usage: jsonb("usage"),
    // RESERVED, RECONCILED (coût recalculé depuis l'usage rapporté), UNCONFIRMED (issue inconnue : la réservation est conservée), RELEASED (appel jamais parti)
    status: text("status").notNull(),
    day: date("day").notNull().default(sql`current_date`),
    created_at: createdAt(),
  },
  (t) => [index("ledger_campaign_idx").on(t.campaign_id), index("ledger_day_idx").on(t.day)],
);

export const step_runs = pgTable(
  "step_runs",
  {
    id: id(),
    campaign_id: uuid("campaign_id").notNull().references(() => campaigns.id),
    prospect_id: uuid("prospect_id").notNull().references(() => prospects.id),
    step: text("step").notNull(),
    config_hash: text("config_hash").notNull(),
    status: text("status").notNull(), // RUNNING, DONE, FAILED
    attempts: integer("attempts").notNull().default(0),
    error: jsonb("error"),
    started_at: ts("started_at").notNull().defaultNow(),
    finished_at: ts("finished_at"),
  },
  // Identité logique d'une étape : la relancer ne crée pas un second résultat.
  (t) => [uniqueIndex("step_runs_uq").on(t.prospect_id, t.step, t.config_hash)],
);

export const suppressions = pgTable("suppressions", {
  id: id(),
  // email normalisé ou domaine : le minimum pour honorer une opposition.
  value: text("value").notNull().unique(),
  kind: text("kind").notNull(), // EMAIL, DOMAIN
  reason: text("reason").notNull(),
  created_at: createdAt(),
});

export const event_log = pgTable(
  "event_log",
  {
    id: id(),
    campaign_id: uuid("campaign_id"),
    prospect_id: uuid("prospect_id"),
    type: text("type").notNull(),
    data: jsonb("data"),
    created_at: createdAt(),
  },
  (t) => [index("event_campaign_idx").on(t.campaign_id, t.created_at)],
);
