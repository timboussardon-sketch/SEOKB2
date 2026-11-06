# -*- coding: utf-8 -*-
"""Top 20 des mots-clés business d'un audit : génère top20.html (tableau de l'onglet 7) et top20_rows.json (lu par cartes.graf_volumes).

Usage : python3 top20.py <dossier-audit> <site>

Le dossier <dossier-audit>/<site>/ contient :
- planner.json : export Google Keyword Planner, {"exacts": {mot-clé: {...}}, "idees": {mot-clé: {...}}},
  chaque entrée avec volume, cpc_low, cpc_high, competition ;
- top20_site.py : TOP = [ (mot-clé, variantes, déjà sur le site ?, P, I, F, clic IA, décision), ... ]
                  ECARTES = [ (recherche, volume, pourquoi), ... ]
  P, I, F de 1 à 5 : proximité business, intention, faisabilité, posées en lisant la SERP et le site
  (chaîne seo-recherche-mots-cles → seo-clustering-mots-cles → seo-mots-cles-resistants-ia → seo-mots-cles-decisionnels → seo-modeles-pseo).
  Clic IA : « forte », « moyenne » ou « faible ».

Note /10 = P × I × F ÷ 12,5, arrondie (5 × 5 × 5 = 10). Le volume n'entre pas dans la note. Outil de tri, pas une mesure.
"""
import json, pathlib, sys, importlib.util

def fmt_vol(v): return "non mesuré" if v is None else ("0 mesuré" if not v else f"{v:,}".replace(",", " "))
def fmt_cpc(m): return "n.d." if not m or m.get("cpc_low") is None else f"{m['cpc_low']:.2f}–{m['cpc_high']:.2f} €".replace(".", ",")
def note(p, i, f): return round(p * i * f / 12.5)

def charger(dossier):
    spec = importlib.util.spec_from_file_location("top20_site", dossier / "top20_site.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m.TOP, getattr(m, "ECARTES", [])

def build(dossier, date_releve=""):
    TOP, ECARTES = charger(dossier)
    d = json.load(open(dossier / "planner.json", encoding="utf-8")); ex = d.get("exacts", {}); idees = d.get("idees", {})
    def m(k):
        return ex.get(k) or idees.get(k) or next((v for kk, v in idees.items() if kk.lower() == k.lower()), None)
    rows = []
    for kw, var, deja, p, i, f, ia, dec in TOP:
        mm = m(kw) or {}
        rows.append(dict(kw=kw, var=var, deja=deja, vol=mm.get("volume"), cpc=fmt_cpc(mm), conc=(mm.get("competition") or "n.d."), n=note(p, i, f), ia=ia, dec=dec))
    rows.sort(key=lambda r: (-r["n"], -(r["vol"] or 0)))
    rows = rows[:20]
    releve = f", relevés le {date_releve}" if date_releve else ""
    h = ['<h3>Top 20 des mots-clés business, scoring et priorité</h3>',
         f'<p>Les volumes, les coûts par clic et la concurrence viennent de Google Keyword Planner{releve}.</p>',
         '<p><b>La note sur 10 sert à trier, ce n\'est pas une mesure.</b> Elle multiplie trois notes de 1 à 5, divisées par 12,5 : 5 × 5 × 5 donne 10.</p>',
         '<p>Les trois notes : la recherche correspond-elle à une offre que vous vendez, la personne cherche-t-elle un prestataire ou une définition, et quelle place les pages déjà affichées laissent à un site de votre taille.</p>',
         '<p>Le volume n\'entre pas dans la note. Quand une recherche compte pour une autre raison, c\'est la colonne Décision qui le dit.</p>',
         '<p><b>La colonne « clic après réponse IA » est une estimation, pas une mesure.</b></p>',
         '<p>Forte : on cherche un prestataire, un lieu ou un achat. Une réponse générée ne remplace pas ça. Moyenne : on cherche un guide ou une méthode, la réponse générée peut suffire. Faible : définition ou comparatif, absorbés par la réponse générée.</p>',
         '<div class="tablewrap"><table class="kwtab"><thead><tr><th class="num">Rang</th><th>Mot-clé</th><th>Déjà sur le site ?</th><th class="num">Vol./mois</th><th class="num">CPC</th><th>Concurrence Ads</th><th class="num">Note /10</th><th>Probabilité estimée de clic après réponse IA</th><th>Décision</th></tr></thead><tbody>']
    for r, row in enumerate(rows, 1):
        cls = ' class="biz"' if row["n"] >= 8 else ""
        var = f' <span class="tag">{row["var"]}</span>' if row["var"] else ""
        h.append(f'<tr{cls}><td class="num">{r}</td><td class="kw">{row["kw"]}{var}</td><td>{row["deja"]}</td><td class="num">{fmt_vol(row["vol"])}</td><td class="num">{row["cpc"]}</td><td>{row["conc"]}</td><td class="num">{row["n"]}</td><td>{row["ia"]}</td><td>{row["dec"]}</td></tr>')
    h.append('</tbody></table></div>')
    if ECARTES:
        h.append('<details class="repli"><summary>Les recherches à fort volume non retenues, et pourquoi</summary><div class="tablewrap"><table><thead><tr><th>Recherche</th><th class="num">Vol./mois</th><th>Pourquoi</th></tr></thead><tbody>')
        for kw, vol, why in ECARTES:
            h.append(f'<tr><td>{kw}</td><td class="num">{vol}</td><td>{why}</td></tr>')
        h.append('</tbody></table></div></details>')
    return "\n".join(h), rows

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit("usage : python3 top20.py <dossier-audit> <site> [date du relevé Keyword Planner]")
    dossier = pathlib.Path(sys.argv[1]) / sys.argv[2]
    html, rows = build(dossier, sys.argv[3] if len(sys.argv) > 3 else "")
    (dossier / "top20.html").write_text(html, encoding="utf-8")
    json.dump(rows, open(dossier / "top20_rows.json", "w", encoding="utf-8"), ensure_ascii=False)
    print(sys.argv[2], [(r["kw"], r["vol"], r["n"]) for r in rows])
