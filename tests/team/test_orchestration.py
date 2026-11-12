"""Full DAG tests, explicitly simulated providers and semantic contracts."""
import _env  # noqa: F401  (coffre de test installé, chemins de scripts/team)
import json
from pathlib import Path
import sys
import tempfile
import threading
import types
import unittest
from unittest.mock import patch

from team import Team


def brief(mode='seo-geo', count=5):
    return dict(name='Workflow fixture', site='example.invalid', objective='Test technique',
                request='Fixture technique', workflow_version=2, mode=mode, keywords=['mot test ' + str(i) for i in range(count)])


def result(phase):
    return dict(status='review', summary='Fixture ' + phase, artifact_markdown='Fixture ' + phase,
                facts=[], blockers=[], next_actions=[], stage_payload={'verdict': 'conforme'} if phase == 'controle' else {},
                keyword_payload={})


class OrchestrationTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.team = Team(self.temp.name)
        self.contract_calls = []
        self.mocks = patch.dict(sys.modules, {
            'keyword_adapter': types.SimpleNamespace(validate=lambda task, value: None),
            'contracts': types.SimpleNamespace(validate=lambda task, value: self.contract_calls.append(task))})
        self.mocks.start()
        self.started = self.team.start(brief())
        self.project = self.started['project']['id']

    def tearDown(self):
        self.mocks.stop()
        self.temp.cleanup()

    def approve(self, m, payload=None):
        candidate = result(m['phase'])
        if payload is not None:
            candidate['stage_payload'] = payload
        submitted = self.team.submit(m['id'], candidate)
        return self.team.approve(m['id'], submitted['sha'], 'Accord simulé', True)

    def finish(self, project=None):
        project = project or self.project
        phases = []
        for _ in range(20):
            self.team.prepare(project)
            state = self.team.next(project)
            if state['complete']:
                return phases
            if not state['ready']:
                self.fail('Workflow figé : ' + json.dumps(state))
            for m in state['ready']:
                phases.append(m['phase'])
                self.approve(m)
        self.fail('Workflow non terminé')

    def test_full_geo_dag_and_idempotent_preparation(self):
        phases = self.finish()
        self.assertEqual(phases.count('intentions'), 5)
        self.assertEqual(phases.count('questions'), 5)
        self.assertEqual(phases.count('preuves'), 5)
        self.assertEqual(phases[-7:], ['panel', 'observations', 'opportunites', 'architecture', 'roadmap', 'synthese', 'controle'])
        count = len(self.team.status(self.project)['missions'])
        self.assertEqual(self.team.prepare(self.project)['created'], [])
        self.assertEqual(len(self.team.status(self.project)['missions']), count)
        self.assertTrue(self.team.next(self.project)['complete'])
        keyword_agents = {}
        for m in self.team.status(self.project)['missions']:
            if m['role'] == 'strategie-mot-cle':
                keyword_agents.setdefault(m['subject']['keyword'], set()).add(m['subject']['agent_key'])
        self.assertEqual(len({next(iter(v)) for v in keyword_agents.values()}), 5)
        self.assertTrue(all(len(v) == 1 for v in keyword_agents.values()))

    def test_seo_mode_skips_ia_only(self):
        p = self.team.start(brief('seo', 10))['project']['id']
        phases = self.finish(p)
        self.assertNotIn('panel', phases)
        self.assertNotIn('observations', phases)
        self.assertEqual(phases.count('preuves'), 10)
        self.assertEqual(phases[-5:], ['opportunites', 'architecture', 'roadmap', 'synthese', 'controle'])

    def test_next_read_only_and_ready_after_approval(self):
        before = self.team.status(self.project)
        state = self.team.next(self.project)
        self.assertEqual(self.team.status(self.project), before)
        self.assertEqual([m['phase'] for m in state['ready']], ['cadrage'])
        self.assertFalse(state['complete'])
        self.approve(self.started['mission'])
        planned = [p for p in self.team.next(self.project)['planned'] if p['can_prepare']]
        self.assertEqual(len(planned), 6)
        self.assertEqual(len(self.team.prepare(self.project)['created']), 6)
        self.assertEqual(self.team.prepare(self.project)['created'], [])

    def test_run_ready_snapshot_stops_at_reviews(self):
        self.approve(self.started['mission'])
        invoked = []
        lock = threading.Lock()
        def provider(task, workspace):
            with lock: invoked.append(task['mission']['phase'])
            return dict(result(task['mission']['phase']), _execution={'provider': 'test', 'mode': 'simulated', 'workspace': str(workspace)})
        outcome = self.team.run_ready(self.project, max_jobs=20, workers=3, provider=provider)
        self.assertEqual(len(outcome['attempted']), 6)
        self.assertEqual(len(outcome['results']), 6)
        self.assertEqual(outcome['errors'], [])
        self.assertEqual(set(invoked), {'intentions', 'diagnostic'})
        self.assertFalse(any(m['phase'] == 'questions' for m in self.team.status(self.project)['missions']))
        self.assertEqual(self.team.run_ready(self.project, max_jobs=20, workers=3, provider=provider)['attempted'], [])

    def test_failed_role_not_automatically_retried(self):
        def broken(task, workspace):
            raise RuntimeError('Test transport failed')
        outcome = self.team.run_ready(self.project, provider=broken)
        self.assertEqual(len(outcome['errors']), 1)
        self.assertEqual(self.team.run_ready(self.project, provider=broken)['attempted'], [])
        self.assertFalse(self.team.next(self.project)['complete'])

    def test_no_generic_add_mission_or_forged_dependencies(self):
        with self.assertRaisesRegex(ValueError, 'prepare'):
            self.team.add_mission(self.project, 'pilote', 'synthese', {}, [self.started['mission']['id']])
        self.approve(self.started['mission'])
        self.team.prepare(self.project)
        m = self.team.next(self.project)['ready'][0]
        with self.team.db() as db:
            forged = self.team._get(db, 'missions', m['id'])
            forged['depends'] = []
            self.team._save(db, forged)
        with self.assertRaisesRegex(ValueError, 'Dépendances'):
            self.team.submit(m['id'], result(m['phase']))

    def test_revision_invalidates_downstream_and_quality(self):
        self.finish()
        missions = self.team.status(self.project)['missions']
        m = next(m for m in missions if m['phase'] == 'questions')
        ids = self.team.revise(m['id'], 'Correction test')['affected']
        self.assertIn(next(m['id'] for m in missions if m['phase'] == 'controle'), ids)
        self.assertIn(next(m['id'] for m in missions if m['phase'] == 'panel'), ids)
        self.assertFalse(self.team.next(self.project)['complete'])
        self.assertEqual([m['id'] for m in self.team.next(self.project)['ready']], [m['id']])

    def test_quality_nonconforme_never_complete(self):
        for _ in range(20):
            self.team.prepare(self.project)
            ready = self.team.next(self.project)['ready']
            for m in ready:
                self.approve(m, {'verdict': 'a_corriger'} if m['phase'] == 'controle' else None)
            if any(m['phase'] == 'controle' for m in ready):
                break
        state = self.team.next(self.project)
        self.assertFalse(state['complete'])
        self.assertTrue(state['blocked'])

    def test_stage_contract_at_submit_and_approve_with_workspace(self):
        m = self.started['mission']
        submitted = self.team.submit(m['id'], result('cadrage'), {'workspace': self.temp.name, 'provider': 'test'})
        self.assertEqual(self.contract_calls[-1]['workspace'], self.temp.name)
        self.team.approve(m['id'], submitted['sha'], 'Accord test', True)
        self.assertEqual(len(self.contract_calls), 2)
        self.assertEqual(self.contract_calls[-1]['workspace'], self.temp.name)

    def test_manual_submit_cannot_race_running_provider(self):
        m = self.started['mission']
        def provider(task, workspace):
            with self.assertRaisesRegex(ValueError, 'Mission en cours'):
                self.team.submit(m['id'], result('cadrage'))
            return dict(result('cadrage'), _execution={'provider': 'test', 'workspace': str(workspace)})
        saved = self.team.run(m['id'], provider)
        self.assertEqual(saved['status'], 'review')

    def test_source_snapshot_suspends_dependents_and_complete(self):
        source = Path(self.temp.name) / 'original.txt'
        source.write_text('Observation fictive conservée')
        r = result('cadrage')
        r['stage_payload'] = {'sources': [{'source_file': str(source), 'excerpt': 'Observation fictive'}]}
        m = self.team.submit(self.started['mission']['id'], r, {'workspace': self.temp.name})
        self.assertEqual(len(m['source_files']), 1)
        self.team.approve(m['id'], m['sha'], 'Accord source test', True)
        self.finish()
        self.assertTrue(self.team.next(self.project)['complete'])
        source.write_text('Texte modifié après approbation')
        state = self.team.next(self.project)
        self.assertFalse(state['complete'])
        self.assertTrue(any('Pièce source' in m.get('blocking_reason', '') for m in state['blocked']))
        with self.assertRaisesRegex(ValueError, 'Pièce source'):
            self.team.bundle(self.project)

    def test_source_snapshot_not_model_controlled(self):
        r = result('cadrage'); r['source_files'] = []
        with self.assertRaisesRegex(ValueError, 'contrôleur'):
            self.team.submit(self.started['mission']['id'], r)
        r = result('cadrage'); r['stage_payload'] = {'nested': {'source_file': '/etc/hosts'}}
        with self.assertRaisesRegex(ValueError, 'hors périmètre'):
            self.team.submit(self.started['mission']['id'], r)

    def test_source_change_before_approval_is_rejected(self):
        source = Path(self.temp.name) / 'trace.txt'
        source.write_text('Original')
        r = result('cadrage'); r['stage_payload'] = {'traces': [{'trace_file': str(source)}]}
        m = self.team.submit(self.started['mission']['id'], r, {'workspace': self.temp.name})
        source.unlink()
        with self.assertRaisesRegex(ValueError, 'Pièce source'):
            self.team.approve(m['id'], m['sha'], 'Accord test', True)

    def test_legacy_not_silently_migrated(self):
        b = brief(); b['workflow_version'] = 1
        old = self.team.start(b)['project']['id']
        with self.assertRaisesRegex(ValueError, 'historique'):
            self.team.prepare(old)


if __name__ == '__main__':
    unittest.main()
