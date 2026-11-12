"""Strategy before keyword specialization; fixtures are explicitly simulated."""
import _env  # noqa: F401  (coffre de test installé, chemins de scripts/team)
import sys
import tempfile
import types
import unittest
from unittest.mock import patch
from team import Team

SELECTED = ['business ' + str(i) for i in range(5)]


def brief(mode='seo-geo'):
    return dict(name='Fixture v3', site='example.invalid', objective='Test technique', request='Fixture', mode=mode, workflow_version=3)


def result(phase, selected=None):
    payload = {'keywords': selected or SELECTED} if phase == 'priorisation' else {'verdict': 'conforme'} if phase == 'controle' else {}
    return dict(status='review', summary='Fixture', artifact_markdown='Fixture ' + phase, facts=[],
                blockers=[], next_actions=[], stage_payload=payload, keyword_payload={})


class V3Test(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.team = Team(self.tmp.name)
        self.mocks = patch.dict(sys.modules, {'contracts': types.SimpleNamespace(validate=lambda *a: None),
                                             'keyword_adapter': types.SimpleNamespace(validate=lambda *a: None)})
        self.mocks.start()
        created = self.team.start(brief())
        self.project, self.cadrage = created['project']['id'], created['mission']

    def tearDown(self):
        self.mocks.stop(); self.tmp.cleanup()

    def approve(self, mission, selected=None):
        m = self.team.submit(mission['id'], result(mission['phase'], selected))
        return self.team.approve(m['id'], m['sha'], 'Accord simulé', True)

    def through(self, target):
        for _ in range(30):
            self.team.prepare(self.project)
            ready = self.team.next(self.project)['ready']
            self.assertTrue(ready)
            for m in ready:
                self.approve(m)
                if m['phase'] == target:
                    return m
        self.fail('Phase non atteinte ' + target)

    def test_start_without_keywords_and_seeds_never_fanout(self):
        p = self.team.status(self.project)['projects'][0]
        self.assertEqual(p['brief']['workflow_version'], 3)
        self.assertEqual(p['brief']['seeds'], [])
        self.assertNotIn('keywords', p['brief'])
        seeded = brief(); seeded['keywords'] = ['seul terme indicatif']
        p = self.team.start(seeded)['project']
        self.assertEqual(p['brief']['seeds'], ['seul terme indicatif'])
        self.assertNotIn('keywords', p['brief'])
        with self.assertRaisesRegex(ValueError, 'priorisation'):
            self.team.fanout(p['id'])

    def test_global_strategy_then_selection_then_agents(self):
        global_mission = self.through('strategie-globale')
        missions = self.team.status(self.project)['missions']
        self.assertFalse(any(m['role'] == 'strategie-mot-cle' for m in missions))
        self.assertFalse(any(m['phase'] == 'priorisation' for m in missions))
        with self.assertRaisesRegex(ValueError, 'priorisation'):
            self.team.fanout(self.project)
        next_state = self.team.prepare(self.project)['next']
        self.assertEqual([m['phase'] for m in next_state['ready']], ['priorisation'])
        self.approve(next_state['ready'][0])
        agents = self.team.fanout(self.project)
        self.assertEqual([m['subject']['keyword'] for m in agents], SELECTED)
        self.assertEqual(len(agents), 5)
        first = agents[0]
        with self.team.db() as db:
            upstream = self.team._upstream(db, first)
        self.assertIn(global_mission['id'], [m['id'] for m in upstream])
        self.assertEqual(len(self.team.prepare(self.project)['created']), 0)

    def test_global_architecture_does_not_need_keyword_bundle(self):
        self.through('architecture')
        self.assertFalse(any(m['role'] == 'strategie-mot-cle' for m in self.team.status(self.project)['missions']))
        with self.assertRaises(ValueError):
            self.team.bundle(self.project)

    def test_full_v3_and_final_consolidation(self):
        self.through('controle')
        state = self.team.next(self.project)
        self.assertTrue(state['complete'])
        missions = self.team.status(self.project)['missions']
        phases = [m['phase'] for m in missions]
        self.assertLess(phases.index('strategie-globale'), phases.index('priorisation'))
        self.assertLess(phases.index('priorisation'), phases.index('intentions'))
        self.assertLess(phases.index('preuves'), phases.index('consolidation'))
        self.assertEqual(len(self.team.bundle(self.project)['keywords']), 5)

    def test_keyword_correction_preserves_global_strategy(self):
        self.through('controle')
        missions = self.team.status(self.project)['missions']
        question = next(m for m in missions if m['phase'] == 'questions')
        affected = self.team.revise(question['id'], 'Correction du spécialiste')['affected']
        for phase in ['architecture', 'roadmap', 'strategie-globale', 'priorisation']:
            self.assertNotIn(next(m['id'] for m in missions if m['phase'] == phase), affected)
        for phase in ['consolidation', 'controle']:
            self.assertIn(next(m['id'] for m in missions if m['phase'] == phase), affected)
        self.assertFalse(self.team.next(self.project)['complete'])

    def test_global_correction_invalidates_all_keyword_agents(self):
        self.through('controle')
        missions = self.team.status(self.project)['missions']
        strategy = next(m for m in missions if m['phase'] == 'strategie-globale')
        affected = self.team.revise(strategy['id'], 'Correction globale')['affected']
        self.assertTrue(all(m['id'] in affected for m in missions if m['role'] == 'strategie-mot-cle'))
        self.assertFalse(self.team.next(self.project)['complete'])
        self.assertEqual([m['phase'] for m in self.team.next(self.project)['ready']], ['strategie-globale'])

    def test_portfolio_change_after_fanout_explicitly_refused(self):
        prior = self.through('priorisation')
        self.team.fanout(self.project)
        self.team.revise(prior['id'], 'Autres mots-clés')
        with self.assertRaisesRegex(ValueError, 'nouveau projet'):
            self.team.submit(prior['id'], result('priorisation', ['autre ' + str(i) for i in range(5)]))
        state = self.team.next(self.project)
        self.assertFalse(state['complete'])
        self.assertEqual(state['keyword_portfolio'], SELECTED)
        self.approve(next(m for m in state['ready'] if m['phase'] == 'priorisation'))
        self.assertEqual(len(self.team.fanout(self.project)), 5)

    def test_seo_without_ia(self):
        started = self.team.start(brief('seo'))
        self.project = started['project']['id']
        self.through('controle')
        phases = [m['phase'] for m in self.team.status(self.project)['missions']]
        self.assertNotIn('panel', phases)
        self.assertNotIn('observations', phases)
        self.assertIn('exploration', phases)
        self.assertTrue(self.team.next(self.project)['complete'])


if __name__ == '__main__':
    unittest.main()
