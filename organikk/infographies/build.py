"""Visuels du système SEO KB, 3 compositions (skill infographie-schema, ORGANIKK Visual Design System).
Chiffres : fichiers .md comptés dans le vault le 2026-10-27. Textes : AGENTS.md.
grain() habille n'importe quelle forme : c'est la seule brique à réutiliser, pas les compositions."""
import math

HEAD = '''<svg xmlns="http://www.w3.org/2000/svg" width="1536" height="1024" viewBox="0 0 1536 1024">
<defs>
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&amp;display=swap');
text{font-family:Inter,sans-serif}
.h{font-size:40px;font-weight:700;fill:#0B0B0F;letter-spacing:-1.2px}
.sub{font-size:20px;fill:#333}
.t{font-size:24px;font-weight:700;fill:#0B0B0F;letter-spacing:-0.5px}
.s{font-size:17px;fill:#333}
.a{font-size:15px;font-weight:500;fill:#777}
.big{font-size:150px;font-weight:700;fill:#0B0B0F;letter-spacing:-6px}
.v{font-size:17px;font-weight:700;fill:#0B0B0F}
.line{fill:none;stroke:#0B0B0F;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.thin{fill:none;stroke:#0B0B0F;stroke-width:1;stroke-linecap:round}
</style>
<linearGradient id="og" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2f4fe0"/><stop offset=".45" stop-color="#2f4fe0"/><stop offset="1" stop-color="#7fa0ff"/></linearGradient>
<filter id="on" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="3" stitchTiles="stitch" result="t"/><feColorMatrix in="t" type="saturate" values="0" result="m"/><feComponentTransfer in="m" result="a"><feFuncA type="linear" slope=".6"/></feComponentTransfer><feComposite in="a" in2="SourceGraphic" operator="in" result="c"/><feBlend in="SourceGraphic" in2="c" mode="overlay"/></filter>
<marker id="p" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M1 1 L8 5 L1 9" fill="none" stroke="#0B0B0F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></marker>
'''

def grain(shape, *_):
    """Outremer grainé Organikk (dégradé et filtre du logo organikk.co) sur n'importe quelle forme SVG."""
    return f'<g fill="url(#og)" filter="url(#on)">{shape}</g>'

def page(name, body):
    open(name, "w").write(HEAD + '</defs>\n<rect width="1536" height="1024" fill="#FFF"/>\n' + "\n".join(body) + "\n</svg>")

# ---------- A : barres ----------
bars = [("sources", 182), ("entities", 81), ("synthèses", 78), ("concepts", 70), ("queries", 52),
        ("briefs", 32), ("méthodes", 27), ("clusters", 14), ("posts LinkedIn", 11), ("revues de presse", 8), ("preuves", 7)]
o = ['<text class="h" x="60" y="110">Ce que contient le vault SEO KB</text>',
     '<text class="sub" x="60" y="148">Pages .md par dossier de wiki/, comptées le 27 octobre 2026</text>',
     '<text class="big" x="52" y="460">1 034</text>',
     '<text class="t" x="60" y="512">pages dans wiki/</text>',
     '<text class="s" x="60" y="544">compilées par Claude Code</text>',
     '<text class="s" x="60" y="570">depuis 1 297 fichiers dans raw/</text>']
x0, y0, step, maxw = 860, 250, 58, 560
o.append(f'<line class="thin" x1="{x0}" y1="{y0-34}" x2="{x0}" y2="{y0+len(bars)*step-30}"/>')
for i, (lab, v) in enumerate(bars):
    y = y0 + i*step
    w = round(v/182*maxw)
    o.append(f'<text class="s" x="{x0-20}" y="{y+6}" text-anchor="end">{lab}</text>')
    if i == 0:
        o.append(grain(f'<rect x="{x0}" y="{y-20}" width="{w}" height="40"/>', x0, y-20, w, 40))
    else:
        o.append(f'<rect x="{x0}" y="{y-11}" width="{w}" height="22" fill="#0B0B0F"/>')
    o.append(f'<text class="v" x="{x0+w+12}" y="{y+6}">{v}</text>')
o.append('<text class="a" x="60" y="964">Source : comptage des fichiers .md de seo-kb, 27/10/2026. Hors registres, index et log.</text>')
page("systeme-seo-kb-a-barres.svg", o)

# ---------- B : cycle ----------
cx, cy, R = 1000, 560, 270
steps = [("raw/", "sources brutes, exports GSC"), ("Claude Code", "ingère, relie, cite"), ("wiki/", "1 034 pages compilées"),
         ("Skills SEO", "briefs, clusters, articles"), ("Publication", "contenu en ligne"), ("Preuve", "mesure à J+30 et J+90")]
