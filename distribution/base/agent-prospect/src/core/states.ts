export const PROSPECT_STATES = [
  "DISCOVERED",
  "QUALIFYING",
  "QUALIFIED",
  "ENRICHING",
  "ENRICHED",
  "VISIBILITY_RUNNING",
  "VISIBILITY_DONE",
  "AUDITING",
  "AUDIT_DONE",
  "KEYWORDS_RUNNING",
  "KEYWORDS_DONE",
  "DRAFTING",
  "DRAFT_READY",
  "FACT_CHECKING",
  "READY_FOR_REVIEW",
  "APPROVED",
  "ARCHIVED_OBSERVED",
  "REJECTED",
  "HUMAN_REVIEW_REQUIRED",
  "BUDGET_BLOCKED",
  "SUPPRESSED",
  "FAILED",
] as const;
export type ProspectState = (typeof PROSPECT_STATES)[number];

export const STEPS = ["qualify", "enrich", "visibility", "audit", "keywords", "draft", "factcheck"] as const;
export type Step = (typeof STEPS)[number];

/** États depuis lesquels l'agent a encore du travail à faire seul, et l'étape correspondante. */
export const STEP_FOR_STATE: Partial<Record<ProspectState, Step>> = {
  DISCOVERED: "qualify",
  QUALIFYING: "qualify",
  QUALIFIED: "enrich",
  ENRICHING: "enrich",
  ENRICHED: "visibility",
  VISIBILITY_RUNNING: "visibility",
  VISIBILITY_DONE: "audit",
  AUDITING: "audit",
  AUDIT_DONE: "keywords",
  KEYWORDS_RUNNING: "keywords",
  KEYWORDS_DONE: "draft",
  DRAFTING: "draft",
  DRAFT_READY: "factcheck",
  FACT_CHECKING: "factcheck",
};

export const RUNNING_STATE: Record<Step, ProspectState> = {
  qualify: "QUALIFYING",
  enrich: "ENRICHING",
  visibility: "VISIBILITY_RUNNING",
  audit: "AUDITING",
  keywords: "KEYWORDS_RUNNING",
  draft: "DRAFTING",
  factcheck: "FACT_CHECKING",
};

const ANY_ACTIVE_EXIT: ProspectState[] = ["FAILED", "BUDGET_BLOCKED", "SUPPRESSED", "HUMAN_REVIEW_REQUIRED"];

const TRANSITIONS: Record<ProspectState, ProspectState[]> = {
  DISCOVERED: ["QUALIFYING", ...ANY_ACTIVE_EXIT],
  QUALIFYING: ["QUALIFIED", "REJECTED", ...ANY_ACTIVE_EXIT],
  QUALIFIED: ["ENRICHING", ...ANY_ACTIVE_EXIT],
  ENRICHING: ["ENRICHED", ...ANY_ACTIVE_EXIT],
  ENRICHED: ["VISIBILITY_RUNNING", ...ANY_ACTIVE_EXIT],
  VISIBILITY_RUNNING: ["VISIBILITY_DONE", "ARCHIVED_OBSERVED", ...ANY_ACTIVE_EXIT],
  VISIBILITY_DONE: ["AUDITING", ...ANY_ACTIVE_EXIT],
  AUDITING: ["AUDIT_DONE", ...ANY_ACTIVE_EXIT],
  AUDIT_DONE: ["KEYWORDS_RUNNING", ...ANY_ACTIVE_EXIT],
  KEYWORDS_RUNNING: ["KEYWORDS_DONE", ...ANY_ACTIVE_EXIT],
  KEYWORDS_DONE: ["DRAFTING", ...ANY_ACTIVE_EXIT],
  DRAFTING: ["DRAFT_READY", ...ANY_ACTIVE_EXIT],
  DRAFT_READY: ["FACT_CHECKING", ...ANY_ACTIVE_EXIT],
  FACT_CHECKING: ["READY_FOR_REVIEW", ...ANY_ACTIVE_EXIT],
  // Une modification du brouillon renvoie au contrôle factuel et annule l'approbation.
  READY_FOR_REVIEW: ["APPROVED", "REJECTED", "DRAFT_READY", "SUPPRESSED"],
  APPROVED: ["DRAFT_READY", "REJECTED", "SUPPRESSED"],
  ARCHIVED_OBSERVED: ["VISIBILITY_DONE", "SUPPRESSED"], // force_audit manuel
  REJECTED: [],
  // La sortie de revue, de blocage budget ou d'échec reprend à l'état mémorisé (resume_state).
  HUMAN_REVIEW_REQUIRED: [...PROSPECT_STATES.filter((s) => s !== "HUMAN_REVIEW_REQUIRED")],
  BUDGET_BLOCKED: [...PROSPECT_STATES.filter((s) => s !== "BUDGET_BLOCKED")],
  FAILED: [...PROSPECT_STATES.filter((s) => s !== "FAILED")],
  SUPPRESSED: [],
};

export function canTransition(from: ProspectState, to: ProspectState): boolean {
  return TRANSITIONS[from].includes(to);
}

export function assertTransition(from: ProspectState, to: ProspectState): void {
  if (!canTransition(from, to)) throw new Error(`Transition interdite : ${from} → ${to}`);
}

/** L'agent travaille encore dessus. */
export function isInFlight(state: ProspectState): boolean {
  return state in STEP_FOR_STATE;
}

export const QUALIFICATION_STATUSES = ["PENDING", "QUALIFIED", "REJECTED", "AMBIGUOUS", "NEEDS_REVIEW"] as const;
export type QualificationStatus = (typeof QUALIFICATION_STATUSES)[number];

export const QUALIFICATION_REASONS = [
  "WRONG_LOCATION",
  "WRONG_PRACTICE",
  "WRONG_CLIENT_TYPE",
  "NO_OFFICIAL_SITE",
  "DUPLICATE",
  "INSUFFICIENT_EVIDENCE",
  "INACTIVE",
  "AMBIGUOUS_ENTITY",
  "BLOCKED_SOURCE",
  "SUPPRESSED_CONTACT",
] as const;
export type QualificationReason = (typeof QUALIFICATION_REASONS)[number];

export const VERDICTS = ["OBSERVED", "FIRM_ONLY", "NOT_OBSERVED_IN_SAMPLE", "INCONCLUSIVE"] as const;
export type Verdict = (typeof VERDICTS)[number];

export const GOAL_TYPES = ["QUALIFIED_PROSPECTS", "AUDITED_PROSPECTS", "EMAIL_READY_PROSPECTS"] as const;
export type GoalType = (typeof GOAL_TYPES)[number];

export const REVIEW_REASONS = [
  "AMBIGUOUS_ENTITY",
  "CONTRADICTORY_EVIDENCE",
  "UNCERTAIN_PRACTICE",
  "FIRM_ONLY",
  "VISIBILITY_INCONCLUSIVE",
  "UNSUPPORTED_CLAIM",
  "STEP_FAILED",
] as const;
export type ReviewReason = (typeof REVIEW_REASONS)[number];
