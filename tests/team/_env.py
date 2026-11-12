"""Prépare un coffre SEOKB2 installé avec l'installateur réel, puis expose scripts/team.

Les tests de la team tournent contre les fichiers tels que les reçoit un élève :
skills dans .claude/skills, base commune dans .seokb/base. SEOKB_VAULT permet de
viser un coffre déjà installé au lieu d'en créer un temporaire.
"""
import atexit
import importlib.util
import os
from pathlib import Path
import shutil
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
TEAM = ROOT / 'scripts' / 'team'
if str(TEAM) not in sys.path:
    sys.path.insert(0, str(TEAM))

if not os.environ.get('SEOKB_VAULT'):
    _tmp = tempfile.mkdtemp(prefix='seokb-team-test-')
    atexit.register(shutil.rmtree, _tmp, ignore_errors=True)
    _spec = importlib.util.spec_from_file_location('seokb_installer', ROOT / 'scripts' / 'install.py')
    _installer = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(_installer)
    _vault = Path(_tmp) / 'coffre'
    _installer.install(ROOT, _vault)
    os.environ['SEOKB_VAULT'] = str(_vault)
