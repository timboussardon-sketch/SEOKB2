import contextlib
import importlib.util
import io
import json
import tempfile
import unittest
from datetime import date
from pathlib import Path

MODULE = Path(__file__).with_name("workflow.py")
SPEC = importlib.util.spec_from_file_location("strategie_mot_cle_workflow", MODULE)
workflow = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(workflow)


class WorkflowTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.vault = Path(self.tmp.name)
        (self.vault / "AGENTS.md").write_text("# Test vault\n")
        (self.vault / "raw" / "clients").mkdir(parents=True)
        (self.vault / "raw" / "clients" / "call.md").write_text("Cas client réel et mesure datée. Comment choisir un logiciel de planning ? Le client veut réduire les erreurs.\n")
        with contextlib.redirect_stdout(io.StringIO()):
            workflow.run(["init", "--vault", str(self.vault), "--keyword", "logiciel planning"])
        self.state = next((self.vault / "wiki" / "strategie-mot-cle").glob("*.json"))

    def tearDown(self):
        self.tmp.cleanup()

    def submit(self, phase, data):
        input_path = self.vault / "candidate.json"
        input_path.write_text(json.dumps(data, ensure_ascii=False))
        with contextlib.redirect_stdout(io.StringIO()):
            workflow.run(["submit", "--state", str(self.state), "--phase", str(phase), "--input", str(input_path)])

    def load_method(self, phase):
        with contextlib.redirect_stdout(io.StringIO()):
            workflow.run(["load-method", "--state", str(self.state), "--phase", str(phase)])

    def approve(self, phase, confirmed=True):
        args = ["approve", "--state", str(self.state), "--phase", str(phase), "--message", f"Je valide l'étape {phase}"]
        if confirmed:
            args.append("--user-approved")
        with contextlib.redirect_stdout(io.StringIO()):
            workflow.run(args)

    @staticmethod
    def intentions(count=5):
        return {"business": {
            "offer": "Logiciel de planning", "prospect": "Responsable d'équipe", "problem": "Erreurs de planning",
            "conversion_action": "Demander une démo", "keyword_value": "Choisir un logiciel adapté",
            "sources": ["raw/clients/call.md"],
            "existing_url": {"status": "none_found", "url": None, "check": "Inventaire des pages fourni par le projet consulté"},
        }, "count_reason": "Seuls ces besoins distincts sont étayés", "dedup_review": "Les variantes de formulation du même besoin ont été regroupées",
            "micro_intentions": [
            {"id": f"m{i}", "query": f"Requête business {i}", "category": "Do", "want": f"Décider {i}",
             "business_signal": "devis", "status": "observed" if i == 1 else "hypothesis",
             "source": "raw/clients/call.md" if i == 1 else None,
             "source_excerpt": "Le client veut réduire les erreurs." if i == 1 else None,
             "decision_need": f"Besoin distinct {i}", "buyer_task": "choisir", "business_link": "Choisir le logiciel avant une démo",
             "distinctness_reason": f"Besoin spécifique {i}"}
            for i in range(1, count + 1)
        ]}

    @staticmethod
    def questions(count=15, micro_count=5):
        return {"count_reason": "Nombre limité aux besoins utiles", "research_log": [
            {"tier": "terrain", "sources": ["raw/clients/call.md"], "finding": "Question d'achat retrouvée dans l'appel"},
            {"tier": "search", "sources": [], "finding": "Aucun export fourni", "unavailable_reason": "GSC et recherches non disponibles dans le coffre test"},
            {"tier": "expertise", "sources": [], "finding": "Aucune note métier fournie", "unavailable_reason": "Pas de document d'expertise dans le coffre test"},
        ], "questions": [
            {"id": f"q{i}", "question": "Comment choisir un logiciel de planning ?" if i == 1 else f"Comment choisir la solution {i} ?", "micro_id": f"m{(i - 1) % micro_count + 1}",
             "origin": "terrain" if i == 1 else "hypothesis", "status": "observed" if i == 1 else "hypothesis",
             "source": "raw/clients/call.md" if i == 1 else None,
             "source_excerpt": "Comment choisir un logiciel de planning ?" if i == 1 else None,
             "gap": "Cas d'usage non abordé dans les pièces consultées" if i > 1 else None} for i in range(1, count + 1)
        ]}

    @staticmethod
    def proof(kind="cas"):
        return {"kind": kind, "source": "raw/clients/call.md", "source_excerpt": "Cas client réel et mesure datée.",
                "detail": "Application réelle", "supports": "Le client veut réduire les erreurs", "proprietary": True,
                "provenance_reason": "Appel du client", "relevance": "direct", "relevance_reason": "Le client décrit précisément son problème",
                "quality": {"reliable": True, "current": True, "usable": True, "reliability_reason": "Source primaire attribuée",
                            "freshness_reason": "Situation toujours applicable vérifiée", "usability_reason": "Contexte exploitable",
                            "source_date": None, "checked_at": date.today().isoformat()},
                "period": "Période donnée dans le document", "attribution": "Client du projet"}

    def test_validation_blocks_skipped_phases_and_unapproved_transition(self):
        with self.assertRaisesRegex(ValueError, "étape 1 non validée"):
            self.submit(2, self.questions())
        with self.assertRaisesRegex(ValueError, "non chargé"):
            self.submit(1, self.intentions())
        self.load_method(1)
        self.submit(1, self.intentions())
        with self.assertRaisesRegex(ValueError, "accord explicite"):
            self.approve(1, confirmed=False)
        with self.assertRaisesRegex(ValueError, "étape 1 non validée"):
            self.submit(2, self.questions())
        self.approve(1)
        with self.assertRaisesRegex(ValueError, "non chargé"):
            self.submit(2, self.questions())
        self.load_method(2)
        self.submit(2, self.questions())
        with self.assertRaisesRegex(ValueError, "étape 2 non validée"):
            self.submit(3, {"scores": []})
        self.approve(2)
        scores = [{"id": item_id, "response_target": "Réduire les erreurs de planning", "score": 0, "evidence": [], "missing": "Cas à collecter"}
                  for item_id in [f"m{i}" for i in range(1, 6)] + [f"q{i}" for i in range(1, 16)]]
        scores[0]["score"] = 1
        scores[0]["evidence"] = [self.proof()]
        self.submit(3, {"scores": scores})
        with self.assertRaisesRegex(ValueError, "accord explicite"):
            self.approve(3, confirmed=False)
        self.approve(3)
        state = json.loads(self.state.read_text())
        self.assertEqual(state["approvals"], {"1": True, "2": True, "3": True})
        page = self.state.with_suffix(".md").read_text()
        self.assertIn("## Étape 1", page)
        self.assertIn("## Étape 2", page)
        self.assertIn("## Étape 3", page)
        self.assertIn("sha256:", page)

    def test_observed_source_must_exist_inside_current_vault(self):
        self.load_method(1)
        data = self.intentions()
        data["micro_intentions"][0]["source"] = "../../outside.md"
        with self.assertRaisesRegex(ValueError, "source introuvable"):
            self.submit(1, data)
        data["micro_intentions"][0]["source"] = "raw/clients/call.md"
        self.submit(1, data)

    def test_business_qualification_required_before_intentions(self):
        data = self.intentions()
        del data["business"]
        with self.assertRaisesRegex(ValueError, "qualification business"):
            workflow.validate_phase_1(data, self.vault)
        data = self.intentions()
        data["business"]["existing_url"]["status"] = "unknown"
        with self.assertRaisesRegex(ValueError, "recherche préalable"):
            workflow.validate_phase_1(data, self.vault)

    def test_variable_counts_and_distinct_buyer_needs(self):
        for count in (3, 7):
            workflow.validate_phase_1(self.intentions(count), self.vault)
        data = self.intentions(3)
        data["micro_intentions"][1]["decision_need"] = data["micro_intentions"][0]["decision_need"]
        with self.assertRaisesRegex(ValueError, "besoin déjà couvert"):
            workflow.validate_phase_1(data, self.vault)
        data = self.intentions(3)
        data["count_reason"] = ""
        with self.assertRaisesRegex(ValueError, "objectif de cinq"):
            workflow.validate_phase_1(data, self.vault)

    def test_dynamic_full_workflow_scores_only_actual_items(self):
        self.load_method(1)
        self.submit(1, self.intentions(3))
        self.approve(1)
        self.load_method(2)
        self.submit(2, self.questions(4, 3))
        self.approve(2)
        ids = ["m1", "m2", "m3", "q1", "q2", "q3", "q4"]
        scores = [{"id": item_id, "response_target": "Réponse à préparer", "score": 0, "evidence": [], "missing": "À collecter"} for item_id in ids]
        self.submit(3, {"scores": scores})
        state = json.loads(self.state.read_text())
        self.assertEqual(len(state["outputs"]["3"]["scores"]), 7)

    def test_terrain_first_and_hypotheses_require_research_and_gap(self):
        micros = self.intentions()["micro_intentions"]
        questions = self.questions()
        del questions["research_log"]
        with self.assertRaisesRegex(ValueError, "rechercher terrain"):
            workflow.validate_phase_2(questions, self.vault, micros)
        questions = self.questions()
        questions["questions"][1]["gap"] = ""
        with self.assertRaisesRegex(ValueError, "lacune"):
            workflow.validate_phase_2(questions, self.vault, micros)
        questions = self.questions()
        first, second = questions["questions"][:2]
        first["origin"], first["status"], first["gap"] = "hypothesis", "hypothesis", "Besoin manquant"
        second["origin"], second["status"] = "terrain", "observed"
        second["source"], second["source_excerpt"] = "raw/clients/call.md", "Cas client réel et mesure datée."
        with self.assertRaisesRegex(ValueError, "dans l'ordre terrain"):
            workflow.validate_phase_2(questions, self.vault, micros)

    def test_score_counts_only_eligible_categories_once(self):
        ids = ["m1"]
        scores = [{"id": "m1", "response_target": "Réduire les erreurs", "score": 5, "evidence": [], "missing": "À collecter"}]
        with self.assertRaisesRegex(ValueError, "note incohérente"):
            workflow.validate_phase_3({"scores": scores}, self.vault, ids)
        scores[0]["score"] = 1
        scores[0]["evidence"] = [self.proof(), self.proof()]
        workflow.validate_phase_3({"scores": scores}, self.vault, ids)

    def test_indirect_unreliable_outdated_or_unusable_proofs_do_not_score(self):
        for rejected_by in ("relevance", "proprietary", "reliable", "current", "usable"):
            with self.subTest(rejected_by=rejected_by):
                proofs = [self.proof(kind) for kind in workflow.EVIDENCE_KINDS]
                for proof in proofs:
                    if rejected_by == "relevance":
                        proof["relevance"] = "indirect"
                    elif rejected_by == "proprietary":
                        proof["proprietary"] = False
                    else:
                        proof["quality"][rejected_by] = False
                item = {"id": "m1", "response_target": "Réponse spécifique", "score": 0, "evidence": proofs, "missing": "Collecter des preuves adaptées"}
                workflow.validate_phase_3({"scores": [item]}, self.vault, ["m1"])
                item["score"] = 5
                with self.assertRaisesRegex(ValueError, "note incohérente"):
                    workflow.validate_phase_3({"scores": [item]}, self.vault, ["m1"])

    def test_proof_excerpt_must_be_found_in_document(self):
        proof = self.proof()
        proof["source_excerpt"] = "Citation inventée"
        item = {"id": "m1", "response_target": "Réponse spécifique", "score": 1, "evidence": [proof], "missing": ""}
        with self.assertRaisesRegex(ValueError, "extrait absent"):
            workflow.validate_phase_3({"scores": [item]}, self.vault, ["m1"])

    def test_approval_rechecks_qualification_in_existing_drafts(self):
        self.load_method(1)
        self.submit(1, self.intentions())
        state = json.loads(self.state.read_text())
        del state["outputs"]["1"]["business"]
        self.state.write_text(json.dumps(state))
        with self.assertRaisesRegex(ValueError, "qualification business"):
            self.approve(1)
        self.assertEqual(json.loads(self.state.read_text())["approvals"], {})


if __name__ == "__main__":
    unittest.main()
