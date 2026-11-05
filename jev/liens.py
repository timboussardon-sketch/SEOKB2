#!/usr/bin/env python3
"""Juger des liens internes proposés (cas 7) : la cible aide-t-elle le lecteur ?

Entrée : JSON ou JSONL de propositions, chacune {source: {url,titre}, cible: {url,titre},
ancre, passage} (le format de l'audit JEV `/api/site/ID`, clé `propositions`), ou un
identifiant de site de l'audit JEV (`--site ID`, lu dans ~/Code/maillage/data).

Deux questions par lien :
  utilite : la page cible répond-elle à une question que le lecteur du passage se pose,
            ou lui permet-elle l'étape suivante ?  (5 niveaux → 0-100)
  ancre   : l'ancre annonce-t-elle ce que la cible contient ? (fidele / vague / trompeuse)

Sortie : JSON + markdown trié dans loops/jev/outputs/, ledger verdicts.jsonl.
"""
import argparse
import json
import sqlite3
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from jev import client, ledger  # noqa: E402

UTILITE = [
    "Aucun rapport : le lecteur du passage n'a pas de raison d'aller sur la cible",
    "Rapport lointain : même thème, mais ne répond à rien de ce que le passage soulève",
    "Utile en marge : complète le passage sans être nécessaire",
    "Répond à une question que le passage ouvre, ou est l'étape logique suivante",
    "Indispensable : sans la cible, le lecteur reste bloqué sur ce que le passage dit",
]
ANCRE = {"fidele": "L'ancre dit ce que la cible contient",
         "vague": "L'ancre est générique (« en savoir plus », « ici », « cette page ») ou trop large",
         "trompeuse": "L'ancre promet autre chose que ce que la cible contient"}


def charger(chemin):
    p = Path(chemin).expanduser()
    if p.suffix == ".jsonl":
        return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]
    data = json.loads(p.read_text(encoding="utf-8"))
    return data.get("propositions", data) if isinstance(data, dict) else data


def depuis_audit_jev(site_id):
    base = Path.home() / "Code" / "maillage" / "data"
    dbs = sorted(base.glob("*.db")) + sorted(base.glob("*.sqlite*"))
    if not dbs:
        sys.exit("aucune base de l'audit JEV dans ~/Code/maillage/data")
    conn = sqlite3.connect(dbs[0])
    conn.row_factory = sqlite3.Row
    # les propositions gardent les ids de pages de leur crawl : on résout sans filtrer par site
    pages = {r["id"]: dict(r) for r in conn.execute("SELECT id,url,title,h1,substr(content_text,1,1200) AS extrait FROM pages")}
    out, orphelins = [], 0
    for o in conn.execute("SELECT id,source_id,target_id,anchor,passage,status FROM opportunities WHERE site_id=? AND status IN ('ouverte','validee')", (site_id,)):
        s, c = pages.get(o["source_id"]), pages.get(o["target_id"])
        if not s or not c:
            orphelins += 1  # pages d'un crawl précédent, plus dans la base : rien à juger
            continue
        out.append({"id": o["id"], "source": {"url": s.get("url"), "titre": s.get("title") or s.get("h1")},
                    "cible": {"url": c.get("url"), "titre": c.get("title") or c.get("h1"), "extrait": c.get("extrait")},
                    "ancre": o["anchor"], "passage": o["passage"]})
    if orphelins:
        print(f"{orphelins} proposition(s) ignorée(s) : pages absentes de la base (recrawl)", file=sys.stderr)
    return out


def juger(p):
    state = {"page_source": p.get("source", {}), "passage_ou_le_lien_serait_pose": p.get("passage"),
             "ancre_proposee": p.get("ancre"), "page_cible": p.get("cible", {})}
    questions = {
        "utilite": {"type": "score", "criteria": UTILITE,
                    "instructions": "Le lecteur lit `passage_ou_le_lien_serait_pose` sur `page_source`. La `page_cible` l'aide-t-elle à répondre à une question que ce passage soulève, ou à faire l'étape suivante ?"},
        "ancre": {"type": "choice", "criteria": ANCRE,
                  "instructions": "`ancre_proposee` annonce-t-elle ce que `page_cible` contient ?"},
    }
    answers, ms, err = client.demander(state, questions)
    if err:
        return {**p, "erreur": err, "ms": ms}
    u, cu = client.score(answers, "utilite", 5)
    an, ca, _ = client.choix(answers, "ancre")
    return {**p, "utilite": u, "confiance_utilite": cu, "ancre_verdict": an, "confiance_ancre": ca, "ms": ms}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("fichier", nargs="?")
    ap.add_argument("--site", type=int, help="id de site dans l'audit JEV")
    ap.add_argument("--seuil", type=int, default=75, help="utilité minimale pour entrer dans la file")
    ap.add_argument("--jobs", type=int, default=6)
    a = ap.parse_args()
    props = depuis_audit_jev(a.site) if a.site else charger(a.fichier)
    if not props:
        sys.exit("aucune proposition de lien")
    with ThreadPoolExecutor(a.jobs) as ex:
        verdicts = list(ex.map(juger, props))
    verdicts.sort(key=lambda v: -(v.get("utilite") or -1))
    retenus = [v for v in verdicts if (v.get("utilite") or 0) >= a.seuil and v.get("ancre_verdict") == "fidele"]
    ancre_a_revoir = [v for v in verdicts if (v.get("utilite") or 0) >= a.seuil and v.get("ancre_verdict") != "fidele"]
    ecartes = [v for v in verdicts if (v.get("utilite") or 0) < a.seuil]
    run = {"date": date.today().isoformat(), "modele": client.MODELE, "entree": a.fichier or f"audit-jev-site-{a.site}",
           "liens": len(verdicts), "retenus": len(retenus), "ancre_a_revoir": len(ancre_a_revoir),
           "ecartes": len(ecartes), "seuil": a.seuil}
    for v in verdicts:
        ledger.ecrire("verdicts", {"usage": "liens", "entree": run["entree"], **v})
    ledger.ecrire("runs", {"usage": "liens", **run})
    out = ledger.BRAIN / "outputs"
    out.mkdir(parents=True, exist_ok=True)
    base = out / f"liens-{Path(run['entree']).stem}-{run['date']}"
    base.with_suffix(".json").write_text(json.dumps({"run": run, "verdicts": verdicts}, ensure_ascii=False, indent=1), encoding="utf-8")

    def ligne(v):
        return (f"- {v.get('source', {}).get('url')} → {v.get('cible', {}).get('url')}  \n"
                f"  ancre « {v.get('ancre')} » ({v.get('ancre_verdict')}), utilité {v.get('utilite')}, confiance {v.get('confiance_utilite')}")
    lignes = [f"# Liens jugés par Jev : {run['entree']}", "",
              f"Liens : {len(verdicts)}. Retenus (utilité ≥ {a.seuil}, ancre fidèle) : {len(retenus)}. "
              f"Ancre à revoir : {len(ancre_a_revoir)}. Écartés : {len(ecartes)}.", ""]
    for titre, sel in (("Retenus : file d'implémentation", retenus), ("Utiles mais ancre à revoir", ancre_a_revoir), ("Écartés", ecartes)):
        if sel:
            lignes += [f"## {titre} ({len(sel)})", ""] + [ligne(v) for v in sel] + [""]
    base.with_suffix(".md").write_text("\n".join(lignes), encoding="utf-8")
    print(json.dumps(run, ensure_ascii=False))
    print(f"rapport : {base.with_suffix('.md')}", file=sys.stderr)


if __name__ == "__main__":
    main()
