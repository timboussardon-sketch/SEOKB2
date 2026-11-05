"""Les 10 fichiers d'un système SEO avec Claude Code, en cascade de dossiers décalés (demande de Tim du 2026-10-28).
Textes : post LinkedIn de Tim du 2026-10-28, rien d'autre."""
import contextlib, io
with contextlib.redirect_stdout(io.StringIO()):
    from build_hubspot_hub import head, CSS, DEEP, grain
from build_10_fichiers_hub import folder

W, H = 1600, 2060
head2 = head.replace('width="1800" height="1200" viewBox="0 0 1800 1200"', f'width="{W}" height="{H}" viewBox="0 0 {W} {H}"')
CSS2 = CSS.replace('</style>', '.d{font-size:20px;fill:#333}\n.code{font-size:18px;fill:#0B0B0F;font-family:"SF Mono",Menlo,monospace}\n</style>')

FILES = [
    ("CLAUDE.md", ["Le premier fichier que Claude Code consulte. Il lui indique", "où trouver tes règles, tes méthodes et tes instructions."]),
    ("AGENTS.md", ["Les règles communes : utiliser les données, vérifier les informations,", "présenter les résultats, valider avant de modifier un site."]),
    ("client.md", ["Ce que ton client vend, à qui, sur quel marché", "et ce qui le différencie."]),
    ("conversions.md", ["Les objectifs commerciaux du site : devis, appels,", "inscriptions, achats."]),
    ("search-console.csv", ["Les données réelles de Google : clics, impressions, positions,", "pages qui ont un potentiel d'amélioration."]),
    ("methodes.md", ["Comment tu recherches les mots-clés, construis une stratégie,", "réalises un audit ou prépares un contenu."]),
    ("wiki.md", ["Tes méthodes, tes observations et les enseignements", "de tes précédentes missions."]),
    ("workflow.md", ["Les étapes dans l'ordre : comprendre l'offre, mots-clés,", "intentions, pages, mesure des résultats."]),
    ("SKILL.md", ["Une tâche précise, réutilisable. Un fichier par skill :", "@.claude/skills/audit-seo/SKILL.md"]),
    ("suivi.md", ["Les actions proposées, les corrections validées", "et les résultats obtenus."]),
]

FW, FH, STEP, DX = 1040, 236, 168, 44
X0, Y0 = 60, 300
o = []
# dossier du fond, outremer grainé
bx, by, bw, bh = 40, 40, 1160, 330
o += [grain(f'<path d="{folder(bx, by, bw, bh, tw=230, th=30, r=18)}"/>'),
      f'<text x="{bx+56}" y="{by+118}" style="font-size:56px;font-weight:700;fill:#FFF;letter-spacing:-1.8px">Ton système SEO</text>',
      f'<text x="{bx+56}" y="{by+162}" style="font-size:24px;fill:#FFF">avec Claude Code, en 10 fichiers</text>',
      f'<text x="{bx+56}" y="{by+212}" style="font-size:20px;fill:#FFF;opacity:.85">Tu ne redonnes plus tes méthodes à chaque conversation. Claude les retrouve.</text>']

for i, (name, lines) in enumerate(FILES):
    x, y = X0 + i*DX, Y0 + i*STEP
    h = FH if i < 9 else 200
    o += [f'<path d="{folder(x, y, FW, h)}" fill="#FFF" stroke="#0B0B0F" stroke-opacity=".4" stroke-width="1.5"/>',
          f'<text x="{x+24}" y="{y+18}" style="font-size:14px;font-weight:700;fill:#0B0B0F;letter-spacing:.5px">{i+1:02d}</text>',
          f'<text class="ct" x="{x+40}" y="{y+70}">{name}</text>']
    for j, t in enumerate(lines):
        cls = "d"
        if t.startswith("@"):
            t, cls = t[1:], "code"
        o.append(f'<text class="{cls}" x="{x+40}" y="{y+108+j*28}">{t}</text>')

svg = head2 + CSS2 + DEEP + '</defs>\n<rect width="100%" height="100%" fill="#FFF"/>\n' + "\n".join(o) + "\n</svg>"
open("systeme-seo-10-fichiers-cascade.svg", "w").write(svg)
