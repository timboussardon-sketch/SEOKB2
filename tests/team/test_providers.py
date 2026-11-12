"""Provider de la team : commande Claude Code, trace d'exécution, erreurs, choix de l'agent.

Aucun appel de modèle : `spawn` est remplacé par un faux agent qui renvoie le JSON de
Claude Code ou de Codex. Les tests du processus lancent un vrai sous-processus Python.
"""
import _env  # noqa: F401  (coffre de test installé, chemins de scripts/team)
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import patch

import providers
from paths import pid_alive
from team import Team
from test_gtm import fixture_v4


def raw_from(result):
    """Réponse brute de l'agent : les payloads voyagent en chaînes JSON."""
    return {'status': result['status'], 'summary': result['summary'], 'artifact_markdown': result['artifact_markdown'],
            'facts': result['facts'], 'blockers': result['blockers'], 'next_actions': result['next_actions'],
            'keyword_payload_json': '{}', 'stage_payload_json': json.dumps(result['stage_payload'])}


def claude_output(raw, **extra):
    data = {'type': 'result', 'subtype': 'success', 'is_error': False, 'result': json.dumps(raw), 'structured_output': raw,
            'total_cost_usd': 0.0123, 'num_turns': 4, 'session_id': 'session-test', 'modelUsage': {'claude-test-1': {}},
            'permission_denials': []}
    data.update(extra)
    return data


def only_claude(name):
    return '/usr/bin/claude' if name == 'claude' else None


class ProviderTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / 'AGENTS.md').write_text('Fixture technique', encoding='utf-8')
        self.team = Team(self.root / 'data')
        self.calls = []

    def tearDown(self):
        self.tmp.cleanup()

    def task(self, **brief_extra):
        brief = dict(name='Fixture', site='https://example.invalid', objective='Essai technique', request='Contexte test',
                     mode='seo', vault=str(self.root), **brief_extra)
        created = self.team.start(brief)
        with self.team.db() as db:
            project = self.team._get(db, 'projects', created['project']['id'])
            return dict(project=project, mission=created['mission'], upstream=self.team._upstream(db, created['mission']))

    def workspace(self):
        return Path(tempfile.mkdtemp(dir=self.root))

    def agent_answering(self, stdout, code=0, stderr=''):
        def spawn(command, prompt, workspace, env=None):
            self.calls.append((command, prompt, workspace))
            return code, stdout if isinstance(stdout, str) else json.dumps(stdout), stderr
        return spawn

    def run_claude(self, task, spawn):
        with patch.object(providers.shutil, 'which', only_claude), patch.object(providers, 'spawn', spawn), \
             patch.dict(os.environ, {'SEOKB_TEAM_AGENT': 'claude'}):
            return providers.run(task, self.workspace())

    def flag(self, command, name):
        return command[command.index(name) + 1]

    def test_claude_run_is_read_only_and_traced(self):
        task = self.task()
        raw = raw_from(fixture_v4(task))
        result = self.run_claude(task, self.agent_answering(claude_output(raw)))
        command, prompt, workspace = self.calls[0]
        self.assertEqual(command[:2], ['/usr/bin/claude', '-p'])
        self.assertEqual(self.flag(command, '--output-format'), 'json')
        self.assertIn('--no-session-persistence', command)
        self.assertEqual(self.flag(command, '--allowedTools'), 'Read,Glob,Grep')
        denied = self.flag(command, '--disallowedTools').split(',')
        for tool in ('Bash', 'Write', 'Edit', 'NotebookEdit', 'Agent'):
            self.assertIn(tool, denied)
        self.assertEqual(self.flag(command, '--max-turns'), '40')
        directories = command[command.index('--add-dir') + 1:]
        self.assertEqual(directories, [str(providers.KB), str(self.root.resolve())])
        if os.name != 'nt':
            self.assertEqual(json.loads(self.flag(command, '--json-schema')), providers.RESPONSE_SCHEMA)
        self.assertIn('Coffre du client : ' + str(self.root.resolve()), prompt)
        self.assertIn('doctrine-seo-reference.md', prompt)
        execution = result['_execution']
        self.assertEqual((execution['provider'], execution['mode'], execution['model']), ('claude-code-cli', 'real', 'claude-test-1'))
        self.assertEqual((execution['cost_usd'], execution['turns'], execution['session_id']), (0.0123, 4, 'session-test'))
        self.assertTrue(execution['methods'] and all(m['sha256'] for m in execution['methods']))
        self.assertEqual(result['keyword_payload'], {})
        self.assertEqual(result['stage_payload'], fixture_v4(task)['stage_payload'])
        for name in ('prompt.txt', 'schema.json', 'events.jsonl'):
            self.assertTrue((workspace / name).is_file(), name)

    def test_the_prompt_never_names_the_consultant(self):
        task = self.task()
        self.run_claude(task, self.agent_answering(claude_output(raw_from(fixture_v4(task)))))
        instructions = self.calls[0][1].split('MISSION ET ENTRÉES VALIDÉES')[0]
        self.assertNotIn('Tim', instructions)
        self.assertNotIn('/Users/', instructions.replace(str(self.root.resolve()), '').replace(str(providers.KB), ''))

    def test_the_coordinator_records_the_run_and_its_trace(self):
        task = self.task()
        spawn = self.agent_answering(claude_output(raw_from(fixture_v4(task))))
        with patch.object(providers.shutil, 'which', only_claude), patch.object(providers, 'spawn', spawn), \
             patch.dict(os.environ, {'SEOKB_TEAM_AGENT': 'claude'}):
            saved = self.team.run(task['mission']['id'])
        self.assertEqual(saved['status'], 'review')
        self.assertEqual(saved['execution']['provider'], 'claude-code-cli')
        self.assertEqual(saved['execution']['cost_usd'], 0.0123)
        self.assertTrue(Path(saved['artifact_path']).is_file())

    def test_web_search_only_when_the_brief_asks_for_it(self):
        offline = self.task()
        self.run_claude(offline, self.agent_answering(claude_output(raw_from(fixture_v4(offline)))))
        self.assertEqual(self.flag(self.calls[0][0], '--allowedTools'), 'Read,Glob,Grep')
        online = self.task(web=True)
        self.run_claude(online, self.agent_answering(claude_output(raw_from(fixture_v4(online)))))
        self.assertEqual(self.flag(self.calls[1][0], '--allowedTools'), 'Read,Glob,Grep,WebSearch,WebFetch')

    def test_model_budget_and_limits_come_from_the_environment(self):
        task = self.task()
        env = {'SEOKB_TEAM_MODEL': 'sonnet', 'SEOKB_TEAM_MAX_BUDGET_USD': '2', 'SEOKB_TEAM_MAX_TURNS': '12'}
        with patch.dict(os.environ, env):
            self.run_claude(task, self.agent_answering(claude_output(raw_from(fixture_v4(task)))))
        command = self.calls[0][0]
        self.assertEqual(self.flag(command, '--model'), 'sonnet')
        self.assertEqual(self.flag(command, '--max-budget-usd'), '2')
        self.assertEqual(self.flag(command, '--max-turns'), '12')

    def test_failures_are_explicit_and_never_retried(self):
        task = self.task()
        raw = raw_from(fixture_v4(task))
        failing = claude_output(raw, is_error=True, subtype='error_max_turns', result='trop de tours')
        cases = [('Échec Claude Code \\(error_max_turns\\)', 1, json.dumps(failing), ''),
                 ('sortie illisible', 1, 'pas du json', 'erreur de connexion'),
                 ('Échec Claude Code \\(1\\)', 1, json.dumps(claude_output(raw, result='refus', subtype='')), '')]
        for pattern, code, stdout, stderr in cases:
            self.calls.clear()
            with self.assertRaisesRegex(RuntimeError, pattern):
                self.run_claude(task, self.agent_answering(stdout, code, stderr))
            self.assertEqual(len(self.calls), 1, pattern)

    def test_json_in_the_text_answer_and_event_lists_are_accepted(self):
        task = self.task()
        raw = raw_from(fixture_v4(task))
        text_only = claude_output(raw, structured_output=None, result='Voici le résultat :\n```json\n' + json.dumps(raw) + '\n```')
        self.assertEqual(self.run_claude(task, self.agent_answering(text_only))['summary'], raw['summary'])
        events = [{'type': 'system'}, claude_output(raw)]
        self.assertEqual(self.run_claude(task, self.agent_answering(events))['summary'], raw['summary'])

    def test_an_answer_without_json_is_refused(self):
        task = self.task()
        raw = raw_from(fixture_v4(task))
        prose = claude_output(raw, structured_output=None, result='Je ne peux pas répondre au format demandé.')
        with self.assertRaisesRegex(RuntimeError, 'sans objet JSON exploitable'):
            self.run_claude(task, self.agent_answering(prose))

    def test_payloads_may_arrive_as_objects_but_not_as_garbage(self):
        task = self.task()
        raw = raw_from(fixture_v4(task))
        raw['stage_payload_json'] = json.loads(raw['stage_payload_json'])
        raw['keyword_payload_json'] = ''
        result = self.run_claude(task, self.agent_answering(claude_output(raw)))
        self.assertEqual(result['keyword_payload'], {})
        raw['stage_payload_json'] = 42
        with self.assertRaisesRegex(ValueError, 'stage_payload_json'):
            self.run_claude(task, self.agent_answering(claude_output(raw)))

    def test_codex_needs_the_chatgpt_login_and_reads_its_output_file(self):
        task = self.task()
        raw = raw_from(fixture_v4(task))

        def spawn(command, prompt, workspace, env=None):
            self.calls.append(command)
            Path(self.flag(command, '--output-last-message')).write_text(json.dumps(raw), encoding='utf-8')
            return 0, '{"event":"done"}\n', ''

        def only_codex(name):
            return '/usr/bin/codex' if name == 'codex' else None

        chatgpt = subprocess.CompletedProcess([], 0, stdout='Logged in using ChatGPT', stderr='')
        with patch.object(providers.shutil, 'which', only_codex), patch.object(providers, 'spawn', spawn), \
             patch.object(providers.subprocess, 'run', lambda *a, **k: chatgpt), patch.dict(os.environ, {'SEOKB_TEAM_AGENT': 'codex'}):
            result = providers.run(task, self.workspace())
        self.assertEqual(result['_execution']['provider'], 'codex-cli')
        self.assertIn('--output-schema', self.calls[0])
        self.assertIn('web_search="disabled"', self.calls[0])
        api_key = subprocess.CompletedProcess([], 0, stdout='Logged in using an API key', stderr='')
        with patch.object(providers.shutil, 'which', only_codex), patch.object(providers.subprocess, 'run', lambda *a, **k: api_key), \
             patch.dict(os.environ, {'SEOKB_TEAM_AGENT': 'codex'}):
            with self.assertRaisesRegex(RuntimeError, 'Connexion Codex ChatGPT requise'):
                providers.run(task, self.workspace())

    def test_agent_choice(self):
        def which(*available):
            return lambda name: '/usr/bin/' + name if name in available else None
        with patch.dict(os.environ, {'SEOKB_TEAM_AGENT': 'auto'}):
            with patch.object(providers.shutil, 'which', which('claude', 'codex')):
                self.assertEqual(providers.choose_agent(), 'claude')
            with patch.object(providers.shutil, 'which', which('codex')):
                self.assertEqual(providers.choose_agent(), 'codex')
            with patch.object(providers.shutil, 'which', which()):
                with self.assertRaisesRegex(RuntimeError, 'Ni `claude`'):
                    providers.choose_agent()
        with patch.dict(os.environ, {'SEOKB_TEAM_AGENT': 'codex'}), patch.object(providers.shutil, 'which', which('claude')):
            with self.assertRaisesRegex(RuntimeError, 'introuvable'):
                providers.choose_agent()

    def test_a_missing_method_names_the_file_and_the_remedy(self):
        with tempfile.TemporaryDirectory() as empty, patch.object(providers, 'KB', Path(empty)):
            with self.assertRaisesRegex(FileNotFoundError, 'update.py'):
                providers.resolve_method(('skill', 'go-to-market'))
            with self.assertRaisesRegex(FileNotFoundError, 'Référence introuvable'):
                providers.resolve_reference('go-to-market', 'livrables')

    def test_every_role_finds_its_methods_in_an_installed_vault(self):
        for role, entries in providers.METHODS.items():
            for entry in [providers.DOCTRINE] + entries:
                self.assertTrue(providers.resolve_method(entry).is_file(), (role, entry))
        for phase, names in providers.GTM_REFERENCES.items():
            for name in names:
                self.assertTrue(providers.resolve_reference('go-to-market', name).is_file(), (phase, name))


class ProcessTests(unittest.TestCase):
    def test_spawn_passes_the_prompt_through_stdin_in_utf8(self):
        with tempfile.TemporaryDirectory() as folder:
            code, out, _ = providers.spawn([sys.executable, '-c', 'import sys; sys.stdout.buffer.write(sys.stdin.buffer.read())'],
                                           'stratégie → écran', folder)
        self.assertEqual(code, 0)
        self.assertEqual(out, 'stratégie → écran')

    def test_a_stuck_agent_is_stopped_at_the_deadline(self):
        started = time.time()
        with tempfile.TemporaryDirectory() as folder, patch.dict(os.environ, {'SEOKB_TEAM_TIMEOUT': '1'}):
            with self.assertRaises(subprocess.TimeoutExpired):
                providers.spawn([sys.executable, '-c', 'import time; time.sleep(60)'], 'x', folder)
        self.assertLess(time.time() - started, 15)

    def test_pid_alive_sees_running_and_finished_processes(self):
        self.assertTrue(pid_alive(os.getpid()))
        child = subprocess.Popen([sys.executable, '-c', 'pass'])
        child.wait()
        self.assertFalse(pid_alive(child.pid))


if __name__ == '__main__':
    unittest.main()
