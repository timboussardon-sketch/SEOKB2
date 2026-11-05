#!/usr/bin/env python3
"""Classer les verdicts de Tim (boucle d'apprentissage) avec Jev, et comparer à la regex.

Aujourd'hui `.claude/bin/apprentissage-extract.py::classer()` range chaque message de Tim
qui suit une livraison en rejet / casse / validation / correction / neutre par regex, puis
la commande /apprentissage décide si l'événement porte une règle réutilisable.

Ici, pour chaque événement extrait : deux questions à Jev.
  verdict      : ce que le message dit de la livraison (rejet / casse / validation / correction / neutre)
  reutilisable : l'événement porte-t-il une règle de travail généralisable, une consigne
                 propre à ce projet, ou rien (bruit, spécification de produit) ?

Puis, si --verite est donné, on lit les fiches wiki/apprentissage/*.md déjà rédigées :
une citation sous « ❌ Rejeté, et la règle qui en sort » a été promue en règle, une
citation sous « Non extraits en règle » a été écartée. On mesure l'accord de Jev et
de la regex avec ces fiches. Jev trie, la décision reste à Tim.

Usage :
  python3 jev/apprentissage.py EVENTS.json [--verite wiki/apprentissage] [--jobs 6]
  (EVENTS.json = sortie de apprentissage-extract.py --out)
"""
import argparse
import json
import re
import sys
import unicodedata
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from jev import client, ledger  # noqa: E402

VERDICT = {
    "rejet": "Tim refuse ce qui a été livré : ce n'est pas ce qu'il a demandé, il annule ou demande de refaire",
    "casse": "Tim constate que quelque chose ne fonctionne plus : bug, erreur, page blanche, régression",
    "validation": "Tim approuve ce qui a été livré, sans demander de changement",
    "correction": "Tim accepte la direction et demande un ajustement précis",
    "neutre": "Le message est une nouvelle consigne, une question ou du contexte, il ne juge pas la livraison",
}
REUTILISABLE = {
    "regle_generalisable": "L'événement révèle une manière de travailler à corriger dans tous les projets (ajout non demandé, skill ignoré, bug annoncé clos sans reproduction, fichier écrasé, sortie non vérifiée)",
    "specifique": "La consigne ne vaut que pour ce projet ou ce produit : règle de jeu, choix de design, spécification fonctionnelle, préférence locale",
    "aucune": "Rien à retenir : test demandé puis écarté, message interrompu, bruit, précision qui revient sur le message précédent",
}


def juger(e):
    e = {**e, "message": masquer(e["message"])}
    state = {
        "message_de_tim": e["message"][:1200],
        "projet": e.get("projet", ""),
        "fichiers_livres_juste_avant": [Path(a).name for a in e.get("artefacts", [])][:12],
        "commits_juste_avant": [c for c in e.get("commits", []) if not c.startswith("$(")][:5],
    }
    questions = {
        "verdict": {"type": "choice",
                    "instructions": "`message_de_tim` est écrit juste après que l'agent a livré `fichiers_livres_juste_avant`. Que dit ce message de la livraison ?",
                    "criteria": VERDICT},
        "reutilisable": {"type": "choice",
                         "instructions": "Si on retient cet événement pour améliorer la façon de travailler de l'agent, qu'est-ce qu'il apprend ?",
                         "criteria": REUTILISABLE},
    }
    answers, ms, err = client.demander(state, questions)
    if err:
        return {**e, "erreur": err, "ms": ms}
    v, cv, _ = client.choix(answers, "verdict")
    r, cr, _ = client.choix(answers, "reutilisable")
    return {"ts_event": e.get("ts"), "projet": e.get("projet"), "message": e["message"][:300],
            "verdict_regex": e.get("verdict"), "verdict_jev": v, "confiance_verdict": cv,
            "reutilisable": r, "confiance_reutilisable": cr, "ms": ms}


# --- vérité-terrain : les fiches wiki/apprentissage déjà rédigées -------------------------
RE_CIT = re.compile(r"«\s*(.+?)\s*»", re.S)
RE_SECRET = re.compile(r"(sk-ant-[A-Za-z0-9_\-]{8,}|sk-[A-Za-z0-9]{20,}|AIza[0-9A-Za-z_\-]{20,}|ghp_[A-Za-z0-9]{20,}|eyJ[A-Za-z0-9_\-]{30,}\.[A-Za-z0-9_\-]+)")


def masquer(s):
    return RE_SECRET.sub("[secret masqué]", s or "")


