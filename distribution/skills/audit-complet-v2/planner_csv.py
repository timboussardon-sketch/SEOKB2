# -*- coding: utf-8 -*-
"""Convertit les exports CSV de Google Keyword Planner en planner.json, le fichier que lit top20.py.

Usage :
    python3 planner_csv.py <dossier-audit>/<site> --idees idees1.csv [idees2.csv ...] [--exacts metriques.csv]

- --idees : les exports « Découvrir de nouveaux mots clés » (une ou deux passes d'idées).
- --exacts : l'export « Obtenir le volume de recherche et les prévisions » sur ta liste de mots-clés
  (métriques exactes). Facultatif : sans lui, top20.py lit les volumes dans les idées.

Les exports Keyword Planner sont en UTF-16 avec tabulations, ou en UTF-8 avec virgules, et commencent
par deux lignes de titre. Les deux formats, en français et en anglais, sont lus.

Écrit <dossier-audit>/<site>/planner.json :
    {"quand": ..., "sources": [...], "exacts": {mot-clé: {...}}, "idees": {mot-clé: {...}}}
chaque entrée avec volume, cpc_low, cpc_high, competition. Aucun chiffre n'est complété : une cellule
vide reste vide (None).
"""
import argparse, csv, io, json, pathlib, re, sys, time

COLONNES = {
    "kw": ["keyword", "mot clé", "mot-clé", "mots clés"],
    "volume": ["avg. monthly searches", "nombre moyen de recherches mensuelles", "recherches mensuelles moyennes"],
    "competition": ["competition", "concurrence"],
    "cpc_low": ["top of page bid (low range)", "enchère en haut de page (plage basse)", "enchère en haut de page (fourchette basse)"],
    "cpc_high": ["top of page bid (high range)", "enchère en haut de page (plage haute)", "enchère en haut de page (fourchette haute)"],
}

def lire_texte(chemin):
    brut = pathlib.Path(chemin).read_bytes()
    for enc in ("utf-16", "utf-8-sig", "latin-1"):
        try:
            texte = brut.decode(enc)
            if "\x00" not in texte:
                return texte
        except UnicodeDecodeError:
            continue
    sys.exit(f"{chemin} : encodage illisible")

def nombre(v, entier=False):
    v = (v or "").strip().replace(" ", "").replace("\xa0", "").replace(" ", "").replace("€", "").replace("$", "")
    if not v or v in ("-", "--"):
        return None
    if re.fullmatch(r"\d+[KkMm]?\s*[–-]\s*\d+[KkMm]?", v):
        return None  # fourchette arrondie (compte sans dépense) : pas un volume mesuré
    if entier:  # volume : toujours un entier, virgules et points ne sont que des séparateurs de milliers
        v = v.replace(",", "").replace(".", "")
    else:
        v = v.replace(",", ".") if v.count(",") == 1 and "." not in v else v.replace(",", "")
    try:
        return float(v)
    except ValueError:
        return None

def lire_csv(chemin):
    lignes = lire_texte(chemin).splitlines()
    i = next((n for n, l in enumerate(lignes) if any(k in l.lower() for k in COLONNES["volume"])), None)
    if i is None:
        sys.exit(f"{chemin} : ligne d'en-tête introuvable (colonne du volume mensuel absente)")
    sep = "\t" if "\t" in lignes[i] else ("," if lignes[i].count(",") >= lignes[i].count(";") else ";")
    lecteur = csv.reader(io.StringIO("\n".join(lignes[i:])), delimiter=sep)
    entete = [h.strip().lower() for h in next(lecteur)]
    def idx(cle):
        return next((n for n, h in enumerate(entete) if h in COLONNES[cle]), None)
    pos = {k: idx(k) for k in COLONNES}
    if pos["kw"] is None or pos["volume"] is None:
        sys.exit(f"{chemin} : colonnes mot-clé ou volume introuvables (en-têtes lus : {entete})")
    out = {}
    for r in lecteur:
        if not r or pos["kw"] >= len(r) or not r[pos["kw"]].strip():
            continue
        cell = lambda k: r[pos[k]] if pos[k] is not None and pos[k] < len(r) else ""
        vol = nombre(cell("volume"), entier=True)
        out[r[pos["kw"]].strip()] = {
            "volume": int(vol) if vol is not None else None,
            "cpc_low": nombre(cell("cpc_low")),
            "cpc_high": nombre(cell("cpc_high")),
            "competition": cell("competition").strip() or None,
        }
    return out

def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("dossier", help="dossier du site dans l'audit, ex. audits/2026-10-13/mon-site")
    ap.add_argument("--idees", nargs="+", default=[], help="exports CSV des idées de mots-clés")
    ap.add_argument("--exacts", help="export CSV des métriques exactes de ta liste")
    a = ap.parse_args()
    if not a.idees and not a.exacts:
        ap.error("donne au moins un export CSV (--idees ou --exacts)")
    idees = {}
    for f in a.idees:
        for k, v in lire_csv(f).items():
            idees.setdefault(k, v)
    exacts = lire_csv(a.exacts) if a.exacts else {}
    dossier = pathlib.Path(a.dossier); dossier.mkdir(parents=True, exist_ok=True)
    sortie = dossier / "planner.json"
    json.dump({"quand": time.strftime("%Y-%m-%d %H:%M"),
               "sources": [pathlib.Path(f).name for f in a.idees + ([a.exacts] if a.exacts else [])],
               "exacts": exacts, "idees": idees},
              open(sortie, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    sans_volume = sum(1 for v in {**idees, **exacts}.values() if v["volume"] is None)
    print(f"{sortie} : {len(exacts)} métriques exactes, {len(idees)} idées, {sans_volume} sans volume mesuré")

if __name__ == "__main__":
    main()
