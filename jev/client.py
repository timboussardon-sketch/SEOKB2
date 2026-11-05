"""Client Jev (TypeSafe System One). Clé lue dans seo-kb/.env.local, jamais copiée.

Un appel = un état + des questions typées (score à N niveaux, choice) ; la réponse
porte un choix, un score et une confiance. On classe, on ne génère pas.
"""
import json
import os
import time
import urllib.request
from pathlib import Path

ENV = Path(__file__).resolve().parents[1] / ".env.local"
URL = "https://api.typesafe.ai/v1/systemone"
# Version fixée : les seuils de calibration valent pour un modèle, pas pour « jev-latest »
# qui peut changer sans prévenir. Changer de version = recalibrer (jev/calibrer.py).
MODELE = os.environ.get("JEV_MODEL", "jev-1.13.0")


def cle():
    if os.environ.get("JEV_API_KEY"):
        return os.environ["JEV_API_KEY"]
    try:
        for ligne in ENV.read_text(encoding="utf-8").splitlines():
            if ligne.startswith("JEV_API_KEY="):
                return ligne.split("=", 1)[1].strip().strip('"')
    except OSError:
        pass
    return None


def demander(state, questions, timeout=25, essais=2):
    """Rend (answers, ms, erreur). answers vaut None en cas d'échec."""
    k = cle()
    if not k:
        return None, 0, "clé JEV absente (seo-kb/.env.local)"
    corps = json.dumps({"state": state, "model": MODELE, "questions": questions}).encode()
    err = None
    debut = time.time()
    for _ in range(essais):
        req = urllib.request.Request(URL, data=corps, method="POST", headers={
            "Authorization": f"Bearer {k}", "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                data = json.loads(resp.read().decode())
            ms = int((time.time() - debut) * 1000)
            if data.get("model") != MODELE:
                return None, ms, f"modèle servi {data.get('model')} ≠ modèle fixé {MODELE}"
            return data.get("answers") or {}, ms, None
        except Exception as exc:  # noqa: BLE001
            err = str(exc)[:160]
            time.sleep(0.5)
    return None, int((time.time() - debut) * 1000), err


def choix(answers, nom):
    a = (answers or {}).get(nom) or {}
    return a.get("choice"), round(float(a.get("confidence") or 0), 2), a.get("probabilities") or {}


def score(answers, nom, niveaux):
    """Score 0..niveaux-1 ramené sur 100, plus confiance."""
    a = (answers or {}).get(nom) or {}
    s = a.get("score")
    if s is None:
        return None, 0.0
    return int(round(float(s) / (niveaux - 1) * 100)), round(float(a.get("confidence") or 0), 2)
