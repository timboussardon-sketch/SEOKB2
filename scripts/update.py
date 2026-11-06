#!/usr/bin/env python3
import argparse,json,subprocess,tempfile,sys
from pathlib import Path
REPOSITORY='https://github.com/timboussardon-sketch/SEOKB2.git'
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');args=ap.parse_args()
    root=Path(__file__).resolve().parents[2]
    try:
        with tempfile.TemporaryDirectory(prefix='seokb2-update-') as temp:
            source=Path(temp)/'release'
            subprocess.run(['git','clone','--quiet','--depth','1',REPOSITORY,str(source)],check=True,timeout=180)
            remote=(source/'VERSION').read_text().strip();local=(root/'.seokb/VERSION').read_text().strip()
            if args.check: print('SEOKB2 : installé '+local+', disponible '+remote);return
            subprocess.run([sys.executable,str(source/'scripts/install.py'),'--target',str(root)],check=True)
            print('Relancer la session pour charger les skills SEOKB2.')
    except (OSError,subprocess.SubprocessError) as e:
        print('Mise à jour non terminée. Vérifier accès au dépôt SEOKB2 et connexion GitHub. '+str(e),file=sys.stderr);sys.exit(2)
if __name__=='__main__':main()
