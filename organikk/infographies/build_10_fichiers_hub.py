"""Les 10 fichiers d'un système SEO avec Claude Code, en cases autour d'une carte centrale outremer grainée.
Modèle « hub à cases » validé par Tim le 2026-10-28. Textes : post LinkedIn de Tim du 2026-10-28 (10 fichiers), rien d'autre."""
from build_hubspot_hub import head, CSS, DEEP, grain, i_file, i_check, i_box, i_users, i_link, i_news

W, H = 2000, 1200
head2 = head.replace('width="1800" height="1200" viewBox="0 0 1800 1200"', f'width="{W}" height="{H}" viewBox="0 0 {W} {H}"')
CSS2 = CSS.replace('</style>', '.mono{font-size:16px;fill:#0B0B0F;font-family:"SF Mono",Menlo,monospace}\n.lb{font-size:17px;font-weight:500;fill:#0B0B0F}\n</style>')

CW, CH = 460, 360
cols = [30, 523, 1016, 1509]
ry = [30, 420, 810]

def folder(x, y, w, h, tw=150, th=24, r=12):
    """Silhouette de dossier : onglet en haut à gauche, corps arrondi."""
    b = y + th
    return (f"M{x} {y+r} Q{x} {y} {x+r} {y} H{x+tw-14} Q{x+tw-6} {y} {x+tw} {y+8} L{x+tw+10} {b-4} Q{x+tw+13} {b} {x+tw+20} {b} "
            f"H{x+w-r} Q{x+w} {b} {x+w} {b+r} V{y+h-r} Q{x+w} {y+h} {x+w-r} {y+h} H{x+r} Q{x} {y+h} {x} {y+h-r} Z")

def card(x, y, n, title, sub):
    return [f'<path d="{folder(x, y, CW, CH)}" fill="#FFF" stroke="#0B0B0F" stroke-opacity=".35" stroke-width="1.5"/>',
            f'<text x="{x+24}" y="{y+18}" style="font-size:14px;font-weight:700;fill:#0B0B0F;letter-spacing:.5px">{n:02d}</text>',
            f'<text class="ct" x="{x+40}" y="{y+66}">{title}</text>',
            f'<text class="cs" x="{x+40}" y="{y+94}">{sub}</text>']

def arrow(x1, y1, x2, y2):
    return f'<path d="M{x1} {y1} L{x2} {y2}" class="line" stroke-width="1.6" marker-end="url(#p)"/>'

o = []
# 1 CLAUDE.md : premier fichier consulté, pointe vers règles / méthodes / instructions
x, y = cols[0], ry[0]
o += card(x, y, 1, "CLAUDE.md", "Le premier fichier lu")
o += [f'<rect x="{x+40}" y="{y+200}" width="120" height="48" rx="8" fill="none" stroke="#0B0B0F" stroke-width="1.6"/>',
      f'<text class="lb" x="{x+100}" y="{y+230}" text-anchor="middle">Claude</text>']
for i, t in enumerate(["où sont les règles", "où sont les méthodes", "où sont les instructions"]):
    yy = y + 150 + i*75
    o.append(f'<path d="M{x+160} {y+224} H{x+190} V{yy} H{x+215}" fill="none" stroke="#0B0B0F" stroke-opacity=".5" stroke-width="1.4"/>')
    o += [i_file(x+225, yy-11), f'<text class="li" x="{x+258}" y="{yy+6}">{t}</text>']

# 2 AGENTS.md : règles communes, coches
x, y = cols[1], ry[0]
o += card(x, y, 2, "AGENTS.md", "Les règles communes")
for i, t in enumerate(["Utiliser les données", "Vérifier les informations", "Présenter les résultats", "Valider avant de modifier un site"]):
    yy = y + 150 + i*48
    o += [i_check(x+40, yy-17), f'<text class="li" x="{x+84}" y="{yy}">{t}</text>']

