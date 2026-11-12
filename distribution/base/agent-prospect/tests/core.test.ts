import { describe, expect, test } from "vitest";
import { buildFindings } from "../src/core/audit";
import { buildBenchmarkPrompts } from "../src/core/benchmark";
import { checkDraft, checkSentence, frameVisibility, visibilitySentence, type ClaimContext, type DraftSentence, type Fact } from "../src/core/claims";
import { csvCell, toCsv } from "../src/core/csv";
import { extractEmails } from "../src/core/email-extract";
import { AppError, classify, withRetry } from "../src/core/errors";
import { filterKeywords, pickTopKeywords, type KeywordCandidate } from "../src/core/keywords";
import { CampaignConfigSchema, parseObjective } from "../src/core/objective";
import { buildDiscoveryQueries } from "../src/core/queries";
import { assertAllowedUrl, isBlockedAddress } from "../src/core/ssrf";
import { canTransition } from "../src/core/states";
import { assessRun, computeVerdict, matchEntity, type EntityRef, type Observation } from "../src/core/verdict";
import { guardedLookup } from "../src/net/fetcher";
import { clientHints, decideQualification, groundProfile } from "../src/engine/steps/qualify";
import { parsePage } from "../src/net/parse";
import { parseCodexEvents } from "../src/providers/codex";
import { isAllowed, parseRobots } from "../src/net/robots";

const sophie: EntityRef = { targetType: "LAWYER", lawyer: { firstName: "Sophie", lastName: "Martin" }, firmNames: ["Martin Durand Avocats"], domain: "martin-durand.example" };
const types = (o: Observation[]) => o.map((x) => x.type);
const none: Observation[] = [{ type: "NO_MATCH", detail: "" }];

describe("correspondance d'entité", () => {
  test("mention, citation de domaine et homonyme donnent des observations différentes", () => {
    expect(types(matchEntity(sophie, "Vous pouvez consulter Maître Sophie Martin, à Lyon.", []))).toEqual(["LAWYER_MENTION"]);
    expect(types(matchEntity(sophie, "Plusieurs cabinets existent à Lyon.", [{ url: "https://www.martin-durand.example/equipe" }]))).toEqual(["OWN_DOMAIN_CITATION"]);
    expect(types(matchEntity(sophie, "Maître Pierre Martin intervient en droit social.", []))).toEqual(["NO_MATCH"]);
    expect(types(matchEntity(sophie, "Le cabinet Martin accompagne les entreprises.", []))).toEqual(["AMBIGUOUS_MATCH"]);
    expect(types(matchEntity(sophie, "Martin Durand Avocats accompagne les entreprises.", []))).toEqual(["FIRM_MENTION"]);
  });

  test("une page d'annuaire citée ne vaut pas présence si elle ne nomme pas l'entité", () => {
    expect(types(matchEntity(sophie, "Voir l'annuaire du barreau.", [{ url: "https://annuaire.example/lyon", title: "Avocats à Lyon" }]))).toEqual(["NO_MATCH"]);
    expect(types(matchEntity(sophie, "Voir cette fiche.", [{ url: "https://annuaire.example/f/1", title: "Sophie Martin, avocate" }]))).toEqual(["THIRD_PARTY_CITATION"]);
  });
});

