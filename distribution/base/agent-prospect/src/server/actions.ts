"use server";

import { revalidatePath } from "next/cache";
import { redirect } from "next/navigation";
import { eq } from "drizzle-orm";
import { CampaignConfigSchema } from "../core/objective";
import { schema } from "../db/client";
import { createCampaign, pauseCampaign, startCampaign, stopCampaign } from "../engine/campaign";
import { approveDraft, editDraft, resolveReview, suppressProspect, type ReviewAction } from "../engine/review";
import { getDeps } from "./context";

const str = (f: FormData, k: string) => String(f.get(k) ?? "").trim();
const list = (f: FormData, k: string) => str(f, k).split(/[,\n]/).map((s) => s.trim()).filter(Boolean);

export async function createCampaignAction(form: FormData): Promise<void> {
  const deps = await getDeps();
  // Les valeurs viennent du formulaire confirmé, jamais directement du texte libre. L'envoi n'y figure pas.
  const config = CampaignConfigSchema.parse({
    practice_area: str(form, "practice_area"),
    subspecialties: list(form, "subspecialties"),
    location: str(form, "location"),
    client_type: str(form, "client_type"),
    target_type: str(form, "target_type"),
    goal_type: str(form, "goal_type"),
    target_count: Number(str(form, "target_count")),
    generate_audit_if: form.get("generate_audit") ? "NOT_OBSERVED_IN_SAMPLE" : "NEVER",
    generate_keywords: !!form.get("generate_keywords"),
    generate_email: !!form.get("generate_email"),
    certified_specialization_required: !!form.get("certified"),
    max_discovery_rounds: Number(str(form, "max_discovery_rounds")),
    max_candidates_per_round: Number(str(form, "max_candidates_per_round")),
    max_total_discovery_results: Number(str(form, "max_total_discovery_results")),
    max_campaign_cost_usd: Number(str(form, "max_campaign_cost_usd")),
    max_prospect_cost_usd: Number(str(form, "max_prospect_cost_usd")),
    excluded_domains: list(form, "excluded_domains"),
    send_email: false,
  });
  const c = await createCampaign(deps, { name: str(form, "name") || `${config.practice_area}, ${config.location}`, objectiveText: str(form, "objective_text") || null, config, simulation: str(form, "mode") !== "real" });
  redirect(`/campaigns/${c.id}`);
}

export async function campaignControlAction(form: FormData): Promise<void> {
  const deps = await getDeps();
  const id = str(form, "id");
  const op = str(form, "op");
  if (op === "start") await startCampaign(deps, id);
  else if (op === "pause") await pauseCampaign(deps, id);
  else if (op === "stop") await stopCampaign(deps, id);
  revalidatePath(`/campaigns/${id}`);
}

export async function reviewAction(form: FormData): Promise<void> {
  const deps = await getDeps();
  await resolveReview(deps, str(form, "id"), str(form, "action") as ReviewAction);
  revalidatePath("/review");
}

export async function editDraftAction(form: FormData): Promise<void> {
  const deps = await getDeps();
  const id = str(form, "prospect_id");
  const texts: Record<string, string> = {};
  for (const [k, v] of form.entries()) if (k.startsWith("s:")) texts[k.slice(2)] = String(v);
  await editDraft(deps, id, { subject: str(form, "subject"), texts });
  revalidatePath(`/prospects/${id}`);
}

export async function approveDraftAction(form: FormData): Promise<void> {
  const deps = await getDeps();
  const id = str(form, "prospect_id");
  await approveDraft(deps, id);
  revalidatePath(`/prospects/${id}`);
}

export async function suppressAction(form: FormData): Promise<void> {
  const deps = await getDeps();
  const id = str(form, "prospect_id");
  await suppressProspect(deps, id, str(form, "reason") || "Suppression demandée depuis le tableau de bord");
  revalidatePath(`/prospects/${id}`);
}

export async function revokeShareAction(form: FormData): Promise<void> {
  const deps = await getDeps();
  const id = str(form, "prospect_id");
  await deps.db.update(schema.audits).set({ share_revoked: true }).where(eq(schema.audits.prospect_id, id));
  revalidatePath(`/prospects/${id}`);
}

export async function forceAuditAction(form: FormData): Promise<void> {
  const deps = await getDeps();
  const id = str(form, "prospect_id");
  const { forceAudit } = await import("../engine/review");
  await forceAudit(deps, id);
  revalidatePath(`/prospects/${id}`);
}

export async function importChatgptAction(form: FormData): Promise<void> {
  const deps = await getDeps();
  const id = str(form, "campaign_id");
  const { importManualObservations } = await import("../engine/manual");
  const questions = Number(str(form, "questions"));
  const reps = Number(str(form, "reps"));
  const responses = Array.from({ length: questions }, (_, p) => Array.from({ length: reps }, (_, r) => str(form, `r:${p}:${r}`)));
  const date = str(form, "observed_at");
  await importManualObservations(deps, id, {
    responses,
    modelShown: str(form, "model") || null,
    webSearch: (["oui", "non"].includes(str(form, "web_search")) ? str(form, "web_search") : "inconnu") as "oui" | "non" | "inconnu",
    observedAt: date ? new Date(`${date}T12:00:00`) : new Date(),
  });
  redirect(`/campaigns/${id}`);
}

export async function sendEmailAction(form: FormData): Promise<void> {
  const deps = await getDeps();
  const { mailerFromEnv, sendApprovedEmail } = await import("../engine/outreach");
  const m = mailerFromEnv();
  const id = str(form, "prospect_id");
  let notice = "Email envoyé";
  if (!m) notice = "Resend n'est pas configuré";
  else await sendApprovedEmail(deps, m.mailer, m.cfg, id).catch((err) => (notice = err instanceof Error ? err.message : String(err)));
  revalidatePath("/suivi");
  redirect(`/suivi?notice=${encodeURIComponent(notice)}`);
}

export async function markReplyAction(form: FormData): Promise<void> {
  const deps = await getDeps();
  const { markReply } = await import("../engine/outreach");
  await markReply(deps, str(form, "prospect_id"), str(form, "kind") === "OPTED_OUT" ? "OPTED_OUT" : "REPLIED");
  revalidatePath("/suivi");
}

export async function syncAction(): Promise<void> {
  const deps = await getDeps();
  const { runSync } = await import("../engine/outreach");
  await runSync(deps).catch(() => null);
  revalidatePath("/suivi");
}

export async function dealStageAction(form: FormData): Promise<void> {
  const deps = await getDeps();
  const { setDealStage } = await import("../engine/missions");
  const v = str(form, "stage");
  await setDealStage(deps, str(form, "prospect_id"), (["MEETING", "PROPOSAL", "SIGNED", "LOST"].includes(v) ? v : null) as "MEETING" | "PROPOSAL" | "SIGNED" | "LOST" | null);
  revalidatePath("/suivi");
  revalidatePath("/missions");
}
