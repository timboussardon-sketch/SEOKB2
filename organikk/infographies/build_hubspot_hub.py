"""Stratégie GEO de HubSpot en 8 étapes, schéma en cases autour d'une carte centrale outremer grainée.
Modèle demandé par Tim le 2026-10-28 (référence : schéma « Claude Code, ton agent SEO », cases numérotées reliées au centre).
Textes : newsletter Algorithme, [[sources/2026-10-27-algorithme-strategie-geo-hubspot]]."""
from build import HEAD

# Outremer profond grainé (consigne de Tim du 2026-10-28) : bords bleu nuit, cœur outremer vif, grain marqué.
DEEP = '''<radialGradient id="dg" cx=".32" cy=".38" r=".78"><stop offset="0" stop-color="#3a5cff"/><stop offset=".35" stop-color="#2341e0"/><stop offset=".7" stop-color="#12249a"/><stop offset="1" stop-color="#070f4d"/></radialGradient>
<filter id="dn" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB"><feTurbulence type="fractalNoise" baseFrequency=".95" numOctaves="2" stitchTiles="stitch" result="t"/><feColorMatrix in="t" type="matrix" values="1 0 0 0 0  1 0 0 0 0  1 0 0 0 0  0 0 0 0 1" result="m"/><feComposite in="SourceGraphic" in2="m" operator="arithmetic" k1="0" k2="1" k3=".62" k4="-.31" result="g"/><feComposite in="g" in2="SourceGraphic" operator="in"/></filter>'''

def grain(shape):
    return f'<g fill="url(#dg)" filter="url(#dn)">{shape}</g>'

W, H = 1800, 1200
head = HEAD.replace('width="1536" height="1024" viewBox="0 0 1536 1024"', f'width="{W}" height="{H}" viewBox="0 0 {W} {H}"')
CSS = '''<style>
.ct{font-size:30px;font-weight:700;fill:#0B0B0F;letter-spacing:-0.8px}
.cs{font-size:19px;fill:#333}
.li{font-size:17px;fill:#0B0B0F}
.lg{font-size:16px;fill:#777}
.n{font-size:22px;font-weight:700;fill:#FFF}
.num{font-size:54px;font-weight:700;fill:#0B0B0F;letter-spacing:-2px}
.ic{fill:none;stroke:#0B0B0F;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
</style>'''

def card(x, y, w, h, n, title, sub):
    return [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="#FFF" stroke="#0B0B0F" stroke-opacity=".35" stroke-width="1.5"/>',
            f'<circle cx="{x+50}" cy="{y+56}" r="25" fill="#0B0B0F"/><text class="n" x="{x+50}" y="{y+64}" text-anchor="middle">{n}</text>',
            f'<text class="ct" x="{x+92}" y="{y+56}">{title}</text>',
            f'<text class="cs" x="{x+92}" y="{y+86}">{sub}</text>']

# icônes façon Lucide, 22 px, coin haut gauche (x, y)
def i_file(x, y): return f'<path class="ic" d="M{x+4} {y+1}h9l6 6v14h-15z M{x+13} {y+1}v6h6"/>'
def i_check(x, y): return f'<circle cx="{x+11}" cy="{y+11}" r="11" fill="#0B0B0F"/><path d="M{x+6} {y+11}l3.5 3.5 6.5-7" fill="none" stroke="#FFF" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>'
def i_box(x, y): return f'<rect class="ic" x="{x+2}" y="{y+2}" width="18" height="18" rx="3"/>'
def i_news(x, y): return f'<path class="ic" d="M{x+2} {y+3}h15v17h-13a2 2 0 0 1-2-2z M{x+17} {y+8}h3v10a2 2 0 0 1-2 2 M{x+6} {y+8}h7 M{x+6} {y+12}h7 M{x+6} {y+16}h4"/>'
def i_users(x, y): return f'<circle class="ic" cx="{x+8}" cy="{y+7}" r="4"/><path class="ic" d="M{x+1} {y+20}a7 7 0 0 1 14 0 M{x+15} {y+3.5}a4 4 0 0 1 0 7 M{x+17} {y+14}a6 6 0 0 1 4 6"/>'
def i_link(x, y): return f'<path class="ic" d="M{x+9} {y+13}a5 5 0 0 0 7 0l3-3a5 5 0 0 0-7-7l-1.5 1.5 M{x+13} {y+9}a5 5 0 0 0-7 0l-3 3a5 5 0 0 0 7 7l1.5-1.5"/>'

