"""Coordinator integration tests; fake domain adapter is explicit, no model calls."""
import _env  # noqa: F401  (coffre de test installé, chemins de scripts/team)
import copy
import json
from pathlib import Path
import sys
import tempfile
import types
import unittest
from unittest.mock import patch
from team import Team


def brief():
    return {'name': 'Fixture', 'site': 'example.test', 'objective': 'Test', 'request': 'Fixture technique',
            'mode': 'seo-geo', 'workflow_version': 1, 'keywords': ['alpha', 'beta', 'gamma', 'delta', 'epsilon']}


def result(text='Fixture, aucune collecte réelle'):
    return {'status': 'review', 'summary': text, 'artifact_markdown': text,
            'facts': [], 'blockers': [], 'next_actions': []}


class TeamTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.team = Team(self.temp.name)
        self.adapter = patch.dict(sys.modules, {'keyword_adapter': types.SimpleNamespace(validate=lambda task, result: None)})
        self.adapter.start()
        started = self.team.start(brief())
        self.project = started['project']['id']
        self.cadrage = started['mission']

    def tearDown(self):
        self.adapter.stop()
        self.temp.cleanup()

    def approve(self, m):
        submitted = self.team.submit(m['id'], result())
        return self.team.approve(m['id'], submitted['sha'], 'Accord fictif de test', True)

    def full(self):
        self.approve(self.cadrage)
        keywords = self.team.fanout(self.project)
        for m in keywords:
            self.approve(m)
            q = self.team.advance(m['id'])
            self.approve(q)
            p = self.team.advance(q['id'])
            self.approve(p)
        return keywords

    def test_keywords_count_duplicates_and_blank(self):
        for words in ([], ['a'] * 5, ['a', 'b', 'c', 'd', ' '], list(map(str, range(11)))):
            b = brief(); b['keywords'] = words
            with self.assertRaises(ValueError): self.team.start(b)
        b = brief(); b['keywords'] = list(map(str, range(10)))
        self.assertEqual(len(self.team.start(b)['project']['brief']['keywords']), 10)

    def test_gate_fanout_idempotent_and_resume(self):
        with self.assertRaises(ValueError): self.team.fanout(self.project)
        self.approve(self.cadrage)
        missions = self.team.fanout(self.project)
        self.assertEqual(len(missions), 5)
        self.assertEqual([m['id'] for m in missions], [m['id'] for m in self.team.fanout(self.project)])
        with self.assertRaises(ValueError): self.team.advance(missions[0]['id'])
        resumed = Team(self.temp.name)
        self.assertEqual(len(resumed.next(self.project)['ready']), 5)
        before = resumed.status(self.project)
        resumed.next(self.project)
        self.assertEqual(before, resumed.status(self.project))

    def test_wrong_sha_no_auto_approval_and_tamper(self):
        submitted = self.team.submit(self.cadrage['id'], result())
        with self.assertRaises(ValueError): self.team.approve(submitted['id'], submitted['sha'], 'oui', False)
        with self.assertRaises(ValueError): self.team.approve(submitted['id'], 'wrong', 'oui', True)
        Path(submitted['artifact_path']).write_text('modified')
        with self.assertRaises(ValueError): self.team.approve(submitted['id'], submitted['sha'], 'oui', True)

    def test_bundle_and_revision_invalidate_descendants(self):
        keywords = self.full()
        self.assertEqual(len(self.team.bundle(self.project)['keywords']), 5)
        plan = self.team.add_mission(self.project, 'architecture-roadmap', 'architecture', {}, [self.cadrage['id']])
        self.approve(plan)
        quality = self.team.add_mission(self.project, 'qualite', 'controle', {}, [plan['id']])
        self.approve(quality)
        prior = {m['id']: m for m in self.team.status(self.project)['missions']}
        affected = self.team.revise(keywords[0]['id'], 'Corriger le besoin')
        self.assertIn(plan['id'], affected['affected'])
        self.assertIn(quality['id'], affected['affected'])
        self.assertEqual(len(affected['affected']), 5)
        with self.assertRaises(ValueError): self.team.bundle(self.project)
        self.assertTrue(Path(prior[plan['id']]['artifact_path']).is_file())
        after = {m['id']: m for m in self.team.status(self.project)['missions']}
        self.assertEqual(after[keywords[1]['id']]['status'], 'approved')
        self.assertEqual(after[keywords[0]['id']]['version'], 2)
        self.assertEqual(len(self.team.next(self.project)['ready']), 1)

    def test_cannot_consolidate_partial_portfolio(self):
        self.approve(self.cadrage)
        first = self.team.fanout(self.project)[0]
        self.approve(first)
        q = self.team.advance(first['id']); self.approve(q)
        p = self.team.advance(q['id']); self.approve(p)
        with self.assertRaises(ValueError): self.team.bundle(self.project)
        with self.assertRaises(ValueError): self.team.add_mission(self.project, 'architecture-roadmap', 'plan', {}, [p['id']])

    def test_no_cross_project_dependency_or_keyword_override(self):
        other = self.team.start(brief())
        with self.assertRaises(ValueError): self.team.add_mission(self.project, 'business', 'collecte', {}, [other['mission']['id']])
        with self.assertRaises(ValueError): self.team.add_mission(self.project, 'strategie-mot-cle', 'preuves', {'keyword': 'rogue'}, [self.cadrage['id']])

    def test_provider_failure_retry_and_trace(self):
        def fails(task, workspace): raise RuntimeError('Test failure')
        with self.assertRaises(RuntimeError): self.team.run(self.cadrage['id'], provider=fails)
        self.assertEqual(self.team.status(self.project)['missions'][0]['status'], 'failed')
        self.team.retry(self.cadrage['id'])
        def succeeds(task, workspace):
            self.assertEqual(task['project']['id'], self.project)
            return dict(result(), _execution={'mode': 'test', 'provider': 'fixture'})
        m = self.team.run(self.cadrage['id'], provider=succeeds)
        self.assertEqual(m['status'], 'review')
        self.assertEqual(m['execution']['mode'], 'test')
        with self.assertRaises(ValueError): self.team.submit(m['id'], result('overwrite'))

    def test_recover_requires_stopped_owner(self):
        with self.team.db() as db:
            m = self.team._get(db, 'missions', self.cadrage['id'])
            m.update(status='running', owner_pid=123456789)
            self.team._save(db, m)
        recovered = self.team.recover(m['id'])
        self.assertEqual(recovered['status'], 'failed')
        self.team.retry(m['id'])
        def provider(task, workspace):
            with self.assertRaises(ValueError): self.team.recover(task['mission']['id'])
            return dict(result(), _execution={'provider': 'fixture', 'mode': 'test'})
        self.assertEqual(self.team.run(m['id'], provider)['status'], 'review')

    def test_normalization_and_vault(self):
        b = brief(); b['keywords'] = ['a  b', 'A b', 'c', 'd', 'e']
        with self.assertRaises(ValueError): self.team.start(b)
        b = brief(); b['keywords'][0] = '  a   b\tc  '
        normalized = self.team.start(b)['project']['brief']
        self.assertEqual(normalized['keywords'][0], 'a b c')
        self.assertTrue(Path(normalized['vault'], 'AGENTS.md').is_file())
        for vault in ('', '/nonexistent-coffre', self.temp.name, None):
            b = brief(); b['vault'] = vault
            with self.assertRaises(ValueError): self.team.start(b)
        vault = Path(self.temp.name) / 'vault'; vault.mkdir(); (vault / 'AGENTS.md').write_text('test')
        b = brief(); b['vault'] = str(vault)
        self.assertEqual(self.team.start(b)['project']['brief']['vault'], str(vault.resolve()))

    def test_architecture_receives_all_keyword_phases(self):
        self.full()
        plan = self.team.add_mission(self.project, 'architecture-roadmap', 'plan', {}, [self.cadrage['id']])
        self.assertEqual(len(plan['depends']), 6)
        def provider(task, workspace):
            phases = [m for m in task['upstream'] if m['role'] == 'strategie-mot-cle']
            self.assertEqual(len(phases), 15)
            self.assertEqual({m['subject']['keyword'] for m in phases}, set(brief()['keywords']))
            return dict(result(), _execution={'provider': 'fixture', 'mode': 'test'})
        submitted = self.team.run(plan['id'], provider)
        proofs = next(m for m in self.team.status(self.project)['missions'] if m['phase'] == 'preuves')
        Path(proofs['artifact_path']).write_text('tampered')
        with self.assertRaises(ValueError): self.team.approve(plan['id'], submitted['sha'], 'Test accord', True)

    def test_retry_gets_new_workspace(self):
        workspaces = []
        def first(task, workspace):
            workspaces.append(workspace)
            (workspace / 'response.json').write_text('stale')
            raise RuntimeError('fixture crash')
        with self.assertRaises(RuntimeError): self.team.run(self.cadrage['id'], first)
        self.team.retry(self.cadrage['id'])
        def second(task, workspace):
            workspaces.append(workspace)
            self.assertFalse((workspace / 'response.json').exists())
            return dict(result(), _execution={'provider': 'fixture', 'mode': 'test'})
        self.team.run(self.cadrage['id'], second)
        self.assertNotEqual(workspaces[0], workspaces[1])
        self.assertTrue((workspaces[0] / 'response.json').exists())

    def test_domain_validation_and_recursive_upstream(self):
        self.approve(self.cadrage)
        m = self.team.fanout(self.project)[0]
        self.approve(m)
        q = self.team.advance(m['id']); self.approve(q)
        p = self.team.advance(q['id'])
        seen = []
        def validate(task, value):
            seen.extend(n['phase'] for n in task['upstream'])
            raise ValueError('Domain fixture rejection')
        with patch.dict(sys.modules, {'keyword_adapter': types.SimpleNamespace(validate=validate)}):
            with self.assertRaises(ValueError): self.team.submit(p['id'], result())
        self.assertIn('intentions', seen)
        self.assertIn('questions', seen)
        current = next(n for n in self.team.status(self.project)['missions'] if n['id'] == p['id'])
        self.assertEqual(current['status'], 'queued')
        self.assertIsNone(current['result'])


if __name__ == '__main__': unittest.main()