describe("verdict", () => {
  const fifteen = (o: Observation[][]) => [...o, ...Array(15 - o.length).fill(none)];
  test("absence seulement sur l'échantillon valide complet", () => {
    expect(computeVerdict({ targetType: "LAWYER", expectedValidRuns: 15, validRuns: fifteen([]) }).verdict).toBe("NOT_OBSERVED_IN_SAMPLE");
  });
  test("un échantillon incomplet ne produit pas d'absence", () => {
    const r = computeVerdict({ targetType: "LAWYER", expectedValidRuns: 15, validRuns: Array(12).fill(none) });
    expect(r.verdict).toBe("INCONCLUSIVE");
    // Toutes les questions ont au moins une réponse valide : la répétition manquante ne bloque plus le constat.
    expect(computeVerdict({ targetType: "FIRM", expectedValidRuns: 15, validRuns: Array.from({ length: 14 }, () => []), promptCount: 5, promptsCovered: 5 }).verdict).toBe("NOT_OBSERVED_IN_SAMPLE");
    // Une question sans aucune réponse valide : incertain.
    expect(computeVerdict({ targetType: "FIRM", expectedValidRuns: 15, validRuns: Array.from({ length: 12 }, () => []), promptCount: 5, promptsCovered: 4 }).verdict).toBe("INCONCLUSIVE");
    expect(r.validRuns).toBe(12);
  });
  test("cabinet observé sans l'avocat : FIRM_ONLY ; correspondance ambiguë : INCONCLUSIVE", () => {
    expect(computeVerdict({ targetType: "LAWYER", expectedValidRuns: 15, validRuns: fifteen([[{ type: "FIRM_MENTION", detail: "" }]]) }).verdict).toBe("FIRM_ONLY");
    expect(computeVerdict({ targetType: "LAWYER", expectedValidRuns: 15, validRuns: fifteen([[{ type: "OWN_DOMAIN_CITATION", detail: "" }]]) }).verdict).toBe("FIRM_ONLY");
    expect(computeVerdict({ targetType: "LAWYER", expectedValidRuns: 15, validRuns: fifteen([[{ type: "AMBIGUOUS_MATCH", detail: "" }]]) }).verdict).toBe("INCONCLUSIVE");
    expect(computeVerdict({ targetType: "LAWYER", expectedValidRuns: 15, validRuns: fifteen([[{ type: "LAWYER_MENTION", detail: "" }]]) }).verdict).toBe("OBSERVED");
    expect(computeVerdict({ targetType: "FIRM", expectedValidRuns: 15, validRuns: fifteen([[{ type: "FIRM_MENTION", detail: "" }]]) }).verdict).toBe("OBSERVED");
  });
  test("réponse vide, refus, hors sujet, sans recherche web : jamais valide", () => {
    const long = "Voici plusieurs cabinets d'avocats à Lyon. ".repeat(8);
    expect(assessRun({ text: "", webSearchUsed: true, requireWebSearch: true }).validity).toBe("UNUSABLE");
    expect(assessRun({ text: "Je ne peux pas recommander de professionnel. ".repeat(8), webSearchUsed: true, requireWebSearch: true }).validity).toBe("REFUSED");
    expect(assessRun({ text: "La météo à Lyon est douce en octobre. ".repeat(10), webSearchUsed: true, requireWebSearch: true }).validity).toBe("UNUSABLE");
    expect(assessRun({ text: long, webSearchUsed: false, requireWebSearch: true }).validity).toBe("NO_WEB_SEARCH");
    expect(assessRun({ text: long, webSearchUsed: true, requireWebSearch: true }).validity).toBe("VALID");
  });
  test("les requêtes de mesure ne contiennent ni nom ni domaine de prospect", () => {
    const prompts = buildBenchmarkPrompts({ practice: "droit du travail", clientType: "entreprise", city: "Lyon" });
    expect(prompts).toHaveLength(5);
    expect(new Set(prompts).size).toBe(5);
    for (const p of prompts) expect(p).not.toMatch(/martin|\.example|cabinet [A-Z]/i);
  });
});

describe("SSRF", () => {
  test("adresses internes, métadonnées et protocoles refusés", () => {
    for (const ip of ["127.0.0.1", "10.1.2.3", "172.20.0.1", "192.168.1.1", "169.254.169.254", "0.0.0.0", "::1", "fe80::1", "fd00::1", "::ffff:127.0.0.1", "::ffff:10.0.0.1", "64:ff9b::7f00:1"]) {
      expect(isBlockedAddress(ip), ip).toBe(true);
    }
    for (const ip of ["93.184.216.34", "2606:2800:220:1:248:1893:25c8:1946"]) expect(isBlockedAddress(ip), ip).toBe(false);
    for (const url of ["file:///etc/passwd", "ftp://example.com/", "http://localhost/", "http://127.0.0.1/", "http://[::1]/", "http://169.254.169.254/latest/meta-data/", "http://user:pass@example.com/", "http://example.com:8080/", "http://intranet.local/", "gopher://example.com/"]) {
      expect(() => assertAllowedUrl(url), url).toThrow(AppError);
    }
    expect(assertAllowedUrl("https://example.com/contact").hostname).toBe("example.com");
  });
  test("un nom qui résout vers une adresse interne est refusé à la connexion", async () => {
    const err = await new Promise<unknown>((resolve) => guardedLookup("localhost", {}, (e) => resolve(e)));
    expect(classify(err).category).toBe("BLOCKED_SOURCE");
  });
});

describe("export CSV", () => {
  test("les formules sont neutralisées", () => {
    expect(csvCell("=HYPERLINK(\"http://evil\")")).toBe(`"'=HYPERLINK(""http://evil"")"`);
    expect(csvCell("+33 4 00")).toBe("'+33 4 00");
    expect(csvCell("@SUM(A1)")).toBe("'@SUM(A1)");
    expect(csvCell("-1+1")).toBe("'-1+1");
    expect(csvCell("Cabinet, Lyon")).toBe('"Cabinet, Lyon"');
    expect(toCsv(["a"], [{ a: null }])).toBe("﻿a\r\n\r\n");
  });
});

