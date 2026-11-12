"""Reuse canonical keyword validators without maintaining a second mutable state."""
import contextlib
import importlib.util
import io
import threading
from pathlib import Path

from paths import skill_file, vault_root

KB = vault_root()
WORKFLOW = skill_file('strategie-mot-cle', 'scripts/workflow.py', KB)
if not WORKFLOW.is_file():
    raise ImportError('Skill strategie-mot-cle absent : ' + str(WORKFLOW) + ' (mettre SEOKB2 à jour, puis relancer la session)')
SPEC = importlib.util.spec_from_file_location('keyword_workflow', WORKFLOW)
workflow = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(workflow)
PHASES = {'intentions': 1, 'questions': 2, 'preuves': 3}
_METHOD_OUTPUT_LOCK = threading.Lock()


def state_for(task):
    mission = task['mission']
    phase = PHASES[mission['phase']]
    keyword = mission['subject']['keyword']
    vault = task['project']['brief'].get('vault', str(KB))
    state = {'vault': vault, 'keyword': keyword, 'outputs': {}, 'methods': {
        name: {'path': str(path), 'sha256': None} for name, path in workflow.METHOD_FILES.items()}, 'loaded_methods': {}}
    for item in task.get('upstream', []):
        if item['role'] != 'strategie-mot-cle' or item.get('subject', {}).get('keyword') != keyword:
            continue
        number = PHASES[item['phase']]
        if number < phase and item['status'] == 'approved':
            state['outputs'][str(number)] = item['result']['keyword_payload']
    for number in range(1, phase):
        if str(number) not in state['outputs']:
            raise ValueError('Phase précédente du même mot-clé non validée')
        workflow.validate_output(state, number, state['outputs'][str(number)])
    return state, phase


def load_methods(task):
    state, phase = state_for(task)
    output = io.StringIO()
    if phase < 3:
        with _METHOD_OUTPUT_LOCK, contextlib.redirect_stdout(output):
            workflow.load_method(state, phase)
    return output.getvalue(), state['loaded_methods'].get(str(phase), {})


def validate(task, result):
    if task['mission']['role'] != 'strategie-mot-cle' or result['status'] == 'blocked':
        return
    state, phase = state_for(task)
    state['loaded_methods'][str(phase)] = result.get('method_hashes', {})
    workflow.require_method_loaded(state, phase)
    payload = result.get('keyword_payload')
    if not isinstance(payload, dict):
        raise ValueError('Livrable structuré strategie-mot-cle manquant')
    workflow.validate_output(state, phase, payload)
