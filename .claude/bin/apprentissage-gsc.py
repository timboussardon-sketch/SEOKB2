#!/usr/bin/env python3
"""
Résolveur de preuve — répond « est-ce que la page publiée a marché ? »

Prend le registre des publications (wiki/apprentissage/publications.jsonl),
va chercher la donnée réelle dans ~/Code/gsc-simcity/data/<slug>/gsc-brut.json
(rows date x page), et remplit les jalons J+30 et J+90.

Jamais d'estimation : si la donnée n'existe pas, le jalon reste vide avec un motif.

Usage :
  apprentissage-gsc.py --registre wiki/apprentissage/publications.jsonl
  apprentissage-gsc.py --url https://organikk.co/blog/x/ --publie 2026-07-07
"""
import argparse, importlib.util, json, os, sys
from datetime import datetime, timedelta
from pathlib import Path
from urllib.parse import urlparse

GSC = os.path.expanduser("~/Code/gsc-simcity/data")


def carte_sites():
    """host -> slug de dossier gsc-simcity."""
    carte = {}
    if not os.path.isdir(GSC):
        return carte
    for slug in sorted(os.listdir(GSC)):
        f = os.path.join(GSC, slug, "gsc-brut.json")
        if not os.path.isfile(f):
            continue
        try:
            with open(f) as fh:
                tete = fh.read(400)
            i = tete.find('"site"')
            if i == -1:
                continue
            site = tete[i:].split('"')[3]
            host = urlparse(site).netloc.replace("www.", "")
            carte.setdefault(host, slug)
        except Exception:
            continue
    return carte


def lignes(slug):
    with open(os.path.join(GSC, slug, "gsc-brut.json")) as fh:
        d = json.load(fh)
    return d.get("datePage") or []


def agrege(rows, url, d1, d2):
    """Somme clics/impressions et position moyenne pondérée sur [d1, d2] pour une URL."""
    clics = imp = 0
    pos_pond = 0.0
    cible = url.rstrip("/")
    for r in rows:
        k = r.get("keys") or []
        if len(k) < 2:
            continue
        date, page = k[0], k[1].rstrip("/")
        if page != cible or not (d1 <= date <= d2):
            continue
        clics += r.get("clicks", 0)
        i = r.get("impressions", 0)
        imp += i
        pos_pond += r.get("position", 0) * i
    return {
        "clics": clics,
        "impressions": imp,
        "position": round(pos_pond / imp, 2) if imp else None,
    }


def resoudre(url, publie, rows_cache, carte):
    host = urlparse(url).netloc.replace("www.", "")
    slug = carte.get(host)
    if not slug:
        return {"statut": "hors-perimetre", "motif": f"{host} absent de gsc-simcity"}
    if slug not in rows_cache:
        rows_cache[slug] = lignes(slug)
    rows = rows_cache[slug]
    if not rows:
        return {"statut": "sans-donnee", "motif": f"aucune ligne date x page pour {slug}"}

    d0 = datetime.fromisoformat(publie).date()
    fin_dispo = max((r["keys"][0] for r in rows if r.get("keys")), default=None)
    out = {"statut": "en-cours", "slug": slug, "donnee_jusquau": fin_dispo}

    out["avant"] = agrege(rows, url, str(d0 - timedelta(days=30)), str(d0 - timedelta(days=1)))
    for jalon, n in (("j30", 30), ("j90", 90)):
        d_fin = d0 + timedelta(days=n)
        if fin_dispo and str(d_fin) > fin_dispo:
            out[jalon] = {"statut": "pas-encore", "echeance": str(d_fin)}
            continue
        out[jalon] = agrege(rows, url, str(d0), str(d_fin))
        out[jalon]["statut"] = "mesure"

    j30 = out.get("j30", {})
    if j30.get("statut") == "mesure":
        if j30["impressions"] == 0:
            out["statut"] = "nulle"          # publiée, jamais servie
        elif j30["impressions"] < 30:
            out["statut"] = "bruitee"        # volume trop faible pour trancher
        else:
            out["statut"] = "mesuree"
    return out


ORDRE = {"nulle": 0, "mesuree": 1, "bruitee": 2, "en-cours": 3, "hors-perimetre": 4}


