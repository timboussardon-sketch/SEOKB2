from pathlib import Path
import re
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parent

def svg(name, title, content, width=720, height=350, background='#eaf2ff'):
    value = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title"><title id="title">{title}</title><rect width="{width}" height="{height}" fill="{background}"/><g font-family="Avenir Next, Avenir, Arial, sans-serif" fill="#193761">{content}</g></svg>'''
    ElementTree.fromstring(value)
    (ROOT / name).write_text(value)

svg('wikipedia-trafic.svg', 'Baisse estimée du trafic de recherche vers Wikipedia anglais : 5,45 % face au groupe allemand, 4,82 % face au groupe français.', '''
<text x="32" y="39" font-size="21" font-weight="700">Wikipedia : une baisse autour de 5 %</text>
<text x="32" y="67" font-size="14" fill="#53627a">Deux groupes de comparaison, une même édition anglophone</text>
<g stroke="#d4dfed" stroke-width="1">
<path d="M220 111V257 M290 111V257 M360 111V257 M430 111V257 M500 111V257 M570 111V257 M640 111V257"/>
</g>
<text x="32" y="151" font-size="16">Face à l’allemand</text>
<text x="32" y="222" font-size="16">Face au français</text>
<rect x="220" y="125" width="381.5" height="40" rx="3" fill="#193761"/>
<rect x="220" y="196" width="337.4" height="40" rx="3" fill="#4674b7"/>
<text x="585" y="151" font-size="18" font-weight="700" text-anchor="end" fill="white">−5,45 %</text>
<text x="541" y="222" font-size="18" font-weight="700" text-anchor="end" fill="white">−4,82 %</text>
<g font-size="12" fill="#53627a" text-anchor="middle">
<text x="220" y="279">0</text><text x="290" y="279">1</text><text x="360" y="279">2</text><text x="430" y="279">3</text><text x="500" y="279">4</text><text x="570" y="279">5</text><text x="640" y="279">6 %</text>
</g>
<text x="640" y="309" text-anchor="end" font-size="13" fill="#53627a">Ampleur de la baisse estimée</text>
''', height=330, background='#f3f6fa')

svg('comparateurs.svg', 'Schéma simplifié : comparateurs et fournisseurs directs dans les résultats Google.', '''
<rect x="33" y="25" width="294" height="45" rx="22" fill="white"/>
<circle cx="56" cy="46" r="8" fill="none" stroke="#193761" stroke-width="2"/><path d="M62 52l6 6" stroke="#193761" stroke-width="2"/>
<text x="84" y="51" font-size="15">Hôtel à Bordeaux</text>
<rect x="25" y="95" width="181" height="146" rx="7" fill="#193761"/>
<text x="40" y="121" font-size="14" fill="white">Comparateurs</text>
<rect x="40" y="137" width="151" height="39" rx="4" fill="#769bcb"/>
<path d="M49 166v-19h23v19m5 0v-25h29v25" stroke="white" stroke-width="2" fill="none"/>
<path d="M117 148h59m-59 12h41M41 193h145m-145 16h108m-108 16h131" stroke="#b9cde8" stroke-width="6"/>
<rect x="219" y="95" width="116" height="146" rx="7" fill="white"/>
<text x="232" y="119" font-size="13">En direct</text>
<path d="M237 178v-31l37-17 39 17v31z" fill="#a6bfdf"/><path d="M267 178v-21h16v21" fill="#193761"/>
<path d="M237 195h77m-77 17h59" stroke="#c6d6e9" stroke-width="6"/>
''', 360, 270)

svg('api-partenaires.svg', 'Schéma : une application accède aux résultats de recherche via un accord partenaire.', '''
<rect x="24" y="67" width="109" height="140" rx="8" fill="white"/>
<path d="M24 97h109" stroke="#cfdaea" stroke-width="2"/>
<circle cx="39" cy="83" r="3" fill="#89a9d2"/><circle cx="51" cy="83" r="3" fill="#89a9d2"/>
<text x="78" y="148" font-size="26" text-anchor="middle" fill="#193761">{ }</text>
<text x="79" y="186" font-size="12" text-anchor="middle">Application</text>
<path d="M139 141h77m-9-7l9 7-9 7" stroke="#193761" stroke-width="3" fill="none"/>
<rect x="157" y="91" width="40" height="31" rx="5" fill="#e9c458"/>
<path d="M165 91v-8a12 12 0 0124 0v8" stroke="#193761" stroke-width="3" fill="none"/>
<circle cx="177" cy="104" r="4" fill="#193761"/>
<rect x="227" y="67" width="109" height="140" rx="8" fill="#193761"/>
<path d="M242 93h78m-78 20h52m-52 25h78m-78 20h63m-63 25h71" stroke="#a8c0e1" stroke-width="5"/>
<text x="180" y="242" font-size="14" text-anchor="middle">Accord partenaire requis</text>
''', 360, 270, '#f0f2f8')

