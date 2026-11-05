// Requêtes Search Console d'organikk.co sur les 28 derniers jours et les 28 précédents.
// Passe par la fonction edge Fusionn déjà utilisée par gsc-simcity/pull.js.
const fs = require('fs'), os = require('os'), path = require('path');
const SECRET = fs.readFileSync(path.join(os.homedir(), '.config/seo-kb/fusionn-gsc-export.secret'), 'utf8').trim();
const ENDPOINT = 'https://fwhfnzbtlddzfxbsejyf.supabase.co/functions/v1/admin-gsc-export';
const SITE = process.argv[2] || 'https://organikk.co/';
const SLUG = process.argv[3] || 'organikk';
const FIN = process.argv[4] || '2026-08-25';
const J = (d, n) => new Date(new Date(d + 'T00:00:00Z').getTime() + n * 86400000).toISOString().slice(0, 10);

async function req(body, essais = 6) {
  // ECONNRESET passager déjà vu sur cette fonction edge : on réessaie, espacé.
  for (let i = 1; ; i += 1) {
    try {
      const res = await fetch(ENDPOINT, { method: 'POST', headers: { 'x-admin-secret': SECRET, 'content-type': 'application/json' }, body: JSON.stringify({ site: SITE, raw: body }) });
      const t = await res.text();
      if (!res.ok) throw new Error(res.status + ' ' + t.slice(0, 200));
      return JSON.parse(t).rows || [];
    } catch (e) {
      if (i >= essais) throw e;
      process.stdout.write(`  essai ${i} : ${String(e.message).slice(0, 40)}\n`);
      await new Promise((r) => setTimeout(r, 2000 * i));
    }
  }
}
async function fenetre(a, b) {
  const out = [];
  for (let startRow = 0; ; startRow += 25000) {
    const lot = await req({ startDate: a, endDate: b, dimensions: ['query'], rowLimit: 25000, startRow });
    out.push(...lot);
    if (lot.length < 25000) break;
  }
  return out;
}
(async () => {
  const cour = await fenetre(J(FIN, -27), FIN);
  const prec = await fenetre(J(FIN, -55), J(FIN, -28));
  fs.writeFileSync(__dirname + `/requetes-${SLUG}.json`, JSON.stringify({ site: SITE, courante: [J(FIN, -27), FIN], precedente: [J(FIN, -55), J(FIN, -28)], cour, prec }, null, 1));
  console.log('28 j courants :', cour.length, 'requêtes distinctes ·', cour.reduce((a, r) => a + r.clicks, 0), 'clics ·', cour.reduce((a, r) => a + r.impressions, 0), 'impressions');
  console.log('28 j précédents :', prec.length, 'requêtes distinctes ·', prec.reduce((a, r) => a + r.clicks, 0), 'clics');
  console.log('top 12 :'); cour.sort((a, b) => b.impressions - a.impressions).slice(0, 12).forEach((r) => console.log('  ', String(r.impressions).padStart(4), 'impr', String(r.clicks).padStart(3), 'clics  pos', r.position.toFixed(1).padStart(5), ' ', r.keys[0]));
})();
