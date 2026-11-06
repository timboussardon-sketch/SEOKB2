#!/usr/bin/env python3
"""Install SEOKB2 without changing student sources or unowned files."""
import argparse, hashlib, json, os, shutil, sys, tempfile
from datetime import datetime, timezone
from pathlib import Path

def digest(data): return hashlib.sha256(data).hexdigest()
def checked(root, rel):
    p=Path(rel)
    if p.is_absolute() or '..' in p.parts: raise ValueError('Chemin interdit : '+rel)
    out=root/p
    for parent in [out,*out.parents]:
        if parent == root.parent: break
        if parent.is_symlink(): raise ValueError('Lien symbolique refusé : '+str(parent))
    return out

def plan(source, target):
    files={}
    def tree(src, dest):
        for p in sorted(src.rglob('*')):
            if p.is_symlink(): raise ValueError('Source avec lien symbolique : '+str(p))
            if p.is_file() and '__pycache__' not in p.parts and '.git' not in p.parts:
                files[dest+'/'+p.relative_to(src).as_posix()]=p.read_bytes()
    for folder in ['wiki','raw']: tree(source/folder,'.seokb/base/'+folder)
    # Published pack fills only gaps in the larger KB.
    existing=set(files)
    tree(source/'distribution/base','.seokb/base')
    for key in existing: files[key]=(source/key.removeprefix('.seokb/base/')).read_bytes()
    tree(source/'distribution/skills','.claude/skills')
    tree(source/'scripts','.seokb/runtime')
    files['.seokb/AGENTS.md']=(source/'distribution/AGENTS.md').read_bytes()
    files['.seokb/VERSION']=(source/'VERSION').read_bytes()
    for name in ['CLAUDE.md','AGENTS.md']:
        p=checked(target,name);old=p.read_text() if p.exists() else ''
        start='<!-- SEOKB2 START -->';end='<!-- SEOKB2 END -->'
        if start in old:
            if end not in old: raise ValueError('Bloc SEOKB2 incomplet : '+name)
            old=old[:old.index(start)]+old[old.index(end)+len(end):]
        block='\n'+start+'\nLire `.seokb/AGENTS.md` pour SEOKB2. Ces règles remplacent les anciennes consignes de mise à jour Organikk ; les autres consignes personnelles restent applicables.\n'+end+'\n'
        files[name]=(old.rstrip()+'\n'+block).encode()
    # Retire only the three known old hooks; preserve settings and other hooks.
    for name in ['mettre-a-jour','verifier-maj','installer-skills']:
        command='update.py' if name=='mettre-a-jour' else 'doctor.py'
        extra=' --check' if name=='verifier-maj' else ''
        files['.claude/hooks/'+name+'.sh']=('#!/usr/bin/env bash\nset -euo pipefail\nROOT="${CLAUDE_PROJECT_DIR:-$(pwd)}"\nexec python3 "$ROOT/.seokb/runtime/'+command+'"'+extra+'\n').encode()
    seeds={
        'wiki/index.md':'# Index du coffre\n\n- [[pilotage/recap]]\n- [[log]]\n',
        'wiki/log.md':'# Journal du coffre\n\n- [[index]]\n- [[pilotage/recap]]\n',
        'wiki/pilotage/recap.md':'# Suivi du projet\n\n## Disponible\nSEOKB2 installé ; bibliothèque commune dans .seokb/base/.\n\n## À cadrer\nOffre, audiences, objectifs, sources et accès aux outils.\n\n## Prochaine action\nPrésenter le cadrage de la mission pour validation.\n\n## Navigation\n[[index]] · [[log]]\n'
    }
    for rel,content in seeds.items():
        if not (target/rel).exists():
            files[rel]=('---\ntype: register\ntitle: '+Path(rel).stem+'\ncreated: 2026-11-06\nupdated: 2026-11-06\ntags: [projet]\nstatus: draft\nconfidence: high\nsources: 0\n---\n\n'+content).encode()
    return files

