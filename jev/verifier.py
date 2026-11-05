#!/usr/bin/env python3
"""Vérifier un draft phrase par phrase contre les extraits du corpus (cas 10).

Pour chaque phrase : les passages du corpus les plus proches (recouvrement lexical),
puis deux questions à Jev :
  appui       : la phrase est-elle appuyée par ces passages ? (appuyée / déduite / absente / hors-source)
  remplissage : la phrase apporte-t-elle une information, ou introduit-elle, résume-t-elle,
                commente-t-elle seulement ? (règle mère : on écrit à partir des faits)

Sortie : rapport markdown + JSON dans loops/jev/outputs/, une ligne par phrase dans
loops/jev/ledgers/verdicts.jsonl. Jev trie ; la décision reste à Tim.

Usage :
  python3 jev/verifier.py DRAFT.md --corpus DOSSIER_OU_FICHIER [...] [--k 5] [--jobs 6]
"""
import argparse
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from jev import client, ledger, texte  # noqa: E402

APPUI = {
    "appuyee": "Un passage fourni dit la même chose, ou porte le chiffre, le fait ou le verbatim de la phrase",
    "deduite": "La phrase généralise ou interprète les passages : elle va plus loin que ce qu'ils disent",
    "absente": "Aucun passage fourni ne porte ce que la phrase affirme",
    "hors_source": "La phrase n'affirme rien qui demande une source (consigne, transition, question, définition évidente)",
}
REMPLISSAGE = {
    "information": "La phrase apporte un fait, un chiffre, un exemple, une instruction ou une opinion précise",
    "remplissage": "La phrase introduit, résume, commente ou conclut sans rien apporter que le lecteur ne sache déjà",
}


def juger(phrase, passages):
    state = {"phrase": phrase,
             "passages": [{"source": Path(p["source"]).name, "texte": p["texte"]} for p in passages]}
    questions = {
        "appui": {"type": "choice",
                  "instructions": "`phrase` vient d'un article. `passages` sont les seuls extraits du corpus disponibles. La phrase est-elle appuyée par ces passages ?",
                  "criteria": APPUI},
        "remplissage": {"type": "choice",
                        "instructions": "Prise seule, `phrase` apporte-t-elle une information au lecteur ?",
                        "criteria": REMPLISSAGE},
    }
    answers, ms, err = client.demander(state, questions)
    if err:
        return {"phrase": phrase, "erreur": err, "ms": ms}
    appui, conf_a, _ = client.choix(answers, "appui")
    remp, conf_r, _ = client.choix(answers, "remplissage")
    return {"phrase": phrase, "appui": appui, "confiance_appui": conf_a,
            "remplissage": remp == "remplissage", "confiance_remplissage": conf_r,
            "sources": sorted({Path(p["source"]).name for p in passages}), "ms": ms}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("draft")
    ap.add_argument("--corpus", nargs="+", required=True)
    ap.add_argument("--k", type=int, default=5)
    ap.add_argument("--jobs", type=int, default=6)
    ap.add_argument("--out", help="dossier de sortie (défaut loops/jev/outputs)")
    a = ap.parse_args()

    draft = Path(a.draft).expanduser()
    md = draft.read_text(encoding="utf-8")
    phs = texte.phrases(md)
    corpus = texte.charger_corpus(a.corpus)
    if not corpus:
        sys.exit("corpus vide : rien à vérifier")
    print(f"{len(phs)} phrases, {len(corpus)} passages de corpus", file=sys.stderr)

    with ThreadPoolExecutor(a.jobs) as ex:
        verdicts = list(ex.map(lambda ph: juger(ph, texte.plus_proches(ph, corpus, a.k)), phs))

    n = len(verdicts)
    compte = {k: sum(1 for v in verdicts if v.get("appui") == k) for k in APPUI}
    remp = sum(1 for v in verdicts if v.get("remplissage"))
    erreurs = sum(1 for v in verdicts if v.get("erreur"))
    a_sourcer = compte["absente"] + compte["deduite"]
    score = None if not n else int(round(100 * (1 - ((a_sourcer + remp) / n) ** 0.5)))

    run = {"date": date.today().isoformat(), "modele": client.MODELE, "draft": str(draft), "corpus": a.corpus,
           "phrases": n, "compte": compte, "remplissage": remp, "erreurs": erreurs, "score": score}
    for v in verdicts:
        ledger.ecrire("verdicts", {"usage": "verifier", "draft": str(draft), **v})
    ledger.ecrire("runs", {"usage": "verifier", **run})

    out = Path(a.out).expanduser() if a.out else ledger.BRAIN / "outputs"
    out.mkdir(parents=True, exist_ok=True)
    base = out / f"verifier-{draft.stem}-{run['date']}"
    (base.with_suffix(".json")).write_text(json.dumps({"run": run, "verdicts": verdicts}, ensure_ascii=False, indent=1), encoding="utf-8")

    lignes = [f"# Vérification Jev : {draft.name}", "",
              f"Corpus : {', '.join(a.corpus)}", "",
              f"Phrases : {n}. Appuyées : {compte['appuyee']}. Déduites : {compte['deduite']}. "
              f"Absentes du corpus : {compte['absente']}. Hors source : {compte['hors_source']}. "
              f"Remplissage : {remp}. Erreurs d'appel : {erreurs}.", "",
              f"Score (100 = tout appuyé, rien de remplissage ; même formule que l'audit JEV) : **{score}**", ""]
    for titre, cle in (("À sourcer ou supprimer : absentes du corpus", "absente"),
                       ("Déduites : la phrase dépasse la source", "deduite")):
        sel = [v for v in verdicts if v.get("appui") == cle]
        if sel:
            lignes += [f"## {titre} ({len(sel)})", ""]
            lignes += [f"- {v['phrase']}  \n  confiance {v['confiance_appui']}, passages proches : {', '.join(v['sources']) or 'aucun'}" for v in sel]
            lignes.append("")
    sel = [v for v in verdicts if v.get("remplissage")]
    if sel:
        lignes += [f"## Remplissage : la phrase n'apporte rien ({len(sel)})", ""]
        lignes += [f"- {v['phrase']}  \n  confiance {v['confiance_remplissage']}" for v in sel]
        lignes.append("")
    base.with_suffix(".md").write_text("\n".join(lignes), encoding="utf-8")
    print(json.dumps(run, ensure_ascii=False))
    print(f"rapport : {base.with_suffix('.md')}", file=sys.stderr)


if __name__ == "__main__":
    main()
