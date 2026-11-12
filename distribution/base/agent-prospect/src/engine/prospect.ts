import { eq, sql } from "drizzle-orm";
import { schema } from "../db/client";
import { classify, POLICIES } from "../core/errors";
import { RUNNING_STATE, STEP_FOR_STATE, type ProspectState, type Step } from "../core/states";
import { stableHash } from "../core/text";
import type { Campaign, Deps, Firm, Prospect, Runtime } from "./deps";
import { logEvent } from "./events";
import { auditStep } from "./steps/audit";
import { draftStep, factcheckStep } from "./steps/draft";
import { enrichStep } from "./steps/enrich";
import { keywordsStep } from "./steps/keywords";
import { qualifyStep } from "./steps/qualify";
import { visibilityStep } from "./steps/visibility";
import { sendToReview, setState } from "./transitions";

const STEPS: Record<Step, (deps: Deps, rt: Runtime, c: Campaign, p: Prospect, f: Firm) => Promise<void>> = {
  qualify: qualifyStep,
  enrich: enrichStep,
  visibility: visibilityStep,
  audit: auditStep,
  keywords: keywordsStep,
  draft: draftStep,
  factcheck: factcheckStep,
};

/** Prochaine étape que l'agent doit mener seul, ou null si le prospect est au repos, en revue ou terminé. */
export function nextStep(p: Pick<Prospect, "state" | "force_audit">, config: Campaign["config"]): Step | null {
  const step = STEP_FOR_STATE[p.state];
  if (!step) return null;
  if (p.state === "VISIBILITY_DONE" && config.generate_audit_if === "NEVER" && !p.force_audit) return null;
  if (p.state === "AUDIT_DONE" && !config.generate_keywords) return config.generate_email ? "draft" : null;
  if (p.state === "KEYWORDS_DONE" && !config.generate_email) return null;
  return step;
}

const before = (state: ProspectState, step: Step): ProspectState => (state === RUNNING_STATE[step] ? (Object.entries(STEP_FOR_STATE).find(([s, st]) => st === step && s !== state)![0] as ProspectState) : state);

/**
 * Fait avancer un prospect d'étape en étape jusqu'à un état de repos. Chaque étape persiste son résultat :
 * après un arrêt brutal, le job est rejoué et reprend à l'état enregistré, sans refaire ce qui est fait.
 */
export async function advanceProspect(deps: Deps, prospectId: string): Promise<"done" | "busy"> {
  // Un seul worker à la fois par prospect : un job doublé ne refait pas le travail en parallèle.
  // "busy" : un autre process tient le prospect (ou vient de s'arrêter) ; l'appelant doit réessayer plus tard.
  const release = await deps.tryLock(`prospect:${prospectId}`);
  if (!release) return "busy";
  try {
    await advanceLocked(deps, prospectId);
    return "done";
  } finally {
    await release();
  }
}

async function advanceLocked(deps: Deps, prospectId: string): Promise<void> {
  const P = schema.prospects;
  let campaignId: string | null = null;
  for (let guard = 0; guard < 12; guard++) {
    const [prospect] = await deps.db.select().from(P).where(eq(P.id, prospectId));
    if (!prospect) return;
    campaignId = prospect.campaign_id;
    const [campaign] = await deps.db.select().from(schema.campaigns).where(eq(schema.campaigns.id, prospect.campaign_id));
    if (campaign.status !== "RUNNING") return; // pause, arrêt, blocage : l'état est conservé pour la reprise
    const step = nextStep(prospect, campaign.config);
    if (!step) break;
    const [firm] = await deps.db.select().from(schema.firms).where(eq(schema.firms.id, prospect.firm_id));
    const origin = before(prospect.state, step);
    const hash = stableHash({ step, config: campaign.config_hash });
    const S = schema.step_runs;
    await deps.db
      .insert(S)
      .values({ campaign_id: campaign.id, prospect_id: prospect.id, step, config_hash: hash, status: "RUNNING", attempts: 1 })
      .onConflictDoUpdate({ target: [S.prospect_id, S.step, S.config_hash], set: { status: "RUNNING", attempts: sql`${S.attempts} + 1`, error: null, finished_at: null } });
    const finish = (status: string, error: unknown = null) =>
      deps.db.update(S).set({ status, error: error as object | null, finished_at: deps.now() }).where(sql`${S.prospect_id} = ${prospect.id} and ${S.step} = ${step} and ${S.config_hash} = ${hash}`);

    try {
      const rt = deps.runtimeFor(campaign);
      const running = await setState(deps, prospect, RUNNING_STATE[step]);
      await STEPS[step](deps, rt, campaign, running, firm);
      await finish("DONE");
    } catch (err) {
      const c = classify(err);
      const recovery = POLICIES[c.category].recovery;
      await finish("FAILED", c);
      const [current] = await deps.db.select().from(P).where(eq(P.id, prospectId));
      await logEvent(deps.db, { campaignId: campaign.id, prospectId, type: "STEP_ERROR", data: { step, ...c, recovery } });
      if (recovery === "BUDGET_BLOCK") {
        await setState(deps, current, "BUDGET_BLOCKED", { resume_state: origin, last_error: c });
      } else if (recovery === "STOP_INTEGRATION") {
        // Clé absente ou refusée : inutile d'user les autres prospects dessus. La campagne s'arrête et dit pourquoi ;
        // le prospect garde son état en cours et reprendra cette étape à la relance.
        await deps.db.update(P).set({ last_error: c }).where(eq(P.id, prospectId));
        await deps.db.update(schema.campaigns).set({ status: "BLOCKED", stop_reason: `Intégration à rétablir (${step}) : ${c.message}`, updated_at: deps.now() }).where(eq(schema.campaigns.id, campaign.id));
        return;
      } else {
        // Les relances bornées ont déjà eu lieu autour de chaque appel externe : l'agent passe la main.
        await sendToReview(deps, current, "STEP_FAILED", `Étape ${step} : ${c.category}. ${c.message}`.slice(0, 500), origin, { last_error: c });
      }
      break;
    }
  }
  if (campaignId) await deps.queue.send("campaign-tick", { campaignId });
}
