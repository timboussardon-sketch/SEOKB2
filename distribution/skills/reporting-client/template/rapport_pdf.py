"""Gabarit PDF du skill reporting-client : couverture outremer grainée, résumé d'appui pour le call,
tableaux avec écarts ▲/▼ colorés. Extrait d'un reporting client validé par Organikk le 26/10/2026.
Mets ta marque dans MARQUE et ton logo (SVG) dans LOGO_SVG. Chrome est cherché aux emplacements
habituels (Mac, Windows, Linux) ; sinon, donne son chemin dans la variable CHROME.

    import sys; sys.path.insert(0, '<dossier du skill reporting-client>/template')
    from rapport_pdf import *
    corps = resume(pages, positions, source_positions, clics_avant, clics_apres, periodes) + sections...
    rendre(document(client, domaine, titre_periodes, donnees_arretees, sources, date, corps), 'sortie.html', 'sortie.pdf')
"""
import html, os, shutil, subprocess

e = html.escape
MARQUE = 'Organikk'  # nom affiché sur la couverture : remplace-le par le tien


def chrome():
    for c in (os.environ.get('CHROME'), '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
              r'C:\Program Files\Google\Chrome\Application\chrome.exe',
              r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
              shutil.which('google-chrome'), shutil.which('chromium'), shutil.which('chrome')):
        if c and os.path.exists(c):
            return c
    raise SystemExit('Chrome introuvable : donne son chemin dans la variable CHROME.')


LOGO_SVG = '''<svg class="mark" viewBox="0 0 96 96" aria-hidden="true"><path d="M0.0 92.84C40.85 54.96 57.38 54.05 96.0 57.49L53.09 91.05Q47.05 96.0 38.78 96.0L3.81 96.0A3.81 3.3 0 0 1 0.0 92.84Z"/><path d="M0.0 36.86C0.0 15.68 45.14 0.0 46.73 0.0L49.91 0.0A1.91 1.65 0 0 1 51.81 1.65L51.81 50.06C53.25 62.39 32.2 59.09 0.0 91.87Z"/></svg>'''  # logo de la couverture (symbole d'Organikk) : remplace-le par ton SVG


def n(x):
    return f'{round(x):,}'.replace(',', ' ')


def dec(x, d=1):
    return f'{x:.{d}f}'.replace('.', ',')


def sgn(v):
    return '+' if v > 0 else '−' if v < 0 else ''


def delta(a, b, kind='abs', d=1):
    """Cellule d'écart (html, classe). kind : abs (compte, + pourcentage), pt (points), pos (position : plus bas = mieux).
    ▲ / ▼ = le nombre monte / baisse ; vert = favorable, rouge = défavorable, gris = nul ou non calculable."""
    if a is None or b is None:
        return ('n/c', 'flat')
    diff = b - a
    if round(diff, 6) == 0:
        return ('= 0', 'flat')
    if kind == 'abs':
        txt = f'{sgn(diff)}{n(abs(diff))}' + (f' ({sgn(diff)}{dec(abs(diff) / a * 100)} %)' if a else ' (depuis 0)')
    elif kind == 'pt':
        txt = f'{sgn(diff)}{dec(abs(diff), d)} pt'
    else:
        txt = f'{sgn(diff)}{dec(abs(diff), d)}'
    good = diff < 0 if kind == 'pos' else diff > 0
    return (('▲ ' if diff > 0 else '▼ ') + txt, 'up' if good else 'down')


def table(head, rows, cls=''):
    h = ''.join(f'<th>{e(str(c))}</th>' for c in head)
    def td(c):
        if isinstance(c, tuple):
            return f'<td class="{c[1]}">{c[0]}</td>'
        return f'<td>{c}</td>'
    r = ''.join('<tr>' + ''.join(td(c) for c in row) + '</tr>' for row in rows)
    return f'<table class="{cls}"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table>'