def ecrire_markdown(resultats, chemin):
    """Tableau des jalons, les cas qui parlent en premier."""
    resultats = sorted(resultats, key=lambda r: (ORDRE.get(r["statut"], 9), r["publie"]))
    lignes = [
        "---", "type: register", "title: Jalons des publications (auto)",
        "tags: [apprentissage, preuves, gsc, jalons]", "status: auto-generated", "---", "",
        "# Jalons des publications", "",
        "> Généré par `.claude/bin/apprentissage-gsc.py` depuis les publications vérifiées et la donnée",
        "> GSC de `gsc-simcity`. Aucune valeur estimée : une case vide est une donnée absente.",
        "",
        "- `nulle` : mise en ligne prouvée, zéro impression à J+30 sur la propriété GSC.",
        "- `mesuree` : au moins 30 impressions à J+30, lisible.",
        "- `bruitee` : servie, volume trop faible pour trancher.",
        "- `en-cours` : échéance non atteinte, ou donnée GSC pas encore à jour.",
        "- `hors-perimetre` : domaine absent de gsc-simcity.",
        "",
        "| Statut | Publié le | URL | Avant (30 j) | J+30 | J+90 |",
        "|---|---|---|---|---|---|",
    ]

    def cell(m):
        if not m:
            return "—"
        if m.get("statut") == "pas-encore":
            return f"échéance {m['echeance']}"
        pos = f", pos {m['position']}" if m.get("position") else ""
        return f"{m.get('clics', 0)} clics / {m.get('impressions', 0)} imp{pos}"

    for r in resultats:
        url = r["url"]
        court = url.replace("https://", "").replace("http://", "")
        lignes.append(
            f"| `{r['statut']}` | {r['publie']} | [{court[:60]}]({url}) | "
            f"{cell(r.get('avant'))} | {cell(r.get('j30'))} | {cell(r.get('j90'))} |"
        )

    compte = {}
    for r in resultats:
        compte[r["statut"]] = compte.get(r["statut"], 0) + 1
    lignes += ["", "## Compte", ""]
    lignes += [f"- {k} : {v}" for k, v in sorted(compte.items(), key=lambda kv: ORDRE.get(kv[0], 9))]
    lignes += ["", "Pages liées : [[apprentissage/retroactif]] · [[preuves/index]] · [[hypotheses]]"]

    os.makedirs(os.path.dirname(os.path.abspath(chemin)), exist_ok=True)
    with open(chemin, "w") as f:
        f.write("\n".join(lignes) + "\n")


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--registre")
    a.add_argument("--url")
    a.add_argument("--publie")
    a.add_argument("--out")
    a.add_argument("--markdown", help="écrit aussi le tableau markdown à ce chemin")
    a.add_argument("--verified", default=str(Path(__file__).resolve().parents[2] / "wiki/apprentissage/publications-verifiees.json"))
    a.add_argument("--rejected", default=str(Path(__file__).resolve().parents[2] / "wiki/apprentissage/publications-refusees.json"))
    a = a.parse_args()

    carte, cache = carte_sites(), {}

    if a.url:
        print(json.dumps(resoudre(a.url, a.publie, cache, carte), ensure_ascii=False, indent=2))
        return

    if not a.registre or not os.path.isfile(a.registre):
        print("registre introuvable", file=sys.stderr)
        sys.exit(1)

    spec = importlib.util.spec_from_file_location("apprentissage_preuves", Path(__file__).with_name("apprentissage-preuves.py"))
    gate = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gate)
    projection = gate.project(a.registre)
    Path(a.verified).write_text(json.dumps(projection["verified"], ensure_ascii=False, indent=2) + "\n")
    Path(a.rejected).write_text(json.dumps({"events": projection["rejected"], "stats": projection["stats"]}, ensure_ascii=False, indent=2) + "\n")
    resultats = []
    for e in projection["verified"]:
        r = resoudre(e["url"], e["publie"], cache, carte)
        r.update({"event_id": e["event_id"], "url": e["url"], "publie": e["publie"],
                  "site_id": e["site_id"], "evidence": e["evidence"]})
        resultats.append(r)

    if a.markdown:
        ecrire_markdown(resultats, a.markdown)

    txt = json.dumps(resultats, ensure_ascii=False, indent=2)
    if a.out:
        open(a.out, "w").write(txt)
        print(f"{len(resultats)} URL résolues -> {a.out}", file=sys.stderr)
    else:
        print(txt)


if __name__ == "__main__":
    main()
