"""Structure pour faire travailler 5 agents SEO ensemble, 1080 × 1350.
Brief de Tim du 2026-10-29 (« design un peu différent des autres fois ») : ni dossiers ni hub.
Une seule colonne vertébrale, de l'orchestrateur à la validation humaine : les 5 agents, le
rapport final, le vérificateur. Les agents déposent leurs rapports dans le coffre à droite,
le coffre alimente le rapport final. La validation humaine est hors du cadre Claude Code.
Itération 2 (29/10) : sous-titre retiré, tailles relevées, tout sur la même colonne.
Textes : post de Tim du 2026-10-29."""
import contextlib, io
with contextlib.redirect_stdout(io.StringIO()):
    from build_hubspot_hub import DEEP, grain

W, H = 1080, 1350
BLUE = "#2341e0"
FX, FY, FW, FB = 48, 150, 984, 1150      # cadre Claude Code : x, y, largeur, bas
SX, TX = 112, 150                         # colonne du workflow, colonne du texte
AGENTS = [("Indexation", "indexation"), ("Core Web Vitals", "core-web-vitals"),
          ("Quick wins", "quick-wins"), ("Cannibalisation", "cannibalisation"),
          ("Maillage interne", "maillage")]
AY = [512, 598, 684, 770, 856]
VX, VW = 656, 344                         # coffre

o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
     '<defs><style>',
     "@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&amp;display=swap');",
     'text{font-family:Inter,sans-serif}',
     '.h{font-size:26px;font-weight:700;fill:#0B0B0F;letter-spacing:-.7px}',
     '.r{font-size:22px;font-weight:700;fill:#0B0B0F;letter-spacing:-.5px}',
     '.d{font-size:19px;fill:#333}',
     '.a{font-size:17px;font-weight:500;fill:#777}',
     '.m{font-size:16px;fill:#777;font-family:"SF Mono",Menlo,monospace}',
     '.mb{font-size:16px;fill:#0B0B0F;font-family:"SF Mono",Menlo,monospace}',
     '</style>', DEEP, '</defs>', f'<rect width="{W}" height="{H}" fill="#FFF"/>']

def wire(d, x, y):
    """Trait outremer 1,5 px, petit carré de 6 px contre la cible."""
    return [f'<path d="{d}" fill="none" stroke="{BLUE}" stroke-width="1.5"/>',
            f'<rect x="{x-3}" y="{y-3}" width="6" height="6" fill="{BLUE}"/>']

o.append(f'<text x="{FX}" y="100" style="font-size:48px;font-weight:700;fill:#0B0B0F;letter-spacing:-1.5px">5 agents SEO qui travaillent ensemble</text>')

# cadre Claude Code, deux lignes d'en-tête alignées
o += [f'<rect x="{FX}" y="{FY}" width="{FW}" height="{FB-FY}" rx="6" fill="none" stroke="#0B0B0F" stroke-width="1.5"/>']
for i, (label, desc) in enumerate([("Claude Code", "l’environnement : lit tes fichiers, lance les analyses"),
                                   ("CLAUDE.md", "les règles communes : dossiers clients, consignes, validations")]):
    y = FY + 46 + i * 68
    o += [f'<text class="r" x="{FX+32}" y="{y}">{label}</text>',
          f'<text class="d" x="{FX+212}" y="{y}">{desc}</text>',
          f'<line x1="{FX}" y1="{y+24}" x2="{FX+FW}" y2="{y+24}" stroke="#0B0B0F" stroke-opacity=".15"/>']

# orchestrateur : seul point focal grainé
OY, OH = 318, 108
o += [grain(f'<rect x="76" y="{OY}" width="452" height="{OH}" rx="14"/>'),
      f'<text x="108" y="{OY+48}" style="font-size:30px;font-weight:700;fill:#FFF;letter-spacing:-.8px">Orchestrateur</text>',
      f'<text x="108" y="{OY+80}" style="font-size:19px;fill:#FFF">lit le workflow, lance les agents</text>']