LEG = ('<p class="legend"><span class="up">▲ vert</span> hausse favorable · <span class="down">▼ rouge</span> baisse défavorable · '
       '<span class="flat">gris</span> écart nul ou non calculable. Le signe ▲ ou ▼ donne le sens du chiffre. '
       'Exception pour la position moyenne : un chiffre plus bas est meilleur, donc vert quand il diminue (▼ vert) et rouge quand il augmente (▲ rouge).</p>')


def cover(client, domaine, periodes, donnees_arretees, sources, date):
    """Couverture pleine page, dégradé outremer grainé, logo et marque."""
    return (f'<section class="cover"><div class="cv-brand"><span class="chip">{LOGO_SVG}</span>{e(MARQUE)}</div>'
            f'<div class="cv-main"><div class="cv-k">{e(client)} · {e(domaine)}</div><h1>Reporting SEO et GEO</h1>'
            f'<p class="cv-sub">{periodes}<br>{donnees_arretees}</p></div>'
            f'<div class="cv-foot"><span>{e(date)}</span><span>Sources : {sources}</span></div></section>')


def resume(pages, positions, source_positions, clics_avant, clics_apres, periodes):
    """Encadré d'appui pour le call (consigne de Tim, 26/10/2026) : pages créées, positions des mots-clés
    business, écart de clics entre les deux périodes. Chiffres seulement, identiques aux sections du rapport.
    pages : [(libellé, nombre)] ; positions : [(mot-clé, position)] ; periodes : (libellé avant, libellé après)."""
    return ('<h2>Résumé</h2>'
            + table(['Pages créées', 'Nombre'], [[e(l), str(v)] for l, v in pages])
            + table(['Mot-clé business', 'Position'], [[e(k), e(p)] for k, p in positions])
            + f'<p class="note">{e(source_positions)}</p>'
            + table(['Clics Search Console', periodes[0], periodes[1], 'Écart'],
                    [['Site entier', n(clics_avant), n(clics_apres), delta(clics_avant, clics_apres)]]) + LEG)


