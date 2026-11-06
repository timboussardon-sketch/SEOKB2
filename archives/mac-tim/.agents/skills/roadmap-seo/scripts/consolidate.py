#!/usr/bin/env python3
"""Vérifie N stratégies mot-clé validées avant une roadmap SEO commune."""

import argparse
import hashlib
import importlib.util
import json
import re
import sys
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

STRATEGY_PATH = Path(__file__).resolve().parents[2] / "strategie-mot-cle" / "scripts" / "workflow.py"
SPEC = importlib.util.spec_from_file_location("keyword_strategy_workflow", STRATEGY_PATH)
STRATEGY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(STRATEGY)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def normalized(value):
    require(isinstance(value, str) and value.strip(), "mot-clé manquant")
    text = unicodedata.normalize("NFKD", value)
    text = "".join(char for char in text if not unicodedata.combining(char))
    return re.sub(r"\W+", " ", text.casefold()).strip()


def in_vault(vault, value):
    require(isinstance(value, str) and value.strip(), "chemin manquant")
    require(not Path(value).is_absolute(), f"chemin absolu interdit : {value}")
    path = (vault / value).resolve()
    require(path.is_relative_to(vault), f"chemin hors coffre : {value}")
    return path


def read_manifest(vault, path):
    require(path.resolve().is_relative_to(vault), "manifeste hors coffre")
    manifest = json.loads(path.read_text())
    require(isinstance(manifest, dict), "manifeste invalide")
    require(isinstance(manifest.get("site"), str) and manifest["site"].strip(), "site manquant")
    entries = manifest.get("keywords")
    require(isinstance(entries, list) and entries, "liste des mots-clés requise")
    keywords, states = set(), set()
    for entry in entries:
        require(isinstance(entry, dict), "entrée de mot-clé invalide")
        key = normalized(entry.get("keyword"))
        require(key not in keywords, f"mot-clé dupliqué : {entry['keyword']}")
        keywords.add(key)
        state_path = in_vault(vault, entry.get("state"))
        require(state_path not in states, "un état de stratégie doit être propre à un mot-clé")
        states.add(state_path)
    bundle = in_vault(vault, manifest.get("bundle"))
    roadmap = in_vault(vault, manifest.get("roadmap"))
    require(bundle.suffix == ".json" and roadmap.suffix == ".md", "sorties attendues : dossier JSON et roadmap Markdown")
    require(bundle not in states and roadmap not in states and bundle != path.resolve() and roadmap != path.resolve(), "sortie en conflit avec une source")
    tracking = roadmap.with_suffix(".json")
    require(tracking not in states and tracking not in {bundle, path.resolve()}, "état de suivi en conflit avec une source")
    require(bundle.is_relative_to(vault / "wiki") and roadmap.is_relative_to(vault / "wiki"), "sorties à conserver dans wiki/")
    return manifest


def checked_state(vault, entry):
    path = in_vault(vault, entry["state"])
    raw = path.read_bytes()
    state = json.loads(raw)
    require(isinstance(state, dict), "état de stratégie invalide")
    require(Path(state.get("vault", "")).resolve() == vault, "stratégie d'un autre coffre")
    require(normalized(state.get("keyword")) == normalized(entry["keyword"]), "mot-clé de la stratégie différent du portefeuille")
    for phase in (1, 2, 3):
        require(state.get("outputs", {}).get(str(phase)), f"étape {phase} absente")
        require(state.get("approvals", {}).get(str(phase)) is True, f"étape {phase} non validée")
        require(any(item.get("phase") == phase and isinstance(item.get("message"), str) and item["message"].strip()
                    for item in state.get("history", [])), f"accord de l'étape {phase} sans trace")
        STRATEGY.validate_output(state, phase, state["outputs"][str(phase)])
    for phase, names in ((1, ("micro_intentions", "micro_intentions_tool")), (2, ("geo_citations",))):
        for name in names:
            method = state.get("methods", {}).get(name, {})
            require(isinstance(method.get("path"), str) and method["path"].strip(), f"source de méthode absente : {name}")
            digest = method.get("sha256")
            require(isinstance(digest, str) and re.fullmatch(r"[0-9a-f]{64}", digest), f"version de méthode absente : {name}")
            require(state.get("loaded_methods", {}).get(str(phase), {}).get(name) == digest, f"méthode non chargée : {name}")
    return {"keyword": entry["keyword"], "state": entry["state"], "sha256": hashlib.sha256(raw).hexdigest(),
            "methods": state["methods"], "outputs": state["outputs"], "approvals": state["approvals"], "history": state["history"]}


def inspect(vault, manifest):
    results, snapshots = [], []
    for entry in manifest["keywords"]:
        try:
            snapshot = checked_state(vault, entry)
            snapshots.append(snapshot)
            results.append({"keyword": entry["keyword"], "status": "validated", "state": entry["state"]})
        except (ValueError, OSError, TypeError, KeyError, AttributeError) as error:
            results.append({"keyword": entry["keyword"], "status": "blocked", "state": entry["state"], "reason": str(error)})
    return {"site": manifest["site"], "expected": len(results), "validated": len(snapshots),
            "ready": len(results) == len(snapshots), "roadmap": manifest["roadmap"], "strategies": results}, snapshots


def bundle(vault, manifest):
    report, snapshots = inspect(vault, manifest)
    blocked = [f"{item['keyword']} : {item['reason']}" for item in report["strategies"] if item["status"] == "blocked"]
    require(report["ready"], "consolidation bloquée — " + "; ".join(blocked))
    for snapshot in snapshots:
        current = in_vault(vault, snapshot["state"]).read_bytes()
        require(hashlib.sha256(current).hexdigest() == snapshot["sha256"], "stratégie modifiée pendant la consolidation : relancer le contrôle")
    output = in_vault(vault, manifest["bundle"])
    if output.exists():
        previous = json.loads(output.read_text())
        previous_sources = [(item["keyword"], item["state"], item["sha256"]) for item in previous["strategies"]]
        current_sources = [(item["keyword"], item["state"], item["sha256"]) for item in snapshots]
        require(previous.get("site") == manifest["site"] and previous.get("roadmap") == manifest["roadmap"] and previous_sources == current_sources,
                "dossier source déjà existant : utiliser un chemin de nouvelle révision pour conserver l'historique")
        return output
    output.parent.mkdir(parents=True, exist_ok=True)
    data = {"site": manifest["site"], "vault": str(vault), "created_at": datetime.now(timezone.utc).isoformat(),
            "strategy_count": len(snapshots), "roadmap": manifest["roadmap"], "strategies": snapshots}
    output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    return output


def run(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("check", "bundle"))
    parser.add_argument("--vault", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    args = parser.parse_args(argv)
    vault = args.vault.resolve()
    require(vault.is_dir(), "coffre absent")
    path = args.manifest if args.manifest.is_absolute() else vault / args.manifest
    manifest = read_manifest(vault, path)
    if args.command == "check":
        report, _ = inspect(vault, manifest)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0 if report["ready"] else 2
    print(bundle(vault, manifest))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(run())
    except (ValueError, OSError, TypeError, KeyError) as exc:
        print(f"ERREUR : {exc}", file=sys.stderr)
        sys.exit(1)
