"""Chemins de la team stratégie dans un coffre SEOKB2 installé.

Dans un coffre installé, ce dossier est `.seokb/runtime/team/` : la racine du coffre
est donc trois niveaux au-dessus du dossier. La variable SEOKB_VAULT la remplace
(tests, coffre lancé depuis un autre dossier).
"""
import os
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent


def vault_root():
    """Racine du coffre de l'élève : celle qui contient `.seokb/manifest.json`."""
    explicit = os.environ.get('SEOKB_VAULT')
    if explicit:
        return Path(explicit).expanduser().resolve()
    for parent in HERE.parents:
        if (parent / '.seokb' / 'manifest.json').is_file():
            return parent
    return HERE.parents[2]


def skills_dir(vault=None):
    return Path(vault or vault_root()) / '.claude' / 'skills'


def base_dir(vault=None):
    return Path(vault or vault_root()) / '.seokb' / 'base'


def team_root(vault=None):
    """Données du coordinateur : base SQLite, briefs, workspaces, livrables."""
    return Path(vault or vault_root()) / 'wiki' / 'projets' / 'team-strategie' / 'data'


def skill_file(name, relative='SKILL.md', vault=None):
    return skills_dir(vault) / name / relative


def base_file(relative, vault=None):
    """Document de la base commune ; le wiki personnel de l'élève passe avant."""
    root = Path(vault or vault_root())
    for candidate in (root / relative, base_dir(root) / relative):
        if candidate.is_file():
            return candidate
    return base_dir(root) / relative


def python_executable():
    return sys.executable or 'python3'


def pid_alive(pid):
    """Le processus existe-t-il encore ? `os.kill(pid, 0)` termine le processus sous Windows."""
    if os.name == 'nt':
        import ctypes
        kernel32 = ctypes.windll.kernel32
        handle = kernel32.OpenProcess(0x1000, False, pid)  # PROCESS_QUERY_LIMITED_INFORMATION
        if not handle:
            return False
        try:
            code = ctypes.c_ulong()
            if not kernel32.GetExitCodeProcess(handle, ctypes.byref(code)):
                return True
            return code.value == 259  # STILL_ACTIVE
        finally:
            kernel32.CloseHandle(handle)
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True
