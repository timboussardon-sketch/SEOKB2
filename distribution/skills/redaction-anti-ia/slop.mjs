#!/usr/bin/env node
// Check mécanique des interdits observables de la règle mère (ton-de-voix § 0).
//
//   node slop.mjs <fichier...>            # .md .html .txt .ts
//   node slop.mjs --strict <fichier...>   # les WARN deviennent bloquants
//
// Ce script ne juge pas le style. Il cherche des chaînes et il compte des
// structures. Tout ce qu'il ne sait pas voir reste à la passe destructive :
// une phrase générique qui ne contient aucune chaîne bannie passe au vert ici
// et doit quand même sauter. Un vert n'est pas un bon à livrer.
//
// Sort 1 si un HARD est trouvé, ou si un WARN dépasse son seuil.

import { readFileSync } from "node:fs";

const argv = process.argv.slice(2);
const strict = argv.includes("--strict");
const fichiers = argv.filter((a) => !a.startsWith("--"));

if (!fichiers.length) {
  console.error("usage: node slop.mjs [--strict] <fichier...>");
  process.exit(2);
}

// ---------------------------------------------------------------- HARD
// Chaînes exactes. Aucune n'a d'usage légitime dans un livrable signé Tim.
const HARD = [
  [/l['’]idée est simple/gi, "« L'idée est simple »"],
  [/le fonctionnement (reste|est) simple/gi, "« le fonctionnement reste simple »"],
  [/c['’]est exactement/gi, "« C'est exactement »"],
  [/(ce|le chiffre) qui compte vraiment/gi, "« ce qui compte vraiment »"],
  [/\ben clair\b/gi, "« En clair »"],
  [/autrement dit/gi, "« Autrement dit »"],
  [/il est important de/gi, "« Il est important de »"],
  [/il convient de/gi, "« il convient de »"],
  [/cela souligne/gi, "« cela souligne »"],
  [/n['’]oublions pas/gi, "« n'oublions pas »"],
  [/force est de constater/gi, "« force est de constater »"],
  [/dans le paysage actuel/gi, "« dans le paysage actuel »"],
  [/dans un monde (en pleine|où)/gi, "« dans un monde en pleine évolution »"],
  [/à l['’]ère (du|de la|des)/gi, "« à l'ère de »"],
  [/construire progressivement/gi, "« construire progressivement »"],
  [/je m['’]occupe du reste/gi, "« je m'occupe du reste »"],
  [/^\s*(De plus|Par ailleurs|En outre|En définitive|Pour conclure)\b/gim, "transition générique"],
  [/—/g, "tiret cadratin"],
];

// ---------------------------------------------------------------- WARN
// Heuristiques. Un ou deux passent, une colonne est un gabarit.
const WARN = [
  [/,\s*jamais\s+/gi, "construction « X, jamais Y »", 1],
  [/\bpas\s+\w+,?\s+mais\b/gi, "opposition « pas X mais Y »", 1],
  [/\b(plutôt que|au lieu de)\b/gi, "opposition « plutôt que / au lieu de »", 2],
  [/\b(un|une|de|des)\s+vrai(e|es|s)?\s+\w+/gi, "« vrai » en épithète d'insistance", 1],
  [/\b(concrètement|en pratique|en réalité|en fait)\b/gi, "charnière de transition", 1],
  [/(?<![\wà-ÿ])(évidemment|bien sûr|naturellement)(?![\wà-ÿ])/gi, "adverbe de connivence", 1],
];

// Fin de paragraphe qui explique ce qu'on vient de lire. Marqueur n°1.
const CONCLUSION = /^(c['’]est (ce qui|aussi|exactement|précisément|pour ça|la raison)|voilà pourquoi|et c['’]est (ça|tout|bien))/i;

// Le texte analysé est nettoyé (balises retirées), donc ses numéros de ligne ne
// sont pas ceux du fichier. On retrouve la vraie ligne en cherchant l'extrait
// dans la source. Sans ça, le rapport envoie vers des lignes inexistantes.
function ligneSource(source, extrait) {
  const i = source.indexOf(extrait);
  if (i === -1) return null;
  return source.slice(0, i).split("\n").length;
}

function texteDe(fichier) {
  let brut = readFileSync(fichier, "utf8");
  if (/\.html?$/i.test(fichier)) {
    brut = brut
      .replace(/<(script|style)[\s\S]*?<\/\1>/gi, " ")
      .replace(/<!--[\s\S]*?-->/g, " ")
      .replace(/<[^>]+>/g, "\n");
  }
  // On ne juge pas ce qui est cité verbatim ni le code. Sans ça, un document qui
  // PARLE des chaînes bannies (rapport, doctrine, skill) se fait attraper sur ses
  // propres citations, et le rouge devient du bruit qu'on apprend à ignorer.
  brut = brut
    .replace(/```[\s\S]*?```/g, " ")     // blocs de code
    .replace(/`[^`\n]*`/g, " ")          // code en ligne
    .replace(/^\s*>.*$/gm, " ")          // citations markdown
    // Citation entre guillemets, sur une seule ligne : un « sans » fermant sur la
    // même ligne ne doit pas avaler le paragraphe suivant.
    .replace(/«[^»\n]{0,200}»/g, " ");
  return brut;
}

function paragraphes(texte) {
  return texte
    .split(/\n\s*\n+/)
    .map((p) => p.replace(/\s+/g, " ").trim())
    .filter((p) => p.length > 40 && /[a-zà-ÿ]{4}/i.test(p));
}

function derniereePhrase(p) {
  const phrases = p.split(/(?<=[.!?…])\s+/).filter(Boolean);
  return phrases[phrases.length - 1] || "";
}

const SEUIL_PHRASES = 0.40; // calibré le 2026-11-17 sur 80 textes : aucune alerte sur des articles publiés, 0.42-0.44 = prose de fiche
let codeSortie = 0;

for (const fichier of fichiers) {
  let texte, source;
  try {
    source = readFileSync(fichier, "utf8");
    texte = texteDe(fichier);
  } catch (e) {
    console.error(`✖ ${fichier} : ${e.message}`);
    codeSortie = 2;
    continue;
  }

  const hits = { hard: [], warn: [] };

  for (const [re, libelle] of HARD) {
    for (const m of texte.matchAll(re)) {
      const extrait = m[0].trim();
      hits.hard.push({ ligne: ligneSource(source, extrait), libelle, extrait });
    }
  }

  for (const [re, libelle, seuil] of WARN) {
    const n = [...texte.matchAll(re)].length;
    if (n > seuil) hits.warn.push({ libelle, n, seuil });
  }

  const paras = paragraphes(texte);
  const conclusions = paras.filter((p) => CONCLUSION.test(derniereePhrase(p)));
  if (conclusions.length > 0) {
    hits.warn.push({
      libelle: "conclusion posée en fin de paragraphe",
      n: conclusions.length,
      seuil: 0,
      exemples: conclusions.slice(0, 5).map((p) => derniereePhrase(p)),
    });
  }

  // Séries trop symétriques : longueurs de paragraphe trop resserrées.
  if (paras.length >= 4) {
    const L = paras.map((p) => p.length);
    const moy = L.reduce((a, b) => a + b, 0) / L.length;
    const ecart = Math.sqrt(L.reduce((a, b) => a + (b - moy) ** 2, 0) / L.length);
    const dispersion = ecart / moy;
    if (dispersion < 0.35) {
      hits.warn.push({
        libelle: `blocs trop réguliers (dispersion ${dispersion.toFixed(2)}, attendu > 0.35)`,
        n: paras.length,
        seuil: 0,
      });
    }
  }


  // Grappe locale : un tell isolé est survivable, trois familles différentes dans
  // un même paragraphe sont un gabarit (critère de densité, pas de présence).
  const familles = [...HARD.map(([re]) => re), ...WARN.map(([re]) => re)];
  const grappes = paras.filter((p) => {
    const n = familles.filter((re) => new RegExp(re.source, re.flags.replace("g", "")).test(p)).length;
    return n >= 3;
  });
  if (grappes.length > 0) {
    hits.warn.push({
      libelle: "grappe de tells (3 familles ou plus dans un même paragraphe)",
      n: grappes.length,
      seuil: 0,
      exemples: grappes.slice(0, 3).map((p) => p.slice(0, 90)),
    });
  }

  // Phrases de longueur trop uniforme sur l'ensemble du texte.
  const lg = paras
    .flatMap((p) => p.split(/(?<=[.!?…])\s+/))
    .map((f) => f.split(/\s+/).filter(Boolean).length)
    .filter((n) => n >= 3);
  if (lg.length >= 15) {
    const m = lg.reduce((a, b) => a + b, 0) / lg.length;
    const cv = Math.sqrt(lg.reduce((a, b) => a + (b - m) ** 2, 0) / lg.length) / m;
    if (cv < SEUIL_PHRASES) {
      hits.warn.push({
        libelle: `phrases de longueur trop uniforme (variation ${cv.toFixed(2)}, attendu > ${SEUIL_PHRASES})`,
        n: lg.length,
        seuil: 0,
      });
    }
  }

  const nHard = hits.hard.length;
  const nWarn = hits.warn.length;
  const etat = nHard ? "✖ HARD" : nWarn ? "▲ WARN" : "✔";
  console.log(`\n${etat}  ${fichier}  (${paras.length} paragraphes, ${texte.length} signes)`);

  for (const h of hits.hard) {
    const ou = h.ligne ? `l.${h.ligne}` : "l.?";
    console.log(`   ✖ ${ou}\t${h.libelle} : « ${h.extrait} »`);
  }
  for (const w of hits.warn) {
    console.log(`   ▲ ${w.libelle} : ${w.n} (seuil ${w.seuil})`);
    for (const ex of w.exemples || []) {
      const l = ligneSource(source, ex.slice(0, 40));
      console.log(`        ${l ? `l.${l}` : "l.?"}\t« ${ex} »`);
    }
  }

  if (nHard || (strict && nWarn)) codeSortie = 1;
}

if (codeSortie === 0) {
  console.log("\nAucun interdit observable. La passe destructive reste à faire : ce script ne voit pas une phrase générique.");
}
process.exit(codeSortie);
