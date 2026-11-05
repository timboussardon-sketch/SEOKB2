import { normalize, wordCount } from "./text";
import type { Verdict } from "./states";

export const CLAIM_RULE_VERSION = "claims-v3";
// Email court, demandé le 2026-10-02 (le cahier des charges initial disait 90 à 140).
export const MIN_WORDS = 60;
export const MAX_WORDS = 140;

export type SentenceKind = "GREETING" | "OBSERVATION" | "VISIBILITY" | "KEYWORDS" | "AUDIT_LINK" | "CTA" | "TRANSPARENCY" | "SIGNATURE";

export interface DraftSentence {
  id: string;
  kind: SentenceKind;
  text: string;
  evidence_ids: string[];
}

/** Fait vérifié auquel une phrase peut s'adosser. `values` liste les nombres et termes qu'elle a le droit de reprendre. */
export interface Fact {
  id: string;
  text: string;
  values: (string | number)[];
}

export type ClaimStatus = "SUPPORTED" | "INFERRED" | "UNSUPPORTED" | "PROMOTIONAL" | "NOT_A_CLAIM";

export interface SentenceCheck {
  id: string;
  status: ClaimStatus;
  reason: string;
}

export interface ClaimContext {
  verdict: Verdict | null;
  /** Fragment obligatoire du mode de test, ex. « API OpenAI avec recherche web ». */
  /** À qui les questions ont été posées, tel que l'email doit le dire : « ChatGPT », « Claude, via son API avec recherche web »… */
  modeFragment: string;
  sampleDate: string;
  validRuns: number;
  /** Nombre de questions distinctes posées, et une question type à citer. */
  questionCount: number;
  exampleQuery: string;
  /** Vrai seulement pour des réponses relevées à la main dans l'interface ChatGPT. */
  chatgptObserved: boolean;
  /** Nom du cabinet et clientèle visée, pour la phrase du constat. */
  firmName: string | null;
  clientPhrase: string;
  /** Résultat relevé pour chaque requête vérifiée : true = cabinet cité, false = non cité. Absent = non vérifié, aucune affirmation permise. */
  keywordChecks: Record<string, boolean>;
  /** IA interrogée pour ces vérifications, telle que l'email la nomme. */
  keywordCheckWho: string;
  keywords: string[];
  auditUrl: string | null;
  lawyerLastName: string | null;
  allowedUrls: string[];
}

const FORBIDDEN: [RegExp, string][] = [
  [/invisible/, "« invisible » : formulation interdite"],
  [/ne vous (recommande|cite|mentionne) jamais/, "« jamais » : généralisation interdite"],
  [/vous perdez|clients perdus|manque a gagner/, "perte chiffrée ou supposée : interdite"],
  [/en profondeur|analyse complete|audit complet/, "portée de l'analyse exagérée"],
  [/suite a notre (echange|conversation|appel)|comme convenu|pour faire suite/, "faux échange antérieur"],
  [/relu par|verifie manuellement|j ai personnellement/, "relecture humaine non effectuée"],
  [/urgent|derniere chance|avant qu il ne soit trop tard/, "fausse urgence"],
  [/\bchatgpt\b/, "ChatGPT cité alors que les réponses ne viennent pas de ChatGPT"],
  [/echantillon/, "mot « échantillon » écarté"],
  // Relevé sur le premier brouillon réel (2026-10-01) : « j'ai regardé comment le site se positionne », alors qu'aucune position n'est mesurée.
  [/comment (le|votre) site se positionne|vos positions|votre classement|votre trafic|vos impressions/, "position, classement ou trafic évoqués alors que rien de tel n'est mesuré"],
];
const CHATGPT_RULE = FORBIDDEN.find(([, why]) => why.startsWith("ChatGPT cité"))![0];
const PROMOTIONAL = /\b(garanti\w*|meilleur\w*|numero 1|n°1|leader|booster|exploser|doubler|tripler|premiere page|top 3|resultats assures|sans engagement)\b/;
const AI_RESULT = /\b(reponses? (generees?|recueillies?|obtenues?|de l ia|des ia|des assistants?)|api claude|api openai|assistants? ia|intelligence artificielle|\bclaude\b|\bchatgpt\b|sont cites|y sont cites)\b/;
const HEDGE = /\b(semble|pourrait|pourraient|peut etre|a priori|possiblement|parait)\b/;

