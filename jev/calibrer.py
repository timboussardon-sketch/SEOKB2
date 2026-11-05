#!/usr/bin/env python3
"""Calibrer Jev contre les verdicts de Tim avant de laisser un workflow agir.

Deux sources de vérité :
  1. loops/jev/ledgers/verdicts_tim.jsonl : une ligne par jugement humain
     {usage, ref, verdict_tim}. `ref` = la phrase (verifier), "source→cible" (liens)
     ou le début du passage (matiere). verdict_tim ∈ ok | ko.
     Ajout : python3 jev/calibrer.py --noter verifier "phrase..." ko
  2. Les verdicts Jev du ledger verdicts.jsonl, rapprochés par usage + ref.

Sortie : accord, faux positifs (Jev ko / Tim ok), faux négatifs (Jev ok / Tim ko),
et le seuil de confiance en dessous duquel Jev se trompe le plus. Écrit
loops/jev/derived/calibration.json. Tant que l'accord est sous 80 % sur ≥ 30 cas,
un usage reste en « tri pour relecture », jamais en action automatique.
Seuls comptent les verdicts produits par le modèle fixé dans client.MODELE.
"""
import argparse
import json
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from jev import client, ledger  # noqa: E402


def _bout(d, *cles):
    """Premier champ non vide d'un dict de page, pour identifier un lien."""
    for c in cles:
        v = (d or {}).get(c)
        if v:
            return str(v)
    return ""


def ref_de(v):
    """Clé de rapprochement entre un verdict Jev et un verdict de Tim.

    Rend "" quand rien n'identifie la ligne : elle est alors non notable, et
    comptée comme telle. Auparavant un lien sans URL produisait "None→None",
    et tous ces liens s'écrasaient sous une seule clé.
    """
    u = v.get("usage")
    if u == "verifier":
        return v.get("phrase", "")
    if u == "liens":
        s = _bout(v.get("source"), "url", "titre", "title")
        c = _bout(v.get("cible") or v.get("target"), "url", "titre", "title")
        if not s and not c:
            return ""
        ancre = v.get("ancre") or v.get("anchor") or ""
        return f"{s}→{c}" + (f" « {ancre} »" if not (s and c) else "")
    if u == "matiere":
        return (v.get("texte") or "")[:80]
    if u == "apprentissage":
        return (v.get("message") or "")[:80]
    return ""


def jev_ok(v):
    u = v.get("usage")
    if u == "verifier":
        return v.get("appui") in ("appuyee", "hors_source") and not v.get("remplissage")
    if u == "liens":
        return (v.get("utilite") or 0) >= 75 and v.get("ancre_verdict") == "fidele"
    if u == "matiere":
        return (v.get("preuve") or 0) >= 75
    if u == "apprentissage":
        return v.get("reutilisable") == "regle_generalisable"
    return None


def confiance(v):
    return min(x for x in (v.get("confiance_appui"), v.get("confiance_remplissage"), v.get("confiance_utilite"),
                           v.get("confiance_ancre"), v.get("confiance_preuve"), v.get("confiance_nature"), v.get("confiance_verdict"), v.get("confiance_reutilisable")) if x is not None) if any(
        v.get(k) is not None for k in ("confiance_appui", "confiance_utilite", "confiance_preuve", "confiance_reutilisable")) else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--noter", nargs=3, metavar=("USAGE", "REF", "VERDICT"), help="ajouter un verdict de Tim (ok|ko)")
    a = ap.parse_args()
    if a.noter:
        usage, ref, verdict = a.noter
        if verdict not in ("ok", "ko"):
            sys.exit("verdict : ok ou ko")
        ledger.ecrire("verdicts_tim", {"usage": usage, "ref": ref, "verdict_tim": verdict})
        print("noté")
    tim = {(t["usage"], t["ref"][:80]): t["verdict_tim"] for t in ledger.lire("verdicts_tim")}
    derniers, non_notables, autre_modele = {}, defaultdict(int), defaultdict(int)
    for v in ledger.lire("verdicts"):
        if v.get("modele") != client.MODELE:  # sans champ = jev-latest d'avant le 12/10, version inconnue
            autre_modele[v.get("usage")] += 1
            continue
        r = ref_de(v)
        if not r:
            non_notables[v.get("usage")] += 1
            continue
        derniers[(v.get("usage"), r[:80])] = v  # le plus récent gagne
    par_usage = defaultdict(lambda: {"cas": 0, "accord": 0, "faux_positifs": [], "faux_negatifs": [], "conf_erreurs": []})
    for k, verdict_tim in tim.items():
        v = derniers.get(k)
        if v is None:
            continue
        j = jev_ok(v)
        r = par_usage[k[0]]
        r["cas"] += 1
        tim_ok = verdict_tim == "ok"
        if j == tim_ok:
            r["accord"] += 1
        else:
            (r["faux_negatifs"] if tim_ok else r["faux_positifs"]).append(k[1])
            c = confiance(v)
            if c is not None:
                r["conf_erreurs"].append(c)
    rapport = {"date": date.today().isoformat(), "modele": client.MODELE, "usages": {}}
    for u in set(par_usage) | set(non_notables) | set(autre_modele):
        r = par_usage[u]
        taux = round(100 * r["accord"] / r["cas"]) if r["cas"] else None
        rapport["usages"][u] = {
            "cas": r["cas"], "accord_pct": taux,
            "faux_positifs": len(r["faux_positifs"]), "faux_negatifs": len(r["faux_negatifs"]),
            "confiance_max_des_erreurs": max(r["conf_erreurs"]) if r["conf_erreurs"] else None,
            "statut": "action possible" if r["cas"] >= 30 and (taux or 0) >= 80 else "tri pour relecture seulement",
            "verdicts_non_notables": non_notables.get(u, 0),
            "verdicts_autre_modele_ignores": autre_modele.get(u, 0),
            "exemples_faux_positifs": r["faux_positifs"][:5], "exemples_faux_negatifs": r["faux_negatifs"][:5]}
    (ledger.BRAIN / "derived").mkdir(parents=True, exist_ok=True)
    (ledger.BRAIN / "derived" / "calibration.json").write_text(json.dumps(rapport, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(rapport, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
