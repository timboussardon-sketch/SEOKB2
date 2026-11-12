/** Règles pures des missions quotidiennes : cibles, heure de Paris, cadence d'envoi. */

export interface Segment {
  key: string;
  label: string;
  practice_area: string;
  subspecialties: string[];
  client_type: "entreprise" | "particulier" | "mixte";
}

/** Cibles choisies par l'opérateur le 2026-10-02 : immobilier et construction, droit du travail, URSSAF, dommage corporel. */
export const SEGMENTS: Segment[] = [
  { key: "construction", label: "Immobilier et construction", practice_area: "droit de la construction", subspecialties: ["droit immobilier", "construction"], client_type: "mixte" },
  { key: "travail", label: "Droit du travail", practice_area: "droit du travail", subspecialties: [], client_type: "entreprise" },
  { key: "urssaf", label: "URSSAF", practice_area: "droit de la sécurité sociale", subspecialties: ["contentieux URSSAF", "cotisations sociales"], client_type: "entreprise" },
  { key: "dommage", label: "Dommage corporel", practice_area: "droit du dommage corporel", subspecialties: ["indemnisation des victimes"], client_type: "particulier" },
];

export interface MissionSettings {
  enabled: boolean;
  autoSend: boolean;
  dailySends: number;
  cities: string[];
  /** Heures de Paris : envois entre sendFrom et sendUntil, rapport à partir de reportAt. */
  sendFrom: number;
  sendUntil: number;
  reportAt: number;
  spacingMinutes: number;
}

export function missionSettings(env: Record<string, string | undefined> = process.env): MissionSettings {
  return {
    enabled: env.MISSIONS_ENABLED === "true",
    autoSend: env.AUTO_SEND === "true",
    dailySends: Number(env.DAILY_SENDS ?? 10),
    cities: (env.MISSION_CITIES ?? "Lyon").split(",").map((s) => s.trim()).filter(Boolean),
    sendFrom: Number(env.SEND_FROM_HOUR ?? 9),
    sendUntil: Number(env.SEND_UNTIL_HOUR ?? 17),
    reportAt: Number(env.REPORT_HOUR ?? 18),
    spacingMinutes: Number(env.SEND_SPACING_MINUTES ?? 20),
  };
}

/** Date (AAAA-MM-JJ), heure et jour de semaine à Paris, quel que soit le fuseau de la machine. */
export function parisClock(now: Date): { day: string; hour: number; minute: number; weekday: number } {
  const parts = Object.fromEntries(
    new Intl.DateTimeFormat("en-GB", { timeZone: "Europe/Paris", year: "numeric", month: "2-digit", day: "2-digit", hour: "2-digit", minute: "2-digit", hourCycle: "h23", weekday: "short" })
      .formatToParts(now).map((p) => [p.type, p.value]),
  );
  const weekday = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"].indexOf(parts.weekday);
  return { day: `${parts.year}-${parts.month}-${parts.day}`, hour: Number(parts.hour), minute: Number(parts.minute), weekday };
}

/** Un envoi est permis en semaine, dans la plage horaire, sous le quota du jour, après l'espacement minimal. */
export function canSendNow(s: MissionSettings, now: Date, sentToday: number, lastSendAt: Date | null): { ok: boolean; why?: string } {
  const c = parisClock(now);
  if (!s.autoSend) return { ok: false, why: "envoi automatique désactivé" };
  if (c.weekday === 0 || c.weekday === 6) return { ok: false, why: "week-end" };
  if (c.hour < s.sendFrom || c.hour >= s.sendUntil) return { ok: false, why: "hors plage horaire" };
  if (sentToday >= s.dailySends) return { ok: false, why: "quota du jour atteint" };
  if (lastSendAt && now.getTime() - lastSendAt.getTime() < s.spacingMinutes * 60_000) return { ok: false, why: "espacement" };
  return { ok: true };
}

/** Jours ouvrés (lundi-vendredi, heure de Paris) écoulés de `from` à `to`, jour de départ exclu. */
export function businessDaysBetween(from: Date, to: Date): number {
  let n = 0;
  const end = parisClock(to).day;
  for (let d = new Date(from.getTime() + 86_400_000); parisClock(d).day <= end; d = new Date(d.getTime() + 86_400_000)) {
    const w = parisClock(d).weekday;
    if (w !== 0 && w !== 6) n++;
  }
  return n;
}

/** Cibles des missions : le message type de l'opérateur parle des « cabinets qui accompagnent les entreprises et dirigeants ». */
export const MISSION_SEGMENTS = SEGMENTS.filter((s) => s.client_type === "entreprise");

/** Cible suivante : la paire spécialité × ville lancée le moins récemment, jamais lancée d'abord. */
export function nextSegment(cities: string[], lastRun: Map<string, number>): { segment: Segment; city: string } {
  const pairs = MISSION_SEGMENTS.flatMap((segment) => cities.map((city) => ({ segment, city, at: lastRun.get(`${segment.practice_area}|${city}`) ?? -1 })));
  pairs.sort((a, b) => a.at - b.at);
  return { segment: pairs[0].segment, city: pairs[0].city };
}