const quoted = (s: string) => [...s.matchAll(/«\s*([^»]+?)\s*»/g)].map((m) => m[1]);
// Nombres isolés seulement : « B2 » dans un nom propre n'est pas un chiffre avancé.
const numbers = (s: string) => [...s.replace(/https?:\/\/\S+/g, "").matchAll(/(?<![\p{L}\d-])\d+(?:[.,]\d+)?(?![\p{L}\d])/gu)].map((m) => m[0]);
const urls = (s: string) => [...s.matchAll(/https?:\/\/[^\s)»]+/g)].map((m) => m[0].replace(/[.,;]$/, ""));

export function checkSentence(s: DraftSentence, facts: Map<string, Fact>, ctx: ClaimContext): SentenceCheck {
  const n = normalize(s.text).replace(/editeur de chatgpt/g, "editeur");
  for (const [re, why] of FORBIDDEN) if (re.test(n) && !(ctx.chatgptObserved && re === CHATGPT_RULE)) return { id: s.id, status: "UNSUPPORTED", reason: why };
  if (PROMOTIONAL.test(n)) return { id: s.id, status: "PROMOTIONAL", reason: "promesse ou superlatif" };
  const allowed = new Set([...ctx.allowedUrls, ...(ctx.auditUrl ? [ctx.auditUrl] : [])]);
  for (const u of urls(s.text)) if (!allowed.has(u)) return { id: s.id, status: "UNSUPPORTED", reason: `lien non généré par l'application : ${u}` };

  // Le résultat de la mesure ne se dit que dans la phrase VISIBILITY, encadrée par le code.
  if (s.kind !== "VISIBILITY" && s.kind !== "SIGNATURE" && s.kind !== "KEYWORDS" && AI_RESULT.test(n)) {
    return { id: s.id, status: "UNSUPPORTED", reason: "résultat de la mesure IA évoqué hors de la phrase encadrée" };
  }

  switch (s.kind) {
    case "GREETING":
      if (/maitre/.test(n) && (!ctx.lawyerLastName || !n.includes(normalize(ctx.lawyerLastName)))) {
        return { id: s.id, status: "UNSUPPORTED", reason: "nom du destinataire non vérifié" };
      }
      return { id: s.id, status: "NOT_A_CLAIM", reason: "" };

    case "OBSERVATION": {
      const cited = s.evidence_ids.map((id) => facts.get(id)).filter((f): f is Fact => !!f);
      if (cited.length === 0 || cited.length !== s.evidence_ids.length) return { id: s.id, status: "UNSUPPORTED", reason: "aucune preuve rattachée" };
      const values = new Set(cited.flatMap((f) => f.values.map((v) => normalize(String(v)))));
      const texts = cited.map((f) => normalize(f.text));
      for (const num of numbers(s.text)) if (!values.has(normalize(num))) return { id: s.id, status: "UNSUPPORTED", reason: `nombre « ${num} » absent des preuves` };
      for (const q of quoted(s.text)) {
        const nq = normalize(q);
        if (!values.has(nq) && !texts.some((t) => t.includes(nq))) return { id: s.id, status: "UNSUPPORTED", reason: `citation « ${q} » absente des preuves` };
      }
      return HEDGE.test(n) ? { id: s.id, status: "INFERRED", reason: "formulation conditionnelle adossée à une preuve" } : { id: s.id, status: "SUPPORTED", reason: "" };
    }

    case "VISIBILITY": {
      if (ctx.verdict !== "NOT_OBSERVED_IN_SAMPLE") return { id: s.id, status: "UNSUPPORTED", reason: `constat d'absence non établi (verdict ${ctx.verdict ?? "aucun"})` };
      // Le constat lui-même doit être dit : une phrase qui cite le test sans donner son résultat ne remplit pas sa fonction.
      if (!/(n apparait (pas|dans aucune)|n a pas ete observe|n est (pas )?cite|n a pas ete cite|n a ete cite aucune fois)/.test(n)) return { id: s.id, status: "UNSUPPORTED", reason: "le résultat du test n'est pas énoncé" };
      if (!normalize(s.text).includes(normalize(ctx.modeFragment))) return { id: s.id, status: "UNSUPPORTED", reason: "mode exact du test absent" };
      const nums = numbers(s.text.replace(ctx.sampleDate, "").replace(/«[^»]*»/g, ""));
      const allowed = new Set([ctx.validRuns, ctx.questionCount, ctx.questionCount ? ctx.validRuns / ctx.questionCount : 0].map(String));
      if (!nums.includes(String(ctx.validRuns)) || nums.some((x) => !allowed.has(x))) {
        return { id: s.id, status: "UNSUPPORTED", reason: `le nombre de réponses doit être ${ctx.validRuns}` };
      }
      return { id: s.id, status: "SUPPORTED", reason: "" };
    }

    case "KEYWORDS": {
      const known = new Set(ctx.keywords.map(normalize));
      // Exemples cités entre guillemets français, ou un par ligne après une flèche.
      const qs = [...quoted(s.text), ...[...s.text.matchAll(/^→\s*(.+?)(?:\s*:\s*votre site .*)?$/gm)].map((m) => m[1].trim())];
      if (qs.length < 2 || qs.length > 3) return { id: s.id, status: "UNSUPPORTED", reason: "deux ou trois exemples attendus" };
      for (const q of qs) if (!known.has(normalize(q))) return { id: s.id, status: "UNSUPPORTED", reason: `mot-clé « ${q} » absent de la liste retenue` };
      // Une ligne qui dit « cité » ou « pas cité » doit correspondre au relevé de cette requête, et l'IA interrogée doit être nommée.
      for (const m of s.text.matchAll(/^→\s*(.+?)\s*:\s*(votre site .+)$/gm)) {
        const says = /n est pas cite/.test(normalize(m[2])) ? false : /est cite/.test(normalize(m[2])) ? true : null;
        const recorded = ctx.keywordChecks[m[1].trim()];
        if (says === null) continue;
        if (recorded === undefined) return { id: s.id, status: "UNSUPPORTED", reason: `« ${m[1]} » : citation affirmée sans vérification enregistrée` };
        if (recorded !== says) return { id: s.id, status: "UNSUPPORTED", reason: `« ${m[1]} » : le relevé dit ${recorded ? "cité" : "non cité"}, l'email dit l'inverse` };
        if (!ctx.keywordCheckWho || !normalize(s.text).includes(normalize(ctx.keywordCheckWho))) return { id: s.id, status: "UNSUPPORTED", reason: "l'IA interrogée pour ces recherches n'est pas nommée" };
      }
      const rest = s.text.replace(/«[^»]*»/g, "").replace(/^→.*$/gm, "");
      for (const num of numbers(rest)) if (num !== String(ctx.keywords.length)) return { id: s.id, status: "UNSUPPORTED", reason: `la liste compte ${ctx.keywords.length} requêtes, pas ${num}` };
      return { id: s.id, status: "SUPPORTED", reason: "" };
    }

    case "AUDIT_LINK":
      if (!ctx.auditUrl || !s.text.includes(ctx.auditUrl)) return { id: s.id, status: "UNSUPPORTED", reason: "lien du pré-audit absent ou non généré" };
      return { id: s.id, status: "SUPPORTED", reason: "" };

    default:
      return { id: s.id, status: "NOT_A_CLAIM", reason: "" };
  }
}