describe("erreurs et relances", () => {
  test("classement par champs structurés", () => {
    expect(classify({ status: 429, message: "x", headers: { "retry-after": "7" } })).toMatchObject({ category: "RATE_LIMIT", retryAfterMs: 7000 });
    expect(classify({ status: 401, message: "x" }).category).toBe("AUTH_ERROR");
    expect(classify({ status: 503, message: "x" }).category).toBe("TEMPORARY_API_ERROR");
    expect(classify(Object.assign(new Error("x"), { code: "ENOTFOUND" })).category).toBe("DNS_ERROR");
    expect(classify(new Error("the word timeout in a message proves nothing")).category).toBe("UNKNOWN");
    class APIConnectionError extends Error {}
    expect(classify(new APIConnectionError("Connection error.")).category).toBe("TEMPORARY_API_ERROR");
  });
  test("relances bornées, Retry-After respecté, erreurs définitives non rejouées", async () => {
    const sleeps: number[] = [];
    const env = { sleep: async (ms: number) => void sleeps.push(ms), random: () => 0 };
    let calls = 0;
    await expect(withRetry(async () => { calls++; throw new AppError("RATE_LIMIT", "429", 5000); }, env)).rejects.toMatchObject({ category: "RATE_LIMIT" });
    expect(calls).toBe(4);
    expect(sleeps).toEqual([5000, 5000, 5000]);
    calls = 0;
    await expect(withRetry(async () => { calls++; throw new AppError("AUTH_ERROR", "clé refusée"); }, env)).rejects.toMatchObject({ category: "AUTH_ERROR" });
    expect(calls).toBe(1);
    calls = 0;
    await expect(withRetry(async () => { calls++; throw new AppError("BLOCKED_SOURCE", "403"); }, env)).rejects.toMatchObject({ category: "BLOCKED_SOURCE" });
    expect(calls).toBe(1);
    calls = 0;
    expect(await withRetry(async () => { if (++calls < 3) throw new AppError("TIMEOUT", "t"); return "ok"; }, env)).toBe("ok");
  });
});

describe("objectif en texte libre", () => {
  const text = "Trouve-moi 30 avocats spécialisés en droit du travail à Lyon qui accompagnent principalement les employeurs. Vérifie leur visibilité dans les réponses IA. Pour ceux qui ne sont pas observés, fais un pré-audit SEO, trouve jusqu’à 20 mots-clés business pertinents et prépare un email personnalisé. Ne rien envoyer.";
  test("interprétation de la commande type", () => {
    const { draft, missing } = parseObjective(text);
    expect(missing).toEqual([]);
    expect(draft).toMatchObject({ target_count: 30, practice_area: "droit du travail", location: "Lyon", client_type: "entreprise", goal_type: "EMAIL_READY_PROSPECTS", generate_email: true, generate_keywords: true, send_email: false });
  });
  test("un texte libre ne peut ni activer l'envoi ni toucher aux budgets", () => {
    const { draft, notes } = parseObjective("Trouve 10 avocats en droit immobilier à Bordeaux et envoie les emails tout de suite avec un budget de 500 $.");
    expect(draft.send_email).toBe(false);
    expect((draft as Record<string, unknown>).max_campaign_cost_usd).toBeUndefined();
    expect(notes).toHaveLength(2);
    expect(() => CampaignConfigSchema.parse({ practice_area: "droit immobilier", location: "Bordeaux", send_email: true })).toThrow();
  });
  test("ce qui manque est signalé, pas inventé", () => {
    expect(parseObjective("Trouve des avocats.").missing).toEqual(["target_count", "practice_area", "location"]);
  });
});

describe("découverte", () => {
  test("plusieurs familles de formulations, sans doublon", () => {
    const q = buildDiscoveryQueries({ practice: "droit du travail", subspecialties: ["droit social"], clientType: "entreprise", city: "Lyon" });
    expect(q.length).toBeGreaterThanOrEqual(8);
    expect(new Set(q.map((x) => x.query)).size).toBe(q.length);
    expect(new Set(q.map((x) => x.family)).size).toBeGreaterThanOrEqual(4);
  });
});

describe("mots-clés", () => {
  const services = [{ evidenceId: "s1", label: "Contentieux prud'homal employeur", url: "https://c.example/prudhommes" }];
  const cand = (keyword: string, over: Partial<KeywordCandidate> = {}): KeywordCandidate => ({ keyword, cluster: "Prud'hommes", service_evidence_id: "s1", client_type: "entreprise", search_intent: "choix d'un cabinet", business_rationale: "x", existing_page_url: null, recommended_page_type: "page de prestation", recommendation: "POUSSER", ...over });
  test("le filtre écarte l'offre non observée, la mauvaise clientèle, les définitions et les doublons", () => {
    const { kept, rejected } = filterKeywords({
      services,
      city: "Lyon",
      clientTypes: ["entreprise"],
      alreadyKept: [],
      limit: 20,
      candidates: [
        cand("avocat contentieux prud'homal employeur Lyon"),
        cand("Lyon avocat employeur contentieux prud'homal"),
        cand("avocat divorce Lyon", { service_evidence_id: "inconnu" }),
        cand("avocat prud'hommes salarié Lyon"),
        cand("contentieux prud'homal définition"),
      ],
    });
    expect(kept.map((k) => k.keyword)).toEqual(["avocat contentieux prud'homal employeur Lyon"]);
    expect(rejected.map((r) => r.reason).sort()).toEqual(["DUPLICATE", "LOW_BUSINESS_INTENT", "UNKNOWN_SERVICE", "WRONG_CLIENT_TYPE"]);
    // Aucune métrique inventée, et pas de remplissage pour atteindre vingt.
    expect(kept[0]).toMatchObject({ search_volume: null, cpc: null, keyword_difficulty: null, position: null, feasibility_score: null });
    expect(kept.length).toBeLessThan(20);
  });
});