# colonne du workflow : de l'orchestrateur à la validation humaine, à travers le cadre
HY = 1236
o += [f'<line x1="{SX}" y1="{OY+OH}" x2="{SX}" y2="{HY-24}" stroke="#0B0B0F" stroke-width="1.5"/>',
      f'<text class="a" x="{TX}" y="{OY+OH+38}">le workflow : un agent après l’autre</text>']

# coffre Obsidian
VB = 920
o += [f'<rect x="{VX}" y="{OY}" width="{VW}" height="{VB-OY}" rx="10" fill="#F5F5F5"/>',
      f'<text class="h" x="{VX+24}" y="{OY+44}">Coffre Obsidian</text>',
      f'<text class="d" x="{VX+24}" y="{OY+74}">la mémoire : chaque agent y écrit,</text>',
      f'<text class="d" x="{VX+24}" y="{OY+100}">le suivant y relit</text>']

for i, ((name, slug), y) in enumerate(zip(AGENTS, AY)):
    o += [f'<circle cx="{SX}" cy="{y}" r="18" fill="#0B0B0F"/>',
          f'<text x="{SX}" y="{y+6}" text-anchor="middle" style="font-size:16px;font-weight:700;fill:#FFF">{i+1}</text>',
          f'<text class="h" x="{TX}" y="{y+2}">{name}</text>',
          f'<text class="m" x="{TX}" y="{y+30}">skills/{slug}/SKILL.md</text>',
          f'<rect x="{VX+18}" y="{y-14}" width="{VW-36}" height="40" rx="6" fill="#FFF" stroke="#0B0B0F" stroke-opacity=".35" stroke-width="1.2"/>',
          f'<text class="mb" x="{VX+36}" y="{y+12}">rapports/{slug}.md</text>']
    o += wire(f"M476 {y+6} L{VX+18} {y+6}", VX + 18, y + 6)

# rapport final : nourri par le coffre
RY = 990
o += [f'<rect x="{SX-11}" y="{RY-11}" width="22" height="22" fill="#0B0B0F"/>',
      f'<text class="h" x="{TX}" y="{RY+2}">Rapport final</text>',
      f'<text class="d" x="{TX}" y="{RY+32}">problèmes, opportunités, actions proposées</text>']
o += wire(f"M{VX+VW//2} {VB} L{VX+VW//2} {RY-6} L{TX+190} {RY-6}", TX + 190, RY - 6)

# vérificateur
CY = 1084
o += [f'<circle cx="{SX}" cy="{CY}" r="18" fill="#FFF" stroke="#0B0B0F" stroke-width="1.5"/>',
      f'<path d="M{SX-7} {CY} l5 5 l9 -10" fill="none" stroke="#0B0B0F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
      f'<text class="h" x="{TX}" y="{CY+2}">Vérificateur</text>',
      f'<text class="d" x="{TX}" y="{CY+32}">méthodes respectées, chiffres sourcés, résultats cohérents</text>']

# validation humaine : hors du cadre, les agents ne touchent pas au site
o += [f'<circle cx="{SX}" cy="{HY}" r="24" fill="#FFF" stroke="#0B0B0F" stroke-width="1.5"/>',
      f'<circle cx="{SX}" cy="{HY-5}" r="6.5" fill="none" stroke="#0B0B0F" stroke-width="1.5"/>',
      f'<path d="M{SX-11} {HY+13} q11 -15 22 0" fill="none" stroke="#0B0B0F" stroke-width="1.5" stroke-linecap="round"/>',
      f'<text class="h" x="{TX+8}" y="{HY+2}">Validation humaine</text>',
      f'<text class="d" x="{TX+8}" y="{HY+32}">Les agents préparent les décisions. Tu valides avant</text>',
      f'<text class="d" x="{TX+8}" y="{HY+58}">toute modification du site.</text>']

o.append('</svg>')
open("5-agents-seo-structure.svg", "w").write("\n".join(o))
