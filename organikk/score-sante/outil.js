// L'outil en une page : un champ URL, le score de santé du site et l'explication de
// chaque note. Toute la donnée est embarquée (aucun appel réseau à l'usage), calculée
// par score.js sur le corpus de référence. Un site hors corpus n'a pas de score :
// il faut sa Search Console, pas un crawl.
//   node outil.js   → outil.html
const fs = require('fs');
const { score, DIMS, eligibles } = require('./score.js');
const M = JSON.parse(fs.readFileSync(__dirname + '/mesures.json', 'utf8')).filter((m) => !m.erreur);

const domaine = (m) => (m.site.startsWith('sc-domain:') ? m.site.slice(10) : m.site.replace(/^https?:\/\//, '').replace(/\/$/, ''));
const hotes = (m) => { const d = domaine(m).replace(/^www\./, ''); return [d, 'www.' + d, ...(m.hote ? [m.hote] : [])]; };

// Ce que chaque note veut dire, en clair, à partir des mesures brutes du site.
const nb = (n) => String(n).replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
const EXPLIQUE = {
  rendement: (m) => `Sur les ${nb(m.declarees)} pages que le sitemap déclare, ${nb(m.cliqueesHote)} ont reçu au moins un clic entre le ${m.fenetre[0]} et le ${m.fenetre[1]}. Les autres sont publiées et ne rapportent aucun clic sur la fenêtre.`,
  concentration: (m) => m.clics28 >= 30
    ? `Sur les ${nb(m.clics28)} clics de la fenêtre, la moitié vient de ${m.pagesMoitie} page${m.pagesMoitie > 1 ? 's' : ''}. Plus ce nombre est bas, plus le site dépend de peu de pages.`
    : `Le site compte ${m.clics28} clics sur la fenêtre. Sous 30 clics, dire qu'une page en fait la moitié ne mesure rien, donc la dimension n'est pas notée.`,
  renouvellement: (m) => m.tauxRenouvellement === null
    ? `${m.cohorte} page${m.cohorte > 1 ? 's' : ''} ${m.cohorte > 1 ? 'sont apparues' : 'est apparue'} dans Search Console ces 90 jours. Il en faut au moins 5 pour noter la dimension.`
    : `${nb(m.cohorte)} pages sont apparues dans Search Console ces 90 jours. ${nb(m.cohorteCliquees)} d'entre elles ont déjà reçu un clic. C'est la part de ce qui vient d'être publié qui atteint des clics.`,
  tenue: (m) => m.tenue === null
    ? `Le relevé couvre ${m.joursSerie} jours. Il en faut 120 pour comparer le niveau actuel au meilleur niveau atteint.`
    : `Sur 28 jours glissants, le site est à ${nb(m.imprCourant)} impressions, contre ${nb(m.imprMax)} à son meilleur niveau des 365 derniers jours, soit ${Math.round(100 * m.tenue)} %.`,
};

const DEF = {
  rendement: 'part des pages déclarées au sitemap qui reçoivent au moins un clic sur 28 jours',
  concentration: 'nombre de pages qui portent la moitié des clics sur 28 jours',
  renouvellement: 'part des pages apparues ces 90 jours qui reçoivent au moins un clic',
  tenue: 'niveau d’impressions actuel rapporté au meilleur niveau des 365 derniers jours',
};

const unite = (id, v) => (id === 'concentration' ? nb(v) + (v > 1 ? ' pages' : ' page') : Math.round(100 * v) + ' %');

const sites = M.map((m) => {
  const eligible = m.impr28 >= 80;
  const S = eligible ? score(m.slug) : null;
  return {
    slug: m.slug, domaine: domaine(m), hotes: hotes(m), eligible, impr28: m.impr28, clics28: m.clics28,
    fenetre: m.fenetre, jours: m.jours,
    score: S ? S.score : null, dimensions: S ? S.dimensions : 0,
    notes: S ? S.notes.map((n) => ({ ...n, explique: EXPLIQUE[n.id](m), valeurTexte: n.valeur === undefined || n.valeur === null ? null : unite(n.id, n.valeur) })) : [],
  };
});

// Distribution de chaque dimension sur le corpus, pour situer le site sur une bande.
const bandes = Object.fromEntries(DIMS.map((d) => [d.id, eligibles.map((s) => ({ slug: s.slug, v: d.valeur(s) })).filter((x) => x.v !== null && x.v !== undefined)]));

const DATA = { sites, dims: DIMS.map((d) => ({ id: d.id, nom: d.nom, def: DEF[d.id] })), bandes, corpus: eligibles.length, total: M.length, releve: M.reduce((a, m) => (m.fin > a ? m.fin : a), '') };

const CSS = `:root{--fond:#F4F5F7;--carte:#FFF;--bord:#E5E7EB;--bord2:#D1D5DB;--encre:#212121;--gris:#374151;--gris2:#6B7280;--gris3:#9CA3AF;--bleu:#2f4fe0}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--fond);color:var(--encre);font-family:Geist,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;font-size:15px;line-height:1.55;-webkit-font-smoothing:antialiased}
main{max-width:1180px;margin:0 auto;padding:40px 32px 72px}
h1{font-size:28px;font-weight:600;letter-spacing:-.5px;margin-bottom:6px}
.sous{color:var(--gris2);margin-bottom:24px;max-width:720px}
form{display:flex;gap:10px;max-width:720px;margin-bottom:32px}
input{flex:1;font:inherit;font-size:16px;padding:12px 14px;border:1px solid var(--bord2);border-radius:10px;background:var(--carte);color:var(--encre);outline:none}
input:focus{border-color:var(--bleu);box-shadow:0 0 0 3px rgba(47,79,224,.15)}
button{font:inherit;font-size:15px;font-weight:500;padding:12px 18px;border:0;border-radius:10px;background:var(--bleu);color:#fff;cursor:pointer}
button:hover{background:#2440c4}
.carte{background:var(--carte);border:1px solid var(--bord);border-radius:16px;padding:22px}
.tete{display:grid;grid-template-columns:220px 1fr;gap:32px;align-items:center;margin-bottom:16px}
@media(max-width:860px){.tete{grid-template-columns:1fr}}
.chiffre{font-size:72px;font-weight:600;line-height:1;letter-spacing:-2px}
.chiffre small{font-size:22px;color:var(--gris3);font-weight:400;letter-spacing:0}
.sitenom{font-size:17px;font-weight:600;margin-bottom:8px}
.tete p{color:var(--gris);margin-bottom:8px}
.tete p:last-child{margin-bottom:0}
.meta{color:var(--gris2);font-size:13px}
.lecture{margin-bottom:16px;color:var(--gris)}
.lecture p{margin-bottom:8px}
.lecture p:last-child{margin-bottom:0}
.grille{display:grid;grid-template-columns:repeat(2,1fr);gap:16px}
@media(max-width:720px){.grille{grid-template-columns:1fr}}
.dimtete{display:flex;justify-content:space-between;align-items:baseline;gap:12px;margin-bottom:4px}
.dim h3{font-size:15px;font-weight:600}
.def{color:var(--gris3);font-size:12.5px;margin-bottom:12px}
.note{font-size:28px;font-weight:600;line-height:1;white-space:nowrap}
.note small{font-size:12px;color:var(--gris3);font-weight:400}
.nm{font-size:13px;font-weight:400;color:var(--gris3)}
.explique{color:var(--gris);font-size:14px}
.rang{color:var(--gris2);font-size:12.5px;margin-top:12px}
.bande{position:relative;height:34px;margin-top:14px}
.axe{position:absolute;top:9px;left:0;right:0;height:2px;background:var(--bord);border-radius:2px}
.pt{position:absolute;top:4px;width:8px;height:8px;margin-left:-4px;border-radius:50%;background:var(--bord2)}
.pt.moi{background:var(--bleu);width:12px;height:12px;top:2px;margin-left:-6px;box-shadow:0 0 0 3px rgba(47,79,224,.18)}
.bornes{position:absolute;top:18px;left:0;right:0;display:flex;justify-content:space-between;color:var(--gris3);font-size:11.5px}
.absent h2{font-size:18px;font-weight:600;margin-bottom:8px}
.absent p{color:var(--gris);margin-bottom:8px}
.absent ul{list-style:none;display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}
.absent li a{display:inline-block;padding:5px 10px;border:1px solid var(--bord);border-radius:8px;color:var(--gris);text-decoration:none;font-size:13px;background:var(--carte)}
.absent li a:hover{border-color:var(--bord2)}
.methode{margin-top:24px;color:var(--gris2);font-size:13px;max-width:820px}
.methode p{margin-bottom:6px}
[hidden]{display:none!important}`;

const JS = `const DATA=${JSON.stringify(DATA)};
const $=(s)=>document.querySelector(s);
const esc=(s)=>String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
const nb=(n)=>String(n).replace(/\\B(?=(\\d{3})+(?!\\d))/g,' ');
const couleur=(n)=>n===null?'#6B7280':n>=65?'#059669':n>=35?'#D97706':'#DC2626';
const situe=(n)=>n>=65?'au-dessus du corpus':n>=35?'dans la moyenne du corpus':'sous le corpus';
const unite=(id,v)=>id==='concentration'?nb(v)+(v>1?' pages':' page'):Math.round(100*v)+' %';
function hote(u){u=u.trim();if(!u)return null;if(!/^https?:\\/\\//i.test(u))u='https://'+u;try{return new URL(u).hostname.toLowerCase()}catch(e){return null}}
function trouve(h){if(!h)return null;const nu=h.replace(/^www\\./,'');return DATA.sites.find((s)=>s.hotes.includes(h)||s.hotes.includes(nu)||s.domaine.replace(/^www\\./,'')===nu)||null}
function bande(id,slug){const vals=DATA.bandes[id];if(!vals||vals.length<5)return '';const vs=vals.map((x)=>x.v);const min=Math.min(...vs),max=Math.max(...vs);const pos=(v)=>max===min?50:100*(v-min)/(max-min);
return '<div class="bande"><div class="axe"></div>'+vals.map((x)=>'<span class="pt'+(x.slug===slug?' moi':'')+'" style="left:'+pos(x.v).toFixed(1)+'%"></span>').join('')+'<div class="bornes"><span>'+unite(id,min)+'</span><span>'+unite(id,max)+'</span></div></div>'}
function rendu(site){
  if(!site.eligible){return '<div class="carte absent"><h2>'+esc(site.domaine)+' : pas de score</h2><p>Le site compte '+nb(site.impr28)+' impressions sur les 28 derniers jours. Sous 80, aucune note : le bruit déciderait à la place de la mesure.</p></div>'}
  const dims=site.notes.map((n)=>{const d=DATA.dims.find((x)=>x.id===n.id);return '<article class="carte dim"><div class="dimtete"><h3>'+esc(n.nom)+'</h3><div class="note" style="color:'+couleur(n.note)+'">'+(n.note===null?'<span class="nm">non mesuré</span>':n.note+'<small>/100</small>')+'</div></div><p class="def">'+esc(d.def)+'</p><p class="explique">'+esc(n.explique)+'</p>'+(n.note===null?'':bande(n.id,site.slug))+'<p class="rang">'+(n.note===null?'La dimension sort du calcul, elle ne vaut pas zéro.':n.rang+' site'+(n.rang>1?'s':'')+' sur '+(n.total-1)+' '+(n.rang>1?'font':'fait')+' moins bien : '+situe(n.note)+'.')+'</p></article>'}).join('');
  const retenues=site.notes.filter((n)=>n.note!==null);const haut=retenues.length?retenues.reduce((a,n)=>n.note>a.note?n:a):null;const bas=retenues.length?retenues.reduce((a,n)=>n.note<a.note?n:a):null;
  const nonMes=site.notes.filter((n)=>n.note===null).map((n)=>n.nom);
  return '<div class="carte tete"><div><div class="chiffre">'+site.score+'<small>/100</small></div><div class="meta" style="margin-top:6px">'+site.dimensions+' dimension'+(site.dimensions>1?'s':'')+' mesurée'+(site.dimensions>1?'s':'')+' sur '+DATA.dims.length+'</div></div><div><div class="sitenom">'+esc(site.domaine)+'</div><p>Le score est la moyenne des notes mesurées, à poids égal. Chaque note est la position du site parmi les '+DATA.corpus+' sites du corpus sur cette mesure : une note de 70 veut dire que 70 % des sites du corpus font moins bien.</p><p>'+(haut&&bas&&haut!==bas?'Note la plus haute : '+esc(haut.nom)+' ('+haut.note+'). Note la plus basse : '+esc(bas.nom)+' ('+bas.note+').':'')+(nonMes.length?' Non mesuré : '+esc(nonMes.join(', '))+'.':'')+'</p><p class="meta">Fenêtre du '+site.fenetre[0]+' au '+site.fenetre[1]+' · relevé Search Console de '+site.jours+' jours · '+nb(site.clics28)+' clics et '+nb(site.impr28)+' impressions sur 28 jours</p></div></div><div class="grille">'+dims+'</div>'}
function absent(h){return '<div class="carte absent"><h2>'+(h?esc(h):'Adresse illisible')+(h?' : pas de score':'')+'</h2><p>Ce score ne se calcule pas depuis un crawl. Il lit la Search Console du site sur 12 à 16 mois : pages déclarées au sitemap qui reçoivent des clics, pages qui portent la moitié des clics, pages récentes qui atteignent des clics, niveau actuel par rapport au meilleur niveau. Sans cet accès, aucune note.</p><p>Sites disponibles aujourd’hui :</p><ul>'+DATA.sites.map((s)=>'<li><a href="?url='+encodeURIComponent(s.domaine)+'">'+esc(s.domaine)+'</a></li>').join('')+'</ul></div>'}
function lance(u){const h=hote(u);const site=trouve(h);$('#res').innerHTML=site?rendu(site):absent(h);$('#res').hidden=false;const url=new URL(location);if(u)url.searchParams.set('url',u);else url.searchParams.delete('url');history.replaceState(null,'',url)}
$('form').addEventListener('submit',(e)=>{e.preventDefault();lance($('input').value)});
const q=new URL(location).searchParams.get('url');if(q){$('input').value=q;lance(q)}`;

const html = `<!doctype html><html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex">
<title>Score de santé d'un site</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&display=swap" rel="stylesheet">
<style>${CSS}</style></head><body>
<main>
<h1>Score de santé d'un site</h1>
<p class="sous">Entrez l'adresse d'un site suivi dans la Search Console. L'outil sort son score sur 100, les quatre dimensions qui le composent et ce que chaque note veut dire.</p>
<form><input type="text" placeholder="organikk.co" autocomplete="off" spellcheck="false"><button type="submit">Voir le score</button></form>
<div id="res" hidden></div>
<div class="methode">
<p>Corpus de référence : ${DATA.corpus} sites au-dessus de 80 impressions sur 28 jours, sur ${DATA.total} suivis. Relevé au ${DATA.releve}.</p>
<p>La technique (erreurs de crawl, balises, vitesse) n'entre pas dans le score. Une page non indexée se voit déjà dans le Rendement.</p>
<p>Le corpus n'est pas figé : ajouter un site déplace la note des autres.</p>
</div>
</main>
<script>${JS}</script>
</body></html>`;

fs.writeFileSync(__dirname + '/outil.html', html);
