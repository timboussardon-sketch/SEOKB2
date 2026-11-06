#!/usr/bin/env python3
import argparse,hashlib,json,sys
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--target',type=Path,default=Path(__file__).resolve().parents[2]);a=p.parse_args();root=a.target
try:
 state=json.loads((root/'.seokb/manifest.json').read_text());bad=[]
 for rel,sha in state['files'].items():
  f=root/rel
  if not f.is_file() or hashlib.sha256(f.read_bytes()).hexdigest()!=sha:bad.append(rel)
 print(json.dumps({'version':state['version'],'repository':state['repository'],'files_checked':len(state['files']),'modified_or_missing':bad,'external_tools':'À connecter séparément ; aucun cron installé.'},ensure_ascii=False,indent=2));sys.exit(bool(bad))
except (OSError,ValueError) as e:print('SEOKB2 non installé ou manifeste illisible : '+str(e));sys.exit(1)