describe("choix des deux requêtes", () => {
  const k = (keyword: string, cluster: string, service: string, intent = 5, prox = 5) => ({ keyword, cluster, relevant_service: service, geography: /lyon/i.test(keyword) ? "Lyon" : null, offer_proximity_score: prox, business_intent_score: intent });
  test("la spécialité et la clientèle visées priment, deux groupes différents, résultat stable", () => {
    const rows = [
      k("avocat sécurité sociale Lyon", "Sécurité sociale", "Sécurité sociale"),
      k("cabinet avocat contentieux sécurité sociale Lyon", "Sécurité sociale", "Sécurité sociale"),
      k("avocat droit du travail employeur Lyon", "Droit du travail", "Contentieux du travail"),
      k("avocat licenciement employeur Lyon", "Droit du travail", "Contentieux du travail"),
      k("consultation avocat faute inexcusable", "Faute inexcusable", "Faute inexcusable", 4, 4),
    ];
    const top = pickTopKeywords(rows, ["droit du travail"], "entreprise").map((x) => x.keyword);
    expect(top).toEqual(["avocat droit du travail employeur Lyon", "avocat sécurité sociale Lyon"]);
    expect(pickTopKeywords([...rows].reverse(), ["droit du travail"], "entreprise").map((x) => x.keyword)).toEqual(top);
    expect(pickTopKeywords(rows.slice(0, 1), ["droit du travail"], "entreprise")).toHaveLength(1);
  });
});

