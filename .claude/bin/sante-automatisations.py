#!/usr/bin/env python3
"""
Santé des automatisations du vault.

Le symptôme d'un cron mort n'est pas une erreur : c'est un fichier qui cesse d'être
écrit. Ce script lit la date DANS LE NOM du dernier fichier produit par chaque
automatisation (jamais la date de modification, qu'un commit suffit à rafraîchir),
la compare à la cadence attendue, et écrit le verdict dans le vault.

Sortie : wiki/ops/sante-automatisations.md (chemin stable, réécrit à chaque passage).
Code de retour : 1 si au moins une automatisation est en panne.

Usage : python3 .claude/bin/sante-automatisations.py [--silencieux]
"""
import argparse, glob, json, os, re, subprocess, sys
from datetime import date, datetime, timedelta

VAULT = os.path.expanduser("~/Code/seo-kb")
SORTIE = os.path.join(VAULT, "wiki/ops/sante-automatisations.md")
RUNNERS = os.path.expanduser("~/.local/bin/seo-kb")
AGENTS = os.path.expanduser("~/Library/LaunchAgents")
GSC = os.path.expanduser("~/Code/gsc-simcity/data")

# (libellé, job launchd, motif de sortie, cadence en jours, tolérance en jours)
# La tolérance est volontairement large : on veut détecter une panne, pas un décalage.
SURVEILLE = [
    ("Journal quotidien",      "com.timboussardon.recap-jour",       "raw/journal/*.md",                        1,  1),
    ("Revue de presse",        "com.timboussardon.revue-presse",     "raw/revue-de-presse/*.md",                1,  1),
    ("Apprentissage",          "com.tim.apprentissage",              "wiki/apprentissage/2*.md",                1,  1),
    ("Dashboard du vault",     "com.timboussardon.dashboard",        "@mtime:wiki/dashboard.md",                1,  1),
    ("Revue hebdo",            "com.timboussardon.revue-hebdo",      "wiki/revue-hebdo/2*-W*.md",               7, 10),
    ("Résurgence",             "com.timboussardon.resurgence",       "wiki/revue-hebdo/resurgence-*.md",        7, 10),
    ("Pôle marketing",         "com.tim.marketing-hebdo",            "organikk/marketing/passages/2*.md",       7, 10),
    ("Santé du site",          "com.tim.health-automations",         "wiki/ops/health-*.md",                    7, 10),
    ("Récap Algorithme",       "com.tim.algorithme-recap",           "wiki/syntheses/algorithme-week-*.md",     7, 12),
    ("Backlog d'ingestion",    "com.timboussardon.ingest-backlog",   "@mtime:wiki/ingest-backlog.md",           7, 10),
    ("Audit du vault",         "com.tim.audit-vault",                "wiki/audit/*.md",                         7, 12),
    ("Contrôle d'indexation",  "com.tim.indexation-check",           "reports/indexation-*.md",                30, 38),
    ("Validation hypothèses",  "com.timboussardon.hypotheses-validation", "@mtime:wiki/hypotheses.md",         30, 38),
    # Hors vault : chemin absolu (os.path.join l'emporte sur VAULT). etat.md est réécrit à chaque passage.
    ("Moteur stopclope.co",    "com.tim.moteur-stopclope",           "@mtime:/Users/timothee/Code/stopclope-v2/moteur/etat.md", 7, 10),
]

MOIS_ISO = re.compile(r"(\d{4})-(\d{2})-(\d{2})")
SEMAINE_ISO = re.compile(r"(\d{4})-W(\d{2})")


def date_du_nom(chemin):
    """Date portée par le nom du fichier. None si le nom n'en porte pas."""
    nom = os.path.basename(chemin)
    m = MOIS_ISO.search(nom)
    if m:
        try:
            return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        except ValueError:
            return None
    m = SEMAINE_ISO.search(nom)
    if m:
        try:
            return date.fromisocalendar(int(m.group(1)), int(m.group(2)), 7)
        except ValueError:
            return None
    return None


def derniere_sortie(motif):
    """(date de la dernière sortie, nom, méthode). Méthode 'nom' ou 'mtime'."""
    if motif.startswith("@mtime:"):
        p = os.path.join(VAULT, motif[7:])
        if not os.path.isfile(p):
            return None, None, "mtime"
        return date.fromtimestamp(os.path.getmtime(p)), os.path.basename(p), "mtime"
    fichiers = glob.glob(os.path.join(VAULT, motif))
    dates = [(date_du_nom(f), os.path.basename(f)) for f in fichiers]
    dates = [(d, n) for d, n in dates if d]
    if not dates:
        return None, None, "nom"
    d, n = max(dates, key=lambda x: x[0])
    return d, n, "nom"


def jobs_charges():
    try:
        out = subprocess.run(["launchctl", "list"], capture_output=True, text=True, timeout=20).stdout
    except Exception:
        return set()
    return {l.split("\t")[-1] for l in out.splitlines() if "\t" in l}


