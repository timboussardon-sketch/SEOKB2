#!/usr/bin/env python3
"""Proposer, valider et suivre une roadmap issue des stratégies validées."""

import argparse
import hashlib
import importlib.util
import json
import re
import sys
from datetime import date, datetime, timezone
from pathlib import Path

SPEC = importlib.util.spec_from_file_location("roadmap_sources", Path(__file__).with_name("consolidate.py"))
SOURCES = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SOURCES)
require = SOURCES.require
STATUS_LABELS = {"todo": "À faire", "in_progress": "En cours", "blocked": "Bloquée", "review": "À valider", "done": "Terminée"}
KINDS = {"collecte", "arbitrage", "contenu", "technique", "maillage", "mesure"}


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True).encode()).hexdigest()


def nonempty(value, message):
    require(isinstance(value, str) and value.strip(), message)


def now():
    return datetime.now(timezone.utc).isoformat()


def validate_plan(plan, bundle):
    for field in ("objective", "success_metric", "horizon", "focus"):
        nonempty(plan.get(field), f"plan : {field} manquant")
    capacity = plan.get("capacity")
    require(isinstance(capacity, dict) and type(capacity.get("confirmed")) is bool, "capacité globale à qualifier")
    nonempty(capacity.get("description"), "capacité globale et limites à décrire")
    actions = plan.get("actions")
    require(isinstance(actions, list) and actions, "actions requises")
    ids = [item.get("id") for item in actions]
    require(all(isinstance(item, str) and re.fullmatch(r"[A-Za-z0-9_-]{1,48}", item) for item in ids) and len(ids) == len(set(ids)), "identifiants d'actions uniques requis")
    strategies = {SOURCES.normalized(s["keyword"]): s for s in bundle["strategies"]}
    covered, duplicates = set(), set()
    by_id = {item["id"]: item for item in actions}
    for index, action in enumerate(actions, 1):
        require(type(action.get("order")) is int and action["order"] == index, "ordre explicite de 1 à N requis")
        require(action.get("kind") in KINDS, f"{action['id']} : type d'action invalide")
        require(action.get("priority") in {"P1", "P2", "P3"}, f"{action['id']} : priorité invalide")
        for field in ("title", "target", "reason", "expected_effect", "done_when", "lot"):
            nonempty(action.get(field), f"{action['id']} : {field} manquant")
        owner = action.get("owner")
        require(owner is None or isinstance(owner, str) and owner.strip(), f"{action['id']} : responsable invalide")
        key = (SOURCES.normalized(action["title"]), SOURCES.normalized(action["target"]))
        require(key not in duplicates, "action identique répétée : regrouper ses mots-clés sources")
        duplicates.add(key)
        dependencies = action.get("depends_on")
        require(isinstance(dependencies, list) and len(dependencies) == len(set(dependencies)), f"{action['id']} : dépendances invalides")
        require(all(dep in by_id and dep != action["id"] for dep in dependencies), f"{action['id']} : dépendance inconnue ou sur elle-même")
        if action.get("due"):
            require(isinstance(action["due"], str) and re.fullmatch(r"\d{4}-\d{2}-\d{2}", action["due"]), "échéance attendue au format AAAA-MM-JJ")
            date.fromisoformat(action["due"])
            require(capacity["confirmed"], "calendrier daté interdit sans capacité globale confirmée")
        refs = action.get("source_refs")
        require(isinstance(refs, list) and refs, f"{action['id']} : stratégies sources requises")
        for ref in refs:
            key = SOURCES.normalized(ref.get("keyword"))
            require(key in strategies, f"{action['id']} : mot-clé absent du portefeuille")
            strategy = strategies[key]
            known = {item["id"] for item in strategy["outputs"]["1"]["micro_intentions"] + strategy["outputs"]["2"]["questions"]}
            require(isinstance(ref.get("ids"), list) and ref["ids"] and set(ref["ids"]).issubset(known), f"{action['id']} : référence d'intention ou de question inconnue")
            covered.add(key)
    require(covered == set(strategies), "chaque mot-clé du portefeuille doit être rattaché à une action, collecte ou arbitrage")
    visiting, visited = set(), set()

    def visit(action_id):
        require(action_id not in visiting, "cycle dans les dépendances")
        if action_id in visited:
            return
        visiting.add(action_id)
        for dep in by_id[action_id]["depends_on"]:
            visit(dep)
        visiting.remove(action_id)
        visited.add(action_id)

    for action_id in ids:
        visit(action_id)
    for action in actions:
        for dep_id in action["depends_on"]:
            dep = by_id[dep_id]
            require(dep["order"] < action["order"], f"{action['id']} : placer son prérequis avant elle")
            if action.get("due") and dep.get("due"):
                require(dep["due"] <= action["due"], f"{action['id']} : échéance avant son prérequis")


