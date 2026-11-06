import copy
import contextlib
import importlib.util
import json
import io
import unittest
from pathlib import Path


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


ROOT = Path(__file__).parent
planner = module("roadmap_planner", ROOT / "plan.py")
fixtures = module("roadmap_test_fixtures", ROOT / "test_consolidate.py")


class PlanTest(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.ConsolidationTest()
        self.fixture.setUp()
        self.vault = self.fixture.vault
        self.manifest = self.fixture.manifest
        self.plan = {
            "objective": "Permettre aux prospects de choisir l'offre adaptée", "success_metric": "Demandes qualifiées depuis les pages suivies",
            "horizon": "Deux lots, échéances à confirmer", "focus": "Collecter les cas nécessaires avant le brief",
            "capacity": {"confirmed": False, "description": "Capacité globale à confirmer avec le client"},
            "actions": [
                {"id": "R1", "order": 1, "kind": "collecte", "title": "Rassembler les cas clients utiles", "target": "Dossier de preuves",
                 "priority": "P1", "reason": "La matière manque pour les cinq mots-clés", "expected_effect": "Documenter les choix des acheteurs",
                 "done_when": "Cas relus avec le client", "lot": "Lot 1", "owner": "Client", "depends_on": [], "due": None,
                 "source_refs": [{"keyword": item["keyword"], "ids": ["m1"]} for item in self.manifest["keywords"]]},
                {"id": "R2", "order": 2, "kind": "contenu", "title": "Préparer le brief de la page offre", "target": "Page offre du site",
                 "priority": "P1", "reason": "Le brief dépend des cas collectés", "expected_effect": "Préparer une page étayée",
                 "done_when": "Brief validé par le consultant", "lot": "Lot 2", "owner": "Consultant", "depends_on": ["R1"], "due": None,
                 "source_refs": [{"keyword": self.manifest["keywords"][0]["keyword"], "ids": ["q1"]}]},
            ],
        }
        self.proof = self.vault / "wiki" / "preuves" / "cas.md"
        self.proof.parent.mkdir()
        self.proof.write_text("Cas relu, référence de validation du test.\n")

    def tearDown(self):
        self.fixture.tearDown()

    def proposed(self, approve=False):
        path = planner.propose(self.vault, self.manifest, self.plan)
        if approve:
            planner.approve(self.vault, path, "Je valide cette roadmap", True)
        return path

    def test_proposal_is_readable_and_execution_requires_approval(self):
        path = self.proposed()
        text = path.with_suffix(".md").read_text()
        self.assertIn("Priorité actuelle", text)
        self.assertIn("En attente", text)
        self.assertIn("Terminé quand", text)
        self.assertIn("0/2 actions terminées", text)
        with self.assertRaisesRegex(ValueError, "non validé"):
            planner.update(self.vault, path, "R1", "in_progress", "Début", [])
        with self.assertRaisesRegex(ValueError, "validation explicite"):
            planner.approve(self.vault, path, "oui", False)
        planner.approve(self.vault, path, "Je valide", True)
        self.assertEqual(planner.summary(json.loads(path.read_text()))["ready"], ["R1"])

    def test_dependencies_and_completion_proof_control_progress(self):
        path = self.proposed(approve=True)
        with self.assertRaisesRegex(ValueError, "prérequis non terminés"):
            planner.update(self.vault, path, "R2", "in_progress", "Début du brief", [])
        with self.assertRaisesRegex(ValueError, "preuve de réalisation"):
            planner.update(self.vault, path, "R1", "done", "Collecte finie", [])
        planner.update(self.vault, path, "R1", "done", "Cas relus", ["wiki/preuves/cas.md"])
        report = planner.summary(json.loads(path.read_text()))
        self.assertEqual(report["done_actions"], 1)
        self.assertEqual(report["ready"], ["R2"])
        planner.update(self.vault, path, "R2", "in_progress", "Préparation du brief", [])
        self.assertIn("1/2 actions terminées", path.with_suffix(".md").read_text())

    def test_cycles_uncovered_keywords_and_unknown_references_are_rejected(self):
        source = json.loads(planner.SOURCES.bundle(self.vault, self.manifest).read_text())
        changed = copy.deepcopy(self.plan)
        changed["actions"][0]["depends_on"] = ["R2"]
        with self.assertRaisesRegex(ValueError, "cycle"):
            planner.validate_plan(changed, source)
        changed = copy.deepcopy(self.plan)
        changed["actions"][0]["source_refs"] = changed["actions"][0]["source_refs"][:1]
        with self.assertRaisesRegex(ValueError, "chaque mot-clé"):
            planner.validate_plan(changed, source)
        changed = copy.deepcopy(self.plan)
        changed["actions"][0]["source_refs"][0]["ids"] = ["q999"]
        with self.assertRaisesRegex(ValueError, "référence.*inconnue"):
            planner.validate_plan(changed, source)

    def test_no_dates_without_capacity_and_no_date_before_prerequisite(self):
        source = json.loads(planner.SOURCES.bundle(self.vault, self.manifest).read_text())
        changed = copy.deepcopy(self.plan)
        changed["actions"][0]["due"] = "2026-11-12"
        with self.assertRaisesRegex(ValueError, "capacité globale confirmée"):
            planner.validate_plan(changed, source)
        changed["capacity"]["confirmed"] = True
        changed["actions"][1]["due"] = "2026-11-10"
        with self.assertRaisesRegex(ValueError, "échéance avant"):
            planner.validate_plan(changed, source)

    def test_changed_strategy_blocks_updates_until_revision(self):
        path = self.proposed(approve=True)
        self.fixture.modify(0, lambda state: state["outputs"]["3"]["scores"][0].update({"missing": "Nouvelle collecte"}))
        with self.assertRaisesRegex(ValueError, "sources à réexaminer"):
            planner.update(self.vault, path, "R1", "in_progress", "Début", [])
        state = json.loads(path.read_text())
        issues = planner.source_issues(self.vault, state)
        self.assertEqual(planner.summary(state, issues)["ready"], [])
        with contextlib.redirect_stdout(io.StringIO()):
            planner.run(["status", "--vault", str(self.vault), "--state", str(path.relative_to(self.vault))])
        self.assertIn("Sources à réexaminer", path.with_suffix(".md").read_text())

    def test_revision_archives_the_plan_and_reopens_affected_dependencies(self):
        path = self.proposed(approve=True)
        for action_id in ("R1", "R2"):
            planner.update(self.vault, path, action_id, "done", "Travail validé", ["wiki/preuves/cas.md"])
        changed = copy.deepcopy(self.plan)
        changed["actions"][0]["target"] = "Nouveau périmètre de cas"
        with self.assertRaisesRegex(ValueError, "nouvelle révision"):
            planner.propose(self.vault, self.manifest, changed)
        planner.propose(self.vault, self.manifest, changed, revision=True, reason="Tim change le périmètre de collecte")
        state = json.loads(path.read_text())
        self.assertIsNone(state["approval"])
        self.assertEqual(state["progress"]["R1"]["status"], "todo")
        self.assertEqual(state["progress"]["R2"]["status"], "todo")
        archives = list((path.parent / "historique").glob("*.json"))
        self.assertTrue(any(json.loads(p.read_text())["progress"]["R2"]["status"] == "done" for p in archives))

    def test_missing_owner_prevents_start(self):
        self.plan["actions"][0]["owner"] = None
        path = self.proposed(approve=True)
        with self.assertRaisesRegex(ValueError, "attribuer un responsable"):
            planner.update(self.vault, path, "R1", "in_progress", "Début", [])

    def test_recap_separates_waiting_current_and_previous_actions(self):
        path = self.proposed(approve=True)
        state = json.loads(path.read_text())
        text = planner.render(state)
        waiting = text.split("## En attente\n", 1)[1].split("## Actions précédentes", 1)[0]
        self.assertIn("Terminer d'abord : Rassembler les cas clients utiles", waiting)
        self.assertNotIn("R1", waiting)
        planner.update(self.vault, path, "R1", "done", "Cas relus avec le client", ["wiki/preuves/cas.md"])
        planner.update(self.vault, path, "R2", "in_progress", "Préparation", [])
        text = path.with_suffix(".md").read_text()
        previous = text.split("## Actions précédentes\n", 1)[1].split("## Détail", 1)[0]
        self.assertIn("Cas relus avec le client", previous)
        self.assertNotIn("Préparer le brief", previous)
        overview = text.split("## Détail", 1)[0]
        self.assertEqual(overview.count("| Préparer le brief de la page offre |"), 1)
        self.assertNotIn("plan_sha256", overview)
        self.assertNotIn("| Prérequis |", overview)
        self.assertTrue(json.loads(path.read_text())["history"])


if __name__ == "__main__":
    unittest.main()
