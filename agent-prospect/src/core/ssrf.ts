import { isIP } from "node:net";
import { AppError } from "./errors";

function v4ToInt(ip: string): number {
  return ip.split(".").reduce((acc, o) => (acc << 8) + Number(o), 0) >>> 0;
}

const V4_BLOCKED: [string, number][] = [
  ["0.0.0.0", 8],
  ["10.0.0.0", 8],
  ["100.64.0.0", 10],
  ["127.0.0.0", 8],
  ["169.254.0.0", 16], // lien local, dont les métadonnées cloud 169.254.169.254
  ["172.16.0.0", 12],
  ["192.0.0.0", 24],
  ["192.0.2.0", 24],
  ["192.168.0.0", 16],
  ["198.18.0.0", 15],
  ["198.51.100.0", 24],
  ["203.0.113.0", 24],
  ["224.0.0.0", 3], // multicast, réservé, broadcast
];

function isBlockedV4(ip: string): boolean {
  const n = v4ToInt(ip);
  return V4_BLOCKED.some(([base, bits]) => {
    const mask = bits === 0 ? 0 : (~0 << (32 - bits)) >>> 0;
    return (n & mask) === (v4ToInt(base) & mask);
  });
}

function expandV6(ip: string): number[] | null {
  let s = ip.toLowerCase().split("%")[0];
  const v4 = s.match(/(\d+\.\d+\.\d+\.\d+)$/);
  if (v4) {
    const n = v4ToInt(v4[1]);
    s = s.slice(0, -v4[1].length) + ((n >>> 16).toString(16) + ":" + (n & 0xffff).toString(16));
  }
  const [head, tail] = s.split("::");
  const h = head ? head.split(":") : [];
  const t = tail !== undefined ? (tail ? tail.split(":") : []) : null;
  const groups = t === null ? h : [...h, ...Array(8 - h.length - t.length).fill("0"), ...t];
  if (groups.length !== 8) return null;
  return groups.map((g) => parseInt(g || "0", 16));
}

function isBlockedV6(ip: string): boolean {
  const g = expandV6(ip);
  if (!g) return true;
  if (g.slice(0, 7).every((x) => x === 0) && (g[7] === 0 || g[7] === 1)) return true; // :: et ::1
  // IPv4 mappée ou compatible, 64:ff9b::/96 (NAT64) : on juge l'IPv4 embarquée.
  const embedded = `${g[6] >> 8}.${g[6] & 255}.${g[7] >> 8}.${g[7] & 255}`;
  if (g.slice(0, 5).every((x) => x === 0) && (g[5] === 0xffff || g[5] === 0)) return isBlockedV4(embedded);
  if (g[0] === 0x64 && g[1] === 0xff9b) return isBlockedV4(embedded);
  if ((g[0] & 0xfe00) === 0xfc00) return true; // fc00::/7 adresses locales uniques
  if ((g[0] & 0xffc0) === 0xfe80) return true; // fe80::/10 lien local
  if ((g[0] & 0xff00) === 0xff00) return true; // multicast
  if (g[0] === 0x2001 && g[1] === 0xdb8) return true; // documentation
  return false;
}

export function isBlockedAddress(ip: string): boolean {
  const kind = isIP(ip);
  if (kind === 4) return isBlockedV4(ip);
  if (kind === 6) return isBlockedV6(ip);
  return true;
}

/** Contrôle statique d'une URL avant toute résolution DNS. */
export function assertAllowedUrl(raw: string): URL {
  let url: URL;
  try {
    url = new URL(raw);
  } catch {
    throw new AppError("INVALID_INPUT", `URL invalide : ${raw}`);
  }
  if (url.protocol !== "http:" && url.protocol !== "https:") throw new AppError("BLOCKED_SOURCE", `Protocole refusé : ${url.protocol}`);
  if (url.username || url.password) throw new AppError("BLOCKED_SOURCE", "URL avec identifiants refusée");
  if (url.port && url.port !== "80" && url.port !== "443") throw new AppError("BLOCKED_SOURCE", `Port refusé : ${url.port}`);
  const host = url.hostname.replace(/^\[|\]$/g, "").toLowerCase();
  if (host === "localhost" || host.endsWith(".localhost") || host.endsWith(".local") || host.endsWith(".internal")) {
    throw new AppError("BLOCKED_SOURCE", `Hôte interne refusé : ${host}`);
  }
  if (isIP(host) && isBlockedAddress(host)) throw new AppError("BLOCKED_SOURCE", `Adresse refusée : ${host}`);
  return url;
}
