#!/usr/bin/env python3
"""Sauvegarde du coffre élève hors de l'ordinateur : archive ZIP contrôlée, rotation, restauration."""
import argparse, sys, zipfile
from datetime import datetime
from pathlib import Path

INCLURE = ['raw', 'wiki', '.claude', '.git', 'CLAUDE.md', 'AGENTS.md']
EXCLURE = {'_backups', 'node_modules', '__pycache__', '.DS_Store'}


def fichiers(root):
    for nom in INCLURE:
        p = root / nom
        if p.is_file():
            yield p
        elif p.is_dir():
            for f in sorted(p.rglob('*')):
                rel = f.relative_to(root).parts
                if f.is_symlink() or not f.is_file() or EXCLURE & set(rel) or f.name.startswith('.env'):
                    continue
                yield f


def sauvegarder(root, destination, garder=7):
    root = root.resolve(); destination = destination.expanduser().resolve()
    if destination == root or destination.is_relative_to(root):
        raise ValueError('La destination doit être hors du coffre.')
    destination.mkdir(parents=True, exist_ok=True)
    nom = root.name + '-' + datetime.now().strftime('%Y-%m-%d-%H%M%S') + '.zip'
    final = destination / nom; tmp = destination / (nom + '.partiel')
    liste = list(fichiers(root))
    with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as z:
        for f in liste:
            z.write(f, f.relative_to(root).as_posix())
    with zipfile.ZipFile(tmp) as z:
        mauvais = z.testzip()
        if mauvais or len(z.namelist()) != len(liste):
            tmp.unlink(); raise ValueError('Archive incomplète ou corrompue : ' + str(mauvais))
    tmp.replace(final)
    anciennes = sorted(destination.glob(root.name + '-*.zip'))
    for vieille in anciennes[:-garder] if garder > 0 else []:
        vieille.unlink()
    return {'archive': str(final), 'fichiers': len(liste), 'taille_mo': round(final.stat().st_size / 1e6, 1)}


def restaurer(archive, vers):
    vers = vers.expanduser().resolve()
    if vers.exists() and any(vers.iterdir()):
        raise ValueError('Restaurer dans un dossier vide.')
    vers.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive) as z:
        for n in z.namelist():
            p = Path(n)
            if p.is_absolute() or '..' in p.parts:
                raise ValueError('Chemin interdit dans l\'archive : ' + n)
        z.extractall(vers)
    return {'restauré': str(vers)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--coffre', type=Path, default=Path(__file__).resolve().parents[2])
    ap.add_argument('--destination', type=Path)
    ap.add_argument('--garder', type=int, default=7)
    ap.add_argument('--restaurer', type=Path)
    ap.add_argument('--vers', type=Path)
    a = ap.parse_args()
    try:
        if a.restaurer:
            if not a.vers: raise ValueError('--vers est obligatoire avec --restaurer.')
            print(restaurer(a.restaurer, a.vers))
        elif a.destination:
            print(sauvegarder(a.coffre, a.destination, a.garder))
        else:
            raise ValueError('Indiquer --destination (dossier synchronisé ou disque externe).')
    except (ValueError, OSError, zipfile.BadZipFile) as e:
        print(str(e), file=sys.stderr); sys.exit(1)


if __name__ == '__main__':
    main()
