"""Découpage et rapprochement lexical, sans modèle : phrases, passages, recouvrement."""
import json
import re
import unicodedata
from pathlib import Path

MOTS_VIDES = set("""le la les un une des du de d l au aux et ou en à a sur pour par avec sans dans
que qui quoi dont où ne pas plus est sont ce cet cette ces se sa son ses leur leurs il elle ils
elles on nous vous je tu y the of and to in is it for on as be or an at by from that this with
mais donc car ni si comme tout tous toute toutes très bien fait faire peut être avoir""".split())


def normaliser(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9 ]+", " ", s)


def termes(s):
    return {t for t in normaliser(s).split() if len(t) > 2 and t not in MOTS_VIDES}


def phrases(md):
    """Phrases d'un markdown, hors titres, code, front matter, tableaux et liens nus."""
    if md.startswith("---"):
        fin = md.find("\n---", 3)
        if fin > 0:
            md = md[fin + 4:]
    md = re.sub(r"```.*?```", " ", md, flags=re.S)
    out = []
    for bloc in re.split(r"\n\s*\n", md):
        bloc = bloc.strip()
        if not bloc or bloc.startswith("#") or bloc.startswith("|") or bloc.startswith("<"):
            continue
        bloc = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", bloc)
        bloc = re.sub(r"^[-*>]\s+", "", bloc, flags=re.M)
        bloc = re.sub(r"\s+", " ", bloc)
        for ph in re.split(r"(?<=[.!?])\s+(?=[A-ZÀ-Ý«\"0-9])", bloc):
            ph = ph.strip()
            if len(termes(ph)) >= 3:
                out.append(ph)
    return out


def charger_corpus(chemins, taille=600):
    """Passages du corpus : fichiers .md/.txt (découpés par paragraphe) et .json
    (chaque chaîne de plus de 40 caractères, quel que soit le schéma)."""
    passages = []

    def ajouter(src, texte):
        texte = re.sub(r"\s+", " ", str(texte)).strip()
        if len(texte) < 40:
            return
        for i in range(0, len(texte), taille):
            passages.append({"source": src, "texte": texte[i:i + taille]})

    def parcourir_json(src, obj):
        if isinstance(obj, str):
            ajouter(src, obj)
        elif isinstance(obj, dict):
            for v in obj.values():
                parcourir_json(src, v)
        elif isinstance(obj, list):
            for v in obj:
                parcourir_json(src, v)

    fichiers = []
    for c in chemins:
        p = Path(c).expanduser()
        fichiers += sorted(p.rglob("*")) if p.is_dir() else [p]
    for f in fichiers:
        if not f.is_file():
            continue
        src = str(f)
        try:
            if f.suffix == ".json":
                parcourir_json(src, json.loads(f.read_text(encoding="utf-8")))
            elif f.suffix in (".md", ".txt", ".csv", ".jsonl"):
                for para in re.split(r"\n\s*\n", f.read_text(encoding="utf-8", errors="ignore")):
                    ajouter(src, para)
        except (OSError, ValueError):
            continue
    for p in passages:
        p["termes"] = termes(p["texte"])
    return passages


def plus_proches(phrase, passages, k=5):
    t = termes(phrase)
    if not t:
        return []
    notes = []
    for p in passages:
        commun = len(t & p["termes"])
        if commun:
            notes.append((commun / (len(t) ** 0.5), p))
    notes.sort(key=lambda x: -x[0])
    return [p for _, p in notes[:k]]