def wire(pts):
    x, y = pts[0]
    d = "M" + " L".join(f"{a} {b}" for a, b in pts)
    return (f'<path d="{d}" fill="none" stroke="#2341e0" stroke-width="1.5"/>'
            f'<rect x="{x-3}" y="{y-3}" width="6" height="6" fill="#2341e0"/>')

WIRES = [[(580, 300), (605, 300), (605, 530), (690, 530)], [(900, 380), (900, 500)],
         [(1220, 300), (1195, 300), (1195, 530), (1110, 530)], [(1220, 610), (1110, 610)],
         [(1220, 900), (1195, 900), (1195, 670), (1110, 670)], [(900, 820), (900, 700)],
         [(580, 900), (605, 900), (605, 670), (690, 670)], [(580, 610), (690, 610)]]

o = []
CW, CH = 540, 340
cols = [40, 630, 1220]
ry = [40, 430, 820]
cx0, cy0, cw, ch = 690, 500, 420, 200

# 1 — priorités business
x, y = cols[0], ry[0]
o += card(x, y, CW, CH, 1, "Priorités business", "5 parcours commerciaux, pas 5 cocons")
for i, (nom, req) in enumerate([("Smart CRM", "CRM pour PME"), ("Marketing Hub", "marketing automation"),
                                ("Sales Hub", "gestion commerciale"), ("Service Hub", "service client"), ("Content Hub", "gestion de contenu")]):
    yy = y + 130 + i*40
    o += [i_box(x+40, yy-17), f'<text class="li" x="{x+76}" y="{yy}">{nom}</text>', f'<text class="lg" x="{x+250}" y="{yy}">{req}</text>']

# 2 — données propriétaires
x, y = cols[1], ry[0]
o += card(x, y, CW, CH, 2, "Données propriétaires", "6 sources par offre")
o.append(f'<line x1="{x+40}" y1="{y+112}" x2="{x+40}" y2="{y+312}" stroke="#0B0B0F" stroke-opacity=".2"/>')
for i, t in enumerate(["Questions posées aux commerciaux", "Objections et motifs d'abandon", "Tickets de support",
                       "Fonctionnalités demandées en démo", "Cas clients sectoriels", "Recherches internes et Search Console"]):
    yy = y + 130 + i*33
    o += [i_file(x+60, yy-17), f'<text class="li" x="{x+96}" y="{yy}">{t}</text>']

# 3 — micro-intentions
x, y = cols[2], ry[0]
o += card(x, y, CW, CH, 3, "Micro-intentions", "10 à 15 questions d'acheteurs par offre")
for i, (v, lab) in enumerate([("5", "offres"), ("25", "micro-intentions"), ("50", "questions")]):
    xx = x + 50 + i*170
    o += [f'<text class="num" x="{xx}" y="{y+220}">{v}</text>', f'<text class="lg" x="{xx}" y="{y+250}">{lab}</text>']
    if i < 2:
        o.append(f'<path d="M{xx+110} {y+202} h34" class="line" marker-end="url(#p)"/>')
o.append(f'<text class="lg" x="{x+50}" y="{y+306}">jusqu\'à 75 avec les demandes réelles des prospects</text>')

# 4 — architecture
x, y = cols[2], ry[1]
o += card(x, y, CW, 360, 4, "Architecture", "Une page par intention, pas par question")
o += [f'<rect x="{x+40}" y="{y+200}" width="170" height="52" rx="8" fill="none" stroke="#0B0B0F" stroke-width="1.6"/>',
      f'<text class="li" x="{x+125}" y="{y+232}" text-anchor="middle" style="font-weight:700">Page business</text>']
for i, (t, ic) in enumerate([("Page sectorielle", i_file), ("Cas client", i_users), ("Page d'appui", i_file), ("Outil interactif", i_box)]):
    yy = y + 140 + i*56
    o.append(f'<path d="M{x+210} {y+226} H{x+240} V{yy} H{x+270}" fill="none" stroke="#0B0B0F" stroke-opacity=".5" stroke-width="1.4"/>')
    o += [ic(x+282, yy-11), f'<text class="li" x="{x+318}" y="{yy+6}">{t}</text>']

