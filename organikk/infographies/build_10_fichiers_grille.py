"""Les 10 fichiers d'un système SEO avec Claude Code : grille 2 × 5 de dossiers identiques, 1080 × 1350.
Brief de Tim du 2026-10-28 (refonte de la cascade). Textes : post LinkedIn de Tim du 2026-10-28."""
import contextlib, io
with contextlib.redirect_stdout(io.StringIO()):
    from build_hubspot_hub import DEEP, grain
    from build_10_fichiers_hub import folder

W, H = 1080, 1350
M, GX, GY = 48, 24, 20
CW = (W - 2*M - GX) // 2          # 480
BY, BH = 40, 214                   # bandeau
GY0 = BY + BH + 30                 # début de la grille
CH = (H - M - GY0 - 4*GY) // 5     # hauteur d'un dossier

FILES = [
    ("CLAUDE.md", "Le premier fichier que Claude lit.", "Où trouver règles, méthodes, instructions."),
    ("AGENTS.md", "Les règles communes : données, vérification,", "résultats, validation avant de modifier."),
    ("client.md", "Ce que ton client vend, à qui, sur quel", "marché, et ce qui le différencie."),
    ("conversions.md", "Les objectifs du site : devis, appels,", "inscriptions, achats."),
    ("search-console.csv", "Les données réelles : clics, impressions,", "positions, pages à potentiel."),
    ("methodes.md", "Comment tu fais tes mots-clés, ta stratégie,", "tes audits et tes contenus."),
    ("wiki.md", "Tes méthodes, tes observations et les", "enseignements de tes missions."),
    ("workflow.md", "Les étapes dans l'ordre : offre, mots-clés,", "intentions, pages, mesure."),
    ("SKILL.md", "Une tâche précise, réutilisable.", "@.claude/skills/audit-seo/SKILL.md"),
    ("suivi.md", "Actions proposées, corrections validées,", "résultats obtenus."),
]

o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
     '<defs><style>',
     "@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&amp;display=swap');",
     'text{font-family:Inter,sans-serif}',
     '.num{font-size:15px;font-weight:700;fill:#0B0B0F;letter-spacing:.6px}',
     '.nm{font-size:29px;font-weight:700;fill:#0B0B0F;letter-spacing:-.7px}',
     '.d{font-size:19px;fill:#333}',
     '.code{font-size:17px;fill:#0B0B0F;font-family:"SF Mono",Menlo,monospace}',
     '</style>', DEEP, '</defs>', f'<rect width="{W}" height="{H}" fill="#FFF"/>']

# bandeau
o += [grain(f'<path d="{folder(M, BY, W-2*M, BH, tw=200, th=26, r=12)}"/>'),
      f'<text x="{M+40}" y="{BY+100}" style="font-size:52px;font-weight:700;fill:#FFF;letter-spacing:-1.6px">Ton système SEO</text>',
      f'<text x="{M+40}" y="{BY+140}" style="font-size:24px;fill:#FFF">avec Claude Code, en 10 fichiers</text>',
      f'<text x="{M+40}" y="{BY+184}" style="font-size:19px;fill:#FFF;opacity:.88">Tu ne redonnes plus tes méthodes à chaque conversation. Claude les retrouve.</text>']

for i, (name, l1, l2) in enumerate(FILES):
    x = M + (i % 2) * (CW + GX)
    y = GY0 + (i // 2) * (CH + GY)
    o += [f'<path d="{folder(x, y, CW, CH, tw=112, th=22, r=8)}" fill="#FFF" stroke="#0B0B0F" stroke-opacity=".38" stroke-width="1.5"/>',
          f'<text class="num" x="{x+22}" y="{y+16}">{i+1:02d}</text>',
          f'<text class="nm" x="{x+28}" y="{y+68}">{name}</text>',
          f'<text class="d" x="{x+28}" y="{y+106}">{l1}</text>']
    if l2.startswith("@"):
        o.append(f'<text class="code" x="{x+28}" y="{y+134}">{l2[1:]}</text>')
    else:
        o.append(f'<text class="d" x="{x+28}" y="{y+134}">{l2}</text>')

o.append('</svg>')
open("systeme-seo-10-fichiers-grille.svg", "w").write("\n".join(o))
print("CH =", CH, "| bas grille =", GY0 + 5*CH + 4*GY)
