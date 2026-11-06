#!/usr/bin/env python3
"""Dashboard HTML autoportant de la stratégie GEO.

Lit les CSV/JSON du dossier <projet>/data/ et produit <projet>/dashboard.html
(un seul fichier, ouvrable hors ligne, sans réseau sauf la police Geist).

Usage :
    python3 build_dashboard.py strategie-geo/<slug> "Nom de la marque"

Fichiers lus (tous optionnels, un onglet absent est signalé, jamais inventé) :

  data/entity.json     {"marque","produit","categorie","icp","marche","langues",
                        "differenciateurs":[{"claim","preuve","statut"}],
                        "limites":[...], "acteurs":{"directs":[],"indirects":[],"alternatives":[]}}
  data/queries.csv     query,intention,priorite,brand_fit,chemin_citation,type_page,cluster,justification
  data/pages.csv       slug,titre,type,cluster,requete_cible,priorite,impact,effort,preuves_requises,bloque_par,statut
  data/proof.csv       affirmation,page,source,url_source,type,confiance,risque,action
  data/authority.csv   cible,type,pourquoi,sujet,preuve_a_fournir,angle,contact,statut
  data/data_assets.csv nom,question,dataset,methodologie,frequence,angle_presse,statut
  data/visibility.csv  query,moteur,mentionnee,recommandee,citee,position,sources_citees,runs,date

Aucune valeur n'est calculée à partir du vide : les compteurs ne comptent que
des lignes réellement présentes. Un fichier manquant affiche « non relevé ».
"""
import csv, html, json, os, sys
from datetime import date

ROOT = os.path.expanduser(sys.argv[1] if len(sys.argv) > 1 else '.')
BRAND = sys.argv[2] if len(sys.argv) > 2 else os.path.basename(ROOT.rstrip('/'))
DATA = os.path.join(ROOT, 'data')
OUT = os.path.join(ROOT, 'dashboard.html')


def esc(s):
    return html.escape(str(s) if s is not None else '')


def read_csv(name):
    p = os.path.join(DATA, name)
    if not os.path.exists(p):
        return None
    with open(p, encoding='utf-8') as f:
        return [r for r in csv.DictReader(f) if any((v or '').strip() for v in r.values())]