def fraicheur_gsc():
    """La donnée GSC alimente toutes les boucles de mesure. Si elle gèle, elles sont aveugles."""
    p = os.path.join(GSC, "organikk", "gsc-brut.json")
    if not os.path.isfile(p):
        return None, None
    try:
        with open(p) as f:
            d = json.load(f)
        recup = datetime.fromisoformat(d["recupereLe"].replace("Z", "+00:00")).date()
        return recup, d.get("fin")
    except Exception:
        return None, None


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--silencieux", action="store_true")
    a = a.parse_args()

    auj = date.today()
    charges = jobs_charges()
    lignes, pannes, retards = [], [], []

    for libelle, job, motif, cadence, tol in SURVEILLE:
        d, nom, methode = derniere_sortie(motif)
        runner_ok = any(os.path.isfile(os.path.join(RUNNERS, f)) for f in os.listdir(RUNNERS)) if os.path.isdir(RUNNERS) else False
        plist_ok = os.path.isfile(os.path.join(AGENTS, job + ".plist"))
        charge = job in charges

        if d is None:
            etat, retard = "jamais produit", None
            pannes.append((libelle, "aucune sortie trouvée"))
        else:
            retard = (auj - d).days
            if retard > tol + cadence:
                etat = "en panne"
                pannes.append((libelle, f"rien depuis le {d} ({retard} j, cadence {cadence} j)"))
            elif retard > tol:
                etat = "en retard"
                retards.append((libelle, f"dernier le {d} ({retard} j, cadence {cadence} j)"))
            else:
                etat = "à jour"

        alerte = []
        if not plist_ok:
            alerte.append("plist absent")
            pannes.append((libelle, "plist absent"))
        elif not charge:
            alerte.append("job non chargé")
            pannes.append((libelle, "job non chargé dans launchd"))

        lignes.append({
            "libelle": libelle, "job": job, "etat": etat,
            "dernier": str(d) if d else "—", "nom": nom or "—",
            "retard": retard, "cadence": cadence, "methode": methode,
            "alerte": ", ".join(alerte) or "—",
        })

    recup, fin = fraicheur_gsc()
    if recup is not None:
        age = (auj - recup).days
        if age > 3:
            pannes.append(("Donnée GSC", f"dernier import le {recup} ({age} j) : les boucles de mesure sont aveugles"))

    ordre = {"en panne": 0, "jamais produit": 1, "en retard": 2, "à jour": 3}
    lignes.sort(key=lambda l: (ordre.get(l["etat"], 9), l["libelle"]))

    out = [
        "---", "type: register", "title: Santé des automatisations",
        "aliases: [sante-automatisations, crons, heartbeat]",
        "tags: [meta, ops, automatisations, surveillance]",
        f"updated: {auj}", "status: auto-generated", "---", "",
        "# Santé des automatisations", "",
        "> Réécrit à chaque passage par `.claude/bin/sante-automatisations.py`, lancé avec la boucle",
        "> d'apprentissage. **Le critère est la date portée par le nom du dernier fichier produit**,",
        "> jamais sa date de modification : un commit suffit à rafraîchir un `mtime` et à faire passer",
        "> un cron mort pour vivant. Le 2026-09-09, quinze runners ont cessé de tourner sans rien dire",
        "> pendant deux jours ; c'est ce fichier qui doit rendre ce silence impossible.", "",
        f"**Relevé du {auj}.**", "",
    ]

    if pannes:
        out += ["## 🚨 En panne", ""]
        out += [f"- **{l}** — {m}" for l, m in pannes] + [""]
    else:
        out += ["## 🚨 En panne", "", "Rien. Toutes les automatisations surveillées produisent.", ""]

    if retards:
        out += ["## ⏳ En retard", ""] + [f"- **{l}** — {m}" for l, m in retards] + [""]

    out += ["## Relevé complet", "",
            "| État | Automatisation | Dernière sortie | Retard | Cadence | Contrôle | Anomalie |",
            "|---|---|---|---|---|---|---|"]
    for l in lignes:
        r = "—" if l["retard"] is None else f"{l['retard']} j"
        out.append(f"| `{l['etat']}` | {l['libelle']} | {l['nom']} | {r} | {l['cadence']} j | "
                   f"{'date du nom' if l['methode']=='nom' else 'date de modif'} | {l['alerte']} |")

    if recup is not None:
        out += ["", "## Donnée GSC", "",
                f"Dernier import `gsc-simcity` : **{recup}**, donnée disponible jusqu'au **{fin}**.",
                "Toutes les boucles de mesure lisent cette source. Si elle gèle, elles ne rendent",
                "plus de verdict, même quand elles tournent."]

    out += ["", "## Périmètre", "",
            "Ce relevé couvre les automatisations qui écrivent dans ce vault, plus la fraîcheur de la",
            "donnée GSC. Les automatisations qui produisent ailleurs (cockpits X et Reddit, brèves,",
            "prospection, SEO City) ne sont pas surveillées ici.", "",
            "Pages liées : [[apprentissage/retroactif]] · [[corrections-recurrentes]] · [[dashboard]]", ""]

    os.makedirs(os.path.dirname(SORTIE), exist_ok=True)
    with open(SORTIE, "w") as f:
        f.write("\n".join(out))

    if not a.silencieux:
        print(f"{len(lignes)} automatisations · {len(pannes)} en panne · {len(retards)} en retard -> {SORTIE}")
        for lib, m in pannes:
            print(f"  PANNE  {lib} : {m}")
    return 1 if pannes else 0


if __name__ == "__main__":
    sys.exit(main())
