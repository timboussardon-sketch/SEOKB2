"""5 skills SEO : bandeau outremer grainé + 5 dossiers identiques en pleine largeur, 1080 × 1350.
Même DA que systeme-seo-10-fichiers-grille (brief de Tim du 2026-10-28). Textes : liste donnée par Tim le 2026-10-28."""
import contextlib, io
with contextlib.redirect_stdout(io.StringIO()):
    from build_hubspot_hub import DEEP, grain
    from build_10_fichiers_hub import folder

W, H = 1080, 1350
M, GY = 48, 22
CW = W - 2*M
BY, BH = 40, 168
GY0 = BY + BH + 32
CH = (H - M - GY0 - 4*GY) // 5

AGENTS = [
    ("Skill GEO", "Analyser une page pour identifier les améliorations", "possibles pour les moteurs génératifs."),
    ("Skill recherche de mots-clés", "Explorer une thématique et identifier les recherches", "pertinentes pour une offre."),
    ("Skill mots-clés décisionnels", "Repérer les requêtes qui présentent le meilleur", "potentiel de conversion."),
    ("Skill brief", "Préparer une structure éditoriale à partir des mots-clés", "et des intentions de recherche."),
    ("Skill FAQ", "Identifier les questions importantes auxquelles", "une page doit répondre."),
]

o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
     '<defs><style>',
     "@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&amp;display=swap');",
     'text{font-family:Inter,sans-serif}',
     '.num{font-size:16px;font-weight:700;fill:#0B0B0F;letter-spacing:.6px}',
     '.nm{font-size:34px;font-weight:700;fill:#0B0B0F;letter-spacing:-.9px}',
     '.d{font-size:24px;fill:#333}',
     '</style>', DEEP, '</defs>', f'<rect width="{W}" height="{H}" fill="#FFF"/>']

o += [grain(f'<path d="{folder(M, BY, CW, BH, tw=200, th=26, r=12)}"/>'),
      f'<text x="{M+40}" y="{BY+108}" style="font-size:60px;font-weight:700;fill:#FFF;letter-spacing:-1.8px">5 skills SEO</text>']

for i, (name, l1, l2) in enumerate(AGENTS):
    x, y = M, GY0 + i*(CH + GY)
    o += [f'<path d="{folder(x, y, CW, CH, tw=120, th=24, r=8)}" fill="#FFF" stroke="#0B0B0F" stroke-opacity=".38" stroke-width="1.5"/>',
          f'<text class="num" x="{x+24}" y="{y+18}">{i+1:02d}</text>',
          f'<text class="nm" x="{x+32}" y="{y+80}">{name}</text>',
          f'<text class="d" x="{x+32}" y="{y+124}">{l1}</text>',
          f'<text class="d" x="{x+32}" y="{y+156}">{l2}</text>']

o.append('</svg>')
open("5-skills-seo.svg", "w").write("\n".join(o))
print("CH =", CH)
