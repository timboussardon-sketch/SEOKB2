"""Le vrai système seo-kb en schéma ORGANIKK (skill infographie-schema, modèle hub à cases).
Version du 2026-11-04, refaite après la remarque de Tim : la première version reprenait les libellés génériques d'une image
générée (Backlinks, Suivi de positions...) qui ne sont pas dans le système.

Matière, une source par case :
- raw/ et wiki/ : fichiers comptés sur disque le 2026-11-04 (find raw -type f ; find wiki -name '*.md'). AGENTS.md §3 : raw/ immuable, wiki/ écrit par l'agent.
- Skills : 119 dossiers avec SKILL.md dans ~/.claude/skills (2026-11-04) ; dossiers de sortie : AGENTS.md §7.
- Agents : ~/.claude/agents (5 fichiers) ; ordre : descriptions de audit-collecte, audit-redaction, verificateur-livrable, agent-contradicteur-seo.
- Boucles : AGENTS.md §14. Automatisations : 14 lignes de wiki/ops/sante-automatisations (relevé 2026-11-01), cadences AGENTS.md §7bis.
La tête de Tim reste un screen : crop de l'image d'origine (obsidian-systeme-seo-tete.png, 288 x 452)."""

W, H = 1672, 941

HEAD = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&amp;display=swap');
text{{font-family:Inter,sans-serif}}
.ct{{font-size:26px;font-weight:700;fill:#0B0B0F;letter-spacing:-0.8px}}
.cs{{font-size:16px;fill:#333}}
.li{{font-size:18px;fill:#0B0B0F}}
.nb{{font-size:18px;font-weight:700;fill:#0B0B0F}}
.lg{{font-size:16px;fill:#777}}
.an{{font-size:13px;font-weight:500;fill:#777}}
.ic{{fill:none;stroke:#0B0B0F;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}}
</style>
<radialGradient id="dg" cx=".32" cy=".38" r=".78"><stop offset="0" stop-color="#3a5cff"/><stop offset=".35" stop-color="#2341e0"/><stop offset=".7" stop-color="#12249a"/><stop offset="1" stop-color="#070f4d"/></radialGradient>
<filter id="dn" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB"><feTurbulence type="fractalNoise" baseFrequency=".95" numOctaves="2" stitchTiles="stitch" result="t"/><feColorMatrix in="t" type="matrix" values="1 0 0 0 0  1 0 0 0 0  1 0 0 0 0  0 0 0 0 1" result="m"/><feComposite in="SourceGraphic" in2="m" operator="arithmetic" k1="0" k2="1" k3=".62" k4="-.31" result="g"/><feComposite in="g" in2="SourceGraphic" operator="in"/></filter>
<clipPath id="face"><rect x="1320" y="220" width="316" height="496" rx="16"/></clipPath>
</defs>
'''

CW, CH = 376, 260
COL = [40, 468, 896]
ROW = [40, 340, 640]
PAD = 30
R = CW - PAD            # bord droit utile d'une case, en coordonnée relative


def wire(pts):
    x, y = pts[0]
    d = "M" + " L".join(f"{a} {b}" for a, b in pts)
    return (f'<path d="{d}" fill="none" stroke="#2341e0" stroke-width="1.5"/>'
            f'<rect x="{x-3}" y="{y-3}" width="6" height="6" fill="#2341e0"/>')


def head(cx, cy, title, sub):
    x, y = COL[cx], ROW[cy]
    return x, y, [
        f'<rect x="{x}" y="{y}" width="{CW}" height="{CH}" rx="12" fill="#FFF" stroke="#0B0B0F" stroke-opacity=".35" stroke-width="1.5"/>',
        f'<text class="ct" x="{x+PAD}" y="{y+52}">{title}</text>',
        f'<text class="cs" x="{x+PAD}" y="{y+80}">{sub}</text>',
        f'<line x1="{x+PAD}" y1="{y+100}" x2="{x+R}" y2="{y+100}" stroke="#0B0B0F" stroke-opacity=".12"/>']


def rowy(y, i):
    return y + 132 + i * 34


def sep(x, y, i, x0=PAD):
    return f'<line x1="{x+x0}" y1="{rowy(y,i)+12}" x2="{x+R}" y2="{rowy(y,i)+12}" stroke="#0B0B0F" stroke-opacity=".12"/>'


# ---- raw/ : liste, chiffre à droite
def c_raw(cx, cy):
    x, y, o = head(cx, cy, "raw/", "Sources brutes, jamais modifiées")
    for i, (n, v) in enumerate([("raw/data", "1 732"), ("raw/notes", "625"), ("raw/articles", "68"), ("raw/transcripts", "35")]):
        yy = rowy(y, i)
        o += [f'<text class="li" x="{x+PAD}" y="{yy}">{n}</text>', f'<text class="nb" x="{x+R}" y="{yy}" text-anchor="end">{v}</text>']
        if i < 3:
            o.append(sep(x, y, i))
    return o


# ---- wiki/ : barres proportionnelles aux pages comptées
def c_wiki(cx, cy):
    x, y, o = head(cx, cy, "wiki/", "1 108 pages, écrites par Claude")
    data = [("sources", 186), ("keywords", 168), ("audit", 124), ("entities", 82)]
    for i, (n, v) in enumerate(data):
        yy = rowy(y, i)
        bw = round(v / 186 * 150)
        o += [f'<text class="li" x="{x+PAD}" y="{yy}">{n}</text>',
              f'<rect x="{x+140}" y="{yy-12}" width="{bw}" height="12" rx="6" fill="#0B0B0F"/>',
              f'<text class="nb" x="{x+R}" y="{yy}" text-anchor="end">{v}</text>']
    return o


# ---- skills : nom -> dossier de sortie dans wiki/
def c_skills(cx, cy):
    x, y, o = head(cx, cy, "Skills", "119 installés. Sorties SEO : wiki/")
    for i, (n, d) in enumerate([("strategie-geo", "strategie-geo/"), ("seo-brief-contenu", "briefs/"),
                                ("seo-cluster-aeo", "clusters/"), ("seo-quick-win", "quick-wins/")]):
        yy = rowy(y, i)
        o += [f'<text class="li" x="{x+PAD}" y="{yy}">{n}</text>',
              f'<path class="ic" d="M{x+200} {yy-6} h20 M{x+214} {yy-12} l6 6 -6 6"/>',
              f'<text class="lg" x="{x+232}" y="{yy}" style="font-size:16px">{d}</text>']
    return o


# ---- agents : chaîne numérotée
def c_agents(cx, cy):
    x, y, o = head(cx, cy, "Agents", "Dans cet ordre, puis Tim valide")
    names = ["audit-collecte", "audit-redaction", "verificateur-livrable", "agent-contradicteur-seo"]
    o.append(f'<line x1="{x+PAD+13}" y1="{rowy(y,0)-6}" x2="{x+PAD+13}" y2="{rowy(y,3)-6}" stroke="#0B0B0F" stroke-opacity=".3" stroke-width="1.4"/>')
    for i, n in enumerate(names):
        yy = rowy(y, i)
        o += [f'<circle cx="{x+PAD+13}" cy="{yy-6}" r="13" fill="#F5F5F5" stroke="#0B0B0F" stroke-opacity=".3"/>',
              f'<text class="lg" x="{x+PAD+13}" y="{yy-1}" text-anchor="middle" style="fill:#0B0B0F;font-weight:500;font-size:15px">{i+1}</text>',
              f'<text class="li" x="{x+PAD+44}" y="{yy}">{n}</text>']
    return o


# ---- boucles : icône de boucle + sens
def loop_icon(x, y):
    return (f'<g transform="translate({x} {y}) scale(.85)"><path class="ic" d="M17 2l4 4-4 4 M3 11v-1a4 4 0 0 1 4-4h14 M7 22l-4-4 4-4 M21 13v1a4 4 0 0 1-4 4H3"/></g>')


def c_boucles(cx, cy):
    x, y, o = head(cx, cy, "Boucles", "4 boucles, revue hebdo le vendredi")
    for i, n in enumerate(["capture → traitement", "doctrine → validation", "sortie → apprentissage", "correction → durcissement"]):
        yy = rowy(y, i)
        o += [loop_icon(x + PAD, yy - 17), f'<text class="li" x="{x+PAD+40}" y="{yy}">{n}</text>']
    return o


# ---- automatisations : libellé, cadence
def c_auto(cx, cy):
    x, y, o = head(cx, cy, "Automatisations", "14 surveillées")
    for i, (n, c) in enumerate([("Revue de presse", "chaque jour"), ("Backlog d'ingest", "lundi"),
                                ("Résurgence", "mercredi"), ("Revue hebdo", "vendredi")]):
        yy = rowy(y, i)
        o += [f'<text class="li" x="{x+PAD}" y="{yy}">{n}</text>', f'<text class="lg" x="{x+R}" y="{yy}" text-anchor="end" style="font-size:17px">{c}</text>']
        if i < 3:
            o.append(sep(x, y, i))
    return o


body = []
body += c_raw(0, 0) + c_wiki(0, 1) + c_skills(0, 2)
body += c_agents(2, 0) + c_boucles(2, 1) + c_auto(2, 2)

# connecteurs : trait outremer 1,5 px, angles droits, carré de 6 px côté case, ils passent sous la carte centrale
WIRES = [[(416, 170), (442, 170), (442, 410), (468, 410)], [(416, 470), (468, 470)], [(416, 770), (442, 770), (442, 530), (468, 530)],
         [(896, 170), (870, 170), (870, 410), (844, 410)], [(896, 470), (844, 470)], [(896, 770), (870, 770), (870, 530), (844, 530)]]
body += [wire(w) for w in WIRES]

# carte centrale, outremer profond grainé
cx0, cy0, cw, ch = 468, 365, 376, 210
body += [f'<g fill="url(#dg)" filter="url(#dn)"><rect x="{cx0}" y="{cy0}" width="{cw}" height="{ch}" rx="18"/></g>',
         f'<text x="{cx0+40}" y="{cy0+100}" style="font-size:42px;font-weight:700;fill:#FFF;letter-spacing:-1.2px">Obsidian</text>',
         f'<text x="{cx0+40}" y="{cy0+138}" style="font-size:21px;fill:#FFF">le vault seo-kb</text>']

# annotation de source (chiffres comptés)
body.append(f'<text class="an" x="40" y="926">Comptes au 4 novembre 2026 : fichiers de raw/, pages .md de wiki/, dossiers de ~/.claude/skills. Automatisations : wiki/ops/sante-automatisations, relevé du 1er novembre.</text>')

# la tête de Tim : screen d'origine, inchangé
body += ['<image x="1320" y="220" width="316" height="496" preserveAspectRatio="xMidYMid slice" clip-path="url(#face)" xlink:href="obsidian-systeme-seo-tete.png"/>',
         '<rect x="1320" y="220" width="316" height="496" rx="16" fill="none" stroke="#0B0B0F" stroke-opacity=".35" stroke-width="1.5"/>']

svg = HEAD + '<rect width="100%" height="100%" fill="#FFF"/>\n' + "\n".join(body) + "\n</svg>"
open("obsidian-systeme-seo-hub.svg", "w").write(svg)
