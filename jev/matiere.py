#!/usr/bin/env python3
"""Trier la matière d'un sujet (cas 6) : quels passages du corpus sont des preuves exploitables ?

Complète le comptage « scorer la page sur la matière » : le comptage dit combien de
documents parlent du sujet, Jev dit lesquels portent une preuve utilisable dans la page.

Pour chaque passage retenu par recouvrement lexical avec le sujet :
  preuve : ce passage donne-t-il une preuve utilisable sur le sujet ? (5 niveaux → 0-100)
  nature : chiffre / fait / verbatim_client / opinion / rien

Usage : python3 jev/matiere.py "sujet en clair" --corpus DOSSIER [...] [--max 200]
Sortie : verbatims classés dans loops/jev/outputs/, ledger verdicts.jsonl.
"""
import argparse
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from jev import client, ledger, texte  # noqa: E402

PREUVE = [
    "Ne parle pas du sujet, ou l'évoque sans rien en dire",
    "Parle du sujet en termes généraux, rien de citable",
    "Donne un élément concret mais partiel (contexte, situation sans résultat)",
    "Donne un fait, un chiffre ou un verbatim précis, citable tel quel",
    "Donne une preuve forte : chiffre daté, situation vécue avec résultat, verbatim client net",
]
NATURE = {"chiffre": "Un nombre mesuré, daté ou attribuable", "fait": "Un fait vérifiable sans chiffre",
          "verbatim_client": "Les mots d'un client ou d'un utilisateur, réutilisables tels quels",
          "opinion": "Une position ou un avis de l'auteur", "rien": "Aucun élément citable"}


def juger(sujet, p):
    state = {"sujet": sujet, "passage": p["texte"], "source": Path(p["source"]).name}
    questions = {
        "preuve": {"type": "score", "criteria": PREUVE,
                   "instructions": "`passage` donne-t-il une preuve utilisable dans une page sur `sujet` ?"},
        "nature": {"type": "choice", "criteria": NATURE, "instructions": "Quelle est la nature de l'élément le plus citable de `passage` ?"},
    }
    answers, ms, err = client.demander(state, questions)
    if err:
        return {"source": p["source"], "texte": p["texte"], "erreur": err, "ms": ms}
    s, cs = client.score(answers, "preuve", 5)
    n, cn, _ = client.choix(answers, "nature")
    return {"source": p["source"], "texte": p["texte"], "preuve": s, "confiance_preuve": cs, "nature": n, "confiance_nature": cn, "ms": ms}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("sujet")
    ap.add_argument("--corpus", nargs="+", required=True)
    ap.add_argument("--max", type=int, default=200, help="passages à juger (les plus proches du sujet)")
    ap.add_argument("--jobs", type=int, default=6)
    a = ap.parse_args()
    corpus = texte.charger_corpus(a.corpus)
    cand = texte.plus_proches(a.sujet, corpus, a.max)
    if not cand:
        sys.exit("aucun passage ne recoupe le sujet")
    print(f"{len(corpus)} passages, {len(cand)} candidats", file=sys.stderr)
    with ThreadPoolExecutor(a.jobs) as ex:
        verdicts = list(ex.map(lambda p: juger(a.sujet, p), cand))
    verdicts.sort(key=lambda v: -(v.get("preuve") or -1))
    fortes = [v for v in verdicts if (v.get("preuve") or 0) >= 75]
    natures = {k: sum(1 for v in fortes if v.get("nature") == k) for k in NATURE}
    run = {"date": date.today().isoformat(), "modele": client.MODELE, "sujet": a.sujet, "corpus": a.corpus, "candidats": len(cand),
           "preuves_fortes": len(fortes), "natures": natures,
           "sources_distinctes": len({v["source"] for v in fortes})}
    for v in verdicts:
        ledger.ecrire("verdicts", {"usage": "matiere", "sujet": a.sujet, **v})
    ledger.ecrire("runs", {"usage": "matiere", **run})
    out = ledger.BRAIN / "outputs"
    out.mkdir(parents=True, exist_ok=True)
    slug = texte.normaliser(a.sujet).strip().replace(" ", "-")[:50]
    base = out / f"matiere-{slug}-{run['date']}"
    base.with_suffix(".json").write_text(json.dumps({"run": run, "verdicts": verdicts}, ensure_ascii=False, indent=1), encoding="utf-8")
    lignes = [f"# Matière jugée par Jev : {a.sujet}", "",
              f"Candidats : {len(cand)}. Preuves fortes (≥ 75) : {len(fortes)} dans {run['sources_distinctes']} sources. "
              + ", ".join(f"{k} {n}" for k, n in natures.items() if n) + ".", ""]
    for v in fortes:
        lignes.append(f"- [{v['nature']} · {v['preuve']}] {v['texte'][:400]}  \n  {Path(v['source']).name}")
    base.with_suffix(".md").write_text("\n".join(lignes), encoding="utf-8")
    print(json.dumps(run, ensure_ascii=False))
    print(f"rapport : {base.with_suffix('.md')}", file=sys.stderr)


if __name__ == "__main__":
    main()