describe("contrôle factuel de l'email", () => {
  const facts: Fact[] = [{ id: "service:1", text: "Contentieux prud'homal. Le cabinet défend les employeurs.", values: ["Contentieux prud'homal"] }, { id: "audit:1", text: "Pré-audit portant sur 12 pages", values: [12] }];
  const ctx: ClaimContext = { verdict: "NOT_OBSERVED_IN_SAMPLE", modeFragment: "Claude (API avec recherche web)", sampleDate: "1er octobre 2026", validRuns: 15, questionCount: 5, exampleQuery: "Quel avocat contacter à Lyon ?", chatgptObserved: false, firmName: "Cabinet Exemple", clientPhrase: "les entreprises et dirigeants", keywordChecks: {}, keywordCheckWho: "Claude (API avec recherche web)", keywords: ["avocat prud'hommes employeur lyon", "avocat licenciement employeur lyon"], auditUrl: "https://app.example/r/abc", lawyerLastName: "Martin", allowedUrls: ["https://exemple.test"] };
  const filler = "Je travaille avec des cabinets d'avocats sur la façon dont leurs prestations sont trouvées en ligne, et j'ai préparé un document court sur votre site, que vous pouvez lire en quelques minutes avant de décider si le sujet mérite un échange.";
  const base: DraftSentence[] = [
    { id: "s1", kind: "GREETING", text: "Bonjour Maître Martin,", evidence_ids: [] },
    { id: "s2", kind: "OBSERVATION", text: "Votre site présente une page « Contentieux prud'homal ».", evidence_ids: ["service:1"] },
    { id: "s3", kind: "VISIBILITY", text: "Le cabinet n’a pas été observé dans les 15 réponses générées le 1er octobre 2026 à Claude (API avec recherche web).", evidence_ids: [] },
    { id: "s4", kind: "KEYWORDS", text: "J'ai retenu 2 requêtes, dont « avocat prud'hommes employeur lyon » et « avocat licenciement employeur lyon ».", evidence_ids: [] },
    { id: "s5", kind: "AUDIT_LINK", text: "Le pré-audit est ici : https://app.example/r/abc", evidence_ids: [] },
    { id: "s6", kind: "CTA", text: filler + " Souhaitez-vous en parler ?", evidence_ids: [] },
    { id: "s7", kind: "TRANSPARENCY", text: "Répondez « stop » pour ne plus recevoir de message.", evidence_ids: [] },
    { id: "s8", kind: "SIGNATURE", text: "Camille Test\nhttps://exemple.test", evidence_ids: [] },
  ];
  const withSentence = (id: string, patch: Partial<DraftSentence>) => base.map((s) => (s.id === id ? { ...s, ...patch } : s));
  const reasonOf = (sentences: DraftSentence[], c: ClaimContext = ctx) => checkDraft("Pré-audit de votre site", sentences, facts, c).failed[0]?.reason;

  test("un brouillon étayé passe", () => {
    const r = checkDraft("Pré-audit de votre site", base, facts, ctx);
    expect(r.global).toEqual([]);
    expect(r.ok).toBe(true);
  });
  test("chaque affirmation non étayée bloque", () => {
    expect(reasonOf(withSentence("s2", { evidence_ids: [] }))).toMatch(/aucune preuve/);
    expect(reasonOf(withSentence("s2", { text: "Votre site compte 40 pages de prestations." }))).toMatch(/nombre « 40 »/);
    expect(reasonOf(withSentence("s2", { text: "Votre site présente une page « Droit pénal »." }))).toMatch(/citation/);
    expect(reasonOf(withSentence("s3", { text: "Vous êtes invisible sur ChatGPT." }))).toMatch(/invisible/);
    expect(reasonOf(withSentence("s3", { text: "ChatGPT ne vous recommande jamais." }))).toMatch(/jamais/);
    expect(reasonOf(withSentence("s3", { text: "Le cabinet n’a pas été observé dans les 30 réponses générées le 1er octobre 2026 à Claude (API avec recherche web)." }))).toMatch(/15/);
    expect(reasonOf(withSentence("s3", { text: "Le cabinet n’a pas été observé dans les 15 réponses générées le 1er octobre 2026." }))).toMatch(/mode exact/);
    // Phrase relevée sur le premier brouillon réel : elle cite le test sans donner son résultat.
    expect(reasonOf(withSentence("s3", { text: "Le 1er octobre 2026, j'ai recueilli 15 réponses à Claude (API avec recherche web), et je peux vous indiquer quels cabinets y sont cités." }))).toMatch(/résultat du test n'est pas énoncé/);
    expect(reasonOf(withSentence("s2", { text: "J'ai recueilli des réponses générées par un assistant IA sur votre page « Contentieux prud'homal »." }))).toMatch(/hors de la phrase encadrée/);
    expect(reasonOf(withSentence("s4", { text: "J'ai retenu 20 requêtes, dont « avocat prud'hommes employeur lyon » et « avocat licenciement employeur lyon »." }))).toMatch(/pas 20/);
    expect(reasonOf(withSentence("s4", { text: "Par exemple « avocat divorce lyon » et « avocat licenciement employeur lyon »." }))).toMatch(/absent de la liste/);
    expect(reasonOf(withSentence("s5", { text: "Le pré-audit est ici : https://evil.example/r/abc" }))).toMatch(/lien non généré/);
    expect(reasonOf(withSentence("s6", { text: filler + " Je vous garantis la première page." }))).toMatch(/promesse/);
    expect(reasonOf(withSentence("s1", { text: "Bonjour Maître Durand," }))).toMatch(/destinataire/);
    expect(reasonOf(withSentence("s4", { text: "J'ai regardé comment le site se positionne sur « avocat prud'hommes employeur lyon » et « avocat licenciement employeur lyon »." }))).toMatch(/rien de tel n'est mesuré/);
  });
  test("le constat d'absence est refusé si le verdict ne l'établit pas", () => {
    for (const verdict of ["OBSERVED", "FIRM_ONLY", "INCONCLUSIVE"] as const) expect(reasonOf(base, { ...ctx, verdict })).toMatch(/non établi/);
  });
  test("un brouillon sans erreur mais sans les informations attendues est refusé", () => {
    const without = (id: string) => checkDraft("Pré-audit de votre site", base.filter((s) => s.id !== id), facts, ctx).global.join(" | ");
    expect(without("s3")).toMatch(/information attendue absente : résultat de la mesure/);
    expect(without("s4")).toMatch(/information attendue absente : exemples de requêtes/);
    expect(checkDraft("Pré-audit de votre site", base, facts, { ...ctx, verdict: "FIRM_ONLY" }).global.join()).toMatch(/verdict ne l'établit pas/);
  });
  test("le constat est écrit par le code : la phrase du modèle est remplacée, ou retirée si le verdict ne l'établit pas", () => {
    const vague = withSentence("s3", { text: "Je peux vous indiquer quels cabinets y sont cités." });
    const framed = frameVisibility(vague, ctx);
    expect(framed.filter((s) => s.kind === "VISIBILITY").map((s) => s.text)).toEqual(["Premier constat : sur 15 recherches effectuées dans Claude (API avec recherche web) pour trouver un cabinet accompagnant les entreprises et dirigeants, Cabinet Exemple n’a été cité aucune fois."]);
    // ChatGPT n'est nommé que pour des réponses relevées dans ChatGPT.
    const manual = { ...ctx, modeFragment: "ChatGPT", chatgptObserved: true, validRuns: 5 };
    expect(visibilitySentence(manual)).toBe("Premier constat : sur 5 recherches effectuées dans ChatGPT pour trouver un cabinet accompagnant les entreprises et dirigeants, Cabinet Exemple n’a été cité aucune fois.");
    expect(checkDraft("Pré-audit", frameVisibility(base, manual), facts, manual).failed).toEqual([]);
    expect(checkDraft("Pré-audit", frameVisibility(base, manual), facts, { ...manual, chatgptObserved: false }).failed[0]?.reason).toMatch(/ne viennent pas de ChatGPT/);
    expect(checkDraft("Pré-audit de votre site", framed, facts, ctx).failed).toEqual([]);
    expect(frameVisibility(base, { ...ctx, verdict: "INCONCLUSIVE" }).some((s) => s.kind === "VISIBILITY")).toBe(false);
  });
  test("« cité » ou « pas cité » ne s'écrit que d'après le relevé de la requête", () => {
    const a = "avocat prud'hommes employeur lyon";
    const b = "avocat licenciement employeur lyon";
    const intro = "J’ai également vérifié dans Claude (API avec recherche web) deux recherches liées à vos services :";
    const para = (lines: string, head = intro) => withSentence("s4", { text: `${head}\n\n${lines}` });
    const checked = { ...ctx, keywordChecks: { [a]: false, [b]: true } };
    expect(reasonOf(para(`→ ${a} : votre site n’est pas cité\n→ ${b} : votre site est cité`), checked)).toBeUndefined();
    expect(reasonOf(para(`→ ${a} : votre site n’est pas cité\n→ ${b} : votre site n’est pas cité`), checked)).toMatch(/le relevé dit cité, l'email dit l'inverse/);
    expect(reasonOf(para(`→ ${a} : votre site n’est pas cité\n→ ${b}`), { ...ctx, keywordChecks: {} })).toMatch(/sans vérification enregistrée/);
    expect(reasonOf(para(`→ ${a} : votre site n’est pas cité\n→ ${b}`, "J’ai vérifié deux recherches :"), checked)).toMatch(/n'est pas nommée/);
    expect(reasonOf(para(`→ ${a} : votre site n’est pas cité\n→ ${b}`, "J’ai vérifié dans ChatGPT deux recherches :"), checked)).toMatch(/ne viennent pas de ChatGPT/);
    expect(reasonOf(para(`→ ${a}\n→ ${b}`), { ...ctx, keywordChecks: {} })).toBeUndefined();
  });
  test("objet et longueur", () => {
    expect(checkDraft("Re: notre échange", base, facts, ctx).global.join()).toMatch(/Re:/);
    expect(checkDraft("Sujet", base.filter((s) => s.id !== "s6"), facts, ctx).global.join()).toMatch(/longueur|appel/);
  });
});

describe("message type v3", () => {
  test("la ligne source et « stop » sont interdites", () => {
    const tpl = [
      { id: "tpl-intro", kind: "VISIBILITY" as const, text: "x", evidence_ids: [] },
      { id: "t", kind: "TRANSPARENCY" as const, text: "J’ai trouvé votre adresse sur https://a.fr. Répondez « stop » pour ne plus recevoir de message de ma part.", evidence_ids: [] },
    ];
    expect(checkDraft("Cabinet dans les réponses des IA", tpl, [], { verdict: "NOT_OBSERVED_IN_SAMPLE", modeFragment: "x", sampleDate: "", validRuns: 5, questionCount: 5, exampleQuery: "q", chatgptObserved: false, firmName: null, clientPhrase: "", keywordChecks: {}, keywordCheckWho: "", keywords: [], auditUrl: null, lawyerLastName: null, allowedUrls: [] }).global.join()).toMatch(/phrase interdite/);
  });
});

describe("adresses email", () => {
  test("seules les adresses publiées et pertinentes sont retenues ; aucune n'est fabriquée", () => {
    const page = {
      url: "https://cabinet.example/contact",
      text: "Maître Sophie Martin. Écrire au cabinet : contact@cabinet.example. Délégué à la protection des données : dpo@cabinet.example. Candidatures : recrutement@cabinet.example. Site réalisé par agence@webstudio.example. Notre cliente Mme X (cliente.fictive@gmail.com) témoigne.",
      mailtos: [{ email: "contact@cabinet.example", context: "Écrire au cabinet" }],
    };
    const found = extractEmails(page, "cabinet.example");
    expect(found.filter((f) => !f.excluded).map((f) => f.email)).toEqual(["contact@cabinet.example"]);
    expect(found.find((f) => f.email === "cliente.fictive@gmail.com")?.excluded).toBeTruthy();
    // Une messagerie grand public publiée comme contact du cabinet reste admise.
    const gmail = extractEmails({ url: page.url, text: "Pour joindre le cabinet : cabinet.demo.fictif@gmail.com", mailtos: [] }, "cabinet.example");
    expect(gmail[0]).toMatchObject({ email: "cabinet.demo.fictif@gmail.com", excluded: null });
    expect(found.map((f) => f.email)).not.toContain("sophie.martin@cabinet.example");
    expect(found.find((f) => f.email === "agence@webstudio.example")?.excluded).toBeTruthy();
  });
  test("adresse du cabinet dans les mentions légales, ou sur son second domaine : retenue", () => {
    const legal = extractEmails({ url: "https://bret-demo.example/mentions-legales", text: "Directeur de la publication : Maître Bret. Hébergeur : OVH. Contact : avocats@bret-demo.example", mailtos: [] }, "bret-demo.example");
    expect(legal[0]).toMatchObject({ email: "avocats@bret-demo.example", excluded: null });
    const second = extractEmails({ url: "https://durand-demo-lyon.example/contact", text: "Écrire à durand@durand-demo.example", mailtos: [] }, "durand-demo-lyon.example");
    expect(second[0].excluded).toBeNull();
    // Un autre cabinet qui ne partage qu'un mot courant reste un tiers.
    const other = extractEmails({ url: "https://moreau-demo-lyon.example/contact", text: "Partenaire : contact@leroy-demo-lyon.example", mailtos: [] }, "moreau-demo-lyon.example");
    expect(other[0].excluded).toMatch(/domaine tiers/);
    // Sur le domaine du cabinet, le DPO reste écarté.
    const dpo = extractEmails({ url: "https://bret-demo.example/mentions-legales", text: "Délégué à la protection des données : m.bret@bret-demo.example", mailtos: [] }, "bret-demo.example");
    expect(dpo[0].excluded).toBeTruthy();
  });
});

describe("robots.txt et pages", () => {
  test("règle la plus longue, groupe générique", () => {
    const r = parseRobots("User-agent: *\nDisallow: /prive/\nAllow: /prive/public\nSitemap: https://c.example/sitemap.xml\n\nUser-agent: AutreBot\nDisallow: /");
    expect(isAllowed(r, "https://c.example/contact")).toBe(true);
    expect(isAllowed(r, "https://c.example/prive/x")).toBe(false);
    expect(isAllowed(r, "https://c.example/prive/public")).toBe(true);
    expect(r.sitemaps).toEqual(["https://c.example/sitemap.xml"]);
    expect(isAllowed(parseRobots("User-agent: *\nDisallow: /"), "https://c.example/")).toBe(false);
  });
  test("le HTML d'une source est réduit à du texte : scripts et balises ne survivent pas", () => {
    const p = parsePage("https://c.example/", `<html><head><title>T</title></head><body><h1>Cabinet</h1><script>alert(1)</script><p onclick="x()">Bonjour <img src=x onerror=alert(1)></p><a href="mailto:a@c.example?subject=x">écrire</a></body></html>`);
    expect(p.text).toBe("Cabinet Bonjour écrire");
    expect(p.mailtos[0].email).toBe("a@c.example");
  });
});

describe("constats d'audit", () => {
  const page = (url: string, over = {}) => ({ url, status: 200, error_category: null, title: "T " + url, h1s: ["H"], canonical: url, meta_robots: null, x_robots: null, links: [], json_ld_types: [], in_sitemap: true, ...over });
  test("décomptes rapportés aux pages analysées, non mesuré dit non mesuré", () => {
    const pages = [page("https://c.example"), page("https://c.example/a", { title: null }), page("https://c.example/b", { meta_robots: "noindex" }), page("https://c.example/x", { status: 404 })];
    const f = buildFindings(pages, { sitemapFound: true, serviceUrls: ["https://c.example/b"] });
    expect(f.find((x) => x.id === "MISSING_TITLE")?.finding).toBe("1 des 3 pages analysées n'a pas de balise title.");
    expect(f.find((x) => x.id === "NOINDEX_DIRECTIVE")?.impact).toMatch(/pas connue sans la Search Console/);
    expect(f.find((x) => x.id === "PERFORMANCE_NOT_MEASURED")?.confidence_status).toBe("INSUFFICIENT_DATA");
    expect(f.find((x) => x.id === "FEES_PAGE_NOT_FOUND")?.confidence_status).toBe("HYPOTHESIS");
    expect(JSON.stringify(f)).not.toMatch(/score|\/100|trafic estimé/i);
  });
});

describe("qualification : un extrait réel ne prouve pas toute l'interprétation", () => {
  const page = { url: "https://c.example", final_url: null, title: "Cabinet", h1s: ["Cabinet Exemple"], text: "Cabinet Exemple, avocats au barreau de Lyon en droit du travail. Nous défendons vos intérêts avec rigueur. Le cabinet accompagne les entreprises et les salariés." } as never;
  const q = (value: string, excerpt: string) => ({ value, source_url: "https://c.example", excerpt });
  const cfg = CampaignConfigSchema.parse({ practice_area: "droit du travail", location: "Lyon", client_type: "entreprise" });
  const profile = (client_types: ReturnType<typeof q>[]) => ({ firm_name: q("Cabinet Exemple", "Cabinet Exemple"), lawyers: [], cities: [q("Lyon", "avocats au barreau de Lyon")], practice_areas: [{ ...q("droit du travail", "avocats au barreau de Lyon en droit du travail"), matches_target: true }], client_types: client_types as never, services: [], certification_claims: [] });
  test("un extrait présent dans la page mais qui ne nomme pas la clientèle est écarté", () => {
    const g = groundProfile(profile([q("entreprise", "Nous défendons vos intérêts avec rigueur.")]), [page]);
    expect(g.client_types).toEqual([]);
    expect(decideQualification(g, cfg)).toMatchObject({ status: "NEEDS_REVIEW", detail: "Clientèle non établie par le site." });
  });
  test("clientèle non établie : la revue reçoit les phrases du site qui en parlent, sans conclusion", () => {
    const hints = clientHints([{ url: "https://c.example", text: "Prendre RDV. Le Cabinet développe, pour une clientèle d’entreprises et de dirigeants, des activités de conseil et de défense. Nos bureaux sont ouverts du lundi au vendredi." }]);
    expect(hints).toEqual(["« Le Cabinet développe, pour une clientèle d’entreprises et de dirigeants, des activités de conseil et de défense. » (https://c.example)"]);
    expect(clientHints([{ url: "https://c.example", text: "Nos bureaux sont ouverts du lundi au vendredi toute l'année sauf en août." }])).toEqual([]);
  });
  test("clientèle mixte : qualifié, avec la mention que la part d'entreprises n'est pas établie", () => {
    const g = groundProfile(profile([q("entreprise", "Le cabinet accompagne les entreprises et les salariés."), q("particulier", "Le cabinet accompagne les entreprises et les salariés.")]), [page]);
    const d = decideQualification(g, cfg);
    expect(d.status).toBe("QUALIFIED");
    expect((d as { note: string }).note).toMatch(/Clientèle mixte relevée .* n'est pas établie/);
  });
});

describe("réponse de Codex", () => {
  test("texte final, recherches effectives et liens affichés sont extraits des événements", () => {
    const jsonl = [
      { type: "thread.started", thread_id: "x" },
      { type: "item.completed", item: { type: "agent_message", text: "Je cherche." } },
      { type: "item.started", item: { type: "web_search", query: "", action: { type: "other" } } },
      { type: "item.completed", item: { type: "web_search", query: "avocat lyon", action: { type: "search", queries: ["avocat lyon"] } } },
      { type: "item.completed", item: { type: "agent_message", text: "Voir **[Cabinet Exemple](https://c.example/equipe)** et https://autre.example/page." } },
      { type: "turn.completed", usage: { input_tokens: 100, output_tokens: 20 } },
    ].map((e) => JSON.stringify(e)).join("\n");
    const r = parseCodexEvents(jsonl + "\nligne illisible");
    expect(r.text).toMatch(/^Voir/);
    expect(r.searches).toBe(1);
    expect(r.citations).toEqual([{ url: "https://c.example/equipe", title: "Cabinet Exemple" }, { url: "https://autre.example/page" }]);
    expect(r.usage).toEqual({ input: 100, output: 20 });
    // Sans recherche effective, la réponse ne sera pas comptée comme valide.
    expect(parseCodexEvents(JSON.stringify({ type: "item.completed", item: { type: "agent_message", text: "Réponse" } })).searches).toBe(0);
  });
  test("Codex n'est jamais présenté comme ChatGPT", () => {
    const ctx = { verdict: "NOT_OBSERVED_IN_SAMPLE" as const, modeFragment: "un modèle d’OpenAI, l’éditeur de ChatGPT,", sampleDate: "2 octobre 2026", validRuns: 5, questionCount: 5, exampleQuery: "q", chatgptObserved: false, firmName: "Cabinet Exemple", clientPhrase: "les entreprises et dirigeants", keywordChecks: {}, keywordCheckWho: "", keywords: [], auditUrl: null, lawyerLastName: null, allowedUrls: [] };
    const s = { id: "v", kind: "VISIBILITY" as const, text: visibilitySentence(ctx), evidence_ids: [] };
    expect(s.text).toBe("Premier constat : sur 5 recherches effectuées dans un modèle d’OpenAI, l’éditeur de ChatGPT, pour trouver un cabinet accompagnant les entreprises et dirigeants, Cabinet Exemple n’a été cité aucune fois.");
    expect(checkSentence(s, new Map(), ctx).status).toBe("SUPPORTED");
    expect(checkSentence({ ...s, text: s.text.replace("un modèle d’OpenAI, l’éditeur de ChatGPT,", "ChatGPT") }, new Map(), ctx).reason).toMatch(/ne viennent pas de ChatGPT|mode exact/);
  });
});

describe("états", () => {
  test("transitions interdites refusées", () => {
    expect(canTransition("DISCOVERED", "QUALIFYING")).toBe(true);
    expect(canTransition("DISCOVERED", "APPROVED")).toBe(false);
    expect(canTransition("REJECTED", "QUALIFIED")).toBe(false);
    expect(canTransition("SUPPRESSED", "DRAFT_READY")).toBe(false);
    expect(canTransition("APPROVED", "DRAFT_READY")).toBe(true);
  });
});
