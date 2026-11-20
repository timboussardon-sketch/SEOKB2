#!/usr/bin/env python3
"""Team mots-clés : suivi d'état (scripts/teams/etat.py) et installation des agents."""
import json, subprocess, sys, tempfile, unittest
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
ETAT = RACINE / 'scripts' / 'teams' / 'etat.py'

def lance(script, *args, ok=True):
    r = subprocess.run([sys.executable, '-X', 'utf8', str(script), *args], capture_output=True, text=True)
    if ok and r.returncode: raise AssertionError(r.stdout + r.stderr)
    return r

class Etat(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.coffre = Path(self.tmp.name) / 'coffre'
        lance(RACINE / 'scripts' / 'install.py', '--target', str(self.coffre))
        self.etat = self.coffre / '.seokb' / 'runtime' / 'teams' / 'etat.py'
        self.projet = self.coffre / 'wiki' / 'keywords' / 'team-exemple'; self.projet.mkdir(parents=True)
    def tearDown(self): self.tmp.cleanup()
    def lire(self): return json.loads((self.projet / '.team' / 'etat.json').read_text(encoding='utf-8'))
    def phase(self, pid): return next(p for p in self.lire()['phases'] if p['id'] == pid)

    def test_installation(self):
        agents = sorted(p.name for p in (self.coffre / '.claude' / 'agents').glob('mots-cles-*.md'))
        self.assertEqual(len(agents), 6)
        self.assertTrue((self.coffre / '.claude' / 'skills' / 'team-mots-cles' / 'phases.json').is_file())
        roles = {p['role'] for p in json.loads((self.coffre / '.claude/skills/team-mots-cles/phases.json').read_text())['phases']} - {'pilote'}
        self.assertEqual(roles, {a[:-3] for a in agents})

    def test_cycle_accord(self):
        lance(self.etat, 'init', 'mots-cles', str(self.projet), '--nom', 'Exemple', '--site', 'exemple.test')
        self.assertTrue((self.coffre / '.seokb' / 'teams' / 'registre.json').is_file())
        f = self.projet / 'cadrage.md'; f.write_text('cadrage v1')
        lance(self.etat, 'demarre', str(self.projet), 'cadrage')
        lance(self.etat, 'livre', str(self.projet), 'cadrage', str(f))
        self.assertIn('cadrage', lance(self.etat, 'status', str(self.projet)).stdout)
        f.write_text('cadrage modifié après présentation')
        refus = lance(self.etat, 'valide', str(self.projet), 'cadrage', '--message', 'ok', ok=False)
        self.assertNotEqual(refus.returncode, 0)
        lance(self.etat, 'livre', str(self.projet), 'cadrage', str(f))
        lance(self.etat, 'valide', str(self.projet), 'cadrage', '--message', 'ok pour le cadrage')
        self.assertEqual(self.phase('cadrage')['statut'], 'valide')
        self.assertEqual(self.phase('cadrage')['accord_recu']['message'], 'ok pour le cadrage')

    def test_phase_bloquee_sans_dependance(self):
        lance(self.etat, 'init', 'mots-cles', str(self.projet), '--nom', 'Exemple')
        self.assertNotEqual(lance(self.etat, 'demarre', str(self.projet), 'collecte', ok=False).returncode, 0)

    def test_correction_remet_les_dependantes(self):
        lance(self.etat, 'init', 'mots-cles', str(self.projet), '--nom', 'Exemple')
        for pid in ('cadrage', 'collecte'):
            f = self.projet / (pid + '.md'); f.write_text(pid)
            lance(self.etat, 'demarre', str(self.projet), pid); lance(self.etat, 'livre', str(self.projet), pid, str(f))
            lance(self.etat, 'valide', str(self.projet), pid, '--message', 'ok ' + pid)
        lance(self.etat, 'corrige', str(self.projet), 'cadrage', '--message', 'le marché est la Suisse')
        self.assertNotEqual(self.phase('cadrage')['statut'], 'valide')
        self.assertNotEqual(self.phase('collecte')['statut'], 'valide')

if __name__ == '__main__': unittest.main()