svg('tailwind-shopify.svg', 'Illustration : une interface de boutique avec son code de mise en page.', '''
<rect x="56" y="37" width="260" height="195" rx="8" fill="white"/>
<path d="M56 73h260" stroke="#b7d9d9" stroke-width="2"/>
<circle cx="72" cy="55" r="4" fill="#4c898e"/><circle cx="87" cy="55" r="4" fill="#94bbbb"/>
<path d="M96 155v-44h55v44" fill="#bfdcda"/>
<path d="M119 111v-11a6 6 0 0112 0v11" fill="none" stroke="#193761" stroke-width="3"/>
<rect x="178" y="100" width="91" height="58" rx="6" fill="#ecda93"/>
<path d="M211 141v-30m-12 0h24" stroke="#193761" stroke-width="3"/>
<path d="M92 177h64m22 0h91m-177 18h46m40 0h61" stroke="#89aaaa" stroke-width="6"/>
<rect x="23" y="197" width="133" height="48" rx="7" fill="#193761"/>
<text x="89" y="228" font-size="21" text-anchor="middle" fill="white">&lt; / &gt;</text>
''', 360, 270, '#e9f3f1')

page = (ROOT / 'index-texte.html').read_text()
hero = '''<figure class="hero-art"><img src="illustration-ouverture.png" width="1536" height="1024" alt="Une recherche ouvre sur des pages d’information et sur la porte d’une chambre d’hôtel, en collage de papier bleu." fetchpriority="high"><figcaption>De l’information à l’expérience : donner une raison de visiter votre site. Illustration générée par IA.</figcaption></figure>'''
page = page.replace('</h1>', '</h1>' + hero, 1)
chart = '''<figure class="data-figure"><img src="wikipedia-trafic.svg" width="720" height="330" loading="lazy" alt="Baisse estimée du trafic de recherche vers Wikipedia anglais : 5,45 % par rapport au groupe allemand, 4,82 % par rapport au groupe français."><figcaption>Résultats de Khosravi et Yoganarasimhan, révision du 2 septembre 2026. Données 2023–2024. Ces estimations ne constituent pas une prévision pour votre site. <a href="https://arxiv.org/abs/2602.18455">Source et méthode</a>.</figcaption></figure>'''
page = page.replace('<p><strong>Mon analyse.</strong>', chart + '<p><strong>Mon analyse.</strong>', 1)

news = re.search(r'(<section id="les-faits-a-retenir"><h2>.*?</h2>)(.*?)(</section>)', page)
articles = re.findall(r'(<h3>.*?</h3><p>.*?</p>)', news.group(2))
images = [('comparateurs.svg', 'Comparateurs et fournisseurs directs dans une recherche d’hôtel.', 'Schéma simplifié'), ('api-partenaires.svg', 'Application reliée aux résultats de recherche par un accès partenaire.', 'Accès aux résultats'), ('tailwind-shopify.svg', 'Une boutique en ligne et son code de mise en page.', 'Outils de création')]
assert len(articles) == len(images)
rows = []
for article, (file, alt, caption) in zip(articles, images):
    rows.append(f'<article class="news-story"><figure><img src="{file}" width="360" height="270" loading="lazy" alt="{alt}"><figcaption>{caption}</figcaption></figure><div>{article}</div></article>')
page = page[:news.start()] + news.group(1) + ''.join(rows) + news.group(3) + page[news.end():]

