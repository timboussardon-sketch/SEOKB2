"""Ledger de la boucle Jev : append-only, une ligne par verdict, capture_mode natif."""
import json
import os
from datetime import datetime, timezone
from pathlib import Path


def _brain():
    """Où écrire les verdicts, les notes et la calibration.

    Jamais dans le dossier des scripts quand celui-ci vient d'un pack : ce dossier
    est un submodule git, et une mise à jour emporterait le travail de l'utilisateur.

    1. JEV_HOME, s'il est posé.
    2. Le dossier loops/jev voisin des scripts, s'il existe déjà (vault de travail).
    3. ~/.claude/jev, hors du dossier des skills, donc épargné par les mises à jour.
    """
    if os.environ.get("JEV_HOME"):
        return Path(os.environ["JEV_HOME"]).expanduser()
    voisin = Path(__file__).resolve().parents[1] / "loops" / "jev"
    if voisin.exists():
        return voisin
    return Path.home() / ".claude" / "jev"


BRAIN = _brain()


def ecrire(nom, ligne):
    ligne = {"ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
             "capture_mode": "native", **ligne}
    if nom in ("verdicts", "runs"):
        from jev.client import MODELE
        ligne.setdefault("modele", MODELE)
    f = BRAIN / "ledgers" / f"{nom}.jsonl"
    f.parent.mkdir(parents=True, exist_ok=True)
    with f.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(ligne, ensure_ascii=False) + "\n")
    return ligne


def lire(nom):
    f = BRAIN / "ledgers" / f"{nom}.jsonl"
    if not f.exists():
        return []
    return [json.loads(l) for l in f.read_text(encoding="utf-8").splitlines() if l.strip()]