pts = [(cx + R*math.cos(math.radians(-90 + 60*i)), cy + R*math.sin(math.radians(-90 + 60*i))) for i in range(6)]
o = ['<text class="h" x="60" y="110">Le cycle du système SEO KB</text>',
     '<text class="sub" x="60" y="148">De la source brute à la preuve mesurée, puis retour dans raw/</text>']
for i in range(6):
    a1, a2 = math.radians(-90 + 60*i + 9), math.radians(-90 + 60*(i+1) - 9)
    x1, y1 = cx + R*math.cos(a1), cy + R*math.sin(a1)
    x2, y2 = cx + R*math.cos(a2), cy + R*math.sin(a2)
    o.append(f'<path class="line" d="M{x1:.1f} {y1:.1f} A{R} {R} 0 0 1 {x2:.1f} {y2:.1f}" marker-end="url(#p)"/>')
for i, ((x, y), (t, s)) in enumerate(zip(pts, steps)):
    if t == "Preuve":
        o.append(grain(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="40"/>', x-40, y-40, 80, 80))
    else:
        o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="#0B0B0F"/>')
    right = x > cx + 1 or (abs(x - cx) < 1)
    if abs(x - cx) < 1:
        tx, anchor, ty = x, "middle", (y - 48 if y < cy else y + 68)
    elif right:
        tx, anchor, ty = x + 30, "start", y - 4
    else:
        tx, anchor, ty = x - (60 if t == "Preuve" else 30), "end", y - 4
    o.append(f'<text class="a" x="{tx:.1f}" y="{ty-30:.1f}" text-anchor="{anchor}">0{i+1}</text>')
    o.append(f'<text class="t" x="{tx:.1f}" y="{ty:.1f}" text-anchor="{anchor}">{t}</text>')
    o.append(f'<text class="s" x="{tx:.1f}" y="{ty+26:.1f}" text-anchor="{anchor}">{s}</text>')
o += ['<text class="t" x="60" y="700">La donnée de preuve ferme la boucle</text>',
      '<text class="s" x="60" y="736">Le contenu publié revient mesuré dans raw/data/exports-gsc/,</text>',
      '<text class="s" x="60" y="762">puis gsc-watcher en tire une fiche preuve.</text>',
      '<text class="s" x="60" y="788">Sans elle, les hypothèses restent ouvertes.</text>',
      '<text class="a" x="60" y="824">AGENTS.md §14</text>']
page("systeme-seo-kb-b-cycle.svg", o)

# ---------- C : frise ----------
ly = 560
cols = [(150, "Tous les jours", "12:30", "ingest-transcript", "chaque call devient une fiche"),
        (450, "Lundi", "08:00", "ingest-backlog-sweep", "trie le raw non digéré"),
        (720, "Mercredi", "09:00", "resurgence-espacee", "remonte un concept oublié"),
        (1230, "1er du mois", "07:00", "gsc-watcher", "puis hypotheses-validation")]
o = ['<text class="h" x="60" y="110">La semaine du système SEO KB</text>',
     '<text class="sub" x="60" y="148">Les automatisations préparent. Un seul moment de décision.</text>',
     f'<line class="line" x1="60" y1="{ly}" x2="1470" y2="{ly}" marker-end="url(#p)"/>']
for x, day, hour, skill, what in cols:
    o.append(f'<line class="thin" x1="{x}" y1="{ly}" x2="{x}" y2="{ly+46}"/><circle cx="{x}" cy="{ly}" r="6" fill="#0B0B0F"/>')
    o.append(f'<text class="t" x="{x}" y="{ly+88}">{day}, {hour}</text>')
    o.append(f'<text class="s" x="{x}" y="{ly+118}">{skill}</text>')
    o.append(f'<text class="s" x="{x}" y="{ly+142}" style="fill:#777">{what}</text>')
fx = 1040
o.append(grain(f'<circle cx="{fx}" cy="{ly}" r="64"/>', fx-64, ly-64, 128, 128))
o.append(f'<line class="thin" x1="{fx}" y1="{ly-64}" x2="{fx}" y2="{ly-150}"/>')
o.append(f'<text class="h" x="{fx}" y="{ly-200}">Vendredi, Tim tranche</text>')
o.append(f'<text class="s" x="{fx}" y="{ly-168}">17:30, revue-hebdo : 8 décisions</text>')
o.append('<text class="a" x="60" y="964">Cadences prévues dans AGENTS.md §7bis. Ce qui tourne vraiment : wiki/ops/sante-automatisations.</text>')
page("systeme-seo-kb-c-semaine.svg", o)
