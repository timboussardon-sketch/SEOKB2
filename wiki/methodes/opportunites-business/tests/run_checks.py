"""Run the phase B suite and actual CLI commands into a new versioned directory."""
import argparse
import datetime as dt
import hashlib
import io
import json
from pathlib import Path
import subprocess
import sys
import unittest
import importlib.metadata

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from common import artifact_hashes, dump


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output_dir')
    args=parser.parse_args()
    out=Path(args.output_dir).resolve()
    if out.exists():raise SystemExit('Conserver les preuves existantes : choisir un nouveau dossier.')
    if 'raw' in out.parts:raise SystemExit('raw/ est immuable.')
    out.mkdir(parents=True)
    stream=io.StringIO()
    suite=unittest.defaultTestLoader.discover(str(ROOT/'tests'),pattern='test_*.py')
    result=unittest.TextTestRunner(stream=stream,verbosity=2).run(suite)
    (out/'tests.txt').write_text(stream.getvalue())
    print(stream.getvalue()[-350:])
    runs=[]
    if result.wasSuccessful():
        for path in sorted((ROOT/'tests/fixtures').glob('*.json')):
            if path.name=='origine-extraits.json':continue
            commands=[([sys.executable,'-B',str(ROOT/'valider.py'),str(path)],None),
                      ([sys.executable,'-B',str(ROOT/'calculer.py'),str(path),'--output',str(out/(path.stem+'-calculs.json'))],None)]
            for audience in ['audit','geo']:
                commands.append(([sys.executable,'-B',str(ROOT/'rendu.py'),str(out/(path.stem+'-calculs.json')),
                                  '--audience',audience,'--output',str(out/(path.stem+'-'+audience+'.md'))],None))
            for command,_ in commands:
                proc=subprocess.run(command,text=True,capture_output=True)
                runs.append({'command':command,'returncode':proc.returncode,'stdout':proc.stdout,'stderr':proc.stderr})
                if proc.returncode:break
    report={'executed_at':dt.datetime.now(dt.timezone.utc).isoformat(),
            'python_version':sys.version,'jsonschema_version':importlib.metadata.version('jsonschema'),
            'tests_run':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),
            'test_success':result.wasSuccessful(),'cli_success':bool(runs) and all(r['returncode']==0 for r in runs),
            'cli_runs':runs,'artifacts_sha256':artifact_hashes(),
            'source_hashes':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
                             for p in sorted(ROOT.rglob('*')) if p.is_file() and 'resultats' not in p.parts and '__pycache__' not in p.parts},
            'external_data_collection':False,'production_workflows_changed':False,
            'scope':'Isolated phase B only; fixtures and documentary extracts, not a customer forecast.'}
    (out/'verification.json').write_text(dump(report))
    print(json.dumps({k:report[k] for k in ['tests_run','failures','errors','test_success','cli_success']},ensure_ascii=False))
    return 0 if report['test_success'] and report['cli_success'] else 1


if __name__=='__main__':sys.exit(main())
