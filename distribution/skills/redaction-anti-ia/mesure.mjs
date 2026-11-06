#!/usr/bin/env node
// Donne à voir le MOTEUR d'un texte, pas sa forme.
//
//   node mesure.mjs <fichier>                              # texte : unité = paragraphe
//   node mesure.mjs <fichier> --champ label,note           # data TS/JS : unité = valeur de champ
//   node mesure.mjs <fichier> --champ note --de 'slug: "ma-page"' --a 'complementTitre'
//
// CE QUE LE SCRIPT SAIT FAIRE : compter, et aligner en colonne. Un gabarit se
// voit à la colonne. Le script ne juge pas à ta place et il ne sait PAS
// détecter le moteur de démonstration (pattern 11) : aucune regex ne distingue
// « Il les laisse faire » qui conclut de « Il les laisse faire » qui constate.
// Tu lis les deux colonnes ci-dessous et tu tranches. Un script qui répondrait
// « 0 violation » ici serait un faux vert, et c'est pire que pas de script.

import { readFileSync } from "node:fs";

const [, , file, ...rest] = process.argv;
if (!file) {
  console.error("usage: node mesure.mjs <fichier> [--champ label,note] [--de 'ancre'] [--a 'ancre']");
  process.exit(1);
}
const opt = (n) => {
  const i = rest.indexOf(n);
  return i === -1 ? null : rest[i + 1];
};

let src = readFileSync(file, "utf8");

const de = opt("--de");
if (de) {
  const i = src.indexOf(de);
  if (i === -1) throw new Error(`ancre --de introuvable : ${de}`);
  src = src.slice(i);
}
const a = opt("--a");
if (a) {
  const j = src.indexOf(a, 1);
  if (j !== -1) src = src.slice(0, j);
}

// Découpe en phrases. Recolle les miettes que le guillemet fermant produit
// (« … ! » coupé après le !), sinon l'histogramme compte des phrases fantômes.
const phrases = (t) =>
  t
    .split(/(?<=[.!?»])\s+/)
    .filter(Boolean)
    .reduce((acc, m) => {
      if (acc.length && (m.length < 4 || /^[»"]/.test(m))) acc[acc.length - 1] += " " + m;
      else acc.push(m);
      return acc;
    }, []);
const coupe = (t, n) => (t.length > n ? t.slice(0, n - 1) + "…" : t);

function unitesDe(champ) {
  if (!champ) {
    return src
      .split(/\n\s*\n/)
      .map((p) => p.trim())
      .filter((p) => p && !/^[#|>-]/.test(p));
  }
  const re = new RegExp(`${champ}:\\s*"((?:[^"\\\\]|\\\\.)*)"`, "g");
  return [...src.matchAll(re)].map((m) => m[1].replace(/\\"/g, '"'));
}

const champs = (opt("--champ") || "").split(",").filter(Boolean);
const jeux = champs.length ? champs.map((c) => [c, unitesDe(c)]) : [["paragraphes", unitesDe(null)]];

// --- Pattern 13 : renvois au dispositif de la page, eux sont détectables ---
const AUTOREF = [
  "cette liste", "de la liste", "contre la liste", "ci-dessus", "ci-dessous",
  "sur cette page", "sur ce site", "affiché ici", "affichée ici", "en face",
  "comme on l'a vu", "nous allons voir", "dans cet article", "comme vu plus haut",
];
const bas = src.toLowerCase();
const autoref = AUTOREF.map((p) => [p, bas.split(p).length - 1]).filter(([, n]) => n);

console.log(`fichier   ${file}\n`);

for (const [nom, unites] of jeux) {
  if (!unites.length) {
    console.log(`champ ${nom} : aucune unité trouvée\n`);
    continue;
  }
  const pct = (n) => Math.round((n / unites.length) * 100);

  const hist = {};
  unites.forEach((u) => {
    const n = phrases(u).length;
    hist[n] = (hist[n] || 0) + 1;
  });
  const cles = Object.keys(hist).map(Number).sort((x, y) => x - y);
  const dom = cles.reduce((b, k) => (hist[k] > hist[b] ? k : b), cles[0]);
  const citNue = unites.filter((u) => /^["«]/.test(u.trim())).length;
  // Un champ de titres fait une phrase par unité par nature : pas d'alerte
  // rythme sur ces champs-là, sinon l'alerte devient du bruit qu'on ignore.
  const moyenne = unites.reduce((s, u) => s + phrases(u).length, 0) / unites.length;

  console.log(`champ ${nom} · ${unites.length} unités`);
  console.log(`  longueurs    ${JSON.stringify(hist)}`);
  console.log(`               dominante ${dom} phrase(s), ${hist[dom]}/${unites.length} (${pct(hist[dom])} %)` +
    (pct(hist[dom]) > 45 && moyenne > 1.5 ? "   ⚠ rythme plat" : ""));
  console.log(`  citation nue ${citNue}/${unites.length} (${pct(citNue)} %)` +
    (pct(citNue) > 30 ? "   ⚠ pattern 14, on recopie la source au lieu de dire ce qu'elle fait" : ""));

  console.log(`\n  OUVERTURES — un moule se voit ici :`);
  unites.forEach((u, i) => console.log(`   ${String(i + 1).padStart(3)} ${coupe(phrases(u)[0], 92)}`));

  console.log(`\n  FINS — si elles concluent toutes, le moteur de démonstration tourne (pattern 11) :`);
  unites.forEach((u, i) => {
    const p = phrases(u);
    console.log(`   ${String(i + 1).padStart(3)} ${coupe(p[p.length - 1], 92)}`);
  });
  console.log("");
}

if (autoref.length) {
  console.log(`auto-référence (pattern 13) : ${autoref.reduce((s, [, n]) => s + n, 0)} occurrence(s)`);
  autoref.forEach(([p, n]) => console.log(`   ${String(n).padStart(3)}x  ${p}`));
} else {
  console.log(`auto-référence (pattern 13) : 0`);
}

console.log(`
À LIRE MAINTENANT, le script ne le fait pas :
  · les deux colonnes ci-dessus, en diagonale. Si les fins concluent toutes,
    réécris-en la moitié pour qu'elles s'arrêtent sur le fait.
  · combien d'unités ne démontrent rien du tout. En dessous de trois, le texte
    est une machine, quels que soient les chiffres.
  · le pattern 12 : une section qui empile A, B, C, D puis sort le concept qui
    range tout. Il ne se compte pas, il se repère à la lecture de la section.`);
