#!/usr/bin/env node
/* Mesure le registre d'écriture d'un texte, pour cibler les réécritures.
   Il compare, il ne juge pas, et il ne casse aucun build.

   Usage : node mesure.mjs <fichier|dossier> [...]
   Lit .md, .mdx, .txt. Un dossier est parcouru récursivement.

   L'étalon vient de trois pages réécrites par Tim les 2026-08-18 (hypnose,
   marché du vapotage, cigarette et joints). Ce qui les sépare d'un texte
   écrit par un agent, mesuré sur ces trois paires avant/après :

   - la longueur de PHRASE est la même, 18 mots de médiane des deux côtés ;
   - le PARAGRAPHE tombe de 36 à 25 mots ;
   - les MODALISATEURS passent de 0 à 19 pour 1000 mots. Cette colonne s'affiche
     mais ne compte pas dans les écarts : une page qui constate l'absence totale
     d'étude n'a rien à nuancer, et lui coller des « peut-être » l'abîmerait.
   - « % » et « € » ne sont plus collés au chiffre.

   Voir SKILL.md pour ce que chaque colonne veut dire. */

import { readdirSync, readFileSync, statSync } from "node:fs";
import { join } from "node:path";

/* Les seuils sont les plafonds relevés sur les pages écrites par Tim lui-même,
   pas un idéal : sa page la plus dense est à 29 mots de paragraphe et 36 mots
   pour sa phrase la plus longue. Viser 25, refuser au-delà de 29. */
const CIBLE = { phraseMediane: 13, paraMediane: 29, phraseMax: 36, modalisateurs: 12 };

/* `\b` est piégeux en français : « ê » n'est pas un caractère de mot pour le
   moteur d'expressions, donc « enquêtes » offre une frontière juste avant
   « tes » et se compte comme un tutoiement. Les bornes s'écrivent donc à la
   main, sur l'alphabet accentué. */
const AVANT = "(?<![A-Za-zÀ-ÿ])";
const APRES = "(?![A-Za-zÀ-ÿ])";

const MODALISATEURS = new RegExp(
  AVANT +
    "(g[ée]n[ée]ralement|notamment|semble|semblent|peut|peuvent|souvent|selon|environ|toutefois|cependant|principalement|appara[îi]t|plut[ôo]t|parfois|certains|certaines|n[ée]cessairement|forc[ée]ment)" +
    APRES,
  "gi",
);

const TUTOIEMENT = new RegExp(AVANT + "(tu|ton|tes|toi)" + APRES, "gi");

function corpsUtile(texte) {
  const sansFm = texte.replace(/^---[\s\S]*?\n---\n/, "");
  return sansFm
    .split("\n")
    .filter((l) => !/^\s*(#|\||>|\*|-\s|\d+\.)/.test(l))
    .join("\n");
}

function mediane(xs) {
  if (!xs.length) return 0;
  const t = [...xs].sort((a, b) => a - b);
  const m = t.length >> 1;
  return t.length % 2 ? t[m] : (t[m - 1] + t[m]) / 2;
}

export function mesurer(texte) {
  const corps = corpsUtile(texte);
  const plat = corps.replace(/\*\*|\[\[|\]\]|\[|\]\([^)]*\)/g, "").replace(/\s+/g, " ");

  const phrases = plat.split(/(?<=[.!?]) /).filter((p) => p.split(" ").length > 3);
  const motsPhrase = phrases.map((p) => p.split(" ").length);
  const paras = corps.split(/\n\s*\n/).filter((p) => p.split(/\s+/).length > 8);
  const motsPara = paras.map((p) => p.split(/\s+/).length);

  const mots = motsPhrase.reduce((a, b) => a + b, 0) || 1;

  return {
    mots,
    phraseMediane: mediane(motsPhrase),
    paraMediane: mediane(motsPara),
    phraseMax: Math.max(0, ...motsPhrase),
    modalisateurs: Math.round(((corps.match(MODALISATEURS) ?? []).length / mots) * 1000),
    colles: (corps.match(/\d\s?(%|€)/g) ?? []).filter((s) => !/\s/.test(s)).length,
    tutoiement: (corps.match(TUTOIEMENT) ?? []).length,
  };
}

function fichiers(cible) {
  if (statSync(cible).isFile()) return [cible];
  return readdirSync(cible)
    .flatMap((e) => (statSync(join(cible, e)).isDirectory() ? fichiers(join(cible, e)) : [join(cible, e)]))
    .filter((f) => /\.(md|mdx|txt)$/.test(f));
}

const cibles = process.argv.slice(2);
if (cibles.length === 0) {
  console.error("usage : node mesure.mjs <fichier|dossier ...>");
  process.exit(2);
}

const lignes = [];
for (const cible of cibles) {
  for (const f of fichiers(cible)) {
    const m = mesurer(readFileSync(f, "utf-8"));
    const ecart =
      (m.phraseMediane > CIBLE.phraseMediane ? 1 : 0) +
      (m.paraMediane > CIBLE.paraMediane ? 1 : 0) +
      (m.phraseMax > CIBLE.phraseMax ? 1 : 0) +
      (m.colles > 0 ? 1 : 0);
    lignes.push({ f, ...m, ecart });
  }
}

lignes.sort((a, b) => b.ecart - a.ecart || b.paraMediane - a.paraMediane);
console.log(
  `${"fichier".padEnd(46)} ${"mots".padStart(5)} ${"phr.méd".padStart(8)} ${"para".padStart(5)} ${"phr.".padStart(5)} ${"mod.".padStart(5)} ${"collé".padStart(5)} ${"tu".padStart(3)} écarts`,
);
for (const l of lignes) {
  console.log(
    `${l.f.slice(-46).padEnd(46)} ${String(l.mots).padStart(5)} ${String(l.phraseMediane).padStart(8)} ${String(l.paraMediane).padStart(5)} ${String(l.phraseMax).padStart(5)} ${String(l.modalisateurs).padStart(5)} ${String(l.colles).padStart(5)} ${String(l.tutoiement).padStart(3)}   ${"■".repeat(l.ecart)}`,
  );
}
const moy = (k) => (lignes.reduce((a, l) => a + l[k], 0) / lignes.length).toFixed(1);
console.log(
  `\n${lignes.length} fichiers. Médiane de paragraphe moyenne ${moy("paraMediane")} (cible ${CIBLE.paraMediane}), ` +
    `modalisateurs ${moy("modalisateurs")} pour 1000 mots (cible ${CIBLE.modalisateurs}), ` +
    `sur ${lignes.length} pages.`,
);