# 5 — preuves
x, y = cols[2], ry[2]
o += card(x, y, CW, CH, 5, "Preuves propriétaires", "Une preuve par question d'acheteur")
for i, t in enumerate(["Cas client du secteur", "Tarifs et budget", "Données clients", "Démonstration", "Déploiement réel", "Avant/après"]):
    xx, yy = x + 50 + (i//3)*250, y + 140 + (i%3)*52
    o += [i_check(xx, yy-17), f'<text class="li" x="{xx+36}" y="{yy}">{t}</text>']
o.append(f'<text class="lg" x="{x+50}" y="{y+296}">Chiffre HubSpot : 92 % des pages sectorielles</text>')
o.append(f'<text class="lg" x="{x+50}" y="{y+320}">citées par des moteurs de réponse</text>')

# 6 — page business
x, y = cols[1], ry[2]
o += card(x, y, CW, CH, 6, "Page optimisée", "Google, les IA et les prospects")
for i, t in enumerate(["Introduction", "Fonctionnalités", "Déploiement", "Prix", "Preuves", "Questions fréquentes", "Conversion"]):
    xx, yy = x + 50 + (i//4)*250, y + 140 + (i%4)*46
    o += [f'<circle cx="{xx+13}" cy="{yy-6}" r="14" fill="#F5F5F5"/><text class="lg" x="{xx+13}" y="{yy-1}" text-anchor="middle" style="fill:#0B0B0F;font-weight:500">{i+1}</text>',
          f'<text class="li" x="{xx+40}" y="{yy}">{t}</text>']

# 7 — distribution
x, y = cols[0], ry[2]
o += card(x, y, CW, CH, 7, "Distribution externe", "Des mentions utiles, sans achat de liens")
for i, (t, ic) in enumerate([("Publications spécialisées", i_news), ("Partenaires sectoriels", i_link), ("Communautés professionnelles", i_users)]):
    yy = y + 150 + i*58
    o += [ic(x+50, yy-17), f'<text class="li" x="{x+90}" y="{yy}">{t}</text>']
    if i < 2:
        o.append(f'<line x1="{x+90}" y1="{yy+24}" x2="{x+500}" y2="{yy+24}" stroke="#0B0B0F" stroke-opacity=".12"/>')

# 8 — dashboard
x, y = cols[0], ry[1]
o += card(x, y, CW, 360, 8, "Dashboard GEO", "Un reporting par offre")
for i, (lvl, m) in enumerate([("SEO", "Clics non-brand, CTR, positions"), ("GEO", "Mentions, citations, couverture"), ("Business", "Essais, démos, leads, clients")]):
    yy = y + 150 + i*66
    o += [f'<rect x="{x+50}" y="{yy-24}" width="104" height="34" rx="17" fill="none" stroke="#0B0B0F" stroke-width="1.5"/>',
          f'<text class="li" x="{x+102}" y="{yy-1}" text-anchor="middle" style="font-weight:700">{lvl}</text>',
          f'<text class="li" x="{x+176}" y="{yy-1}">{m}</text>']

# centre
o += [grain(f'<rect x="{cx0}" y="{cy0}" width="{cw}" height="{ch}" rx="18"/>'),
      f'<text x="{cx0+40}" y="{cy0+90}" style="font-size:42px;font-weight:700;fill:#FFF;letter-spacing:-1.2px">Stratégie GEO</text>',
      f'<text x="{cx0+40}" y="{cy0+126}" style="font-size:21px;fill:#FFF">HubSpot, en 8 étapes</text>']

wires = [wire(w) for w in WIRES]
k = len(o) - 3   # les traits passent sous la carte centrale
body = o[:k] + wires + o[k:]
svg = head + CSS + DEEP + '</defs>\n<rect width="100%" height="100%" fill="#FFF"/>\n' + "\n".join(x for x in body if x) + "\n</svg>"
open("strategie-geo-hubspot-hub.svg", "w").write(svg)
