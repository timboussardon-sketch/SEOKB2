"""Structure d'un agent SEO en local : grille 2 × 4 de dossiers identiques, 1080 × 1350.
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
CH = (H - M - GY0 - 3*GY) // 4     # hauteur d'un dossier

FILES = [
    ("Claude Code", ["La version de Claude qui travaille", "dans ton terminal : lit, crée des", "fichiers, lance des commandes."]),
    ("Terminal", ["Une application de ton ordinateur", "qui permet d'exécuter des", "commandes."]),
    ("Obsidian", ["Une application gratuite pour", "consulter et organiser tes notes,", "pratique pour une base de connaissances."]),
    ("Vault", ["Un dossier contenant tes notes.", "Le nom d'un espace de travail", "Obsidian."]),
    ("Skill", ["Une tâche que tu transformes en", "instructions réutilisables", "par Claude."]),
    ("Workflow", ["Plusieurs tâches enchaînées", "dans un ordre précis."]),
    ("Routine", ["Une tâche qui se déclenche", "automatiquement, par exemple", "tous les lundis."]),
    ("Boucle", ["Un mécanisme qui récupère les résultats", "et les corrections pour améliorer", "ton système."]),
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
      f'<text x="{M+40}" y="{BY+100}" style="font-size:52px;font-weight:700;fill:#FFF;letter-spacing:-1.6px">Ton agent SEO en local</text>',
      f'<text x="{M+40}" y="{BY+140}" style="font-size:24px;fill:#FFF">8 notions à connaître pour le construire</text>',
      f'<text x="{M+40}" y="{BY+184}" style="font-size:19px;fill:#FFF;opacity:.88">Du terminal à la boucle : la structure, dans l’ordre.</text>']

for i, (name, lines) in enumerate(FILES):
    x = M + (i % 2) * (CW + GX)
    y = GY0 + (i // 2) * (CH + GY)
    o += [f'<path d="{folder(x, y, CW, CH, tw=112, th=22, r=8)}" fill="#FFF" stroke="#0B0B0F" stroke-opacity=".38" stroke-width="1.5"/>',
          f'<text class="num" x="{x+22}" y="{y+16}">{i+1:02d}</text>',
          f'<text class="nm" x="{x+28}" y="{y+72}">{name}</text>']
    for j, l in enumerate(lines):
        o.append(f'<text class="d" x="{x+28}" y="{y+116+j*30}">{l}</text>')

o.append('</svg>')
open("agent-seo-local-8-notions.svg", "w").write("\n".join(o))
print("CH =", CH, "| bas grille =", GY0 + 4*CH + 3*GY)