def source_issues(vault, state):
    issues = []
    if state.get("approval") and state["approval"]["plan_sha256"] != digest(state["plan"]):
        issues.append("Plan modifié depuis sa validation")
    path = SOURCES.in_vault(vault, state["manifest"]["bundle"])
    if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != state["bundle_sha256"]:
        issues.append("Dossier des stratégies modifié ou absent")
    report, snapshots = SOURCES.inspect(vault, state["manifest"])
    issues.extend(f"{item['keyword']} : {item['reason']}" for item in report["strategies"] if item["status"] != "validated")
    expected = {item["state"]: item["sha256"] for item in state["source_versions"]}
    issues.extend(f"Stratégie modifiée : {item['keyword']}" for item in snapshots if expected.get(item["state"]) != item["sha256"])
    return issues


def summary(state, issues=None):
    actions = state["plan"]["actions"]
    progress = state["progress"]
    done = {action_id for action_id, item in progress.items() if item["status"] == "done"}
    ready, blocked, review, active = [], [], [], []
    for action in actions:
        item = progress[action["id"]]
        waiting = [dep for dep in action["depends_on"] if dep not in done]
        if item["status"] == "review":
            review.append(action["id"])
        if item["status"] == "in_progress":
            active.append(action["id"])
        if item["status"] != "done":
            reasons = ([item["note"]] if item["status"] == "blocked" else []) + (["Responsable à attribuer"] if not action.get("owner") else [])
            if waiting:
                reasons.append("Attendre " + ", ".join(waiting))
            if reasons:
                blocked.append({"id": action["id"], "reason": "; ".join(reasons)})
            elif item["status"] == "todo":
                ready.append(action["id"])
    approved = bool(state.get("approval") and state["approval"]["plan_sha256"] == digest(state["plan"]))
    return {"approved": approved, "sources_to_review": issues or [], "total_actions": len(actions),
            "done_actions": len(done), "ready": ready if approved and not issues else [],
            "blocked": blocked, "awaiting_review": review, "in_progress": active}


def cell(value):
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def render(state, issues=None):
    plan = state["plan"]
    report = summary(state, issues)
    approved = report["approved"]
    lines = ["---", "type: synthesis", "title: " + json.dumps("Roadmap SEO : " + state["site"], ensure_ascii=False),
             "tags: [seo, roadmap, pilotage]", "created: " + state["created_at"][:10], "updated: " + date.today().isoformat(),
             "sources: " + str(len(state["source_versions"])), "confidence: medium", "status: " + ("stable" if approved and not issues else "draft"), "---", "",
             "# Roadmap SEO — " + state["site"], "", plan["objective"], "",
             "État : " + ("validée" if approved else "proposée, validation attendue") + ". Horizon : " + plan["horizon"] + ".", "",
             "Résultat à suivre : " + plan["success_metric"], "", "Moyens disponibles : " + plan["capacity"]["description"], "",
             "## Priorité actuelle", "", plan["focus"], "",
             f"{report['done_actions']}/{report['total_actions']} actions terminées.", ""]
    by_id = {item["id"]: item for item in plan["actions"]}
    if report["in_progress"]:
        lines += ["En cours : " + "; ".join(by_id[action_id]["title"] for action_id in report["in_progress"]), ""]
    if report["ready"]:
        first = by_id[report["ready"][0]]
        lines += [f"Prochaine action : **{first['title']}** ({first['owner']}).", ""]
    if issues:
        lines += ["## Sources à réexaminer", "", "Les analyses ont changé ou ne peuvent plus être vérifiées. Il faut les revoir avant de poursuivre.", ""]
    groups = {"En cours": [], "À suivre": [], "En attente": [], "Actions précédentes": []}
    done = {key for key, item in state["progress"].items() if item["status"] == "done"}
    for action in plan["actions"]:
        item = state["progress"][action["id"]]
        waiting = [by_id[key]["title"] for key in action["depends_on"] if key not in done]
        reasons = []
        if item["status"] == "blocked":
            reasons.append(item["note"] or "La raison du blocage reste à préciser")
        if item["status"] == "review":
            reasons.append("Validation attendue")
        if not action.get("owner"):
            reasons.append("Choisir qui s'en occupe")
        if waiting:
            reasons.append("Terminer d'abord : " + "; ".join(waiting))
        group = "Actions précédentes" if item["status"] == "done" else "En attente" if reasons else "En cours" if item["status"] == "in_progress" else "À suivre"
        label = "Terminé" if group == "Actions précédentes" else "Bloqué" if item["status"] == "blocked" else STATUS_LABELS[item["status"]]
        detail = "; ".join(reasons) if group == "En attente" else item["note"] if group == "Actions précédentes" else action["reason"]
        if action.get("due"):
            detail += " — Pour le " + action["due"]
        groups[group].append(f"| {cell(action['title'])} | {cell(detail)} | {cell(action.get('owner') or 'À choisir')} | {label} |")
    for title, rows in groups.items():
        lines += ["## " + title, ""]
        if rows:
            middle = "Ce qu'on attend" if title == "En attente" else "Ce qui a été fait" if title == "Actions précédentes" else "Pourquoi"
            lines += [f"| Action | {middle} | Qui | État |", "|---|---|---|---|"] + rows + [""]
        else:
            lines += ["Aucune action pour le moment.", ""]
    if not approved:
        lines += ["Le plan attend ta validation avant de commencer.", ""]
    lines += ["", "## Détail des actions", ""]
    for action in plan["actions"]:
        refs = "; ".join(ref["keyword"] for ref in action["source_refs"])
        lines += [f"### {action['title']}", "", "Page ou sujet : " + action["target"], "",
                  "Pourquoi cet ordre : " + action["reason"], "", "Effet attendu : " + action["expected_effect"], "",
                  "Terminé quand : " + action["done_when"], "", "Mots-clés concernés : " + refs, ""]
        progress = state["progress"][action["id"]]
        if progress["note"]:
            lines += ["Dernier point : " + progress["note"], ""]
        if progress["evidence"]:
            links = []
            for path in progress["evidence"]:
                target = str(Path(path).with_suffix(""))
                links.append("[[" + (target[5:] if target.startswith("wiki/") else target) + "]]")
            lines += ["Preuves : " + " · ".join(links), ""]
    lines += ["", "Méthode : [[methodes/roadmap-seo-portefeuille-mots-cles]]. Référence : [[moc/doctrine-seo-reference]].", ""]
    return "\n".join(lines)


