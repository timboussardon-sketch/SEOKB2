import copy
import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location("roadmap_consolidation", Path(__file__).with_name("consolidate.py"))
roadmap = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(roadmap)


class ConsolidationTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.vault = Path(self.tmp.name).resolve()
        (self.vault / "wiki" / "strategie-mot-cle").mkdir(parents=True)
        self.manifest = {"site": "client.test", "keywords": [],
                         "bundle": "wiki/roadmap-seo/strategies.json", "roadmap": "wiki/roadmap-seo/roadmap.md"}
        for number in range(1, 6):
            keyword = f"Mot-clé business {number}"
            relative = f"wiki/strategie-mot-cle/strategie-{number}.json"
            self.manifest["keywords"].append({"keyword": keyword, "state": relative})
            state = self.strategy(keyword)
            (self.vault / relative).write_text(json.dumps(state, ensure_ascii=False))
        self.path = self.vault / "wiki" / "manifest.json"
        self.path.write_text(json.dumps(self.manifest))

    def tearDown(self):
        self.tmp.cleanup()

    def strategy(self, keyword):
        digest = hashlib.sha256(b"method fixture").hexdigest()
        methods = {name: {"path": f"fixture/{name}.md", "sha256": digest}
                   for name in ("micro_intentions", "micro_intentions_tool", "geo_citations")}
        return {"vault": str(self.vault), "keyword": keyword, "methods": methods,
                "loaded_methods": {"1": {"micro_intentions": digest, "micro_intentions_tool": digest}, "2": {"geo_citations": digest}},
                "approvals": {"1": True, "2": True, "3": True},
                "history": [{"phase": phase, "message": f"Je valide cette étape {phase}"} for phase in (1, 2, 3)],
                "outputs": {
                    "1": {"business": {"offer": "Offre du client", "prospect": "Acheteur", "problem": "Problème réel",
                                       "conversion_action": "Demander un devis", "keyword_value": "Besoin proche de l'offre",
                                       "sources": [], "user_context": "Contexte donné par Tim pour le test",
                                       "existing_url": {"status": "none_found", "url": None, "check": "Inventaire du test consulté"}},
                          "count_reason": "Un seul besoin distinct dans le test", "dedup_review": "Variantes regroupées",
                          "micro_intentions": [{"id": "m1", "query": "Comment choisir la solution ?", "category": "Do", "want": "Choisir",
                                                "business_signal": "devis", "decision_need": "choix de solution", "buyer_task": "choisir",
                                                "business_link": "Choisir avant le devis", "distinctness_reason": "Besoin distinct",
                                                "status": "hypothesis", "source": None}]},
                    "2": {"count_reason": "Une question utile dans le test", "research_log": [
                        {"tier": tier, "sources": [], "finding": "Aucune pièce dans la fixture", "unavailable_reason": "Coffre de test"}
                        for tier in ("terrain", "search", "expertise")],
                        "questions": [{"id": "q1", "question": "Quelle solution choisir ?", "micro_id": "m1", "origin": "hypothesis",
                                       "status": "hypothesis", "source": None, "gap": "Critère absent des sources test"}]},
                    "3": {"scores": [{"id": item_id, "response_target": "Critère de choix", "score": 0,
                                      "evidence": [], "missing": "Cas à collecter"} for item_id in ("m1", "q1")]}}}

    def modify(self, index, edit):
        path = self.vault / self.manifest["keywords"][index]["state"]
        state = json.loads(path.read_text())
        edit(state)
        path.write_text(json.dumps(state, ensure_ascii=False))

    def test_five_validated_strategies_produce_one_shared_bundle(self):
        manifest = roadmap.read_manifest(self.vault, self.path)
        report, _ = roadmap.inspect(self.vault, manifest)
        self.assertTrue(report["ready"])
        self.assertEqual(report["expected"], 5)
        output = roadmap.bundle(self.vault, manifest)
        data = json.loads(output.read_text())
        self.assertEqual(data["strategy_count"], 5)
        self.assertEqual(len({s["keyword"] for s in data["strategies"]}), 5)
        self.assertEqual(data["roadmap"], "wiki/roadmap-seo/roadmap.md")
        self.assertEqual(len(list(output.parent.glob("*.json"))), 1)
        self.assertEqual(roadmap.bundle(self.vault, manifest), output)

    def test_one_pending_validation_blocks_the_whole_bundle(self):
        self.modify(4, lambda state: state["approvals"].update({"3": False}))
        report, _ = roadmap.inspect(self.vault, self.manifest)
        self.assertFalse(report["ready"])
        self.assertEqual(report["validated"], 4)
        self.assertIn("étape 3 non validée", report["strategies"][4]["reason"])
        with self.assertRaisesRegex(ValueError, "consolidation bloquée"):
            roadmap.bundle(self.vault, self.manifest)
        self.assertFalse((self.vault / self.manifest["bundle"]).exists())

    def test_duplicate_keywords_and_outside_vault_paths_are_rejected(self):
        manifest = copy.deepcopy(self.manifest)
        manifest["keywords"][1]["keyword"] = manifest["keywords"][0]["keyword"].upper()
        self.path.write_text(json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, "dupliqué"):
            roadmap.read_manifest(self.vault, self.path)
        manifest = copy.deepcopy(self.manifest)
        manifest["keywords"][0]["state"] = "../other/state.json"
        self.path.write_text(json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, "hors coffre"):
            roadmap.read_manifest(self.vault, self.path)

    def test_wrong_keyword_or_vault_cannot_supply_an_analysis(self):
        self.modify(0, lambda state: state.update({"keyword": "Autre mot-clé"}))
        self.modify(1, lambda state: state.update({"vault": str(self.vault.parent / "other")}))
        report, _ = roadmap.inspect(self.vault, self.manifest)
        self.assertFalse(report["ready"])
        self.assertIn("différent du portefeuille", report["strategies"][0]["reason"])
        self.assertIn("autre coffre", report["strategies"][1]["reason"])

    def test_approval_flags_do_not_hide_an_invalid_result(self):
        self.modify(0, lambda state: state["outputs"]["3"]["scores"][0].update({"score": 5}))
        self.modify(1, lambda state: state.update({"history": []}))
        report, _ = roadmap.inspect(self.vault, self.manifest)
        self.assertFalse(report["ready"])
        self.assertIn("note incohérente", report["strategies"][0]["reason"])
        self.assertIn("sans trace", report["strategies"][1]["reason"])

    def test_changed_strategy_does_not_overwrite_an_existing_snapshot(self):
        output = roadmap.bundle(self.vault, self.manifest)
        before = output.read_bytes()
        self.modify(0, lambda state: state["outputs"]["3"]["scores"][0].update({"missing": "Nouveau cas à collecter"}))
        with self.assertRaisesRegex(ValueError, "nouvelle révision"):
            roadmap.bundle(self.vault, self.manifest)
        self.assertEqual(output.read_bytes(), before)

    def test_tracking_state_cannot_replace_a_keyword_strategy(self):
        manifest = copy.deepcopy(self.manifest)
        manifest["roadmap"] = "wiki/strategie-mot-cle/strategie-1.md"
        self.path.write_text(json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, "suivi en conflit"):
            roadmap.read_manifest(self.vault, self.path)


if __name__ == "__main__":
    unittest.main()
