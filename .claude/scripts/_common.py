"""Helpers partagés entre les scripts d'indexation du vault."""
from __future__ import annotations

import re
from pathlib import Path
from typing import Iterator

import yaml

VAULT_ROOT = Path(__file__).resolve().parents[2]
INDEX_DIR = VAULT_ROOT / ".claude" / "index"
VECTOR_STORE = VAULT_ROOT / ".claude" / "vector-store"

WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
H2_RE = re.compile(r"^##\s+", re.MULTILINE)

# Liste BLANCHE des zones indexables. Volontairement une liste blanche et pas une
# liste noire : avec une liste noire, tout nouveau dossier créé à la racine du repo
# entrait dans l'index sans que personne ne l'ait décidé. C'est comme ça que
# agent-synthetic/ (mémoire opérationnelle de SyntheticBrain) s'est mis à peser 27 %
# de l'index et à sortir en position 1 sur des requêtes de doctrine.
# Ajouter un dossier ici est une décision explicite. Cf. §3 AGENTS.md : le vault,
# c'est raw/ + wiki/, le reste du repo est de l'outillage.
INDEXED_ROOTS = {
    "raw",
    "wiki",
}

# Exclusions à l'intérieur des zones indexables.
SKIP_DIRS = {
    "raw/revue-de-presse",
    "wiki/pilotage/projets",  # archives du pilotage annulé, pas de doctrine à multiplier
}


def iter_markdown(root: Path = VAULT_ROOT) -> Iterator[Path]:
    """Yield all .md files under root, limited to INDEXED_ROOTS, minus SKIP_DIRS.

    Note : le filtre INDEXED_ROOTS ne s'applique que quand on parcourt la racine du
    vault. Appelé sur un sous-dossier (root != VAULT_ROOT), on parcourt tout ce
    sous-dossier, seul SKIP_DIRS s'applique.
    """
    at_vault_root = root.resolve() == VAULT_ROOT.resolve()
    for path in root.rglob("*.md"):
        rel = path.relative_to(root).as_posix()
        if at_vault_root and rel.split("/")[0] not in INDEXED_ROOTS:
            continue
        if any(rel == d or rel.startswith(d + "/") for d in SKIP_DIRS):
            continue
        yield path


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Return (frontmatter_dict, body). Empty dict if no frontmatter."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    try:
        data = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        data = {}
    body = text[m.end():]
    return data if isinstance(data, dict) else {}, body


def slug_from_path(path: Path) -> str:
    """wiki/concepts/aeo.md -> aeo"""
    return path.stem


def extract_wikilinks(body: str) -> list[str]:
    """Return slugs of [[wikilinks]] found in body."""
    out = []
    seen = set()
    for m in WIKILINK_RE.finditer(body):
        target = m.group(1).strip()
        slug = target.split("/")[-1]
        if slug not in seen:
            seen.add(slug)
            out.append(slug)
    return out


def read_markdown(path: Path) -> tuple[dict, str]:
    """Read file, return (frontmatter, body)."""
    text = path.read_text(encoding="utf-8", errors="replace")
    return parse_frontmatter(text)
