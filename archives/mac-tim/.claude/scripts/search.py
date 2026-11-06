"""CLI de recherche sur le vault — combine filtre déterministe + recherche vectorielle.

Usage :
  search.py "agentic search ranking"
  search.py "passage ranking" --k 8
  search.py "RRF" --type concept
  search.py "GSC" --source-type gsc-export
  search.py "anti-AI writing" --tag doctrine-tim

Output : pour chaque hit : chemin + score + extrait + section.
"""
from __future__ import annotations

import argparse
import json
import sys
import textwrap
import warnings
import re
from pathlib import Path

warnings.filterwarnings("ignore")

from _common import VECTOR_STORE, INDEX_DIR, VAULT_ROOT

COLLECTION_NAME = "seo_kb"
MODEL_NAME = "paraphrase-multilingual-mpnet-base-v2"


def lexical_fallback(query: str, k: int, filters: dict) -> list[dict]:
    """Recherche locale de secours quand le modèle n'est pas installé.

    Le vault reste consultable hors réseau : ce fallback ne remplace pas le
    classement vectoriel, mais évite qu'une dépendance Hugging Face bloque tout.
    """
    from _common import iter_markdown, parse_frontmatter

    terms = [t for t in re.findall(r"[\wàâçéèêëîïôûùüÿñæœ-]+", query.lower()) if len(t) > 1]
    if not terms:
        return []
    hits = []
    for path in iter_markdown():
        text = path.read_text(encoding="utf-8", errors="replace")
        fm, body = parse_frontmatter(text)
        if filters.get("type") and fm.get("type") != filters["type"]:
            continue
        if filters.get("source_type") and fm.get("source_type") != filters["source_type"]:
            continue
        haystack = (fm.get("title", "") + "\n" + body).lower()
        score = sum(haystack.count(term) for term in terms)
        if not score:
            continue
        first = min((haystack.find(term) for term in terms if term in haystack), default=0)
        excerpt = re.sub(r"\s+", " ", body[max(0, first - 120):first + 380]).strip()
        hits.append({
            "path": path.relative_to(VAULT_ROOT).as_posix(),
            "title": fm.get("title") or path.stem,
            "section": "fallback lexical local",
            "type": fm.get("type"),
            "tags": ", ".join(fm.get("tags") or []),
            "score": score,
            "excerpt": excerpt,
        })
    return sorted(hits, key=lambda h: (-h["score"], h["path"]))[:k]


def load_concepts_alias_hit(query: str) -> list[dict]:
    """Si la query matche exactement un slug ou alias de concepts.json, on remonte ce hit en tête."""
    concepts_path = INDEX_DIR / "concepts.json"
    if not concepts_path.exists():
        return []
    nodes = json.loads(concepts_path.read_text())
    q = query.strip().lower()
    hits = []
    for slug, node in nodes.items():
        candidates = {slug.lower(), node.get("title", "").lower()}
        for alias in node.get("aliases", []):
            candidates.add(str(alias).lower())
        if q in candidates:
            hits.append({
                "path": node["file"],
                "title": node.get("title"),
                "type": node.get("type"),
                "kind": "exact-concept-match",
                "backrefs": len(node.get("backrefs", [])),
            })
    return hits


def build_where(filters: dict) -> dict | None:
    """ChromaDB n'accepte qu'un $and au top level avec >=2 clauses."""
    clauses = []
    for k, v in filters.items():
        if v is not None:
            clauses.append({k: v})
    if not clauses:
        return None
    if len(clauses) == 1:
        return clauses[0]
    return {"$and": clauses}


def main() -> int:
    ap = argparse.ArgumentParser(description="Recherche sémantique sur le vault")
    ap.add_argument("query", help="La requête (en français ou anglais)")
    ap.add_argument("--k", type=int, default=5, help="Nombre de résultats (default 5)")
    ap.add_argument("--type", help="Filtre frontmatter type=...")
    ap.add_argument("--source-type", dest="source_type", help="Filtre source_type=...")
    ap.add_argument("--tag", help="Filtre tag (contient)")
    ap.add_argument("--json", action="store_true", help="Output JSON brut")
    args = ap.parse_args()

    from sentence_transformers import SentenceTransformer
    import chromadb

    client = chromadb.PersistentClient(path=str(VECTOR_STORE))
    try:
        collection = client.get_collection(COLLECTION_NAME)
    except Exception:
        print(f"Collection {COLLECTION_NAME} introuvable. Lance d'abord: ./kb rebuild", file=sys.stderr)
        return 1

    where = build_where({
        "type": args.type,
        "source_type": args.source_type,
    })

    try:
        # Ne jamais déclencher un téléchargement implicite durant une recherche.
        model = SentenceTransformer(MODEL_NAME, local_files_only=True)
        embedding = model.encode([args.query], normalize_embeddings=True).tolist()[0]
        results = collection.query(
            query_embeddings=[embedding],
            n_results=args.k * 3 if args.tag else args.k,
            where=where,
        )
    except Exception as exc:
        print(f"[kb] modèle vectoriel local indisponible ({exc.__class__.__name__}) ; fallback lexical local.", file=sys.stderr)
        hits = lexical_fallback(args.query, args.k, {"type": args.type, "source_type": args.source_type})
        if args.tag:
            hits = [h for h in hits if args.tag.lower() in (h.get("tags") or "").lower()]
        results = {"documents": [[]], "metadatas": [[]], "distances": [[]]}

    docs = results.get("documents", [[]])[0]
    metas = results.get("metadatas", [[]])[0]
    dists = results.get("distances", [[]])[0]

    hits = locals().get("hits", [])
    for doc, meta, dist in zip(docs, metas, dists):
        if args.tag and args.tag.lower() not in (meta.get("tags") or "").lower():
            continue
        hits.append({
            "path": meta.get("path"),
            "title": meta.get("title"),
            "section": meta.get("section"),
            "type": meta.get("type"),
            "tags": meta.get("tags"),
            "score": round(1 - dist, 4),
            "excerpt": doc[:400],
        })
        if len(hits) >= args.k:
            break

    exact = load_concepts_alias_hit(args.query)
    concept_backrefs = []
    if exact:
        concepts_path = INDEX_DIR / "concepts.json"
        nodes = json.loads(concepts_path.read_text())
        for h in exact:
            slug = Path(h["path"]).stem
            node = nodes.get(slug, {})
            concept_backrefs.extend(node.get("backrefs", [])[:5])

    if args.json:
        print(json.dumps(
            {"exact": exact, "backrefs": concept_backrefs, "hits": hits},
            ensure_ascii=False, indent=2,
        ))
        return 0

    if exact:
        print("=== Exact concept/entity match ===")
        for h in exact:
            print(f"  [{h['type']}] {h['title']} ({h['backrefs']} backrefs)")
            print(f"    -> {h['path']}")
        if concept_backrefs:
            print("  Top backrefs (graphe direct) :")
            for ref in concept_backrefs[:5]:
                print(f"    -> {ref}")
        print()

    print(f"=== Top {len(hits)} hits sémantiques pour: {args.query!r} ===\n")
    for i, h in enumerate(hits, 1):
        print(f"{i}. [{h['score']:.3f}] {h['title']}  §{h['section']}")
        print(f"   {h['path']}  ({h['type']})")
        wrapped = textwrap.fill(h["excerpt"].replace("\n", " "), width=90,
                                initial_indent="   > ", subsequent_indent="   > ")
        print(wrapped)
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
