/** Règles pures du suivi d'envoi : statut d'après Resend, réponses relevées dans Gmail. */

export type OutreachStatus = "SENDING" | "FAILED" | "SENT" | "DELIVERED" | "BOUNCED" | "REPLIED" | "OPTED_OUT";

export interface InboxMessage {
  id: string;
  from: string;
  date: Date;
  snippet: string;
}

// « stop » comme mot, ou une demande explicite de ne plus être contacté.
const OPT_OUT = /(^|[^\p{L}])stop([^\p{L}]|$)|désinscri|desinscri|ne plus (me |nous )?(recevoir|contacter|écrire|solliciter)|retirez[- ](moi|nous)/iu;
export const isOptOut = (text: string) => OPT_OUT.test(text);

const addressOf = (from: string) => (from.match(/<([^>]+)>/)?.[1] ?? from).trim().toLowerCase();

/** Les réponses viennent de l'adresse écrite, ou d'une autre adresse du même domaine (associé, secrétariat). */
export function isFromProspect(from: string, recipient: string): boolean {
  const a = addressOf(from);
  const r = recipient.toLowerCase();
  return a === r || a.split("@")[1] === r.split("@")[1];
}

/** Réponses reçues après l'envoi : la première fixe la date, une opposition l'emporte. null s'il n'y en a aucune. */
export function replyState(messages: InboxMessage[], recipient: string, sentAt: Date): { status: "REPLIED" | "OPTED_OUT"; repliedAt: Date; excerpt: string; received: number } | null {
  const replies = messages.filter((m) => m.date >= sentAt && isFromProspect(m.from, recipient)).sort((a, b) => a.date.getTime() - b.date.getTime());
  if (!replies.length) return null;
  const optOut = replies.find((m) => isOptOut(m.snippet));
  return { status: optOut ? "OPTED_OUT" : "REPLIED", repliedAt: replies[0].date, excerpt: (optOut ?? replies[0]).snippet.slice(0, 280), received: replies.length };
}

/** Statut après un évènement Resend. Une réponse ou une opposition déjà relevée n'est jamais écrasée. */
export function statusAfterDelivery(current: OutreachStatus, event: string): OutreachStatus {
  if (current === "REPLIED" || current === "OPTED_OUT") return current;
  if (event === "bounced" || event === "failed" || event === "suppressed") return "BOUNCED";
  if (event === "complained") return "OPTED_OUT";
  if (event === "delivered" || event === "opened" || event === "clicked") return "DELIVERED";
  return current === "DELIVERED" ? "DELIVERED" : "SENT";
}
