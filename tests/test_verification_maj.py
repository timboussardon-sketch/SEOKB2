import json,os,shutil,subprocess,sys,tempfile,unittest,importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('installer',ROOT/'scripts/install.py');inst=importlib.util.module_from_spec(spec);spec.loader.exec_module(inst)
def git(*a,cwd):subprocess.run(['git',*a],cwd=cwd,check=True,capture_output=True)
class Verification(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();t=Path(self.tmp.name)
  self.depot=t/'depot';self.depot.mkdir()
  (self.depot/'VERSION').write_text('9.1.0\n')
  (self.depot/'CHANGELOG.md').write_text('# Versions\n\n## 9.1.0 — x\n\nBrief du matin. Autre phrase.\n\n## 9.0.0 — x\n\nSauvegarde.\n\n## 1.0.0 — x\n\nAncien.\n')
  git('init','-q',cwd=self.depot);git('add','.',cwd=self.depot);git('-c','user.name=t','-c','user.email=t@t.test','commit','-qm','v',cwd=self.depot)
  self.coffre=t/'coffre';(self.coffre/'.seokb/runtime').mkdir(parents=True)
  shutil.copy(ROOT/'scripts/update.py',self.coffre/'.seokb/runtime/update.py')
  (self.coffre/'.seokb/VERSION').write_text('2.0.0\n')
 def tearDown(self):self.tmp.cleanup()
 def check(self,depot=None,*extra):
  env={**os.environ,'SEOKB2_REPOSITORY':str(depot or self.depot)}
  return subprocess.run([sys.executable,str(self.coffre/'.seokb/runtime/update.py'),'--check',*extra],env=env,capture_output=True,text=True)
 def test_nouvelle_version_annoncee_puis_silence_le_meme_jour(self):
  r=self.check();self.assertEqual(r.returncode,0);out=json.loads(r.stdout)
  self.assertIn('SEOKB2 9.1.0 disponible (installé : 2.0.0)',out['systemMessage'])
  ctx=out['hookSpecificOutput']['additionalContext'];self.assertIn('9.1.0 : Brief du matin.',ctx);self.assertIn('9.0.0 : Sauvegarde.',ctx);self.assertNotIn('Ancien',ctx)
  self.assertEqual(self.check().stdout,'')
 def test_a_jour_silencieux(self):
  (self.coffre/'.seokb/VERSION').write_text('9.1.0\n');self.assertEqual(self.check().stdout,'')
 def test_depot_inaccessible_ne_bloque_pas(self):
  r=self.check(Path(self.tmp.name)/'absent');self.assertEqual(r.returncode,0);self.assertIn('impossible',json.loads(r.stdout)['systemMessage'])
class Installation(unittest.TestCase):
 def setUp(self):self.tmp=tempfile.TemporaryDirectory();self.target=Path(self.tmp.name)/'coffre';self.target.mkdir()
 def tearDown(self):self.tmp.cleanup()
 def hooks(self):return json.loads((self.target/'.claude/settings.json').read_text())
 def test_hook_ajoute_reglages_conserves_idempotent(self):
  s=self.target/'.claude/settings.json';s.parent.mkdir();s.write_text(json.dumps({'permissions':{'allow':['Bash(ls)']},'hooks':{'SessionStart':[{'hooks':[{'type':'command','command':'echo perso'}]}]}}))
  inst.install(ROOT,self.target);d=self.hooks()
  self.assertEqual(d['permissions'],{'allow':['Bash(ls)']})
  cmds=[h['command'] for e in d['hooks']['SessionStart'] for h in e['hooks']];self.assertIn('echo perso',cmds);self.assertEqual(sum('verifier-maj.sh' in c for c in cmds),1)
  self.assertEqual(inst.install(ROOT,self.target)['changes'],0)
 def test_coffre_neuf_recoit_le_hook(self):
  inst.install(ROOT,self.target);self.assertIn('verifier-maj.sh',json.dumps(self.hooks()))
 def test_reglages_illisibles_non_touches(self):
  s=self.target/'.claude/settings.json';s.parent.mkdir();s.write_text('{ pas du json');inst.install(ROOT,self.target);self.assertEqual(s.read_text(),'{ pas du json')
 def test_reglages_modifies_ensuite_pas_de_conflit_ni_alerte_doctor(self):
  inst.install(ROOT,self.target);s=self.target/'.claude/settings.json';d=self.hooks();d['model']='opus';s.write_text(json.dumps(d))
  inst.install(ROOT,self.target)
  r=subprocess.run([sys.executable,str(self.target/'.seokb/runtime/doctor.py'),'--target',str(self.target)],capture_output=True,text=True)
  self.assertEqual(json.loads(r.stdout)['modified_or_missing'],[])
if __name__=='__main__':unittest.main()
