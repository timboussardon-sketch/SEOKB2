CREATE TABLE "keyword_checks" (
	"id" uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL,
	"prospect_id" uuid NOT NULL,
	"keyword" text NOT NULL,
	"provider" text NOT NULL,
	"model" text NOT NULL,
	"response_text" text,
	"citations" jsonb DEFAULT '[]'::jsonb NOT NULL,
	"result" text NOT NULL,
	"detail" text DEFAULT '' NOT NULL,
	"checked_at" timestamp with time zone DEFAULT now() NOT NULL
);
--> statement-breakpoint
ALTER TABLE "keyword_checks" ADD CONSTRAINT "keyword_checks_prospect_id_prospects_id_fk" FOREIGN KEY ("prospect_id") REFERENCES "public"."prospects"("id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
CREATE UNIQUE INDEX "keyword_checks_uq" ON "keyword_checks" USING btree ("prospect_id","keyword","provider");