export interface DraftCheck {
  ok: boolean;
  sentences: SentenceCheck[];
  failed: SentenceCheck[];
  global: string[];
  wordCount: number;
}

export function checkDraft(subject: string, sentences: DraftSentence[], facts: Fact[], ctx: ClaimContext): DraftCheck {
  const map = new Map(facts.map((f) => [f.id, f]));
  const checks = sentences.map((s) => checkSentence(s, map, ctx));
  const failed = checks.filter((c) => c.status === "UNSUPPORTED" || c.status === "PROMOTIONAL");
  const global: string[] = [];
  const body = sentences.filter((s) => s.kind !== "SIGNATURE" && s.kind !== "TRANSPARENCY").map((s) => s.text).join(" ");
  const words = wordCount(body);
  if (words < MIN_WORDS || words > MAX_WORDS) global.push(`longueur hors cadre : ${words} mots (${MIN_WORDS} à ${MAX_WORDS} attendus)`);
  if (sentences.filter((s) => s.kind === "CTA").length !== 1) global.push("un seul appel à l'action attendu");
  if (!sentences.some((s) => s.kind === "OBSERVATION")) global.push("aucune observation vérifiable sur l'activité ou le site");
  if (!sentences.some((s) => s.kind === "TRANSPARENCY")) global.push("mention de transparence et d'opposition absente");
  // Second contrôle, distinct du premier : ce qui est écrit est-il justifié, ET ce qui était attendu est-il présent ?
  if (visibilityRequired(ctx) && !sentences.some((s) => s.kind === "VISIBILITY")) global.push("information attendue absente : résultat de la mesure de présence IA");
  if (!visibilityRequired(ctx) && sentences.some((s) => s.kind === "VISIBILITY")) global.push("constat de présence IA présent alors que le verdict ne l'établit pas");
  if (ctx.keywords.length >= 2 && !sentences.some((s) => s.kind === "KEYWORDS")) global.push("information attendue absente : exemples de requêtes");
  const ns = normalize(subject);
  if (/^(re|tr|fwd?)\s*:/.test(subject.trim().toLowerCase())) global.push("objet : faux « Re: »");
  if (subject.length > 80 || subject.length < 5) global.push("objet : longueur hors cadre");
  for (const [re, why] of FORBIDDEN) if (re.test(ns) && !(ctx.chatgptObserved && re === CHATGPT_RULE)) global.push(`objet : ${why}`);
  if (PROMOTIONAL.test(ns)) global.push("objet : promesse ou superlatif");
  return { ok: failed.length === 0 && global.length === 0, sentences: checks, failed, global, wordCount: words };
}