# 3 client.md : fiche, champs
x, y = cols[2], ry[0]
o += card(x, y, 3, "client.md", "La fiche de ton client")
for i, t in enumerate(["Ce qu'il vend", "À qui", "Sur quel marché", "Ce qui le différencie"]):
    yy = y + 150 + i*48
    o += [f'<text class="lg" x="{x+40}" y="{yy}">{t}</text>',
          f'<line x1="{x+240}" y1="{yy+2}" x2="{x+420}" y2="{yy+2}" stroke="#0B0B0F" stroke-opacity=".25" stroke-width="1.2"/>']

# 4 conversions.md : objectifs en pilules
x, y = cols[3], ry[0]
o += card(x, y, 4, "conversions.md", "Les objectifs commerciaux")
for i, t in enumerate(["Devis", "Appels", "Inscriptions", "Achats"]):
    xx, yy = x + 48 + (i%2)*190, y + 170 + (i//2)*70
    o += [f'<rect x="{xx}" y="{yy-26}" width="170" height="40" rx="20" fill="none" stroke="#0B0B0F" stroke-width="1.5"/>',
          f'<text class="lb" x="{xx+85}" y="{yy}" text-anchor="middle">{t}</text>']
o.append(f'<text class="lg" x="{x+40}" y="{y+316}">Les actions qui peuvent générer des clients</text>')

# 5 search-console.csv : tableau sans chiffres
x, y = cols[3], ry[1]
o += card(x, y, 5, "search-console.csv", "Les données réelles de Google")
heads = ["Pages", "Clics", "Impr.", "Position"]
xs = [x+40, x+190, x+275, x+360]
o += [f'<text class="lb" x="{xx}" y="{y+150}">{t}</text>' for xx, t in zip(xs, heads)]
o.append(f'<line x1="{x+40}" y1="{y+166}" x2="{x+420}" y2="{y+166}" stroke="#0B0B0F" stroke-width="1.2"/>')
for r in range(4):
    yy = y + 190 + r*38
    o.append(f'<rect x="{xs[0]}" y="{yy}" width="{110 - r*12}" height="10" rx="5" fill="#E6E6E6"/>')
    for xx in xs[1:]:
        o.append(f'<rect x="{xx}" y="{yy}" width="44" height="10" rx="5" fill="#E6E6E6"/>')

# 6 methodes.md : liste avec icônes
x, y = cols[3], ry[2]
o += card(x, y, 6, "methodes.md", "Tes méthodes SEO")
for i, (t, ic) in enumerate([("Recherche de mots-clés", i_box), ("Stratégie", i_link), ("Audit", i_file), ("Contenu", i_news)]):
    yy = y + 150 + i*50
    o += [ic(x+40, yy-17), f'<text class="li" x="{x+84}" y="{yy}">{t}</text>']

# 7 wiki.md : trois couches empilées
x, y = cols[2], ry[2]
o += card(x, y, 7, "wiki.md", "La base de connaissances")
for i, t in enumerate(["Méthodes", "Observations", "Enseignements des missions"]):
    yy = y + 130 + i*62
    o += [f'<rect x="{x+40+i*14}" y="{yy}" width="{364-i*28}" height="46" rx="6" fill="{"#F5F5F5" if i%2==0 else "#FFF"}" stroke="#0B0B0F" stroke-opacity=".3"/>',
          f'<text class="li" x="{x+68+i*14}" y="{yy+29}">{t}</text>']

# 8 workflow.md : étapes sur une ligne
x, y = cols[1], ry[2]
o += card(x, y, 8, "workflow.md", "Les étapes, dans l'ordre")
steps = ["Comprendre l'offre", "Mots-clés", "Intentions", "Préparer les pages", "Mesurer"]
o.append(f'<line x1="{x+62}" y1="{y+140}" x2="{x+62}" y2="{y+316}" stroke="#0B0B0F" stroke-opacity=".3" stroke-width="1.4"/>')
for i, t in enumerate(steps):
    yy = y + 140 + i*44
    o += [f'<circle cx="{x+62}" cy="{yy}" r="14" fill="#F5F5F5" stroke="#0B0B0F" stroke-opacity=".3"/><text class="lg" x="{x+62}" y="{yy+5}" text-anchor="middle" style="fill:#0B0B0F;font-weight:500">{i+1}</text>',
          f'<text class="li" x="{x+92}" y="{yy+6}">{t}</text>']

# 9 SKILL.md : arborescence
x, y = cols[0], ry[2]
o += card(x, y, 9, "SKILL.md", "Une tâche précise, réutilisable")
tree = [(".claude/", 0), ("skills/", 1), ("audit-seo/", 2), ("SKILL.md", 3)]
for i, (t, d) in enumerate(tree):
    yy = y + 160 + i*44
    xx = x + 48 + d*36
    if d:
        o.append(f'<path d="M{xx-24} {yy-30} V{yy-6} H{xx-6}" fill="none" stroke="#0B0B0F" stroke-opacity=".4" stroke-width="1.3"/>')
    style = ' style="font-weight:700"' if d == 3 else ''
    o.append(f'<text class="mono" x="{xx}" y="{yy}"{style}>{t}</text>')
o.append(f'<text class="lg" x="{x+40}" y="{y+330}">Un fichier par skill</text>')

# 10 suivi.md : action -> correction -> résultat
x, y = cols[0], ry[1]
o += card(x, y, 10, "suivi.md", "La trace du travail")
for i, t in enumerate(["Actions proposées", "Corrections validées", "Résultats obtenus"]):
    yy = y + 160 + i*64
    o += [f'<text class="li" x="{x+40}" y="{yy}" style="font-weight:{700 if i==2 else 400}">{t}</text>']
    if i < 2:
        o.append(arrow(x+60, yy+12, x+60, yy+40))

# centre
cx0, cy0, cw, ch = 640, 480, 720, 240
o += [grain(f'<path d="{folder(cx0, cy0-28, cw, ch+28, tw=220, th=28, r=18)}"/>'),
      f'<text x="{cx0+48}" y="{cy0+92}" style="font-size:42px;font-weight:700;fill:#FFF;letter-spacing:-1.2px">Ton système SEO</text>',
      f'<text x="{cx0+48}" y="{cy0+130}" style="font-size:21px;fill:#FFF">avec Claude Code, en 10 fichiers</text>',
      f'<text x="{cx0+48}" y="{cy0+186}" style="font-size:18px;fill:#FFF;opacity:.85">Tu ne redonnes plus tes méthodes à chaque conversation.</text>',
      f'<text x="{cx0+48}" y="{cy0+212}" style="font-size:18px;fill:#FFF;opacity:.85">Claude les retrouve et les applique.</text>']
NC = 5

def wire(pts):
    x, y = pts[0]
    d = "M" + " L".join(f"{a} {b}" for a, b in pts)
    return (f'<path d="{d}" fill="none" stroke="#2341e0" stroke-width="1.5"/>'
            f'<rect x="{x-3}" y="{y-3}" width="6" height="6" fill="#2341e0"/>')

WIRES = [[(260, 390), (260, 405), (700, 405), (700, 490)],
         [(753, 390), (753, 490)], [(1246, 390), (1246, 490)],
         [(1739, 390), (1739, 405), (1300, 405), (1300, 490)],
         [(1509, 600), (1340, 600)],
         [(1739, 834), (1739, 795), (1300, 795), (1300, 700)],
         [(1246, 834), (1246, 700)], [(753, 834), (753, 700)],
         [(260, 834), (260, 795), (700, 795), (700, 700)],
         [(490, 600), (660, 600)]]
body = o[:-NC] + [wire(w) for w in WIRES] + o[-NC:]
svg = head2 + CSS2 + DEEP + '</defs>\n<rect width="100%" height="100%" fill="#FFF"/>\n' + "\n".join(body) + "\n</svg>"
open("systeme-seo-10-fichiers-hub.svg", "w").write(svg)
