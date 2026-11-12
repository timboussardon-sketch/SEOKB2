import type { ClaimContext, DraftSentence } from "../core/claims";
import type { DraftRequest } from "../providers/types";
import { identity } from "../core/identity";

/** Message type fourni par l'opérateur le 2026-10-02 (v3). Texte fixe ; seules les requêtes testées s'ajoutent entre parenthèses. */
export const EMAIL_TEMPLATE_VERSION = "gabarit-v3";

export function renderEmailTemplate(req: DraftRequest, ctx: ClaimContext, _practiceFactId: string | null): { subject: string; sentences: DraftSentence[] } {
  const out: DraftSentence[] = [];
  const push = (kind: DraftSentence["kind"], text: string, evidence_ids: string[] = []) => out.push({ id: `s${out.length + 1}`, kind, text, evidence_ids });
  const prompts = ctx.template?.prompts ?? [];

  push("GREETING", "Bonjour,");
  out.push({ id: "tpl-intro", kind: "VISIBILITY", evidence_ids: [], text: "J’ai analysé comment votre cabinet ressortait dans les réponses de ChatGPT sur plusieurs recherches liées aux cabinets qui accompagnent les entreprises et dirigeants." });
  out.push({ id: "tpl-constat", kind: "VISIBILITY", paragraph: true, evidence_ids: [], text: `Pour le moment, votre cabinet n’apparaît pas sur vos ${prompts.length} requêtes principales testées (${prompts.map((q) => `« ${q.trim()} »`).join(", ")}).` });
  // Sans pré-audit préparé, la phrase n'est pas écrite : le contrôle bloque alors l'envoi (aucune observation vérifiable).
  if (req.auditFactId) push("OBSERVATION", "Je vous ai préparé un pré-audit gratuit de votre site avec les principales opportunités pour améliorer votre visibilité dans les moteurs de recherche et les réponses IA.", [req.auditFactId]);
  push("CTA", "Je peux vous l’envoyer ?");
  // Ligne source et « stop » retirées à la demande de l'opérateur (2026-10-02) ; l'en-tête List-Unsubscribe reste.
  push("SIGNATURE", ["Excellente journée,", identity().name, identity().url].filter(Boolean).join("\n"));
  return { subject: `${req.firmName ?? "Votre cabinet"} dans les réponses ${ctx.chatgptObserved ? "de ChatGPT" : "des IA"}`.slice(0, 80), sentences: out };
}
