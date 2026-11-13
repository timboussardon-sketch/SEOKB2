#!/usr/bin/env python3
"""Mise à jour SEOKB2. --check : vérification au démarrage de session (une fois par jour, silencieuse si à jour)."""
import argparse, json, os, re, subprocess, sys, tempfile, time
from pathlib import Path

REPOSITORY = os.environ.get('SEOKB2_REPOSITORY', 'https://github.com/timboussardon-sketch/SEOKB2.git')
INTERVALLE = 24 * 3600


def version(v):
    return tuple(int(x) for x in re.findall(r'\d+', v)[:3])


def nouveautes(changelog, locale):
    """Sections du CHANGELOG plus récentes que la version installée, première phrase de chacune."""
    lignes = []
    for titre, corps in re.findall(r'^## (\S+)[^\n]*\n(.*?)(?=^## |\Z)', changelog, flags=re.M | re.S):
        if version(titre) > version(locale):
            phrases = corps.strip().split('\n')[0].split('. ')
            texte = phrases[0]
            for suite in phrases[1:]:  # une phrase trop courte ne dit pas ce qui change
                if len(texte) >= 80: break
                texte += '. ' + suite
            lignes.append(titre + ' : ' + texte.rstrip('.') + '.')
    return lignes


def sortie_hook(message, contexte):
    print(json.dumps({'systemMessage': message,
                      'hookSpecificOutput': {'hookEventName': 'SessionStart', 'additionalContext': contexte}},
                     ensure_ascii=False))


def verifier(root, force=False):
    etat = root / '.seokb/derniere-verification'
    if not force and etat.is_file() and time.time() - etat.stat().st_mtime < INTERVALLE:
        return
    etat.parent.mkdir(parents=True, exist_ok=True); etat.write_text(time.strftime('%Y-%m-%dT%H:%M:%S'))
    locale = (root / '.seokb/VERSION').read_text().strip()
    try:
        with tempfile.TemporaryDirectory(prefix='seokb2-check-') as temp:
            source = Path(temp) / 'release'
            subprocess.run(['git', 'clone', '--quiet', '--depth', '1', REPOSITORY, str(source)],
                           check=True, timeout=15, capture_output=True)
            distante = (source / 'VERSION').read_text().strip()
            changelog = (source / 'CHANGELOG.md').read_text() if (source / 'CHANGELOG.md').is_file() else ''
    except (OSError, subprocess.SubprocessError):
        sortie_hook('SEOKB2 : vérification des mises à jour impossible (connexion GitHub ou invitation au dépôt).',
                    "La vérification SEOKB2 a échoué. Si l'utilisateur parle de mise à jour, lui demander de vérifier `gh auth status` et son invitation au dépôt SEOKB2.")
        return
    if version(distante) <= version(locale):
        return
    liste = nouveautes(changelog, locale)
    sortie_hook('SEOKB2 ' + distante + ' disponible (installé : ' + locale + '). Tape « mets à jour SEOKB2 ».',
                'Une mise à jour SEOKB2 est disponible : ' + distante + ' (installé : ' + locale + '). '
                "Dans ta première réponse, propose-la à l'utilisateur en une ou deux phrases, avec ces nouveautés : "
                + ' '.join(liste) + " Ne lance la mise à jour (skill `mise-a-jour`) qu'avec son accord explicite.")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--check', action='store_true'); ap.add_argument('--force', action='store_true')
    args = ap.parse_args()
    root = Path(__file__).resolve().parents[2]
    if args.check:
        try:
            verifier(root, args.force)
        except Exception as e:  # le démarrage de session ne doit jamais bloquer
            print('SEOKB2 : vérification non terminée (' + type(e).__name__ + ').', file=sys.stderr)
        return
    try:
        with tempfile.TemporaryDirectory(prefix='seokb2-update-') as temp:
            source = Path(temp) / 'release'
            subprocess.run(['git', 'clone', '--quiet', '--depth', '1', REPOSITORY, str(source)], check=True, timeout=180)
            subprocess.run([sys.executable, str(source / 'scripts/install.py'), '--target', str(root)], check=True)
            print('Relancer la session pour charger les skills SEOKB2.')
    except (OSError, subprocess.SubprocessError) as e:
        print('Mise à jour non terminée. Vérifier accès au dépôt SEOKB2 et connexion GitHub. ' + str(e), file=sys.stderr); sys.exit(2)


if __name__ == '__main__':
    main()
