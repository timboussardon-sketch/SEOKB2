#!/usr/bin/env python3
"""État et gates du workflow « stratégie d'un mot-clé » dans le coffre courant."""

import argparse
import hashlib
import json
import re
import sys
import unicodedata
from datetime import date, datetime, timezone
from pathlib import Path

CATEGORIES = {"Know-Simple", "Know", "Do"}
EVIDENCE_KINDS = {"contexte", "methode", "cas", "verbatim", "mesure"}
QUESTION_ORIGINS = {"terrain": 0, "search": 1, "expertise": 2, "hypothesis": 3}
BUYER_TASKS = {"comprendre", "comparer", "choisir", "acheter"}
SKILL_DIR = Path(__file__).resolve().parent.parent
METHOD_FILES = {
    "micro_intentions": SKILL_DIR / "references" / "methode-micro-intentions.md",
    "geo_citations": SKILL_DIR.parent / "geo-citations" / "SKILL.md",
}


def slugify(value):
    value = unicodedata.normalize("NFKD", value)
    value = "".join(c for c in value if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")[:80]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def source_in_vault(vault, value):
    require(isinstance(value, str) and value.strip(), "source manquante")
    require(not Path(value).is_absolute(), f"source hors coffre : {value}")
    root = Path(vault).resolve()
    target = (root / value).resolve()
    require(target.is_relative_to(root) and target.is_file(), f"source introuvable dans le coffre : {value}")
    return value


def nonempty(value, message):
    require(isinstance(value, str) and value.strip(), message)


def normalized(value):
    return re.sub(r"\W+", " ", value.casefold()).strip()


def check_quote(vault, source, quote):
    source_in_vault(vault, source)
    nonempty(quote, "extrait source manquant")
    content = (Path(vault) / source).read_text()
    require(" ".join(quote.split()) in " ".join(content.split()), f"extrait absent de la source : {source}")


def validate_business(data, vault):
    business = data.get("business")
    require(isinstance(business, dict), "qualification business requise avant les micro-intentions")
    for field in ("offer", "prospect", "problem", "conversion_action", "keyword_value"):
        nonempty(business.get(field), f"qualification business : {field} manquant")
    sources = business.get("sources")
    require(isinstance(sources, list), "qualification business : sources à préciser")
    for source in sources:
        source_in_vault(vault, source)
    if not sources:
        nonempty(business.get("user_context"), "qualification business sans source : contexte fourni par l'utilisateur requis")
    existing = business.get("existing_url")
    require(isinstance(existing, dict) and existing.get("status") in {"existing", "none_found"}, "URL existante : recherche préalable requise")
    nonempty(existing.get("check"), "URL existante : contrôle effectué à décrire")
    if existing["status"] == "existing":
        require(isinstance(existing.get("url"), str) and re.match(r"^https?://", existing["url"]), "URL existante invalide")
    else:
        require(not existing.get("url"), "aucune URL trouvée : laisser url vide")


def validate_phase_1(data, vault):
    validate_business(data, vault)
    items = data.get("micro_intentions")
    require(isinstance(items, list) and items, "étape 1 : au moins une micro-intention qualifiée requise")
    if len(items) != 5:
        nonempty(data.get("count_reason"), "écart à l'objectif de cinq intentions à justifier")
    nonempty(data.get("dedup_review"), "revue des besoins distincts requise")
    require([item.get("id") for item in items] == [f"m{i}" for i in range(1, len(items) + 1)], "étape 1 : identifiants m1 à mN attendus")
    seen = set()
    needs = set()
    for item in items:
        require(item.get("category") in CATEGORIES, f"catégorie invalide : {item.get('id')}")
        for field in ("query", "want", "business_signal", "decision_need", "business_link", "distinctness_reason"):
            nonempty(item.get(field), f"{item['id']} : {field} manquant")
        require(item.get("buyer_task") in BUYER_TASKS, f"{item['id']} : tâche de l'acheteur invalide")
        key = normalized(item["query"])
        require(key not in seen, f"micro-intention répétée : {item['query']}")
        seen.add(key)
        need = normalized(item["decision_need"])
        require(need not in needs, f"besoin déjà couvert : {item['decision_need']}")
        needs.add(need)
        require(item.get("status") in {"observed", "hypothesis"}, f"{item['id']} : statut invalide")
        if item["status"] == "observed":
            check_quote(vault, item.get("source"), item.get("source_excerpt"))
        elif item.get("source"):
            source_in_vault(vault, item["source"])


def validate_phase_2(data, vault, micro_intentions):
    items = data.get("questions")
    require(isinstance(items, list) and items, "étape 2 : questions d'acheteurs requises")
    if len(items) != 15:
        nonempty(data.get("count_reason"), "écart à l'objectif de quinze questions à justifier")
    require([item.get("id") for item in items] == [f"q{i}" for i in range(1, len(items) + 1)], "étape 2 : identifiants q1 à qN attendus")
    research = data.get("research_log")
    require(isinstance(research, list) and [entry.get("tier") for entry in research] == ["terrain", "search", "expertise"], "rechercher terrain, recherches observées puis expertise avant les hypothèses")
    for entry in research:
        nonempty(entry.get("finding"), f"bilan de recherche manquant : {entry['tier']}")
        require(isinstance(entry.get("sources"), list), "sources de recherche à préciser")
        for source in entry["sources"]:
            source_in_vault(vault, source)
        if not entry["sources"]:
            nonempty(entry.get("unavailable_reason"), f"absence de données à expliquer : {entry['tier']}")
    micro_ids = {item["id"] for item in micro_intentions}
    seen = set()
    last_priority = -1
    for item in items:
        require(item.get("micro_id") in micro_ids, f"{item['id']} : micro-intention inconnue")
        question = item.get("question")
        require(isinstance(question, str) and question.strip().endswith("?"), f"{item['id']} : question invalide")
        key = normalized(question)
        require(key not in seen, f"question répétée : {question}")
        seen.add(key)
        origin = item.get("origin")
        require(origin in QUESTION_ORIGINS, f"{item['id']} : origine invalide")
        priority = QUESTION_ORIGINS[origin]
        require(priority >= last_priority, "présenter les questions dans l'ordre terrain, search, expertise, hypothèses")
        last_priority = priority
        expected_status = "hypothesis" if origin == "hypothesis" else "expertise" if origin == "expertise" else "observed"
        require(item.get("status") == expected_status, f"{item['id']} : statut incohérent avec l'origine")
        if origin == "hypothesis":
            nonempty(item.get("gap"), f"{item['id']} : lacune justifiant l'hypothèse à nommer")
            if item.get("source"):
                source_in_vault(vault, item["source"])
        else:
            check_quote(vault, item.get("source"), item.get("source_excerpt"))
            tier_sources = next(entry["sources"] for entry in research if entry["tier"] == origin)
            require(item["source"] in tier_sources, f"{item['id']} : source absente du journal de recherche {origin}")


def evidence_eligible(proof):
    quality = proof.get("quality", {})
    return (proof.get("proprietary") is True and proof.get("relevance") == "direct"
            and quality.get("reliable") is True and quality.get("current") is True
            and quality.get("usable") is True)


def validate_phase_3(data, vault, expected):
    items = data.get("scores")
    require(isinstance(items, list) and len(items) == len(expected), "étape 3 : noter tous les éléments réellement validés")
    require([item.get("id") for item in items] == expected, "étape 3 : identifiants différents des intentions et questions validées")
    for item in items:
        nonempty(item.get("response_target"), f"{item['id']} : réponse ou affirmation à étayer requise")
        evidence = item.get("evidence")
        require(isinstance(evidence, list), f"{item['id']} : preuves manquantes")
        kinds = set()
        for proof in evidence:
            kind = proof.get("kind")
            require(kind in EVIDENCE_KINDS, f"{item['id']} : catégorie de preuve invalide")
            check_quote(vault, proof.get("source"), proof.get("source_excerpt"))
            for field in ("detail", "supports", "relevance_reason", "provenance_reason"):
                nonempty(proof.get(field), f"{item['id']} : {field} manquant")
            require(proof.get("relevance") in {"direct", "indirect", "unrelated"}, f"{item['id']} : pertinence à qualifier")
            require(type(proof.get("proprietary")) is bool, f"{item['id']} : origine propriétaire à qualifier")
            quality = proof.get("quality")
            require(isinstance(quality, dict), f"{item['id']} : qualité de preuve à qualifier")
            for field in ("reliable", "current", "usable"):
                require(type(quality.get(field)) is bool, f"{item['id']} : qualité {field} à qualifier")
            for field in ("reliability_reason", "freshness_reason", "usability_reason"):
                nonempty(quality.get(field), f"{item['id']} : justification {field} requise")
            for field in ("source_date", "checked_at"):
                value = quality.get(field)
                require(value or field == "source_date", f"{item['id']} : date de vérification requise")
                if value:
                    require(isinstance(value, str) and re.fullmatch(r"\d{4}-\d{2}-\d{2}", value), f"{item['id']} : date {field} invalide")
                    require(date.fromisoformat(value) <= date.today(), f"{item['id']} : date {field} future")
            if evidence_eligible(proof):
                kinds.add(kind)
                if kind == "mesure":
                    nonempty(proof.get("period"), f"{item['id']} : période de mesure requise")
                if kind == "verbatim":
                    nonempty(proof.get("attribution"), f"{item['id']} : attribution du verbatim requise")
        require(type(item.get("score")) is int and item["score"] == len(kinds), f"{item['id']} : note incohérente avec les catégories prouvées")
        require(isinstance(item.get("missing"), str), f"{item['id']} : données manquantes à préciser")
        if item["score"] < 5:
            nonempty(item["missing"], f"{item['id']} : note partielle, données à collecter requises")


def wikilink(path):
    if not path:
        return "hypothèse"
    return f"[[{str(Path(path).with_suffix(''))}]]"


def cell(value):
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def render(state):
    now = date.today().isoformat()
    source_paths = set()
    for phase_data in state["outputs"].values():
        for key in ("micro_intentions", "questions", "scores"):
            for item in phase_data.get(key, []):
                if item.get("source"):
                    source_paths.add(item["source"])
                for proof in item.get("evidence", []):
                    source_paths.add(proof["source"])
        source_paths.update(phase_data.get("business", {}).get("sources", []))
        for entry in phase_data.get("research_log", []):
            source_paths.update(entry.get("sources", []))
    lines = [
        "---", "type: synthesis", f"title: \"Stratégie du mot-clé : {state['keyword'].replace(chr(34), chr(39))}\"",
        "aliases: []", "tags: [seo, mots-cles, geo, strategie]", f"created: {state['created'][:10]}",
        f"updated: {now}", f"sources: {len(source_paths)}", "confidence: low",
        f"status: {'stable' if state['approvals'].get('3') else 'draft'}", "---", "",
        f"# Stratégie du mot-clé « {state['keyword']} »", "",
        f"Coffre : `{state['vault']}`. Méthode : [[methodes/strategie-mot-cle-par-etapes]].",
        "Les validations ci-dessous portent uniquement sur l'étape nommée.", "",
    ]
    lines += ["## Méthodes sources et versions", ""]
    for name, source in state["methods"].items():
        version = f"`sha256:{source['sha256']}`" if source["sha256"] else "indisponible"
        loaded = "chargée" if any(name in names for names in state.get("loaded_methods", {}).values()) else "à charger"
        lines.append(f"- `{name}` : `{source['path']}` ; version {version} ; {loaded}")
    lines.append("")
    for phase in (1, 2, 3):
        data = state["outputs"].get(str(phase))
        if not data:
            continue
        if phase == 1:
            business = data.get("business", {})
            lines += ["## Qualification business", "", "| Point | Contexte du projet |", "|---|---|"]
            for field, label in (("offer", "Offre à vendre"), ("prospect", "Prospect"), ("problem", "Problème résolu"), ("conversion_action", "Action recherchée"), ("keyword_value", "Intérêt du mot-clé")):
                lines.append(f"| {label} | {cell(business.get(field, 'À préciser'))} |")
            existing = business.get("existing_url", {})
            lines += [f"| URL existante | {cell(existing.get('url') or 'Aucune trouvée dans le périmètre vérifié')} ; {cell(existing.get('check', 'À vérifier'))} |", ""]
            if business.get("sources"):
                lines += ["Sources du cadrage : " + " · ".join(wikilink(s) for s in business["sources"]), ""]
            elif business.get("user_context"):
                lines += ["Contexte fourni par l'utilisateur : " + cell(business["user_context"]), ""]
            lines += [f"## Étape 1 — {len(data['micro_intentions'])} micro-intentions retenues", ""]
            if data.get("count_reason"):
                lines += [cell(data["count_reason"]), ""]
            lines += ["Revue des besoins distincts : " + cell(data.get("dedup_review", "À reprendre")), "", "| ID | Requête | Catégorie | Besoin de l'acheteur | Lien business | Provenance |", "|---|---|---|---|---|---|"]
            for item in data["micro_intentions"]:
                lines.append(f"| {item['id']} | {cell(item['query'])} | {item['category']} | {cell(item.get('buyer_task', ''))} : {cell(item['want'])} | {cell(item.get('business_link', item['business_signal']))} | {item['status']} : {wikilink(item.get('source'))} |")
        elif phase == 2:
            lines += [f"## Étape 2 — {len(data['questions'])} questions d'acheteurs", "", "Les formulations conservent le langage des acheteurs. Un éventuel panel GEO fera l'objet d'une adaptation distincte.", ""]
            if data.get("count_reason"):
                lines += [cell(data["count_reason"]), ""]
            for entry in data.get("research_log", []):
                sources = " · ".join(wikilink(s) for s in entry["sources"]) or cell(entry.get("unavailable_reason", ""))
                lines.append(f"- {entry['tier']} : {cell(entry['finding'])} ; {sources}")
            lines += ["", "| ID | Question | Micro-intention | Origine | Provenance |", "|---|---|---|---|---|"]
            for item in data["questions"]:
                wording = "hypothèse" if item["status"] == "hypothesis" else "proposée depuis l'expertise" if item["status"] == "expertise" else "verbatim" if " ".join(item["question"].split()) in " ".join(item.get("source_excerpt", "").split()) else "reformulée depuis la source"
                original = f" ; extrait : {cell(item['source_excerpt'])}" if item.get("source_excerpt") else ""
                lines.append(f"| {item['id']} | {cell(item['question'])} | {item['micro_id']} | {cell(item.get('origin', item['status']))} ; {wording} | {wikilink(item.get('source'))}{original} {cell(item.get('gap', ''))} |")
        else:
            lines += ["## Étape 3 — matière propriétaire disponible", "", "La note compte les catégories de preuves directement pertinentes, fiables, actuelles et exploitables. Une note basse indique un besoin de collecte ; la valeur business du sujet reste distincte.", "", "| ID | Réponse à étayer | Note /5 | Preuves retenues | Données à collecter |", "|---|---|---:|---|---|"]
            for item in data["scores"]:
                proofs = "; ".join(f"{p['kind']} : {cell(p['supports'])} {wikilink(p['source'])}" for p in item["evidence"] if evidence_eligible(p)) or "aucune"
                lines.append(f"| {item['id']} | {cell(item.get('response_target', 'À préciser'))} | {item['score']}/5 | {proofs} | {cell(item['missing'])} |")
            lines += ["", "### Contrôle des preuves", ""]
            for item in data["scores"]:
                for proof in item["evidence"]:
                    quality = proof.get("quality", {})
                    label = "retenue" if evidence_eligible(proof) else "écartée du score"
                    lines += [f"- {item['id']} / {proof['kind']} — {label} : {wikilink(proof['source'])}",
                              f"  Extrait : {cell(proof.get('source_excerpt', ''))}",
                              f"  Affirmation soutenue : {cell(proof.get('supports', ''))}. Pertinence : {cell(proof.get('relevance_reason', ''))}.",
                              f"  Origine : {cell(proof.get('provenance_reason', ''))}. Fiabilité : {cell(quality.get('reliability_reason', ''))}.",
                              f"  Actualité : {cell(quality.get('freshness_reason', ''))} (source : {quality.get('source_date') or 'non datée'}, contrôle : {quality.get('checked_at', 'non renseigné')}). Exploitabilité : {cell(quality.get('usability_reason', ''))}."]
        lines += ["", f"Validation : **{'oui' if state['approvals'].get(str(phase)) else 'en attente'}**.", ""]
    lines += ["## Journal des validations", ""]
    for entry in state["history"]:
        lines.append(f"- {entry['at']} — étape {entry['phase']} : {entry['message']}")
    lines += ["", "Références : [[moc/doctrine-seo-reference]] · [[concepts/preuve-atomique]].", ""]
    return "\n".join(lines)


def save(path, state):
    path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")
    path.with_suffix(".md").write_text(render(state))


def load(path):
    state = json.loads(path.read_text())
    require(Path(state["vault"]).is_dir(), "coffre absent")
    return state


def load_method(state, phase):
    names = ("micro_intentions",) if phase == 1 else ("geo_citations",)
    for name in names:
        source = Path(state["methods"][name]["path"])
        require(source.is_file(), f"méthode indisponible : {source}")
        data = source.read_text()
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        state["methods"][name]["sha256"] = digest
        excerpt = data
        print(f"\n### {name} — {source} — sha256:{digest}\n{excerpt}\n")
    state.setdefault("loaded_methods", {})[str(phase)] = {
        name: state["methods"][name]["sha256"] for name in names
    }


def require_method_loaded(state, phase):
    names = ("micro_intentions",) if phase == 1 else ("geo_citations",) if phase == 2 else ()
    loaded = state.get("loaded_methods", {}).get(str(phase), {})
    for name in names:
        source = Path(state["methods"][name]["path"])
        require(source.is_file(), f"méthode indisponible : {source}")
        current = hashlib.sha256(source.read_bytes()).hexdigest()
        require(loaded.get(name) == current, f"skill {name} non chargé dans sa version actuelle")


def validate_output(state, phase, data):
    if phase == 1:
        validate_phase_1(data, state["vault"])
    elif phase == 2:
        validate_phase_2(data, state["vault"], state["outputs"]["1"]["micro_intentions"])
    else:
        expected = [item["id"] for item in state["outputs"]["1"]["micro_intentions"] + state["outputs"]["2"]["questions"]]
        validate_phase_3(data, state["vault"], expected)


def run(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    init = sub.add_parser("init")
    init.add_argument("--vault", required=True)
    init.add_argument("--keyword", required=True)
    submit = sub.add_parser("submit")
    submit.add_argument("--state", type=Path, required=True)
    submit.add_argument("--phase", type=int, choices=(1, 2, 3), required=True)
    submit.add_argument("--input", type=Path, required=True)
    approve = sub.add_parser("approve")
    approve.add_argument("--state", type=Path, required=True)
    approve.add_argument("--phase", type=int, choices=(1, 2, 3), required=True)
    approve.add_argument("--message", required=True)
    approve.add_argument("--user-approved", action="store_true")
    status = sub.add_parser("status")
    status.add_argument("--state", type=Path, required=True)
    method = sub.add_parser("load-method")
    method.add_argument("--state", type=Path, required=True)
    method.add_argument("--phase", type=int, choices=(1, 2), required=True)
    args = parser.parse_args(argv)
    if args.command == "init":
        vault = Path(args.vault).resolve()
        require(vault.is_dir() and any((vault / f).exists() for f in ("AGENTS.md", "CLAUDE.md", ".seokb/base/wiki/AGENTS.md")), "coffre sans AGENTS.md ni CLAUDE.md : lance la commande depuis la racine du coffre")
        keyword = args.keyword.strip()
        require(keyword and len(keyword) <= 160 and "\n" not in keyword, "mot-clé manquant ou invalide")
        require(slugify(keyword), "mot-clé sans slug utilisable")
        path = vault / "wiki" / "strategie-mot-cle" / f"{date.today().isoformat()}-{slugify(keyword)}.json"
        require(not path.exists(), f"stratégie déjà ouverte : {path}")
        methods = {}
        for name, source in METHOD_FILES.items():
            if name != "geo_citations":
                require(source.is_file(), f"méthode indisponible : {source}")
            methods[name] = {"path": str(source), "sha256": hashlib.sha256(source.read_bytes()).hexdigest() if source.is_file() else None}
        path.parent.mkdir(parents=True, exist_ok=True)
        state = {"keyword": keyword, "vault": str(vault), "created": datetime.now(timezone.utc).isoformat(), "methods": methods, "outputs": {}, "approvals": {}, "history": []}
        save(path, state)
        print(path)
        print(path.with_suffix(".md"))
        return
    path = args.state.resolve()
    state = load(path)
    require(path.is_relative_to(Path(state["vault"]).resolve()), "état hors coffre")
    if args.command == "status":
        print(json.dumps({"keyword": state["keyword"], "submitted": sorted(state["outputs"]), "approved": sorted(state["approvals"]), "loaded_methods": sorted(state.get("loaded_methods", {}))}, ensure_ascii=False))
        return
    if args.command == "load-method":
        require(args.phase == 1 or state["approvals"].get("1"), "étape 1 non validée")
        load_method(state, args.phase)
        save(path, state)
        return
    phase = args.phase
    require(phase == 1 or state["approvals"].get(str(phase - 1)), f"étape {phase - 1} non validée")
    require(not state["approvals"].get(str(phase)), f"étape {phase} déjà validée")
    for previous in range(1, phase):
        validate_output(state, previous, state["outputs"][str(previous)])
    if args.command == "submit":
        require_method_loaded(state, phase)
        data = json.loads(args.input.read_text())
        validate_output(state, phase, data)
        state["outputs"][str(phase)] = data
        save(path, state)
        print(f"étape {phase} soumise ; validation de l'utilisateur attendue")
        return
    require(args.user_approved, "accord explicite de l'utilisateur requis")
    require(state["outputs"].get(str(phase)), f"étape {phase} non soumise")
    require(args.message.strip(), "texte de validation manquant")
    require_method_loaded(state, phase)
    validate_output(state, phase, state["outputs"][str(phase)])
    state["approvals"][str(phase)] = True
    state["history"].append({"phase": phase, "message": args.message.strip(), "at": datetime.now(timezone.utc).isoformat()})
    save(path, state)
    print(f"étape {phase} validée")


if __name__ == "__main__":
    try:
        run()
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print(f"ERREUR : {exc}", file=sys.stderr)
        sys.exit(1)
