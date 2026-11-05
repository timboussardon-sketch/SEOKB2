#!/usr/bin/env python3
"""Noter les verdicts de Jev, ligne par ligne, sans retaper de référence.

`calibrer.py --noter USAGE REF ok` demande de recopier la clé exacte. C'est pour
ça qu'il y a 463 verdicts Jev et aucune note sur liens, verifier et matiere.

Ici on déroule les verdicts non encore notés, on affiche ce que Jev a répondu, et
on attend une touche :

    o   Jev a raison
    k   Jev a tort
    s   passer, on ne sait pas
    q   arrêter et écrire ce qui est noté

Chaque note part dans le même ledger que `calibrer.py --noter`, avec la même clé
de rapprochement (ref_de), donc la calibration la voit immédiatement.

  python3 jev/noter.py liens
  python3 jev/noter.py verifier --limite 30
  python3 jev/noter.py liens --depuis 2026-09-24 --desaccords-dabord
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from jev import ledger  # noqa: E402
from jev.calibrer import jev_ok, ref_de  # noqa: E402

USAGES = ("liens", "verifier", "matiere", "apprentissage")


def resume(v):
    """Ce que Jev a répondu, en une ou deux lignes lisibles."""
    u = v.get("usage")
    if u == "liens":
        s = (v.get("source") or {}).get("url") or (v.get("source") or {}).get("titre") or "?"
        c = (v.get("cible") or {}).get("url") or (v.get("cible") or {}).get("titre") or "?"
        return [f"{s}", f"  → {c}",
                f"  ancre « {v.get('ancre')} » : {v.get('ancre_verdict')} "
                f"(conf. {v.get('confiance_ancre')})",
                f"  utilité {v.get('utilite')} (conf. {v.get('confiance_utilite')})"]
    if u == "verifier":
        return [f"« {(v.get('phrase') or '')[:300]} »",
                f"  appui : {v.get('appui')} (conf. {v.get('confiance_appui')})"
                f"   remplissage : {v.get('remplissage')}"]
    if u == "matiere":
        return [f"« {(v.get('texte') or '')[:300]} »",
                f"  preuve {v.get('preuve')} · nature {v.get('nature')}"]
    return [f"« {(v.get('message') or '')[:300]} »",
            f"  {v.get('reutilisable')} (conf. {v.get('confiance_reutilisable')})"]


def verdict_lisible(v):
    j = jev_ok(v)
    if j is None:
        return "Jev : sans verdict exploitable"
    return "Jev retient cette ligne" if j else "Jev écarte cette ligne"


def main():
    ap = argparse.ArgumentParser(description="Noter les verdicts de Jev un par un")
    ap.add_argument("usage", choices=USAGES)
    ap.add_argument("--limite", type=int, default=0, help="s'arrêter après N notes (0 = tout)")
    ap.add_argument("--depuis", help="ne prendre que les verdicts à partir de cette date (AAAA-MM-JJ)")
    ap.add_argument("--desaccords-dabord", action="store_true",
                    help="commencer par les lignes que Jev écarte : c'est là qu'il se trompe le plus")
    ap.add_argument("--renoter", action="store_true", help="reprendre aussi les lignes déjà notées")
    a = ap.parse_args()

    deja = {t["ref"][:80] for t in ledger.lire("verdicts_tim") if t.get("usage") == a.usage}

    vus, file = set(), []
    for v in ledger.lire("verdicts"):
        if v.get("usage") != a.usage:
            continue
        if a.depuis and (v.get("ts") or "") < a.depuis:
            continue
        r = ref_de(v)
        if not r:
            continue
        if not a.renoter and r[:80] in deja:
            continue
        if r[:80] in vus:
            continue
        vus.add(r[:80])
        file.append((r, v))

    if not file:
        non_notables = sum(1 for v in ledger.lire("verdicts")
                           if v.get("usage") == a.usage and not ref_de(v))
        msg = f"rien à noter pour « {a.usage} »."
        if deja:
            msg += f" {len(deja)} ligne(s) déjà notée(s) (--renoter pour les reprendre)."
        if non_notables:
            msg += f" {non_notables} verdict(s) sans clé identifiable, non notables."
        sys.exit(msg)

    if a.desaccords_dabord:
        file.sort(key=lambda rv: (jev_ok(rv[1]) is not False))

    total = len(file) if not a.limite else min(a.limite, len(file))
    print(f"{len(file)} ligne(s) à noter pour « {a.usage} ». o = Jev a raison, "
          f"k = Jev a tort, s = passer, q = arrêter.\n")

    notes = 0
    for i, (ref, v) in enumerate(file, 1):
        if a.limite and notes >= a.limite:
            break
        print(f"─── {i}/{len(file)}  ({notes} notée(s) sur {total} visées)")
        for ligne in resume(v):
            print(ligne)
        print(f"  {verdict_lisible(v)}")
        while True:
            try:
                rep = input("  [o/k/s/q] ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print("\ninterrompu.")
                rep = "q"
            if rep in ("o", "k", "s", "q"):
                break
        if rep == "q":
            break
        if rep == "s":
            print()
            continue
        ledger.ecrire("verdicts_tim", {"usage": a.usage, "ref": ref,
                                       "verdict_tim": "ok" if rep == "o" else "ko",
                                       "origine": "noté à la main par Tim (jev/noter.py)"})
        notes += 1
        print()

    print(f"\n{notes} verdict(s) notés et écrits dans le ledger.")
    if notes:
        print("Recalculer la calibration :  python3 jev/calibrer.py")


if __name__ == "__main__":
    main()
