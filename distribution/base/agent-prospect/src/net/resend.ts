import { readFile } from "node:fs/promises";
import { join } from "node:path";
import { BANNER_CID, bannerFile } from "../core/email-presentation";
import { Resend } from "resend";

export interface OutgoingEmail {
  from: string;
  replyTo: string;
  to: string;
  subject: string;
  text: string;
  html?: string;
  headers: Record<string, string>;
  /** Même clé = même envoi : Resend ne renvoie pas deux fois. */
  idempotencyKey: string;
}

export interface Mailer {
  send(email: OutgoingEmail): Promise<{ id: string }>;
  /** Dernier évènement connu de Resend : sent, delivered, bounced, complained… */
  lastEvent(id: string): Promise<string>;
}

export interface MailConfig {
  from: string;
  replyTo: string;
  maxPerDay: number;
}

export function mailConfig(env: Record<string, string | undefined> = process.env): MailConfig | null {
  if (!env.RESEND_API_KEY || !env.MAIL_FROM || !env.MAIL_REPLY_TO || !env.SENDER_NAME?.trim()) return null;
  return { from: env.MAIL_FROM, replyTo: env.MAIL_REPLY_TO, maxPerDay: Number(env.MAX_SENDS_PER_DAY ?? 20) };
}

export function resendMailer(apiKey: string): Mailer {
  const resend = new Resend(apiKey);
  return {
    async send(e) {
      const file = bannerFile();
      const attachments = file && e.html?.includes(`src="cid:${BANNER_CID}"`)
        ? [{ filename: file, content: await readFile(join(process.cwd(), "public", "email", file)), contentType: "image/png", contentId: BANNER_CID }]
        : undefined;
      const { data, error } = await resend.emails.send({ from: e.from, replyTo: e.replyTo, to: e.to, subject: e.subject, text: e.text, html: e.html, attachments, headers: e.headers }, { idempotencyKey: e.idempotencyKey });
      if (error || !data) throw new Error(`Resend : ${error?.message ?? "aucune réponse"}`);
      return { id: data.id };
    },
    async lastEvent(id) {
      const { data, error } = await resend.emails.get(id);
      if (error || !data) throw new Error(`Resend : ${error?.message ?? "email introuvable"}`);
      return data.last_event;
    },
  };
}
