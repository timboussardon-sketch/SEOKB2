import importlib.util,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('sauvegarde',ROOT/'scripts/sauvegarde.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class Sauvegarde(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();t=Path(self.tmp.name);self.coffre=t/'coffre';self.dest=t/'dest'
  for rel,txt in [('wiki/a.md','A'),('raw/b.md','B'),('.claude/skills/x/SKILL.md','X'),('.env.local','SECRET'),('wiki/.env','S2'),('_backups/old.md','O'),('.seokb/base/wiki/c.md','C'),('CLAUDE.md','CL')]:
   p=self.coffre/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(txt)
 def tearDown(self):self.tmp.cleanup()
 def test_aller_retour(self):
  r=m.sauvegarder(self.coffre,self.dest);out=Path(self.tmp.name)/'restore'
  m.restaurer(Path(r['archive']),out)
  self.assertEqual((out/'wiki/a.md').read_text(),'A');self.assertEqual((out/'.claude/skills/x/SKILL.md').read_text(),'X')
  for absent in ['.env.local','wiki/.env','_backups/old.md','.seokb/base/wiki/c.md']:self.assertFalse((out/absent).exists(),absent)
 def test_destination_dans_le_coffre_refusee(self):
  with self.assertRaises(ValueError):m.sauvegarder(self.coffre,self.coffre/'wiki')
 def test_rotation(self):
  import time
  for _ in range(3):m.sauvegarder(self.coffre,self.dest,garder=2);time.sleep(1.1)
  self.assertEqual(len(list(self.dest.glob('coffre-*.zip'))),2)
 def test_restauration_dossier_non_vide_refusee(self):
  r=m.sauvegarder(self.coffre,self.dest)
  with self.assertRaises(ValueError):m.restaurer(Path(r['archive']),self.coffre)
if __name__=='__main__':unittest.main()
