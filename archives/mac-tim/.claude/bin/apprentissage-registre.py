#!/usr/bin/env python3
"""
Tient à jour deux fichiers déterministes de la boucle d'apprentissage :

- wiki/apprentissage/domaines.txt      : les domaines dont on possède la donnée GSC
- wiki/apprentissage/publications.jsonl : les pages mises en ligne, une ligne par publication

Fusion sans doublon sur le couple (date, URL). Aucun LLM.

Usage : apprentissage-registre.py --extraction .claude/tmp/apprentissage-AAAA-MM-JJ.json
"""
import argparse, json, os
from urllib.parse import urlparse

VAULT = os.path.expanduser("~/Code/seo-kb")
GSC = os.path.expanduser("~/Code/gsc-simcity/data")
DOMAINES = os.path.join(VAULT, "wiki/apprentissage/domaines.txt")
REGISTRE = os.path.join(VAULT, "wiki/apprentissage/publications.jsonl")


def rafraichir_domaines():
    hosts = set()
    if not os.path.isdir(GSC):
        return 0
    for slug in os.listdir(GSC):
        f = os.path.join(GSC, slug, "gsc-brut.json")
        if not os.path.isfile(f):
            continue
        try:
            tete = open(f).read(400)
            i = tete.find('"site"')
            if i == -1:
                continue
            h = urlparse(tete[i:].split('"')[3]).netloc.replace("www.", "")
            if h:
                hosts.add(h)
        except Exception:
            continue
    os.makedirs(os.path.dirname(DOMAINES), exist_ok=True)
    with open(DOMAINES, "w") as f:
        f.write("\n".join(sorted(hosts)) + "\n")
    return len(hosts)


def fusionner(extraction):
    with open(extraction) as f:
        d = json.load(f)

    connus = set()
    lignes = []
    if os.path.isfile(REGISTRE):
        with open(REGISTRE) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                e = json.loads(line)
                lignes.append(e)
                for u in e.get("urls", []):
                    connus.add((e["publie"], u))

    ajouts = 0
    for p in d.get("publications", []):
        date = (p.get("ts") or "")[:10]
        urls = []
        for u in p.get("urls", []):
            if urlparse(u).path in ("", "/"):     # la home n'est pas une publication
                continue
            if (date, u) in connus:
                continue
            connus.add((date, u))
            urls.append(u)
        if not urls:
            continue
        lignes.append({"publie": date, "urls": urls, "projet": p.get("projet", ""),
                       "contexte": (p.get("commande") or "")[:90]})
        ajouts += len(urls)

    lignes.sort(key=lambda e: e["publie"])
    with open(REGISTRE, "w") as f:
        for e in lignes:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")
    return ajouts, len(lignes)


if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--extraction", required=True)
    a = a.parse_args()
    n = rafraichir_domaines()
    ajouts, total = fusionner(a.extraction)
    print(f"domaines mesurables: {n} | URLs ajoutées: {ajouts} | publications suivies: {total}")
