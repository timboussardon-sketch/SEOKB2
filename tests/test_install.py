import importlib.util,json,shutil,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('installer',ROOT/'scripts/install.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class Migration(unittest.TestCase):
 def setUp(self):self.tmp=tempfile.TemporaryDirectory();self.target=Path(self.tmp.name)/'coffre avec espaces';self.target.mkdir()
 def tearDown(self):self.tmp.cleanup()
 def install(self,**kw):return m.install(ROOT,self.target,**kw)
 def test_fresh_idempotent_personal_preserved_rollback(self):
  for rel in ['raw/client.md','wiki/client.md','.claude/settings.local.json','.claude/skills/personnel/SKILL.md']:
   p=self.target/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_text('PERSONNEL')
  first=self.install();self.assertEqual(self.install()['changes'],0)
  self.assertEqual((self.target/'raw/client.md').read_text(),'PERSONNEL')
  m.restore(self.target,Path(first['backup']));self.assertFalse((self.target/'.seokb/manifest.json').exists());self.assertEqual((self.target/'wiki/client.md').read_text(),'PERSONNEL')
 def test_modified_skill_aborts_before_any_write(self):
  self.install();skill=self.target/'.claude/skills/mise-a-jour/SKILL.md';skill.write_text('CUSTOM');before=(self.target/'.seokb/manifest.json').read_bytes()
  with self.assertRaises(ValueError):self.install()
  self.assertEqual(skill.read_text(),'CUSTOM');self.assertEqual((self.target/'.seokb/manifest.json').read_bytes(),before)
 def test_symlink_refused(self):
  outside=Path(self.tmp.name)/'outside';outside.mkdir();(self.target/'.seokb').symlink_to(outside)
  with self.assertRaises(ValueError):self.install()
  self.assertEqual(list(outside.iterdir()),[])
 def test_legacy_migration(self):
  legacy=self.target/'organikk-seo-system/skills/mise-a-jour/SKILL.md';legacy.parent.mkdir(parents=True);legacy.write_text('ancien')
  installed=self.target/'.claude/skills/mise-a-jour/SKILL.md';installed.parent.mkdir(parents=True);installed.write_text('ancien')
  self.install();self.assertIn('SEOKB2',installed.read_text());self.assertEqual(legacy.read_text(),'ancien')
 def test_custom_skill_collision(self):
  f=self.target/'.claude/skills/mise-a-jour/SKILL.md';f.parent.mkdir(parents=True);f.write_text('personnel')
  with self.assertRaises(ValueError):self.install()
  self.assertFalse((self.target/'.seokb').exists())
 def test_dry_run_does_not_create_target(self):
  target=self.target/'absent';m.install(ROOT,target,dry=True);self.assertFalse(target.exists())
 def test_failed_write_rolls_back(self):
  from unittest.mock import patch
  real=m.os.replace;count=0
  def fail(src,dst):
   nonlocal count
   count+=1
   if count==3:raise OSError('simulated failure')
   return real(src,dst)
  with patch.object(m.os,'replace',side_effect=fail):
   with self.assertRaises(OSError):self.install()
  self.assertFalse((self.target/'.seokb/manifest.json').exists())
  self.assertFalse((self.target/'.claude/skills/mise-a-jour/SKILL.md').exists())
if __name__=='__main__':unittest.main(verbosity=2)