CSS = '''
@page { size: A4; margin: 16mm 14mm 16mm 14mm; @bottom-right { content: counter(page); font-size: 8pt; color:#6B7280 } }
@page kwpage { size: A4 landscape; margin: 11mm 12mm 12mm 12mm; @bottom-right { content: counter(page); font-size: 8pt; color:#6B7280 } }
:root{--ink:#212121;--muted:#6B7280;--line:#E5E7EB;--blue:#4685F0;--blue-deep:#2956B2;--blue-soft:#ECF2FE;--up:#059669;--down:#DC2626}
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact} body{font-family:'Geist',system-ui,-apple-system,'Helvetica Neue',Arial,sans-serif;color:var(--ink);font-size:9.5pt;line-height:1.45;margin:0}
@page cover{size:A4;margin:0}.cover{page:cover;position:relative;isolation:isolate;overflow:hidden;width:100%;height:297mm;padding:22mm 20mm 30mm;display:flex;flex-direction:column;justify-content:space-between;color:#fff;background:radial-gradient(ellipse at 95% 110%,#aec5ff 0%,transparent 62%),linear-gradient(145deg,#2f4fe0 20%,#567af1 70%,#7fa0ff);page-break-after:always}.cover::after{content:'';position:absolute;inset:0;z-index:-1;background-image:url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='260' height='260'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.7' numOctaves='3' stitchTiles='stitch'/><feColorMatrix type='saturate' values='0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>\");background-size:260px 260px;opacity:.5;mix-blend-mode:overlay}.cv-brand{display:flex;align-items:center;gap:11px;font-size:17pt;font-weight:500;letter-spacing:-.02em}.cv-brand .chip{display:grid;place-items:center;width:40px;height:40px;border-radius:13px;background:rgba(255,255,255,.16);border:1px solid rgba(255,255,255,.3)}.cv-brand .mark{width:24px;height:24px;fill:#fff}.cv-k{font-family:'Geist Mono',ui-monospace,Menlo,monospace;font-size:9.5pt;letter-spacing:.1em;text-transform:uppercase;margin-bottom:18px}.cover h1{font-size:44pt;font-weight:500;letter-spacing:-.05em;line-height:1.04;margin:0 0 24px;color:#fff}.cv-sub{font-size:11pt;line-height:1.55;max-width:150mm;margin:0}.cv-foot{display:flex;gap:24px;font-size:8.5pt;line-height:1.45;opacity:.9}.cv-foot span:first-child{font-family:'Geist Mono',ui-monospace,Menlo,monospace;white-space:nowrap}.sub{color:var(--muted);font-size:10pt}
h2{font-size:15pt;margin:22px 0 8px;padding-bottom:4px;border-bottom:2px solid var(--blue);page-break-after:avoid}
h3{font-size:10.5pt;margin:16px 0 6px;color:var(--blue-deep);page-break-after:avoid}
h4{font-size:9.5pt;margin:12px 0 4px;color:var(--ink);page-break-after:avoid}
table{width:100%;border-collapse:collapse;margin:6px 0 10px;font-size:8.8pt}
th{background:var(--blue-soft);text-align:left;font-weight:600;border-bottom:1px solid var(--blue);padding:4px 6px}
td{padding:3.5px 6px;border-bottom:1px solid var(--line);vertical-align:top}td,th{hyphens:none;-webkit-hyphens:none;word-break:normal;overflow-wrap:normal}table.mq{table-layout:fixed}table.mq td:first-child,table.mq th:first-child{width:13%}
table.small{font-size:8pt}table.tiny{font-size:8pt}table.tiny td,table.tiny th{padding:2.5px 4px}
table.kv td:first-child{width:24%;font-weight:600}
td.up{background:rgba(5,150,105,.14);white-space:nowrap}
td.down{background:rgba(220,38,38,.12);white-space:nowrap}
td.flat{background:rgba(107,114,128,.10);color:#374151;white-space:nowrap}
td.up::first-letter{color:var(--up);font-weight:700}td.down::first-letter{color:var(--down);font-weight:700}
.dl{padding:1px 6px;font-weight:600}.dl.up{background:rgba(5,150,105,.14)}.dl.down{background:rgba(220,38,38,.12)}.dl.flat{background:rgba(107,114,128,.10)}
.legend{font-size:8pt;color:var(--muted);margin:2px 0 8px}.legend .up{color:var(--up);font-weight:600}.legend .down{color:var(--down);font-weight:600}.legend .flat{color:#6B7280;font-weight:600}
tr{page-break-inside:avoid}
h2.brk{page-break-before:always}table.keep{page-break-inside:avoid}table.small code,table.tiny code{font-size:1em}.legend{page-break-inside:avoid}
code{font-family:'Geist Mono',ui-monospace,Menlo,monospace;font-size:.88em;word-break:break-all}
p{margin:6px 0}.note{color:var(--muted);font-size:8.6pt}ul{margin:4px 0 8px;padding-left:18px}li{margin:2px 0}
figure.chart{margin:8px 0;page-break-inside:avoid}figcaption{font-size:8pt;color:var(--muted)}'''

FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap">'


def document(client, domaine, periodes, donnees_arretees, sources, date, corps, css_extra=''):
    return (f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>{e(client)} · Reporting SEO et GEO · {e(date)}</title>'
            f'{FONTS}<style>{CSS}{css_extra}</style></head><body>'
            f'{cover(client, domaine, periodes, donnees_arretees, sources, date)}{corps}</body></html>')


def rendre(doc, html_path, pdf_path):
    """Écrit le HTML puis le PDF (Chrome headless ; --virtual-time-budget laisse charger les polices).
    Contrôler ensuite la couverture : pdftoppm -f 1 -l 1, aucune bande blanche, pas de page vide en 2."""
    open(html_path, 'w').write(doc)
    subprocess.run([chrome(), '--headless', '--disable-gpu', '--no-pdf-header-footer', '--virtual-time-budget=8000',
                    f'--print-to-pdf={os.path.abspath(pdf_path)}', 'file://' + os.path.abspath(html_path)],
                   check=True, capture_output=True)
