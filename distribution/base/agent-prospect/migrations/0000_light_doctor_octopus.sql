CREATE TABLE "approvals" (
	"id" uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL,
	"draft_id" uuid NOT NULL,
	"content_hash" text NOT NULL,
	"recipient" text,
	"approved_at" timestamp with time zone DEFAULT now() NOT NULL,
	"invalidated_at" timestamp with time zone,
	"invalidated_reason" text
);
--> statement-breakpoint
CREATE TABLE "audits" (
	"id" uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL,
	"prospect_id" uuid NOT NULL,
	"pages_analyzed" integer NOT NULL,
	"findings" jsonb NOT NULL,
	"report" jsonb NOT NULL,
	"report_md" text NOT NULL,
	"report_html" text NOT NULL,
	"share_token" text NOT NULL,
	"share_expires_at" timestamp with time zone NOT NULL,
	"share_revoked" boolean DEFAULT false NOT NULL,
	"created_at" timestamp with time zone DEFAULT now() NOT NULL,
	CONSTRAINT "audits_prospect_id_unique" UNIQUE("prospect_id"),
	CONSTRAINT "audits_share_token_unique" UNIQUE("share_token")
);
--> statement-breakpoint
CREATE TABLE "budget_ledger" (
	"id" uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL,
	"campaign_id" uuid NOT NULL,
	"prospect_id" uuid,
	"benchmark_id" uuid,
	"step" text NOT NULL,
	"model" text NOT NULL,
	"estimated_usd" numeric(12, 6) NOT NULL,
	"actual_usd" numeric(12, 6),
	"usage" jsonb,
	"status" text NOT NULL,
	"day" date DEFAULT current_date NOT NULL,
	"created_at" timestamp with time zone DEFAULT now() NOT NULL
);
--> statement-breakpoint
CREATE TABLE "campaigns" (
	"id" uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL,
	"name" text NOT NULL,
	"objective_text" text,
	"config" jsonb NOT NULL,
	"config_hash" text NOT NULL,
	"goal_type" text NOT NULL,
	"target_count" integer NOT NULL,
	"status" text DEFAULT 'DRAFT' NOT NULL,
	"stop_reason" text,
	"simulation" boolean DEFAULT false NOT NULL,
	"discovery_rounds_done" integer DEFAULT 0 NOT NULL,
	"discovery_results_total" integer DEFAULT 0 NOT NULL,
	"empty_rounds" integer DEFAULT 0 NOT NULL,
	"created_at" timestamp with time zone DEFAULT now() NOT NULL,
	"updated_at" timestamp with time zone DEFAULT now() NOT NULL
);
--> statement-breakpoint
CREATE TABLE "contacts" (
	"id" uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL,
	"firm_id" uuid NOT NULL,
	"email" text NOT NULL,
	"source_url" text NOT NULL,
	"source_type" text NOT NULL,
	"context" text NOT NULL,
	"excluded_reason" text,
	"publicly_published" boolean DEFAULT true NOT NULL,
	"syntax_valid" boolean NOT NULL,
	"domain_routable" boolean,
	"mailbox_verified" boolean DEFAULT false NOT NULL,
	"selected" boolean DEFAULT false NOT NULL,
	"observed_at" timestamp with time zone DEFAULT now() NOT NULL
);
--> statement-breakpoint
CREATE TABLE "discovery_queries" (
	"id" uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL,
	"campaign_id" uuid NOT NULL,
	"round" integer NOT NULL,
	"family" text NOT NULL,
	"query" text NOT NULL,
	"provider" text NOT NULL,
	"rule_version" text NOT NULL,
	"results_count" integer DEFAULT 0 NOT NULL,
	"new_candidates" integer DEFAULT 0 NOT NULL,
	"duplicates" integer DEFAULT 0 NOT NULL,
	"error" jsonb,
	"created_at" timestamp with time zone DEFAULT now() NOT NULL
);
--> statement-breakpoint
CREATE TABLE "email_drafts" (
	"id" uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL,
	"prospect_id" uuid NOT NULL,
	"recipient" text,
	"subject" text NOT NULL,
	"sentences" jsonb NOT NULL,
	"body" text NOT NULL,
	"word_count" integer NOT NULL,
	"fact_check" jsonb,
	"facts" jsonb NOT NULL,
	"claim_context" jsonb NOT NULL,
	"rewrite_rounds" integer DEFAULT 0 NOT NULL,
	"blockers" jsonb DEFAULT '[]'::jsonb NOT NULL,
	"content_hash" text NOT NULL,
	"prompt_version" text NOT NULL,
	"edited_by_human" boolean DEFAULT false NOT NULL,
	"updated_at" timestamp with time zone DEFAULT now() NOT NULL,
	CONSTRAINT "email_drafts_prospect_id_unique" UNIQUE("prospect_id")
);
--> statement-breakpoint
CREATE TABLE "entity_observations" (
	"id" uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL,
	"prospect_id" uuid NOT NULL,
	"run_id" uuid NOT NULL,
	"type" text NOT NULL,
	"detail" text DEFAULT '' NOT NULL
);
--> statement-breakpoint
CREATE TABLE "event_log" (
	"id" uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL,
	"campaign_id" uuid,
	"prospect_id" uuid,
	"type" text NOT NULL,
	"data" jsonb,
	"created_at" timestamp with time zone DEFAULT now() NOT NULL
);
--> statement-breakpoint
CREATE TABLE "evidence" (
	"id" uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL,
	"prospect_id" uuid NOT NULL,
	"kind" text NOT NULL,
	"value" text NOT NULL,
	"source_url" text NOT NULL,
	"excerpt" text NOT NULL,
	"extraction_method" text NOT NULL,
	"verification_status" text NOT NULL,
	"observed_at" timestamp with time zone DEFAULT now() NOT NULL
);
--> statement-breakpoint
CREATE TABLE "firms" (
	"id" uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL,
	"canonical_domain" text NOT NULL,
	"website" text NOT NULL,
	"name" text,
	"aliases" jsonb DEFAULT '[]'::jsonb NOT NULL,
	"city" text,
	"robots_status" text,
	"robots_txt" text,
	"sitemap_urls" jsonb DEFAULT '[]'::jsonb NOT NULL,
	"crawl_blocked_reason" text,
	"created_at" timestamp with time zone DEFAULT now() NOT NULL,
	CONSTRAINT "firms_canonical_domain_unique" UNIQUE("canonical_domain")
);
--> statement-breakpoint
CREATE TABLE "keywords" (
	"id" uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL,
	"prospect_id" uuid NOT NULL,
	"round" integer NOT NULL,
	"normalized" text NOT NULL,
	"keyword" text NOT NULL,
	"cluster" text NOT NULL,
	"search_intent" text NOT NULL,
	"client_type" text NOT NULL,
	"relevant_service" text NOT NULL,
	"service_evidence_id" uuid NOT NULL,
	"geography" text,
	"existing_page_url" text,
	"recommended_page_type" text NOT NULL,
	"business_rationale" text NOT NULL,
	"recommendation_status" text NOT NULL,
	"offer_proximity_score" integer NOT NULL,
	"business_intent_score" integer NOT NULL,
	"feasibility_score" integer,
	"search_volume" integer,
	"cpc" numeric,
	"keyword_difficulty" integer,
	"position" integer,
	"scoring_version" text NOT NULL
);
--> statement-breakpoint
CREATE TABLE "lawyers" (
	"id" uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL,
	"firm_id" uuid NOT NULL,
	"first_name" text NOT NULL,
	"last_name" text NOT NULL,
	"normalized_name" text NOT NULL,
	"certified_specialization_status" text DEFAULT 'NOT_VERIFIED' NOT NULL,
	"source_url" text,
	"created_at" timestamp with time zone DEFAULT now() NOT NULL
);
--> statement-breakpoint
CREATE TABLE "prospects" (
	"id" uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL,
	"campaign_id" uuid NOT NULL,
	"firm_id" uuid NOT NULL,
	"lawyer_id" uuid,
	"candidate_name" text,
	"source_url" text,
	"discovery_query_id" uuid,
	"state" text DEFAULT 'DISCOVERED' NOT NULL,
	"resume_state" text,
	"qualification_status" text DEFAULT 'PENDING' NOT NULL,
	"qualification_reason" text,
	"qualification_detail" text,
	"email_status" text,
	"visibility_verdict" text,
	"visibility_summary" jsonb,
	"benchmark_id" uuid,
	"keyword_status" text,
	"keyword_count" integer,
	"send_eligibility" text DEFAULT 'PROVIDER_BLOCKED' NOT NULL,
	"force_audit" boolean DEFAULT false NOT NULL,
	"review_reason" text,
	"last_error" jsonb,
	"created_at" timestamp with time zone DEFAULT now() NOT NULL,
	"updated_at" timestamp with time zone DEFAULT now() NOT NULL
);
--> statement-breakpoint
CREATE TABLE "review_items" (
	"id" uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL,
	"campaign_id" uuid NOT NULL,
	"prospect_id" uuid NOT NULL,
	"reason" text NOT NULL,
	"detail" text NOT NULL,
	"status" text DEFAULT 'OPEN' NOT NULL,
	"resolution" text,
	"created_at" timestamp with time zone DEFAULT now() NOT NULL,
	"resolved_at" timestamp with time zone
);
--> statement-breakpoint
CREATE TABLE "site_pages" (
	"id" uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL,
	"firm_id" uuid NOT NULL,
	"url" text NOT NULL,
	"final_url" text,
	"status" integer,
	"error_category" text,
	"redirect_chain" jsonb DEFAULT '[]'::jsonb NOT NULL,
	"title" text,
	"h1s" jsonb DEFAULT '[]'::jsonb NOT NULL,
	"canonical" text,
	"meta_robots" text,
	"x_robots" text,
	"text" text,
	"links" jsonb DEFAULT '[]'::jsonb NOT NULL,
	"mailtos" jsonb DEFAULT '[]'::jsonb NOT NULL,
	"json_ld_types" jsonb DEFAULT '[]'::jsonb NOT NULL,
	"in_sitemap" boolean,
	"fetched_at" timestamp with time zone DEFAULT now() NOT NULL
);
--> statement-breakpoint
CREATE TABLE "step_runs" (
	"id" uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL,
	"campaign_id" uuid NOT NULL,
	"prospect_id" uuid NOT NULL,
	"step" text NOT NULL,
	"config_hash" text NOT NULL,
	"status" text NOT NULL,
	"attempts" integer DEFAULT 0 NOT NULL,
	"error" jsonb,
	"started_at" timestamp with time zone DEFAULT now() NOT NULL,
	"finished_at" timestamp with time zone
);
--> statement-breakpoint
CREATE TABLE "suppressions" (
	"id" uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL,
	"value" text NOT NULL,
	"kind" text NOT NULL,
	"reason" text NOT NULL,
	"created_at" timestamp with time zone DEFAULT now() NOT NULL,
	CONSTRAINT "suppressions_value_unique" UNIQUE("value")
);
--> statement-breakpoint
CREATE TABLE "visibility_benchmarks" (
	"id" uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL,
	"campaign_id" uuid NOT NULL,
	"config_hash" text NOT NULL,
	"segment" jsonb NOT NULL,
	"provider" text NOT NULL,
	"model" text NOT NULL,
	"params" jsonb NOT NULL,
	"prompt_version" text NOT NULL,
	"prompts" jsonb NOT NULL,
	"repetitions" integer NOT NULL,
	"expected_valid_runs" integer NOT NULL,
	"valid_runs" integer DEFAULT 0 NOT NULL,
	"status" text DEFAULT 'RUNNING' NOT NULL,
	"started_at" timestamp with time zone DEFAULT now() NOT NULL,
	"finished_at" timestamp with time zone
);
--> statement-breakpoint
CREATE TABLE "visibility_runs" (
	"id" uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL,
	"benchmark_id" uuid NOT NULL,
	"prompt_index" integer NOT NULL,
	"repetition" integer NOT NULL,
	"attempt" integer NOT NULL,
	"prompt" text NOT NULL,
	"response_text" text,
	"citations" jsonb DEFAULT '[]'::jsonb NOT NULL,
	"web_search_used" boolean,
	"model" text,
	"provider_response_id" text,
	"usage" jsonb,
	"validity" text NOT NULL,
	"validity_note" text,
	"error" jsonb,
	"created_at" timestamp with time zone DEFAULT now() NOT NULL
);
--> statement-breakpoint
ALTER TABLE "approvals" ADD CONSTRAINT "approvals_draft_id_email_drafts_id_fk" FOREIGN KEY ("draft_id") REFERENCES "public"."email_drafts"("id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "audits" ADD CONSTRAINT "audits_prospect_id_prospects_id_fk" FOREIGN KEY ("prospect_id") REFERENCES "public"."prospects"("id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "budget_ledger" ADD CONSTRAINT "budget_ledger_campaign_id_campaigns_id_fk" FOREIGN KEY ("campaign_id") REFERENCES "public"."campaigns"("id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "contacts" ADD CONSTRAINT "contacts_firm_id_firms_id_fk" FOREIGN KEY ("firm_id") REFERENCES "public"."firms"("id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "discovery_queries" ADD CONSTRAINT "discovery_queries_campaign_id_campaigns_id_fk" FOREIGN KEY ("campaign_id") REFERENCES "public"."campaigns"("id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "email_drafts" ADD CONSTRAINT "email_drafts_prospect_id_prospects_id_fk" FOREIGN KEY ("prospect_id") REFERENCES "public"."prospects"("id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "entity_observations" ADD CONSTRAINT "entity_observations_prospect_id_prospects_id_fk" FOREIGN KEY ("prospect_id") REFERENCES "public"."prospects"("id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "entity_observations" ADD CONSTRAINT "entity_observations_run_id_visibility_runs_id_fk" FOREIGN KEY ("run_id") REFERENCES "public"."visibility_runs"("id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "evidence" ADD CONSTRAINT "evidence_prospect_id_prospects_id_fk" FOREIGN KEY ("prospect_id") REFERENCES "public"."prospects"("id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "keywords" ADD CONSTRAINT "keywords_prospect_id_prospects_id_fk" FOREIGN KEY ("prospect_id") REFERENCES "public"."prospects"("id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "keywords" ADD CONSTRAINT "keywords_service_evidence_id_evidence_id_fk" FOREIGN KEY ("service_evidence_id") REFERENCES "public"."evidence"("id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "lawyers" ADD CONSTRAINT "lawyers_firm_id_firms_id_fk" FOREIGN KEY ("firm_id") REFERENCES "public"."firms"("id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "prospects" ADD CONSTRAINT "prospects_campaign_id_campaigns_id_fk" FOREIGN KEY ("campaign_id") REFERENCES "public"."campaigns"("id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "prospects" ADD CONSTRAINT "prospects_firm_id_firms_id_fk" FOREIGN KEY ("firm_id") REFERENCES "public"."firms"("id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "prospects" ADD CONSTRAINT "prospects_lawyer_id_lawyers_id_fk" FOREIGN KEY ("lawyer_id") REFERENCES "public"."lawyers"("id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "prospects" ADD CONSTRAINT "prospects_discovery_query_id_discovery_queries_id_fk" FOREIGN KEY ("discovery_query_id") REFERENCES "public"."discovery_queries"("id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "review_items" ADD CONSTRAINT "review_items_campaign_id_campaigns_id_fk" FOREIGN KEY ("campaign_id") REFERENCES "public"."campaigns"("id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "review_items" ADD CONSTRAINT "review_items_prospect_id_prospects_id_fk" FOREIGN KEY ("prospect_id") REFERENCES "public"."prospects"("id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "site_pages" ADD CONSTRAINT "site_pages_firm_id_firms_id_fk" FOREIGN KEY ("firm_id") REFERENCES "public"."firms"("id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "step_runs" ADD CONSTRAINT "step_runs_campaign_id_campaigns_id_fk" FOREIGN KEY ("campaign_id") REFERENCES "public"."campaigns"("id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "step_runs" ADD CONSTRAINT "step_runs_prospect_id_prospects_id_fk" FOREIGN KEY ("prospect_id") REFERENCES "public"."prospects"("id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "visibility_benchmarks" ADD CONSTRAINT "visibility_benchmarks_campaign_id_campaigns_id_fk" FOREIGN KEY ("campaign_id") REFERENCES "public"."campaigns"("id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "visibility_runs" ADD CONSTRAINT "visibility_runs_benchmark_id_visibility_benchmarks_id_fk" FOREIGN KEY ("benchmark_id") REFERENCES "public"."visibility_benchmarks"("id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
CREATE INDEX "ledger_campaign_idx" ON "budget_ledger" USING btree ("campaign_id");--> statement-breakpoint
CREATE INDEX "ledger_day_idx" ON "budget_ledger" USING btree ("day");--> statement-breakpoint
CREATE UNIQUE INDEX "contacts_firm_email_uq" ON "contacts" USING btree ("firm_id","email");--> statement-breakpoint
CREATE UNIQUE INDEX "discovery_round_uq" ON "discovery_queries" USING btree ("campaign_id","round");--> statement-breakpoint
CREATE UNIQUE INDEX "observations_uq" ON "entity_observations" USING btree ("prospect_id","run_id","type");--> statement-breakpoint
CREATE INDEX "event_campaign_idx" ON "event_log" USING btree ("campaign_id","created_at");--> statement-breakpoint
CREATE INDEX "evidence_prospect_idx" ON "evidence" USING btree ("prospect_id");--> statement-breakpoint
CREATE UNIQUE INDEX "keywords_prospect_norm_uq" ON "keywords" USING btree ("prospect_id","normalized");--> statement-breakpoint
CREATE UNIQUE INDEX "lawyers_firm_name_uq" ON "lawyers" USING btree ("firm_id","normalized_name");--> statement-breakpoint
CREATE UNIQUE INDEX "prospects_campaign_firm_uq" ON "prospects" USING btree ("campaign_id","firm_id");--> statement-breakpoint
CREATE INDEX "prospects_state_idx" ON "prospects" USING btree ("campaign_id","state");--> statement-breakpoint
CREATE INDEX "review_open_idx" ON "review_items" USING btree ("status");--> statement-breakpoint
CREATE UNIQUE INDEX "site_pages_firm_url_uq" ON "site_pages" USING btree ("firm_id","url");--> statement-breakpoint
CREATE UNIQUE INDEX "step_runs_uq" ON "step_runs" USING btree ("prospect_id","step","config_hash");--> statement-breakpoint
CREATE UNIQUE INDEX "benchmarks_campaign_hash_uq" ON "visibility_benchmarks" USING btree ("campaign_id","config_hash");--> statement-breakpoint
CREATE UNIQUE INDEX "runs_slot_uq" ON "visibility_runs" USING btree ("benchmark_id","prompt_index","repetition","attempt");