def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def verite(dossier):
    """Rend {norm(début de citation): 'regle'|'ecartee'|'casse'|'validation'} lues dans les fiches."""
    labels = {}
    for f in sorted(Path(dossier).glob("2026-*.md")):
        section, sous = None, None
        for ligne in f.read_text(encoding="utf-8").splitlines():
            if ligne.startswith("## "):
                section, sous = ligne, None
                continue
            if ligne.startswith("Non extraits en règle"):
                sous = "ecartee"
                continue
            if not section:
                continue
            lab = None
            if "Rejeté" in section:
                lab = sous or "regle"
            elif "cassé" in section:
                lab = "casse"
            elif "Validé" in section:
                lab = "validation"
            if not lab:
                continue
            for m in RE_CIT.finditer(ligne):
                labels[norm(m.group(1))[:60]] = lab
    return labels


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("events")
    ap.add_argument("--verite", help="dossier wiki/apprentissage")
    ap.add_argument("--jobs", type=int, default=6)
    ap.add_argument("--out", help="dossier de sortie (défaut loops/jev/outputs)")
    a = ap.parse_args()

    data = json.loads(Path(a.events).read_text(encoding="utf-8"))
    evs = [e for e in data["evenements"] if e.get("message")]
    print(f"{len(evs)} événements", file=sys.stderr)
    with ThreadPoolExecutor(a.jobs) as ex:
        verdicts = list(ex.map(juger, evs))

    for v in verdicts:
        ledger.ecrire("verdicts", {"usage": "apprentissage", **v})

    ok = [v for v in verdicts if "erreur" not in v]
    lignes = [f"# Verdicts d'apprentissage jugés par Jev : {Path(a.events).name}", "",
              f"Événements : {len(verdicts)}. Jugés : {len(ok)}. Erreurs d'appel : {len(verdicts) - len(ok)}. "
              f"Latence médiane : {sorted(v['ms'] for v in ok)[len(ok) // 2] if ok else 0} ms.", ""]

    # accord regex / Jev sur le verdict
    acc = sum(1 for v in ok if v["verdict_regex"] == v["verdict_jev"])
    lignes += [f"## Verdict : regex contre Jev", "",
               f"Accord sur {acc}/{len(ok)} ({round(100 * acc / len(ok)) if ok else 0} %).", ""]
    croise = {}
    for v in ok:
        croise.setdefault(v["verdict_regex"], {}).setdefault(v["verdict_jev"], 0)
        croise[v["verdict_regex"]][v["verdict_jev"]] += 1
    for r, d in croise.items():
        lignes.append(f"- regex `{r}` → Jev " + ", ".join(f"{k} {n}" for k, n in sorted(d.items(), key=lambda x: -x[1])))
    lignes.append("")

    # accord avec les fiches déjà rédigées
    if a.verite:
        labels = verite(a.verite)
        appar = []
        for v in ok:
            k = norm(v["message"])[:60]
            lab = labels.get(k)
            if lab is None:
                lab = next((l for c, l in labels.items() if c and (c.startswith(k[:40]) or k.startswith(c[:40]))), None)
            if lab:
                appar.append((v, lab))
        lignes += ["## Contre les fiches wiki/apprentissage (relues par l'agent, pas encore par Tim)", "",
                   f"Citations retrouvées dans les fiches : {len(appar)} sur {len(labels)} citations labellisées.", ""]
        # règle retenue = reutilisable regle_generalisable ; écartée = specifique/aucune
        n_r = sum(1 for v, l in appar if l in ("regle", "ecartee"))
        a_r = sum(1 for v, l in appar if (l == "regle") == (v["reutilisable"] == "regle_generalisable") and l in ("regle", "ecartee"))
        lignes += [f"Règle retenue ou écartée : Jev d'accord sur {a_r}/{n_r}." if n_r else "Aucune citation rejet/écartée appariée.", ""]
        for v, l in appar:
            fiche_regle = l == "regle"
            jev_regle = v["reutilisable"] == "regle_generalisable"
            marque = "✓" if (l not in ("regle", "ecartee") or fiche_regle == jev_regle) else "✗"
            lignes.append(f"- {marque} fiche `{l}` · regex `{v['verdict_regex']}` · Jev `{v['verdict_jev']}` ({v['confiance_verdict']}) / `{v['reutilisable']}` ({v['confiance_reutilisable']}) · « {v['message'][:110]} »")
            ledger.ecrire("verdicts_tim", {"usage": "apprentissage", "ref": v["message"][:80],
                                           "verdict_tim": "ok" if fiche_regle else "ko",
                                           "origine": "wiki/apprentissage, fiche rédigée par l'agent, non relue par Tim"})
        lignes.append("")

    lignes += ["## Désaccords regex / Jev à relire", ""]
    for v in ok:
        if v["verdict_regex"] != v["verdict_jev"]:
            lignes.append(f"- regex `{v['verdict_regex']}` · Jev `{v['verdict_jev']}` ({v['confiance_verdict']}) · `{v['reutilisable']}` · « {v['message'][:120]} »")

    out = Path(a.out) if a.out else ledger.BRAIN / "outputs"
    out.mkdir(parents=True, exist_ok=True)
    base = out / f"apprentissage-{Path(a.events).stem}-{date.today().isoformat()}"
    base.with_suffix(".md").write_text("\n".join(lignes) + "\n", encoding="utf-8")
    base.with_suffix(".json").write_text(json.dumps(verdicts, ensure_ascii=False, indent=1), encoding="utf-8")
    ledger.ecrire("runs", {"usage": "apprentissage", "events": str(a.events), "n": len(verdicts),
                           "erreurs": len(verdicts) - len(ok), "rapport": str(base.with_suffix(".md"))})
    print("\n".join(lignes[:12]))
    print(f"\nrapport : {base.with_suffix('.md')}")


if __name__ == "__main__":
    main()