def read_json(name):
    p = os.path.join(DATA, name)
    if not os.path.exists(p):
        return None
    try:
        with open(p, encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return None


NON_BLOQUANT = {'', 'aucun', 'aucune', 'non', 'rien', '-', 'n/a', 'nc', 'n/d', 'sans'}


def bloquant(v):
    """Un intrant manquant, pas une case remplie par politesse."""
    return (v or '').strip().lower() not in NON_BLOQUANT


entity = read_json('entity.json')
queries = read_csv('queries.csv')
pages = read_csv('pages.csv')
proof = read_csv('proof.csv')
authority = read_csv('authority.csv')
assets = read_csv('data_assets.csv')
visib = read_csv('visibility.csv')

C = dict(
    bg='#fbf9f4', panel='#ffffff', line='rgba(16,20,34,.09)', txt='#101422',
    muted='#5c667e', faint='#8b93a7', accent='#1B3E8F', accent2='#4685F0',
    warn='#b45309', bad='#be123c', good='#1f7a4d',
)

PRIO = {'P0': C['bad'], 'P1': C['accent'], 'P2': C['faint'],
        'P3': C['faint']}
CONF = {'haute': C['good'], 'high': C['good'], 'moyenne': C['warn'],
        'medium': C['warn'], 'faible': C['bad'], 'low': C['bad']}


def chip(txt, color):
    return (f'<span class="chip" style="color:{color};border-color:{color}33;'
            f'background:{color}12">{esc(txt)}</span>')


def missing(what, how):
    return (f'<div class="empty"><strong>{esc(what)} : non relevé.</strong>'
            f'<div>{esc(how)}</div></div>')


def yesno(v):
    v = (v or '').strip().lower()
    if v in ('oui', 'yes', 'true', '1'):
        return f'<span class="dot ok"></span>oui'
    if v in ('non', 'no', 'false', '0'):
        return f'<span class="dot no"></span>non'
    return '<span class="muted">n/d</span>'


# ---------- Synthèse ----------
def count_by(rows, key):
    out = {}
    for r in rows or []:
        k = (r.get(key) or '').strip() or 'n/d'
        out[k] = out.get(k, 0) + 1
    return out


kpis = []
if queries is not None:
    byp = count_by(queries, 'priorite')
    kpis.append(('Requêtes', len(queries),
                 ' · '.join(f'{k} {v}' for k, v in sorted(byp.items()))))
else:
    kpis.append(('Requêtes', 'n/d', 'queries.csv absent'))

if pages is not None:
    bloq = sum(1 for r in pages if bloquant(r.get('bloque_par')))
    kpis.append(('Pages au portefeuille', len(pages),
                 f'{bloq} bloquée(s) par un intrant client' if bloq else 'aucun intrant bloquant'))
else:
    kpis.append(('Pages au portefeuille', 'n/d', 'pages.csv absent'))

if proof is not None:
    third = sum(1 for r in proof if 'tier' in (r.get('type') or '').lower()
                or 'third' in (r.get('type') or '').lower())
    weak = sum(1 for r in proof if (r.get('confiance') or '').strip().lower()
               in ('faible', 'low'))
    kpis.append(('Affirmations tracées', len(proof),
                 f'{third} adossée(s) à une source tierce · {weak} en confiance faible'))
else:
    kpis.append(('Affirmations tracées', 'n/d', 'proof.csv absent'))

if visib is not None and visib:
    tot = len(visib)
    men = sum(1 for r in visib if (r.get('mentionnee') or '').lower().startswith(('o', 'y')))
    cit = sum(1 for r in visib if (r.get('citee') or '').lower().startswith(('o', 'y')))
    kpis.append(('Relevés de visibilité IA', tot,
                 f'{men}/{tot} mentionnée · {cit}/{tot} citée en source'))
else:
    kpis.append(('Relevés de visibilité IA', 'n/d',
                 'aucun relevé, à lancer avec geo-citations (30 runs min.)'))

kpi_html = ''.join(
    f'<div class="kpi"><div class="kn">{esc(v)}</div><div class="kl">{esc(l)}</div>'
    f'<div class="ks">{esc(s)}</div></div>' for l, v, s in kpis)

# Entité
if entity:
    def field(label, key):
        v = entity.get(key)
        if isinstance(v, list):
            v = ' · '.join(str(x) for x in v)
        if not v:
            return ''
        return (f'<div class="frow"><div class="fk">{esc(label)}</div>'
                f'<div class="fv">{esc(v)}</div></div>')
    ent_rows = ''.join([
        field('Marque', 'marque'), field('Produit', 'produit'),
        field('Catégorie', 'categorie'), field('ICP', 'icp'),
        field('Marché', 'marche'), field('Langues', 'langues'),
    ])
    diffs = entity.get('differenciateurs') or []
    dh = ''
    if diffs:
        dh = '<table class="t"><thead><tr><th>Différenciateur</th><th>Preuve</th><th>Statut</th></tr></thead><tbody>'
        for d in diffs:
            st = (d.get('statut') or '').strip()
            col = C['bad'] if 'NON' in st.upper() or 'PRODUIRE' in st.upper() else C['good']
            dh += (f'<tr><td>{esc(d.get("claim"))}</td><td class="muted">{esc(d.get("preuve"))}</td>'
                   f'<td>{chip(st or "n/d", col)}</td></tr>')
        dh += '</tbody></table>'
    lim = entity.get('limites') or []
    lh = ('<ul class="ul">' + ''.join(f'<li>{esc(x)}</li>' for x in lim) + '</ul>') if lim else ''
    entity_html = (f'<div class="card"><h3>Entité</h3><div class="fields">{ent_rows}</div></div>'
                   + (f'<div class="card"><h3>Différenciateurs et preuves</h3>{dh}</div>' if dh else '')
                   + (f'<div class="card"><h3>Limites assumées</h3>{lh}</div>' if lh else ''))
else:
    entity_html = missing('Carte d\'entité', 'Renseigner data/entity.json (phase 1).')


def table(rows, cols, cellfn=None, searchkeys=None, filters=None):
    """cols: [(clé, libellé)] ; cellfn(clé, valeur, ligne) -> html ou None."""
    if rows is None:
        return None
    head = ''.join(f'<th>{esc(l)}</th>' for _, l in cols)
    body = []
    for r in rows:
        tds = []
        for k, _ in cols:
            v = (r.get(k) or '').strip()
            cell = cellfn(k, v, r) if cellfn else None
            dash = '<span class="muted">n/d</span>'
            tds.append('<td>' + (cell if cell is not None else (esc(v) or dash)) + '</td>')
        blob = ' '.join((r.get(k) or '') for k in (searchkeys or [c for c, _ in cols])).lower()
        attrs = ''.join(f' data-{f}="{esc((r.get(f) or "").strip().lower())}"' for f in (filters or []))
        body.append(f'<tr data-s="{esc(blob)}"{attrs}>' + ''.join(tds) + '</tr>')
    return (f'<table class="t"><thead><tr>{head}</tr></thead><tbody>'
            + ''.join(body) + '</tbody></table>')


def qcell(k, v, r):
    if k == 'priorite':
        return chip(v or 'n/d', PRIO.get(v.upper(), C['faint']))
    if k == 'brand_fit':
        try:
            n = float(v)
        except (TypeError, ValueError):
            return None
        col = C['good'] if n >= 8 else (C['accent'] if n >= 5 else C['faint'])
        return (f'<span class="bar"><i style="width:{min(100, n * 10):.0f}%;background:{col}"></i></span>'
                f'<span class="bn">{esc(v)}</span>')
    return None


q_html = table(queries,
               [('query', 'Requête'), ('intention', 'Intention'), ('priorite', 'Priorité'),
                ('brand_fit', 'Adéquation'), ('chemin_citation', 'Chemin de citation'),
                ('type_page', 'Module'), ('cluster', 'Cluster')],
               qcell, ['query', 'intention', 'cluster', 'type_page'],
               ['priorite', 'intention']) or missing(
    'Univers de requêtes', 'Produire data/queries.csv (phase 2).')


def pcell(k, v, r):
    if k == 'priorite':
        return chip(v or 'n/d', PRIO.get(v.upper(), C['faint']))
    if k == 'bloque_par':
        return chip(v, C['warn']) if bloquant(v) else f'<span class="muted">{esc(v) or "aucun"}</span>'
    if k in ('impact', 'effort') and v:
        return f'<span class="bn">{esc(v)}</span>'
    return None


p_html = table(pages,
               [('titre', 'Page'), ('type', 'Module'), ('cluster', 'Cluster'),
                ('requete_cible', 'Requête cible'), ('priorite', 'Priorité'),
                ('impact', 'Impact'), ('effort', 'Effort'),
                ('preuves_requises', 'Preuve requise'), ('bloque_par', 'Bloqué par'),
                ('statut', 'Statut')],
               pcell, ['titre', 'type', 'cluster', 'requete_cible', 'statut'],
               ['priorite', 'type', 'statut']) or missing(
    'Portefeuille de contenus', 'Produire data/pages.csv (phases 4 et 17).')


def prcell(k, v, r):
    if k == 'confiance':
        return chip(v or 'n/d', CONF.get(v.lower(), C['faint']))
    if k == 'type':
        col = C['accent'] if 'tier' in v.lower() or 'third' in v.lower() else C['faint']
        return chip(v or 'n/d', col)
    if k == 'source' and (r.get('url_source') or '').strip():
        return f'<a href="{esc(r["url_source"])}" target="_blank" rel="noopener">{esc(v or r["url_source"])}</a>'
    return None


pr_html = table(proof,
                [('affirmation', 'Affirmation'), ('page', 'Page'), ('source', 'Source'),
                 ('type', 'Type'), ('confiance', 'Confiance'), ('risque', 'Risque'),
                 ('action', 'Action')],
                prcell, ['affirmation', 'page', 'source', 'action'],
                ['confiance', 'type']) or missing(
    'Proof Map', 'Produire data/proof.csv (phases 7 et 8).')

a_html = table(authority,
               [('cible', 'Cible'), ('type', 'Type'), ('pourquoi', 'Pourquoi elle est pertinente'),
                ('sujet', 'Sujet'), ('preuve_a_fournir', 'Preuve à fournir'),
                ('angle', 'Angle'), ('statut', 'Statut')],
               None, ['cible', 'type', 'sujet', 'angle'], ['type', 'statut']) or missing(
    'Plan d\'autorité tierce', 'Produire data/authority.csv (phase 10).')

as_html = table(assets,
                [('nom', 'Actif'), ('question', 'Question à laquelle il répond'),
                 ('dataset', 'Jeu de données'), ('methodologie', 'Méthodologie'),
                 ('frequence', 'Fréquence'), ('angle_presse', 'Angle presse'),
                 ('statut', 'Statut')], None, None, ['statut'])
auth_html = a_html + ('<h3 class="sec">Actifs de données</h3>' + as_html if as_html else '')


def vcell(k, v, r):
    if k in ('mentionnee', 'recommandee', 'citee'):
        return yesno(v)
    if k == 'runs' and v:
        try:
            n = int(v)
        except ValueError:
            return None
        return chip(v, C['good'] if n >= 30 else C['bad'])
    return None


v_html = table(visib,
               [('query', 'Requête'), ('moteur', 'Moteur'), ('mentionnee', 'Mentionnée'),
                ('recommandee', 'Recommandée'), ('citee', 'Citée en source'),
                ('position', 'Position'), ('sources_citees', 'Sources citées à la place'),
                ('runs', 'Relevés'), ('date', 'Date')],
               vcell, ['query', 'moteur', 'sources_citees'], ['moteur']) or missing(
    'Visibilité dans les réponses IA',
    'Aucun relevé. Lancer geo-citations (30 relevés minimum par requête et par moteur, coût à valider avant). '
    'Tant qu\'il n\'y a pas de relevé, aucun chiffre de visibilité ne doit être présenté.')

if visib:
    v_html = ('<div class="note">Un taux ne vaut que sur 30 relevés minimum par requête '
              'et par moteur. Les lignes en rouge dans la colonne « Relevés » sont sous ce seuil : '
              'ce ne sont pas des échantillons crédibles.</div>' + v_html)

TABS = [('synthese', 'Synthèse', entity_html),
        ('requetes', 'Requêtes', q_html),
        ('pages', 'Pages', p_html),
        ('preuves', 'Preuves', pr_html),
        ('autorite', 'Autorité', auth_html),
        ('visibilite', 'Visibilité IA', v_html)]

tabs_nav = ''.join(
    f'<button class="tab{" active" if i == 0 else ""}" data-t="{t}">{esc(l)}</button>'
    for i, (t, l, _) in enumerate(TABS))
tabs_body = ''.join(
    f'<section class="pane{" active" if i == 0 else ""}" id="p-{t}">{c}</section>'
    for i, (t, l, c) in enumerate(TABS))

HTML = f"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Stratégie GEO · {esc(BRAND)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
*{{box-sizing:border-box}}
body{{margin:0;background:{C['bg']};color:{C['txt']};
 font:15px/1.55 Geist,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
 -webkit-font-smoothing:antialiased}}
.wrap{{max-width:1360px;margin:0 auto;padding:0 28px 80px}}
header{{padding:52px 0 26px}}
h1{{font-size:34px;letter-spacing:-.02em;margin:0 0 6px;font-weight:600}}
.sub{{color:{C['muted']};font-size:14px}}
.mono{{font-family:Geist Mono,ui-monospace,monospace;font-size:12px;color:{C['faint']}}}
.kpis{{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:14px;margin:22px 0 30px}}
.kpi{{background:{C['panel']};border:1px solid {C['line']};border-radius:14px;padding:18px 18px 16px}}
.kn{{font-size:30px;font-weight:600;letter-spacing:-.02em;line-height:1}}
.kl{{font-size:13px;font-weight:500;margin-top:8px}}
.ks{{font-size:12px;color:{C['muted']};margin-top:4px}}
nav{{display:flex;gap:4px;flex-wrap:wrap;border-bottom:1px solid {C['line']};margin-bottom:22px}}
.tab{{appearance:none;background:none;border:0;border-bottom:2px solid transparent;
 padding:11px 15px;font:500 14px Geist,sans-serif;color:{C['muted']};cursor:pointer}}
.tab:hover{{color:{C['txt']}}}
.tab.active{{color:{C['accent']};border-bottom-color:{C['accent']}}}
.pane{{display:none}} .pane.active{{display:block}}
.toolbar{{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:16px}}
input.q{{flex:1;min-width:240px;padding:10px 14px;border:1px solid {C['line']};border-radius:10px;
 background:{C['panel']};font:14px Geist,sans-serif;color:{C['txt']}}}
input.q:focus{{outline:none;border-color:{C['accent2']};box-shadow:0 0 0 3px {C['accent2']}1f}}
.fbtn{{appearance:none;background:{C['panel']};border:1px solid {C['line']};border-radius:999px;
 padding:8px 14px;font:500 13px Geist,sans-serif;color:{C['muted']};cursor:pointer}}
.fbtn.active{{background:{C['accent']};border-color:{C['accent']};color:#fff}}
table.t{{width:100%;border-collapse:separate;border-spacing:0;background:{C['panel']};
 border:1px solid {C['line']};border-radius:14px;overflow:hidden;font-size:13.5px}}
.tw{{overflow-x:auto}}
th{{text-align:left;font-weight:500;font-size:11.5px;letter-spacing:.06em;text-transform:uppercase;
 color:{C['faint']};padding:12px 14px;background:#f6f7fa;border-bottom:1px solid {C['line']};white-space:nowrap}}
td{{padding:12px 14px;border-bottom:1px solid {C['line']};vertical-align:top}}
tr:last-child td{{border-bottom:0}}
tbody tr:hover{{background:{C['accent2']}0a}}
.muted{{color:{C['faint']}}}
a{{color:{C['accent']}}}
.chip{{display:inline-block;border:1px solid;border-radius:999px;padding:2px 9px;
 font:500 12px Geist,sans-serif;white-space:nowrap}}
.bar{{display:inline-block;width:52px;height:6px;border-radius:3px;background:{C['line']};
 vertical-align:middle;margin-right:7px;overflow:hidden}}
.bar i{{display:block;height:100%}}
.bn{{font-family:Geist Mono,monospace;font-size:12px;color:{C['muted']}}}
.dot{{display:inline-block;width:7px;height:7px;border-radius:50%;margin-right:6px}}
.dot.ok{{background:{C['good']}}} .dot.no{{background:{C['bad']}}}
.card{{background:{C['panel']};border:1px solid {C['line']};border-radius:14px;padding:20px 22px;margin-bottom:16px}}
.card h3{{margin:0 0 14px;font-size:15px;font-weight:600}}
.fields{{display:grid;gap:2px}}
.frow{{display:grid;grid-template-columns:180px 1fr;gap:14px;padding:7px 0;border-bottom:1px solid {C['line']}}}
.frow:last-child{{border-bottom:0}}
.fk{{color:{C['faint']};font-size:13px}}
.ul{{margin:0;padding-left:18px;color:{C['muted']};font-size:14px}}
.ul li{{margin:4px 0}}
.empty{{background:{C['panel']};border:1px dashed {C['line']};border-radius:14px;padding:26px;
 color:{C['muted']};font-size:14px}}
.empty strong{{color:{C['txt']};display:block;margin-bottom:6px}}
.note{{background:#fff8ec;border:1px solid #f0dfc0;border-radius:12px;padding:12px 16px;
 font-size:13px;color:{C['warn']};margin-bottom:14px}}
.sec{{font-size:15px;font-weight:600;margin:30px 0 12px}}
footer{{margin-top:44px;padding-top:18px;border-top:1px solid {C['line']};
 color:{C['faint']};font-size:12px}}
@media(max-width:720px){{.frow{{grid-template-columns:1fr}} .wrap{{padding:0 16px 60px}}}}
</style></head><body>
<div class="wrap">
<header>
  <h1>Stratégie GEO · {esc(BRAND)}</h1>
  <div class="sub">Univers de requêtes, portefeuille de contenus, preuves, autorité tierce et visibilité dans les réponses génératives.</div>
  <div class="mono">Généré le {date.today().strftime('%d/%m/%Y')} · {esc(ROOT)}</div>
</header>
<div class="kpis">{kpi_html}</div>
<nav>{tabs_nav}</nav>
<div class="toolbar"><input class="q" type="search" placeholder="Rechercher dans le tableau affiché…"></div>
{tabs_body}
<footer>Les cases vides sont des relevés manquants, pas des zéros. Aucun chiffre de visibilité n'est affiché sans relevé réel (30 minimum par requête et par moteur).</footer>
</div>
<script>
const panes=[...document.querySelectorAll('.pane')];
document.querySelectorAll('.tab').forEach(b=>b.onclick=()=>{{
  document.querySelectorAll('.tab').forEach(x=>x.classList.remove('active'));
  b.classList.add('active');
  panes.forEach(p=>p.classList.toggle('active',p.id==='p-'+b.dataset.t));
  document.querySelector('input.q').value='';filter();toolbar();
}});
function toolbar(){{
  const pane=document.querySelector('.pane.active');
  document.querySelector('.toolbar').style.display=
    (pane&&pane.querySelector('table.t'))?'flex':'none';
}}
function filter(){{
  const q=document.querySelector('input.q').value.trim().toLowerCase();
  const pane=document.querySelector('.pane.active');
  if(!pane)return;
  pane.querySelectorAll('tbody tr').forEach(tr=>{{
    tr.style.display=(!q||(tr.dataset.s||'').includes(q))?'':'none';
  }});
}}
document.querySelector('input.q').addEventListener('input',filter);
toolbar();
document.querySelectorAll('table.t').forEach(t=>{{
  const w=document.createElement('div');w.className='tw';
  t.parentNode.insertBefore(w,t);w.appendChild(t);
}});
</script>
</body></html>"""

os.makedirs(ROOT, exist_ok=True)
with open(OUT, 'w', encoding='utf-8') as f:
    f.write(HTML)

present = [n for n, v in [('entity.json', entity), ('queries.csv', queries), ('pages.csv', pages),
                          ('proof.csv', proof), ('authority.csv', authority),
                          ('data_assets.csv', assets), ('visibility.csv', visib)] if v]
absent = [n for n, v in [('entity.json', entity), ('queries.csv', queries), ('pages.csv', pages),
                         ('proof.csv', proof), ('authority.csv', authority),
                         ('data_assets.csv', assets), ('visibility.csv', visib)] if not v]
print(f'Dashboard écrit : {OUT}')
print(f'  présents : {", ".join(present) or "aucun"}')
if absent:
    print(f'  manquants (affichés comme non relevés) : {", ".join(absent)}')
