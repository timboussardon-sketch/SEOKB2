// Le score : chaque mesure brute devient une note par sa POSITION dans la distribution
// observée sur le corpus de référence. Aucun barème décidé à la main.
// Corpus de référence : les sites du compte de Tim, uniquement. Les villes construites
// pour d'autres comptes ne sont pas utilisées tant que ce n'est pas tranché.
const fs = require('fs');
const M = JSON.parse(fs.readFileSync(__dirname + '/mesures.json', 'utf8')).filter((m) => !m.erreur);

// Base minimale : sous 80 impressions sur 28 jours, on ne note rien.
const BASE = 80;
const eligibles = M.filter((m) => m.impr28 >= BASE);

const DIMS = [
  { id: 'rendement', nom: 'Rendement',
    phrase: (m) => `${m.cliqueesHote} des ${m.declarees} pages déclarées reçoivent au moins un clic`,
    valeur: (m) => m.partCliquees, sens: 1 },
  { id: 'concentration', nom: 'Concentration',
    phrase: (m) => `il faut ${m.pagesMoitie} page${m.pagesMoitie > 1 ? 's' : ''} pour faire la moitié des clics`,
    // Sous 30 clics sur 28 jours, « une page fait la moitié des clics » n'est plus une
    // mesure de concentration, c'est du bruit : on ne note pas.
    valeur: (m) => (m.clics28 >= 30 ? m.pagesMoitie : null), sens: 1 },
  { id: 'renouvellement', nom: 'Renouvellement',
    phrase: (m) => `${m.cohorteCliquees} des ${m.cohorte} pages apparues ces 90 jours reçoivent des clics`,
    valeur: (m) => m.tauxRenouvellement, sens: 1 },
  { id: 'tenue', nom: 'Tenue',
    phrase: (m) => (m.tenue === null ? 'moins de 120 jours de relevé' : `le site est à ${Math.round(100 * m.tenue)} % de son meilleur niveau d'impressions sur la période`),
    valeur: (m) => m.tenue, sens: 1 },
];

function note(dim, m) {
  const v = dim.valeur(m);
  if (v === null || v === undefined) return null;
  const autres = eligibles.map(dim.valeur).filter((x) => x !== null && x !== undefined);
  if (autres.length < 5) return null;
  const moins = autres.filter((x) => x < v).length;
  const egaux = autres.filter((x) => x === v).length - 1;
  return { note: Math.round((100 * (moins + egaux / 2)) / (autres.length - 1)), rang: moins, total: autres.length, valeur: v };
}

function score(slug) {
  const m = M.find((x) => x.slug === slug);
  const notes = DIMS.map((d) => ({ id: d.id, nom: d.nom, phrase: d.phrase(m), ...(note(d, m) || { note: null }) }));
  const retenues = notes.filter((n) => n.note !== null);
  return { mesures: m, notes, score: retenues.length ? Math.round(retenues.reduce((a, n) => a + n.note, 0) / retenues.length) : null, dimensions: retenues.length, eligibles: eligibles.length };
}

if (require.main === module) {
  console.log(`corpus de référence : ${eligibles.length} sites sur ${M.length} (au moins ${BASE} impressions sur 28 j)`);
  console.log(eligibles.map((m) => m.slug).join(', '), '\n');
  for (const m of eligibles) {
    const s = score(m.slug);
    console.log(String(s.score).padStart(3), '·', m.slug.padEnd(26), s.notes.map((n) => `${n.nom.slice(0, 5)} ${n.note === null ? ' n/a' : String(n.note).padStart(3)}`).join(' · '));
  }
  console.log('\n--- organikk.co, le détail ---');
  const s = score('organikk');
  s.notes.forEach((n) => console.log(` ${n.nom.padEnd(15)} ${n.note === null ? 'non mesuré' : String(n.note).padStart(3) + '/100'}   ${n.phrase}   ${n.note === null ? '' : `(${n.rang} sites sur ${n.total - 1} font moins bien)`}`));
  console.log(` Score : ${s.score}/100 sur ${s.dimensions} dimensions`);
  fs.writeFileSync(__dirname + '/score-organikk.json', JSON.stringify({ ...s, corpus: eligibles.map((m) => ({ slug: m.slug, ...Object.fromEntries(DIMS.map((d) => [d.id, d.valeur(m)])) })) }, null, 1));
}
module.exports = { score, DIMS, eligibles };