export const visibilityRequired = (ctx: ClaimContext) => ctx.verdict === "NOT_OBSERVED_IN_SAMPLE" && ctx.validRuns > 0 && !!ctx.modeFragment;

/** Phrase du constat, écrite par le code à partir du résultat structuré. Formulation du message type de Tim (2026-10-02). */
export function visibilitySentence(ctx: ClaimContext): string {
  const target = ctx.clientPhrase ? `un cabinet accompagnant ${ctx.clientPhrase}` : "un cabinet";
  return `Premier constat : sur ${ctx.validRuns} recherches effectuées dans ${ctx.modeFragment} pour trouver ${target}, ${ctx.firmName ?? "votre cabinet"} n’a été cité aucune fois.`;
}

/** Le modèle ne rédige pas le constat : toute phrase VISIBILITY qu'il propose est remplacée par la phrase encadrée, ou retirée si le verdict ne l'établit pas. */
export function frameVisibility(sentences: DraftSentence[], ctx: ClaimContext): DraftSentence[] {
  const rest = sentences.filter((s) => s.kind !== "VISIBILITY");
  if (!visibilityRequired(ctx)) return rest;
  const framed: DraftSentence = { id: "visibility", kind: "VISIBILITY", text: visibilitySentence(ctx), evidence_ids: [] };
  const at = Math.max(rest.findIndex((s) => s.kind === "OBSERVATION"), rest.findIndex((s) => s.kind === "GREETING"));
  return [...rest.slice(0, at + 1), framed, ...rest.slice(at + 1)];
}

export function renderBody(sentences: DraftSentence[]): string {
  const blocks: string[] = [];
  let current: string[] = [];
  let lastGroup = "";
  const group = (k: SentenceKind) => (k === "GREETING" ? "g" : k === "SIGNATURE" ? "s" : k === "TRANSPARENCY" ? "t" : k === "CTA" || k === "AUDIT_LINK" ? "c" : k === "KEYWORDS" ? "k" : k === "VISIBILITY" ? "v" : "o");
  for (const s of sentences) {
    const g = group(s.kind);
    if (g !== lastGroup && current.length) {
      blocks.push(current.join(" "));
      current = [];
    }
    current.push(s.text);
    lastGroup = g;
  }
  if (current.length) blocks.push(current.join(" "));
  return blocks.join("\n\n");
}
