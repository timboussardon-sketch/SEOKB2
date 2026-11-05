// Inspection d'indexation sur un ÉCHANTILLON stratifié, quand le sitemap dépasse le quota
// URL Inspection (2 000 URLs par jour et par propriété). Strate = premier segment d'URL.
// Tirage déterministe (pas de hasard) : une URL sur k dans chaque strate.
const fs = require('fs'), os = require('os'), path = require('path');
const SECRET = fs.readFileSync(path.join(os.homedir(), '.config/seo-kb/fusionn-gsc-export.secret'), 'utf8').trim();
const ANON = (fs.readFileSync('/Users/timothee/Code/newFusionn/.env.local', 'utf8').match(/VITE_SUPABASE_ANON_KEY=(\S+)/) || [])[1];
const ENDPOINT = 'https://fwhfnzbtlddzfxbsejyf.supabase.co/functions/v1/admin-gsc-inspect';
const [SITE, SLUG, FICHIER, PAR_STRATE] = [process.argv[2], process.argv[3], process.argv[4], Number(process.argv[5] || 50)];

const urls = fs.readFileSync(FICHIER, 'utf8').trim().split('\n');
const strates = {};
for (const u of urls) { const k = (u.split('/')[3] || '(racine)'); (strates[k] = strates[k] || []).push(u); }
const tire = [];
for (const [k, liste] of Object.entries(strates)) {
  const pas = Math.max(1, Math.floor(liste.length / PAR_STRATE));
  const pris = liste.filter((_, i) => i % pas === 0).slice(0, PAR_STRATE);
  tire.push(...pris);
  console.log(`  ${k} : ${pris.length} tirées sur ${liste.length}`);
}
console.log(`échantillon : ${tire.length} URLs sur ${urls.length}`);

(async () => {
  const res = [];
  for (let i = 0; i < tire.length; i += 100) {
    const lot = tire.slice(i, i + 100);
    for (let essai = 1; ; essai += 1) {
      try {
        const rep = await fetch(ENDPOINT, { method: 'POST', headers: { 'x-admin-secret': SECRET, authorization: 'Bearer ' + ANON, 'content-type': 'application/json' }, body: JSON.stringify({ siteUrl: SITE, urls: lot }) });
        const t = await rep.text();
        if (!rep.ok) throw new Error(rep.status + ' ' + t.slice(0, 200));
        res.push(...(JSON.parse(t).results || []));
        break;
      } catch (e) { if (essai >= 6) throw e; console.log('  essai', essai, String(e.message).slice(0, 60)); await new Promise((r) => setTimeout(r, 2500 * essai)); }
    }
    console.log(`  lot ${i / 100 + 1} : ${res.length}/${tire.length}`);
  }
  fs.writeFileSync(`${__dirname}/indexation-${SLUG}.json`, JSON.stringify({ site: SITE, le: new Date().toISOString(), urls: urls.length, echantillon: tire.length, res }, null, 1));
  const par = {}; for (const r of res) par[r.coverageState] = (par[r.coverageState] || 0) + 1;
  console.log('\nétats :'); Object.entries(par).sort((a, b) => b[1] - a[1]).forEach(([k, n]) => console.log(String(n).padStart(5), k, `(${Math.round(100 * n / res.length)} %)`));
})();
