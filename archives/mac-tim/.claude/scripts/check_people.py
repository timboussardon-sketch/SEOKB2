#!/usr/bin/env python3
"""check_people — transcripts de raw/transcripts/ sans fiche people (wiki/entities/) ni fiche source.

Usage : check_people.py [--json]
Sortie : une ligne par transcript en défaut. Exit 1 s'il en reste, 0 sinon.
Un transcript est « couvert » quand son slug (nom de fichier sans .md) est cité
dans au moins une fiche wiki/entities/*.md ET une fiche wiki/sources/*.md.
Les vidéos (video-*.md) ne sont pas des calls : ignorées.
"""
import json, os, sys, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "raw" / "transcripts"
ENT = ROOT / "wiki" / "entities"
SRC = ROOT / "wiki" / "sources"

def corpus(d):
    out = {}
    for p in d.glob("*.md"):
        out[p.name] = p.read_text(errors="ignore")
    return out

ents, srcs = corpus(ENT), corpus(SRC)
gaps = []
for t in sorted(RAW.glob("*.md")):
    if t.name.startswith("video-"):
        continue
    slug = t.stem
    in_ent = [n for n, c in ents.items() if slug in c]
    in_src = [n for n, c in srcs.items() if slug in c]
    if not in_ent or not in_src:
        gaps.append({"transcript": f"raw/transcripts/{t.name}",
                     "fiche_people": bool(in_ent), "fiche_source": bool(in_src)})

if "--json" in sys.argv:
    print(json.dumps(gaps, ensure_ascii=False))
else:
    if not gaps:
        print("[people] OK — tous les transcripts ont leur fiche people et leur fiche source.")
    for g in gaps:
        miss = [k for k in ("fiche_people", "fiche_source") if not g[k]]
        print(f"[people] MANQUE {' + '.join(miss)} : {g['transcript']}")
sys.exit(1 if gaps else 0)
