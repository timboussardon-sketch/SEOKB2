/**
 * Relances, décidées par l'opérateur le 2026-10-02 : deux au plus, 3 jours ouvrés après le message précédent sans réponse.
 * Texte : l'opérateur le fournira. Tant qu'une entrée vaut null, cette relance ne part pas.
 */
export const FOLLOWUP_DELAY_BUSINESS_DAYS = 3;
export const FOLLOWUPS: (string | null)[] = [null, null];
