"""Full workflow tests with real validators and explicitly synthetic provider/approvals."""
import _env  # noqa: F401  (coffre de test installé, chemins de scripts/team)
import importlib.util
from pathlib import Path
import tempfile
import unittest

from team import Team
from keyword_adapter import KB, load_methods
from test_contracts import fixture
from test_contracts_v3 import fixture_v3
from test_gtm import fixture_v4

spec = importlib.util.spec_from_file_location('canonical_fixtures', Path(__file__).resolve().parents[1] / 'strategie-mot-cle' / 'test_workflow.py')
canonical = importlib.util.module_from_spec(spec)
spec.loader.exec_module(canonical)


class EndToEndTest(unittest.TestCase):
    def exercise(self, mode, count, version=2):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            vault = root / 'vault'
            (vault / 'raw/clients').mkdir(parents=True)
            (vault / 'AGENTS.md').write_text('Test synthétique isolé, aucun client réel')
            (vault / 'raw/clients/call.md').write_text('Cas client réel et mesure datée. Comment choisir un logiciel de planning ? Le client veut réduire les erreurs.')
            receipt = vault / 'synthetic-response.json'
            receipt.write_text('Réponse synthétique sans lien.')
            team = Team(root / 'data')
            launched = team.start(dict(name='Fixture', site='example.invalid', objective='Test synthétique', request='Contexte synthétique du test', workflow_version=version, mode=mode, vault=str(vault), **({'keywords':['mot '+str(i) for i in range(count)]} if version == 2 else {'test_candidate_count':count+2, 'test_selection_count':count}), sources=[str(receipt)]))
            project = launched['project']['id']
            calls = []
            def provider(task, workspace):
                m = task['mission']
                calls.append((m['role'], m['phase'], m['subject'].get('agent_key')))
                if m['role'] == 'strategie-mot-cle':
                    _, hashes = load_methods(task)
                    if m['phase'] == 'intentions': payload = canonical.WorkflowTest.intentions()
                    elif m['phase'] == 'questions': payload = canonical.WorkflowTest.questions()
                    else:
                        ids = ['m'+str(i) for i in range(1,6)] + ['q'+str(i) for i in range(1,16)]
                        payload = {'scores': [dict(id=i,response_target='À documenter',score=0,missing='Collecte nécessaire pour la fixture',evidence=[]) for i in ids]}
                    r = dict(status='review',summary='Résultat synthétique',artifact_markdown='# Test synthétique',facts=[],blockers=[],next_actions=[],keyword_payload=payload,method_hashes=hashes)
                else:
                    r = fixture_v4(task, receipt) if version == 4 else fixture_v3(task, receipt) if version == 3 else fixture(task, receipt)
                r['_execution'] = {'provider':'synthetic-fixture', 'mode':'test', 'workspace':str(workspace)}
                return r
            waves = 0
            while not team.next(project)['complete']:
                waves += 1
                self.assertLess(waves, 50, 'Workflow bloqué ou boucle')
                output = team.run_ready(project, max_jobs=3, workers=3, provider=provider)
                self.assertFalse(output['errors'], output['errors'])
                self.assertTrue(output['results'], output['next'])
                for result in output['results']:
                    self.assertEqual(result['status'], 'review')
                    team.approve(result['id'], result['sha'], 'Validation simulée du test seulement', True)
            current = team.status(project)
            if version >= 3:
                phases = [c[1] for c in calls]
                self.assertLess(phases.index('strategie-globale'), phases.index('priorisation'))
                self.assertLess(phases.index('priorisation'), phases.index('intentions'))
                self.assertLess(phases.index('preuves'), phases.index('consolidation'))
                self.assertFalse(launched['project']['brief'].get('keywords'))
                if version == 4:
                    self.assertLess(phases.index('gtm-transmission'), phases.index('exploration'))
            keyword_calls = [c for c in calls if c[0] == 'strategie-mot-cle']
            self.assertEqual(len(keyword_calls), count * 3)
            self.assertEqual(len(set(c[2] for c in keyword_calls)), count)
            self.assertEqual(len(team.bundle(project)['keywords']), count)
            self.assertEqual(any(c[1]=='observations' for c in calls), mode=='seo-geo')
            before = current['events']
            self.assertTrue(team.next(project)['complete'])
            self.assertEqual(team.status(project)['events'], before)
            first = next(m for m in current['missions'] if m['phase']=='intentions')
            team.revise(first['id'], 'Correction synthétique de la première stratégie')
            self.assertFalse(team.next(project)['complete'])
            self.assertEqual(next(m for m in team.status(project)['missions'] if m['phase']=='controle')['status'], 'queued')

    def test_seo_five_keywords_real_validators(self):
        self.exercise('seo', 5)

    def test_geo_ten_keywords_real_validators(self):
        self.exercise('seo-geo', 10)

    def test_v3_global_first_seo_without_keywords(self):
        self.exercise('seo', 5, version=3)

    def test_v3_global_first_geo_ten_selected_from_twelve(self):
        self.exercise('seo-geo', 10, version=3)

    def test_v4_gtm_then_full_seo(self):
        self.exercise('seo', 5, version=4)

    def test_v4_gtm_then_full_geo(self):
        self.exercise('seo-geo', 5, version=4)


if __name__ == '__main__': unittest.main()
