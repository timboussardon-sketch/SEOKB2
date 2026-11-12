import { identity } from "../core/identity";

/** User-Agent du crawler : le jeton est neutre, l'URL de contact vient de SENDER_URL. */
export const AGENT_UA = `ProspectAgent/1.0${identity().url ? ` (+${identity().url})` : ""}`;
const AGENT_TOKEN = "prospectagent";

interface Rule {
  allow: boolean;
  path: string;
}

export interface Robots {
  rules: Rule[];
  sitemaps: string[];
}

export function parseRobots(txt: string): Robots {
  const groups: { agents: string[]; rules: Rule[] }[] = [];
  const sitemaps: string[] = [];
  let current: { agents: string[]; rules: Rule[] } | null = null;
  let lastWasAgent = false;
  for (const raw of txt.split(/\r?\n/)) {
    const line = raw.replace(/#.*$/, "").trim();
    const m = line.match(/^([a-z-]+)\s*:\s*(.*)$/i);
    if (!m) continue;
    const key = m[1].toLowerCase();
    const value = m[2].trim();
    if (key === "sitemap") {
      sitemaps.push(value);
    } else if (key === "user-agent") {
      if (!current || !lastWasAgent) {
        current = { agents: [], rules: [] };
        groups.push(current);
      }
      current.agents.push(value.toLowerCase());
      lastWasAgent = true;
      continue;
    } else if ((key === "allow" || key === "disallow") && current) {
      if (value) current.rules.push({ allow: key === "allow", path: value });
    }
    lastWasAgent = false;
  }
  const own = groups.filter((g) => g.agents.some((a) => a !== "*" && AGENT_TOKEN.includes(a)));
  const chosen = own.length ? own : groups.filter((g) => g.agents.includes("*"));
  return { rules: chosen.flatMap((g) => g.rules), sitemaps };
}

function toRegExp(path: string): RegExp {
  const anchored = path.endsWith("$");
  const body = (anchored ? path.slice(0, -1) : path).split("*").map((p) => p.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")).join(".*");
  return new RegExp(`^${body}${anchored ? "$" : ""}`);
}

/** Règle la plus longue gagne ; à égalité, l'autorisation. */
export function isAllowed(robots: Robots, url: string): boolean {
  const u = new URL(url);
  const target = u.pathname + u.search;
  let best: Rule | null = null;
  for (const r of robots.rules) {
    if (!toRegExp(r.path).test(target)) continue;
    if (!best || r.path.length > best.path.length || (r.path.length === best.path.length && r.allow)) best = r;
  }
  return best ? best.allow : true;
}