def save(vault, path, state, issues=None):
    if path.exists():
        old = path.read_bytes()
        history = path.parent / "historique"
        require(history.resolve().is_relative_to(vault), "historique hors coffre")
        history.mkdir(exist_ok=True)
        archive = history / (path.stem + "-" + hashlib.sha256(old).hexdigest()[:16] + ".json")
        if not archive.exists():
            archive.write_bytes(old)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")
    SOURCES.in_vault(vault, state["manifest"]["roadmap"]).write_text(render(state, issues))


def propose(vault, manifest, plan, revision=False, reason=None):
    source_path = SOURCES.bundle(vault, manifest)
    source_bytes = source_path.read_bytes()
    bundle = json.loads(source_bytes)
    validate_plan(plan, bundle)
    roadmap_path = SOURCES.in_vault(vault, manifest["roadmap"])
    path = roadmap_path.with_suffix(".json")
    require(path != source_path, "état de suivi en conflit avec le dossier source")
    previous = json.loads(path.read_text()) if path.exists() else None
    require(not previous or previous.get("site") == manifest["site"], "chemin de roadmap déjà utilisé pour un autre site")
    require(not previous or not previous.get("approval") or revision, "roadmap déjà validée : proposer une nouvelle révision avant de changer son plan")
    if revision:
        require(previous, "aucune roadmap à réviser")
        nonempty(reason, "motif de révision requis")
    require(previous or not roadmap_path.exists(), "roadmap existante sans état de suivi : conserver sa version avant de la remplacer")
    stamp = now()
    progress = {action["id"]: {"status": "todo", "note": "", "evidence": []} for action in plan["actions"]}
    if previous:
        old = {item["id"]: item for item in previous["plan"]["actions"]}
        changed = {item["id"] for item in plan["actions"] if old.get(item["id"]) != item}
        old_sources = {item["state"]: item["sha256"] for item in previous["source_versions"]}
        changed_keywords = {SOURCES.normalized(item["keyword"]) for item in bundle["strategies"] if old_sources.get(item["state"]) != item["sha256"]}
        changed.update(item["id"] for item in plan["actions"] if any(SOURCES.normalized(ref["keyword"]) in changed_keywords for ref in item["source_refs"]))
        again = True
        while again:
            affected = {item["id"] for item in plan["actions"] if set(item["depends_on"]) & changed}
            again = not affected.issubset(changed)
            changed.update(affected)
        for action in plan["actions"]:
            if action["id"] not in changed:
                progress[action["id"]] = previous["progress"][action["id"]]
    state = {"site": manifest["site"], "vault": str(vault), "manifest": manifest, "plan": plan, "created_at": previous["created_at"] if previous else stamp,
             "bundle_sha256": hashlib.sha256(source_bytes).hexdigest(), "source_versions": [{"state": s["state"], "sha256": s["sha256"]} for s in bundle["strategies"]],
             "approval": None, "progress": progress,
             "history": (previous.get("history", []) if previous else []) + [{"at": stamp, "message": ("Révision : " + reason if revision else "Proposition de roadmap") + " — " + digest(plan)}]}
    save(vault, path, state)
    return path


