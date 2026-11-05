"""Run after enrichir-visuels.py. Integrate authentic source extracts and visual explanations."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
page = (ROOT / 'index.html').read_text()
if 'id="preuves-visuelles"' in page:
    raise SystemExit('Déjà intégré. Relancer enrichir-visuels.py avant ce script.')

def capture(file, alt, source, label, caption):
    return f'''<figure class="source-capture"><div class="capture-label">{label}</div><button type="button" class="zoom-image" data-image="{file}" data-caption="{alt}" aria-label="Agrandir : {alt}"><img src="{file}" alt="{alt}" loading="lazy"><span class="zoom-label">Agrandir la capture</span></button><figcaption>{caption} <a href="{source}" target="_blank" rel="noopener">Consulter la source</a>.</figcaption></figure>'''

wiki = capture('capture-arxiv-titre.png', 'Titre original du travail sur AI Overviews et le trafic de Wikipedia', 'https://arxiv.org/abs/2602.18455', 'arXiv · travail de recherche', 'Capture du titre original. Révision du 2 septembre 2026.')
monde = capture('capture-le-monde-titre.png', 'Titre de l’entretien original avec Louis Dreyfus publié par INfluencia', 'https://www.influencia.net/louis-dreyfus-nous-navons-pas-constate-dimpact-dai-overviews-sur-nos-audiences/', 'INfluencia · entretien', 'Capture du titre original. Entretien publié le 8 septembre 2026.')
evidence = f'''<div id="preuves-visuelles" class="evidence-board"><h4>Deux sources, deux façons de mesurer</h4><div class="evidence-pair"><div>{wiki}<dl><dt>Ce qui est étudié</dt><dd>Les visites issues des moteurs vers Wikipedia en anglais.</dd><dt>La comparaison</dt><dd>Les versions allemande et française des articles.</dd><dt>La limite</dt><dd>Une estimation sur Wikipedia, avec des données de 2023–2024.</dd></dl></div><div>{monde}<dl><dt>Ce qui est rapporté</dt><dd>L’évolution des audiences du groupe Le Monde.</dd><dt>La méthode</dt><dd>Le constat de son directeur général dans un entretien.</dd><dt>La limite</dt><dd>Une déclaration d’éditeur, pas une mesure isolée de l’effet des réponses IA.</dd></dl></div></div><p class="evidence-takeaway">À retenir : ces observations portent sur des mesures différentes. Elles ne se contredisent pas nécessairement.</p></div>'''
page = page.replace('<figure class="data-figure">', evidence + '<figure class="data-figure">', 1)

# Replace generic drawings with the original Google image and short authentic excerpts.
news = re.search(r'(<section id="les-faits-a-retenir">)(.*?)(</section>)', page)
section = news.group(2)
articles = re.findall(r'<article class="news-story">.*?</article>', section)
assert len(articles) == 3

official = '''<figure class="official-google"><button type="button" class="zoom-image" data-image="google-aggregator-officiel.png" data-caption="Exemple d’unité d’agrégation publié dans la documentation Google" aria-label="Agrandir l’exemple officiel Google"><img src="google-aggregator-officiel.png" width="800" height="1800" loading="lazy" alt="Exemple officiel Google : un comparateur développé avec carte et hôtels, puis d’autres comparateurs repliés"><span class="zoom-label">Agrandir le visuel Google</span></button><figcaption>Visuel original de Google Search Central, <a href="https://developers.google.com/search/docs/appearance/aggregator-unit">documentation de l’unité d’agrégation</a>, sous <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>. Exemple illustratif fourni par Google.</figcaption></figure>'''
a = re.sub(r'<figure>.*?</figure>', official, articles[0], count=1)
a = a.replace('class="news-story"', 'class="news-story official-story"', 1)
notes = '''<div class="reading-notes"><h4>Ce qu’il faut regarder</h4><dl><dt>Le comparateur sélectionné</dt><dd>Ses hôtels sont développés avec leur carte et leurs prix.</dd><dt>Le lien de sortie</dt><dd>Il conduit vers ce comparateur.</dd><dt>Les autres comparateurs</dt><dd>L’internaute peut en sélectionner un autre dans la liste.</dd></dl></div>'''
a = a.replace('</div></article>', notes + '</div></article>')
section = section.replace(articles[0], a)

api = capture('capture-api-condition.png', 'Condition officielle : le Client ID est associé à un accord partenaire', 'https://developers.google.com/web-search-service/overview', 'Google for Developers · prérequis', 'Extrait authentique de la liste des prérequis, capturé le 12 septembre 2026. La condition porte sur l’accord partenaire.')
b = re.sub(r'<figure>.*?</figure>', '', articles[1], count=1)
b = b.replace('class="news-story"', 'class="news-story source-story"', 1)
b = b.replace('</div></article>', api + '<div class="access-flow" aria-label="Conditions d’accès"><span>Projet Google Cloud</span><span>Clé API</span><strong>Accord partenaire</strong></div></div></article>')
section = section.replace(articles[1], b)

tailwind = capture('capture-tailwind-titre.png', 'Annonce originale : Tailwind Labs is joining Shopify', 'https://tailwindcss.com/blog/tailwind-is-joining-shopify', 'Tailwind · annonce officielle', 'Capture du titre de l’annonce d’Adam Wathan, publiée le 9 septembre 2026.')
c = re.sub(r'<figure>.*?</figure>', '', articles[2], count=1)
c = c.replace('class="news-story"', 'class="news-story source-story"', 1)
c = c.replace('</div></article>', tailwind + '<div class="change-summary"><div><span>Projet ouvert</span><strong>Licence MIT maintenue</strong></div><div><span>Produits commerciaux</span><strong>Nouvelles inscriptions fermées</strong></div></div></div></article>')
section = section.replace(articles[2], c)
page = page[:news.start()] + news.group(1) + section + news.group(3) + page[news.end():]

# Make the existing image explain the editorial idea with nearby, readable labels.
page = page.replace('<figcaption>De l’information à l’expérience', '<figcaption>De l’information à l’expérience', 1)
hero_legend = '''<div class="hero-reading"><div><span>La recherche</span><strong>Comprendre une information</strong></div><svg aria-hidden="true" width="36" height="24" viewBox="0 0 36 24"><path d="M2 12h29m-8-8 8 8-8 8" fill="none" stroke="currentColor" stroke-width="2"/></svg><div><span>La page utile</span><strong>Pouvoir prendre une décision</strong></div></div>'''
page = page.replace('Illustration générée par IA.</figcaption></figure>', 'Illustration générée par IA.</figcaption>' + hero_legend + '</figure>', 1)

modal = '''<dialog id="image-dialog" aria-labelledby="image-dialog-caption"><div class="dialog-toolbar"><p id="image-dialog-caption"></p><button type="button" id="close-image">Fermer</button></div><div class="dialog-scroll"><img id="enlarged-image" alt=""></div></dialog><script>
const dialog=document.querySelector('#image-dialog');
const enlarged=document.querySelector('#enlarged-image');
const caption=document.querySelector('#image-dialog-caption');
document.querySelectorAll('[data-image]').forEach(button=>button.addEventListener('click',()=>{enlarged.src=button.dataset.image;enlarged.alt=button.dataset.caption;caption.textContent=button.dataset.caption;dialog.showModal();}));
document.querySelector('#close-image').addEventListener('click',()=>dialog.close());
dialog.addEventListener('click',event=>{if(event.target===dialog)dialog.close();});
</script>'''
page = page.replace('</body>', modal + '</body>')

css = '''
.hero-reading{display:flex;align-items:center;justify-content:space-between;gap:20px;padding:18px 0;font-family:"Avenir Next",Avenir,sans-serif}.hero-reading span{display:block;color:var(--muted);font-size:12px}.hero-reading strong{display:block;font-size:17px}.hero-reading svg{flex-shrink:0;color:#7597c4}
.evidence-board{margin:36px 0 25px;font-family:"Avenir Next",Avenir,sans-serif}.evidence-board h4,.reading-notes h4{font-size:21px;line-height:1.4;margin:0 0 21px;color:var(--blue)}.evidence-pair{display:grid;grid-template-columns:1fr 1fr;gap:25px}.evidence-pair>div{border:1px solid #d6dfeb;border-radius:8px;overflow:hidden}.source-capture{margin:22px 0;max-width:850px}.evidence-pair .source-capture{margin:0}.capture-label{font:600 12px/1.5 "Avenir Next",Avenir,sans-serif;color:var(--muted);padding:13px 17px;background:#f2f5f9}.zoom-image{display:block;width:100%;padding:0;border:0;background:#fff;color:var(--blue);cursor:zoom-in;text-align:left}.zoom-image img{display:block;width:100%;height:auto;max-height:none;object-fit:contain}.evidence-pair .zoom-image{padding:18px 10px 0}.evidence-pair .zoom-image img{min-height:68px;max-height:95px;object-fit:contain}.zoom-label{display:block;font:12px/1.4 "Avenir Next",Avenir,sans-serif;text-align:right;padding:9px 12px;color:#53627a;text-decoration:underline;text-underline-offset:3px}.source-capture figcaption{padding:10px 15px 0}.evidence-pair dl{padding:0 17px 16px;margin:18px 0 0}.evidence-pair dt,.reading-notes dt{font-size:12px;color:#53627a;font-weight:600;margin-top:15px}.evidence-pair dd,.reading-notes dd{font-size:14px;line-height:1.55;margin:3px 0 0}.evidence-takeaway{font-size:15px;line-height:1.6;background:#eaf2ff;padding:16px 20px;margin:16px 0 0;border-radius:6px}.official-story{grid-template-columns:240px minmax(0,1fr);gap:28px}.official-google .zoom-image img{max-height:540px;object-fit:contain;background:white}.official-google figcaption{font-size:11px}.reading-notes{background:#f3f6fa;padding:20px 24px;margin-top:25px;font-family:"Avenir Next",Avenir,sans-serif}.reading-notes h4{font-size:17px;margin:0}.reading-notes dl{margin:0}.source-story{display:block;padding-top:30px;border-top:1px solid #d6dfeb}.source-story .source-capture{border:1px solid #d6dfeb;border-radius:6px;overflow:hidden;padding-bottom:12px}.source-story .source-capture .zoom-image{padding:18px 18px 0}.source-story .source-capture img{max-height:145px;object-fit:contain}.access-flow{display:flex;flex-wrap:wrap;gap:10px;align-items:center;font:14px/1.5 "Avenir Next",Avenir,sans-serif}.access-flow span,.access-flow strong{padding:10px 15px;border-radius:5px;background:#f1f5fa}.access-flow strong{background:#eaf2ff;color:#193761}.change-summary{display:grid;grid-template-columns:1fr 1fr;gap:25px;font-family:"Avenir Next",Avenir,sans-serif}.change-summary span{font-size:12px;display:block;color:#53627a}.change-summary strong{font-size:16px;display:block}.zoom-image:focus-visible,button:focus-visible{outline:3px solid #477bcc;outline-offset:4px}
dialog{width:min(1120px,94vw);max-height:92vh;border:0;padding:0;border-radius:8px;background:white;color:var(--ink);box-shadow:0 20px 90px #0006}dialog::backdrop{background:#101d32b8}.dialog-toolbar{display:flex;justify-content:space-between;align-items:center;gap:22px;padding:17px 20px;border-bottom:1px solid #dce4ed;font:15px/1.5 "Avenir Next",Avenir,sans-serif}.dialog-toolbar p{margin:0}.dialog-toolbar button{background:#193761;color:white;border:0;padding:10px 17px;border-radius:5px;cursor:pointer;font:inherit}.dialog-scroll{overflow:auto;max-height:76vh;padding:22px}.dialog-scroll img{display:block;width:auto;max-width:100%;height:auto;margin:auto}
@media(max-width:1050px){.official-story{grid-template-columns:200px minmax(0,1fr);gap:20px}}@media(max-width:700px){.evidence-pair{grid-template-columns:1fr}.evidence-pair .zoom-image img{min-height:0;max-height:none}.hero-reading strong{font-size:14px}.hero-reading{gap:10px}.official-story{display:block}.official-google{max-width:290px;margin:0 auto 25px!important}.source-story .source-capture .zoom-image{padding:12px 8px 0}.source-story .source-capture img{max-height:none}.access-flow{font-size:12px}.change-summary{gap:15px}.change-summary strong{font-size:14px}.dialog-toolbar{font-size:13px;padding:12px}.dialog-scroll{padding:10px}.dialog-scroll img{min-width:640px;max-width:none}.dialog-scroll:has(img[src*="aggregator"]) img{min-width:0;width:100%;max-width:700px}.evidence-pair dl{display:grid;grid-template-columns:110px 1fr;gap:12px 15px}.evidence-pair dt,.evidence-pair dd{margin:0}.hero-reading>svg{width:24px}}
@media print{.zoom-label{display:none}.source-capture,.evidence-pair>div{break-inside:avoid}.evidence-board{break-inside:auto}.evidence-pair{display:block}.evidence-pair>div{margin-bottom:15px}.official-story{display:grid;grid-template-columns:180px 1fr}.source-story{display:block}.hero-reading{display:none}}
'''
page = page.replace('</style>', css + '</style>')
page = page.replace('Sources originales consultées le 12 septembre 2026.', 'Sources originales consultées et captures réalisées le 12 septembre 2026.')
(ROOT / 'index.html').write_text(page)
print('Quatre captures authentiques, un visuel officiel commenté et agrandissement intégrés.')