decision = '''<div class="decision-example" aria-label="Exemple de requête décisionnelle"><div class="query-example"><svg width="23" height="23" viewBox="0 0 24 24" aria-hidden="true"><circle cx="10" cy="10" r="6" fill="none" stroke="currentColor" stroke-width="2"/><path d="m15 15 6 6" stroke="currentColor" stroke-width="2"/></svg><span>Hôtel Bordeaux chambre familiale parking</span></div><div class="decision-grid"><div><span>Où ?</span><strong>Bordeaux</strong></div><div><span>Pour qui ?</span><strong>Une famille</strong></div><div><span>Quelle contrainte ?</span><strong>Le parking</strong></div></div><p>La page doit permettre de vérifier ces critères.</p></div>'''
page = page.replace('<h3>La requête décisionnelle</h3>', '<h3>La requête décisionnelle</h3>' + decision)

timeline = '''<ol class="test-timeline" aria-label="Les étapes du test"><li><span>Aujourd’hui</span><strong>Choisir 10 pages</strong><small>Relever visites et demandes</small></li><li><span>Une modification</span><strong>Enrichir 1 page</strong><small>Ajouter une information utile</small></li><li><span>Dans 4 semaines</span><strong>Examiner les résultats</strong><small>Prolonger si le volume est faible</small></li></ol>'''
page = page.replace('<h3>Suivez dix pages jusqu&#x27;à la demande commerciale</h3>', '<h3>Suivez dix pages jusqu&#x27;à la demande commerciale</h3>' + timeline)
if 'class="test-timeline"' not in page:
    page = page.replace('<h3>Suivez dix pages jusqu’à la demande commerciale</h3>', '<h3>Suivez dix pages jusqu’à la demande commerciale</h3>' + timeline)