def approve(vault, path, message, confirmed):
    require(confirmed, "validation explicite de Tim requise")
    nonempty(message, "message de validation requis")
    state = json.loads(path.read_text())
    require(state.get("vault") == str(vault), "roadmap d'un autre coffre")
    require(not state.get("approval"), "roadmap déjà validée")
    issues = source_issues(vault, state)
    require(not issues, "sources à réexaminer : " + "; ".join(issues))
    bundle = json.loads(SOURCES.in_vault(vault, state["manifest"]["bundle"]).read_text())
    validate_plan(state["plan"], bundle)
    state["approval"] = {"message": message, "at": now(), "plan_sha256": digest(state["plan"])}
    state["history"].append({"at": now(), "message": "Roadmap validée : " + message})
    save(vault, path, state)


def update(vault, path, action_id, status, note, evidence):
    state = json.loads(path.read_text())
    require(state.get("vault") == str(vault), "roadmap d'un autre coffre")
    approval = state.get("approval")
    require(approval and approval["plan_sha256"] == digest(state["plan"]), "plan actuel non validé")
    issues = source_issues(vault, state)
    require(not issues, "sources à réexaminer : " + "; ".join(issues))
    require(status in STATUS_LABELS, "statut invalide")
    action = next((item for item in state["plan"]["actions"] if item["id"] == action_id), None)
    require(action, "action inconnue")
    nonempty(note, "fait ou raison du changement requis")
    if state["progress"][action_id]["status"] == "done":
        require(status == "done", "action terminée : sa reprise nécessite un arbitrage et une révision")
    for source in evidence:
        require(SOURCES.in_vault(vault, source).is_file(), "preuve de réalisation introuvable")
    if status in {"in_progress", "review", "done"}:
        require(action.get("owner"), "attribuer un responsable avant de démarrer")
        waiting = [dep for dep in action["depends_on"] if state["progress"][dep]["status"] != "done"]
        require(not waiting, "prérequis non terminés : " + ", ".join(waiting))
    if status == "done":
        require(evidence, "preuve de réalisation requise pour terminer")
    state["progress"][action_id] = {"status": status, "note": note, "evidence": evidence}
    state["history"].append({"at": now(), "message": f"{action_id} — {STATUS_LABELS[status]} : {note}"})
    save(vault, path, state)


def run(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("propose", "revise", "approve", "update", "status"))
    parser.add_argument("--vault", type=Path, required=True)
    parser.add_argument("--manifest")
    parser.add_argument("--input", type=Path)
    parser.add_argument("--state")
    parser.add_argument("--message")
    parser.add_argument("--user-approved", action="store_true")
    parser.add_argument("--action")
    parser.add_argument("--status", choices=tuple(STATUS_LABELS))
    parser.add_argument("--note")
    parser.add_argument("--evidence", nargs="*", default=[])
    args = parser.parse_args(argv)
    vault = args.vault.resolve()
    if args.command in {"propose", "revise"}:
        require(args.manifest and args.input, "manifeste et proposition JSON requis")
        manifest = SOURCES.read_manifest(vault, SOURCES.in_vault(vault, args.manifest))
        print(propose(vault, manifest, json.loads(args.input.read_text()), revision=args.command == "revise", reason=args.message))
        return
    path = SOURCES.in_vault(vault, args.state)
    if args.command == "approve":
        approve(vault, path, args.message, args.user_approved)
    elif args.command == "update":
        update(vault, path, args.action, args.status, args.note, args.evidence)
    state = json.loads(path.read_text())
    require(state.get("vault") == str(vault), "roadmap d'un autre coffre")
    issues = source_issues(vault, state)
    if args.command == "status":
        SOURCES.in_vault(vault, state["manifest"]["roadmap"]).write_text(render(state, issues))
    print(json.dumps(summary(state, issues), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        run()
    except (ValueError, OSError, TypeError, KeyError) as error:
        print(f"ERREUR : {error}", file=sys.stderr)
        sys.exit(1)
