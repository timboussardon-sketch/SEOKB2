export const STATE_LABEL: Record<string, [string, string]> = {
  DISCOVERED: ["Trouvé", ""],
  QUALIFYING: ["Qualification en cours", "info"],
  QUALIFIED: ["Qualifié", "info"],
  ENRICHING: ["Enrichissement en cours", "info"],
  ENRICHED: ["Enrichi", "info"],
  VISIBILITY_RUNNING: ["Mesure IA en cours", "info"],
  VISIBILITY_DONE: ["Mesure IA faite", "info"],
  AUDITING: ["Pré-audit en cours", "info"],
  AUDIT_DONE: ["Pré-audit fait", "info"],
  KEYWORDS_RUNNING: ["Mots-clés en cours", "info"],
  KEYWORDS_DONE: ["Mots-clés faits", "info"],
  DRAFTING: ["Rédaction en cours", "info"],
  DRAFT_READY: ["Brouillon à contrôler", "info"],
  FACT_CHECKING: ["Contrôle factuel en cours", "info"],
  READY_FOR_REVIEW: ["Prêt à relire", "ok"],
  APPROVED: ["Approuvé", "ok"],
  ARCHIVED_OBSERVED: ["Déjà observé, archivé", ""],
  REJECTED: ["Écarté", "bad"],
  HUMAN_REVIEW_REQUIRED: ["Revue humaine", "warn"],
  BUDGET_BLOCKED: ["Suspendu : budget", "warn"],
  SUPPRESSED: ["Supprimé (opposition)", "bad"],
  FAILED: ["Échec", "bad"],
};

export const CAMPAIGN_STATUS: Record<string, [string, string]> = {
  DRAFT: ["Non lancée", ""],
  RUNNING: ["En cours", "info"],
  PAUSED: ["En pause", "warn"],
  STOPPED: ["Arrêtée", "bad"],
  COMPLETED: ["Objectif atteint", "ok"],
  PARTIAL: ["Objectif non atteint", "warn"],
  BLOCKED: ["Bloquée", "bad"],
};

export const REASON_LABEL: Record<string, string> = {
  WRONG_LOCATION: "Hors zone",
  WRONG_PRACTICE: "Autre pratique",
  WRONG_CLIENT_TYPE: "Autre clientèle",
  NO_OFFICIAL_SITE: "Pas de site exploitable",
  DUPLICATE: "Doublon",
  INSUFFICIENT_EVIDENCE: "Preuves insuffisantes",
  INACTIVE: "Inactif",
  AMBIGUOUS_ENTITY: "Identité ambiguë",
  BLOCKED_SOURCE: "Site qui refuse l'exploration",
  SUPPRESSED_CONTACT: "Opposition enregistrée",
  MANUAL: "Écarté en revue",
};

export const VERDICT_LABEL: Record<string, [string, string]> = {
  OBSERVED: ["Observé", "ok"],
  FIRM_ONLY: ["Cabinet seul", "warn"],
  NOT_OBSERVED_IN_SAMPLE: ["Non observé dans l'échantillon", ""],
  INCONCLUSIVE: ["Non concluant", "warn"],
};

export const GOAL_LABEL: Record<string, string> = {
  QUALIFIED_PROSPECTS: "prospects qualifiés",
  AUDITED_PROSPECTS: "prospects audités",
  EMAIL_READY_PROSPECTS: "prospects avec email prêt à relire",
};

export const REVIEW_LABEL: Record<string, string> = {
  AMBIGUOUS_ENTITY: "Identité ambiguë",
  CONTRADICTORY_EVIDENCE: "Preuves contradictoires",
  UNCERTAIN_PRACTICE: "Qualification incertaine",
  FIRM_ONLY: "Cabinet observé, avocat non identifié",
  VISIBILITY_INCONCLUSIVE: "Mesure IA non concluante",
  UNSUPPORTED_CLAIM: "Affirmation non étayée dans l'email",
  STEP_FAILED: "Étape en échec",
};

export const ACTION_LABEL: Record<string, string> = { APPROVE: "Valider", REJECT: "Écarter", RETRY: "Relancer" };