css = '''
.layout{max-width:1240px;grid-template-columns:180px minmax(0,900px);gap:54px}.masthead{padding-left:max(25px,calc((100vw - 1192px)/2));padding-right:max(25px,calc((100vw - 1192px)/2))}main{min-width:0}main>section>p,main>section>h3,.opening>p{max-width:720px}.opening h1{max-width:840px;font-size:clamp(34px,4.5vw,58px);margin-bottom:30px}.opening p{margin-top:25px}figure{margin:0}.hero-art{margin:0 0 28px}.hero-art img{width:100%;height:auto;display:block;border-radius:8px}.hero-art figcaption{margin-top:9px}figcaption{font:12px/1.6 "Avenir Next",Avenir,sans-serif;color:var(--muted);max-width:720px}img{max-width:100%}.data-figure{margin:32px 0;max-width:720px}.data-figure img{width:100%;height:auto;display:block;border-radius:6px}.data-figure figcaption{padding-top:10px}.news-story{display:grid;grid-template-columns:210px minmax(0,1fr);gap:27px;margin:28px 0 38px;align-items:start}.news-story figure{margin-top:4px}.news-story img{width:100%;height:auto;display:block;border-radius:6px}.news-story figcaption{padding-top:7px}.news-story h3,#les-faits-a-retenir .news-story h3{font-size:25px;margin:0 0 14px}.news-story p{font-size:18px;margin:0}.decision-example{margin:26px 0;max-width:720px;background:#f3f6fa;padding:27px;border-radius:8px;font-family:"Avenir Next",Avenir,sans-serif}.query-example{display:flex;align-items:center;gap:12px;background:white;border:1px solid #cdd9e8;border-radius:24px;padding:13px 18px;font-size:16px;font-weight:600;line-height:1.5}.query-example svg{flex-shrink:0}.decision-grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;margin:22px 0}.decision-grid>div{border-left:3px solid #7e9fc9;padding-left:12px}.decision-grid span{display:block;font-size:12px;color:#53627a}.decision-grid strong{display:block;font-size:16px}.decision-example>p{font-size:14px;color:#53627a;margin:0}.test-timeline{display:grid;grid-template-columns:1fr 1fr 1fr;gap:22px;list-style:none;padding:0;counter-reset:step;margin:28px 0 34px;font-family:"Avenir Next",Avenir,sans-serif}.test-timeline li{position:relative;padding-top:42px;counter-increment:step;line-height:1.5}.test-timeline li:before{content:counter(step);position:absolute;top:0;left:0;width:29px;height:29px;display:grid;place-items:center;border:1px solid #688bb9;border-radius:50%;font-size:14px;background:white;color:var(--blue);z-index:1}.test-timeline li:not(:last-child):after{content:"";position:absolute;top:14px;left:29px;width:calc(100% - 7px);height:1px;background:#9ab2d2}.test-timeline span{font-size:12px;color:#53627a;display:block}.test-timeline strong{display:block;font-size:16px;margin:5px 0}.test-timeline small{display:block;font-size:12px;color:#53627a}.foot{max-width:none}
@media(min-width:851px){.hero-art img{aspect-ratio:3/2;object-fit:cover}#a-tester-sur-votre-site{margin-right:0;margin-left:0}}@media(max-width:1050px){.layout{gap:30px;grid-template-columns:160px minmax(0,1fr)}.news-story{grid-template-columns:155px minmax(0,1fr);gap:21px}}
@media(max-width:850px){.layout{display:block;max-width:760px}.toc{margin-bottom:30px}.news-story{grid-template-columns:170px minmax(0,1fr)}.hero-art{margin-left:-8px;margin-right:-8px}}
@media(max-width:560px){.news-story{display:block}.news-story figure{margin-bottom:20px}.news-story img{width:100%;max-height:240px;object-fit:contain;background:#eaf2ff}.news-story h3,#les-faits-a-retenir .news-story h3{font-size:25px}.hero-art{margin-left:-22px;margin-right:-22px}.hero-art img{border-radius:0}.hero-art figcaption{padding:0 22px}.decision-example{padding:18px}.query-example{font-size:14px;border-radius:14px;padding:12px}.decision-grid{grid-template-columns:1fr;gap:12px}.decision-grid>div{display:flex;align-items:center;justify-content:space-between;gap:10px}.decision-grid strong{font-size:15px}.test-timeline{grid-template-columns:1fr;gap:22px}.test-timeline li{padding:0 0 0 43px;min-height:65px}.test-timeline li:not(:last-child):after{left:14px;top:29px;height:calc(100% + 22px);width:1px}.test-timeline strong{margin:2px 0}.data-figure{margin-left:-12px;margin-right:-12px}.data-figure figcaption{padding:0 12px}.data-figure img{min-height:180px}.opening h1{font-size:36px}}
@media print{.layout{display:block}.hero-art{max-width:430px}.hero-art img{width:100%}.data-figure,.news-story,.decision-example,.test-timeline{break-inside:avoid}.news-story{grid-template-columns:110px 1fr}.test-timeline{display:flex}.test-timeline li{flex:1}.hero-art figcaption{font-size:9pt}}
'''
mobile_chart = '<div class="mobile-chart"><strong>Wikipedia : une baisse autour de 5 %</strong><p>Trafic vers l’édition anglophone</p><div class="chart-row"><span>Face à l’allemand</span><b>−5,45 %</b></div><div class="bar-track"><span style="width:90.833333%"></span></div><div class="chart-row"><span>Face au français</span><b>−4,82 %</b></div><div class="bar-track"><span style="width:80.333333%"></span></div><div class="chart-axis"><span>0</span><span>3</span><span>6 % de baisse</span></div></div>'
page = page.replace('<figure class="data-figure">', '<figure class="data-figure">' + mobile_chart)
css += '.mobile-chart{display:none}@media(max-width:560px){.data-figure>img{display:none}.mobile-chart{display:block;background:#f3f6fa;padding:23px 18px;border-radius:6px;font:14px/1.5 "Avenir Next",Avenir,sans-serif}.mobile-chart>strong{display:block;font-size:19px;line-height:1.3}.mobile-chart>p{font-size:12px;color:#53627a;margin:9px 0 22px}.chart-row{display:flex;justify-content:space-between;gap:12px;margin:16px 0 7px}.bar-track{height:24px;background:#e0e7f0;border-radius:3px;overflow:hidden}.bar-track>span{display:block;height:100%;background:#193761}.bar-track:nth-of-type(4)>span{background:#4674b7}.chart-axis{display:flex;justify-content:space-between;font-size:11px;color:#53627a;margin-top:8px}.data-figure figcaption{margin-top:10px}}'
page = page.replace('</style>', css + '</style>')
assert 'test-timeline' in page
assert '<ol class="test-timeline"' in page
(ROOT / 'index.html').write_text(page)
print('Illustration, graphique, trois visuels de brèves, exemple visuel et frise intégrés.')
