import { frameVisibility, type ClaimContext, type DraftSentence } from "../core/claims";
import type { DraftRequest } from "../providers/types";

/** Message type fourni par Tim le 2026-10-02. Le texte est fixe ; seuls les faits du cabinet changent. */
export const EMAIL_TEMPLATE_VERSION = "gabarit-tim-v2";

const de = (name: string) => (/^[aeiouyhàâéèêëîïôöùûü]/i.test(name) ? `d’${name}` : `de ${name}`);

export function renderEmailTemplate(req: DraftRequest, ctx: ClaimContext, practiceFactId: string | null): { subject: string; sentences: DraftSentence[] } {
  const out: DraftSentence[] = [];
  const push = (kind: DraftSentence["kind"], text: string, evidence_ids: string[] = []) => out.push({ id: `s${out.length + 1}`, kind, text, evidence_ids });
  const practice = req.practice.toLowerCase();
  const topic = practice.startsWith("droit") ? `liées au ${practice}` : `liées à la pratique « ${practice} »`;

  push("GREETING", "Bonjour,");
  push("OBSERVATION", `J’ai analysé la visibilité en ligne ${req.firmName ? de(req.firmName) : "de votre cabinet"} sur plusieurs recherches SEO GEO ${topic} à ${req.city}.`, practiceFactId ? [practiceFactId] : []);
  if (req.keywords.length >= 2) {
    const two = req.keywords.slice(0, 2);
    const verified = two.filter((k) => req.keywordChecks[k] !== undefined);
    // Une ligne ne dit « cité » ou « pas cité » que si la requête a été vérifiée ; sinon elle ne dit rien.
    const line = (k: string) => (req.keywordChecks[k] === undefined ? `→ ${k}` : `→ ${k} : votre site ${req.keywordChecks[k] ? "est cité" : "n’est pas cité"}`);
    const intro = verified.length
      ? `J’ai également vérifié dans ${req.keywordCheckWho} deux recherches directement liées à vos services :`
      : "J’ai également identifié plusieurs recherches Google directement liées à vos services sur lesquelles votre cabinet pourrait se positionner, par exemple :";
    push("KEYWORDS", `${intro}\n\n${two.map(line).join("\n")}`);
  }
  if (req.auditPages && req.auditFactId) {
    push("OBSERVATION", `Je prépare pour vous gratuitement un pré-audit de ${req.auditPages} pages de votre site avec les opportunités identifiées pour faire remonter votre cabinet dans les recherches IA.`, [req.auditFactId]);
  }
  push("CTA", "Je vous l’envoie ?");
  push("TRANSPARENCY", `${req.contactSourceUrl ? `J’ai trouvé votre adresse sur ${req.contactSourceUrl}. ` : ""}Répondez « stop » pour ne plus recevoir de message de ma part.`);
  push("SIGNATURE", "Excellente journée,\nTimothée Boussardon\nOrganikk\nhttps://organikk.co");
  // Le constat est inséré par le code après la première observation, seulement si le verdict l'établit.
  return { subject: `${req.firmName ?? "Votre cabinet"} dans les réponses ${ctx.chatgptObserved ? "de ChatGPT" : "des IA"}`.slice(0, 80), sentences: frameVisibility(out, ctx) };
}
