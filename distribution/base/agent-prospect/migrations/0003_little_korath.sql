CREATE TABLE "missions" (
	"id" uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL,
	"day" date NOT NULL,
	"target_sends" integer NOT NULL,
	"sent" integer DEFAULT 0 NOT NULL,
	"campaign_ids" jsonb DEFAULT '[]'::jsonb NOT NULL,
	"log" jsonb DEFAULT '[]'::jsonb NOT NULL,
	"last_send_at" timestamp with time zone,
	"last_pipeline_at" timestamp with time zone,
	"report_sent_at" timestamp with time zone,
	"created_at" timestamp with time zone DEFAULT now() NOT NULL,
	CONSTRAINT "missions_day_unique" UNIQUE("day")
);
--> statement-breakpoint
ALTER TABLE "outreach" ADD COLUMN "deal_stage" text;--> statement-breakpoint
ALTER TABLE "outreach" ADD COLUMN "deal_updated_at" timestamp with time zone;