def install(source,target,replace=False,dry=False):
    source=source.resolve();target=target.absolute()
    checked(target,'.seokb/manifest.json')
    if target.resolve()==source: raise ValueError('Choisir un coffre distinct du dépôt source.')
    for required in ['VERSION','distribution/AGENTS.md','distribution/skills/mise-a-jour/SKILL.md','scripts/update.py','wiki/index.md']:
        if not (source/required).is_file(): raise ValueError('Distribution incomplète : '+required)
    mf=target/'.seokb/manifest.json'; previous=json.loads(mf.read_text()) if mf.exists() else {'files':{}}
    payload=plan(source,target); conflicts=[]
    for rel,data in payload.items():
        p=checked(target,rel)
        if p.exists() and not p.is_file(): raise ValueError('Fichier attendu : '+rel)
        if not p.exists() or p.read_bytes()==data: continue
        if rel in ['CLAUDE.md','AGENTS.md']: continue
        oldhash=previous['files'].get(rel)
        if oldhash and digest(p.read_bytes())==oldhash: continue
        # Legacy-owned files can be replaced only when identical to their installed package.
        legacy=False
        if rel.startswith('.claude/skills/'):
            old=target/'organikk-seo-system/skills'/rel.removeprefix('.claude/skills/')
            legacy=old.is_file() and not old.is_symlink() and old.read_bytes()==p.read_bytes()
        if rel.startswith('.claude/hooks/') and (target/'organikk-seo-system/.claude-plugin/plugin.json').is_file():
            legacy=digest(p.read_bytes()) in json.loads((source/'distribution/legacy-hooks.json').read_text()).get(p.name, [])
        if not legacy: conflicts.append(rel)
    stale=[]
    for rel,sha in previous['files'].items():
        p=checked(target,rel)
        if rel not in payload and p.is_file():
            if digest(p.read_bytes())!=sha: conflicts.append(rel)
            stale.append(rel)
    if conflicts and not replace: raise ValueError('Conflits locaux ; rien modifié. Examiner avant --replace-modified :\n'+'\n'.join(conflicts))
    changed={rel:data for rel,data in payload.items() if not (target/rel).exists() or (target/rel).read_bytes()!=data}
    if dry: return {'version':(source/'VERSION').read_text().strip(),'files':len(payload),'changes':len(changed),'conflicts':conflicts,'dry_run':True}
    target.mkdir(parents=True,exist_ok=True)
    backup=target/'_backups/seokb2'/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ');backup.mkdir(parents=True)
    operations=list(changed)+stale+['.seokb/manifest.json']; existed=[];written=[]
    for rel in operations:
        p=checked(target,rel)
        if p.exists():
            dest=backup/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest);existed.append(rel)
    receipt={'restore':existed,'remove':[rel for rel in operations if rel not in existed]}
    (backup/'rollback.json').write_text(json.dumps(receipt,indent=2))
    try:
        for rel,data in changed.items():
            p=checked(target,rel);p.parent.mkdir(parents=True,exist_ok=True)
            with tempfile.NamedTemporaryFile(dir=p.parent,delete=False) as f: f.write(data);tmp=f.name
            try: os.replace(tmp,p)
            finally:
                if os.path.exists(tmp): os.unlink(tmp)
            written.append(rel)
        for rel in stale: checked(target,rel).unlink()
        state={'version':(source/'VERSION').read_text().strip(),'repository':'https://github.com/timboussardon-sketch/SEOKB2.git','files':{k:digest(v) for k,v in payload.items() if not k.startswith('wiki/')}}
        mf.write_text(json.dumps(state,indent=2)+'\n')
    except BaseException:
        restore(target,backup);raise
    return {'version':state['version'],'files':len(payload),'changes':len(changed),'backup':str(backup),'doctor':'python3 .seokb/runtime/doctor.py'}

def restore(target,backup):
    receipt=json.loads((backup/'rollback.json').read_text())
    for rel in receipt['remove']:
        p=checked(target,rel)
        if p.is_file(): p.unlink()
    for rel in receipt['restore']:
        p=checked(target,rel);p.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(backup/rel,p)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--target',type=Path,required=True);ap.add_argument('--source',type=Path,default=Path(__file__).resolve().parents[1]);ap.add_argument('--dry-run',action='store_true');ap.add_argument('--replace-modified',action='store_true');ap.add_argument('--rollback',type=Path)
    args=ap.parse_args()
    try:
        if args.rollback: restore(args.target.absolute(),args.rollback.resolve());print('Sauvegarde restaurée.');return
        print(json.dumps(install(args.source,args.target,args.replace_modified,args.dry_run),ensure_ascii=False,indent=2))
    except (ValueError,OSError,json.JSONDecodeError) as e: print(str(e),file=sys.stderr);sys.exit(1)
if __name__=='__main__':main()
