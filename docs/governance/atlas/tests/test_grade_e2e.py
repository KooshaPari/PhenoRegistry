"""Actual Python CLI child-process tests of the reference grader, with synthetic data."""
import sys,tempfile,unittest,subprocess,json,os
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'proof'))
from test_support import CASES,make_case,save_case,mutate
def execute(name):
 with tempfile.TemporaryDirectory() as td:
  p=Path(td);r,rs=make_case(p);mutate(name,p,r,rs);save_case(p,r,rs)
  cmd=[sys.executable]
  if os.environ.get('PROOF_CLI_COVERAGE')=='1':cmd += ['-m','coverage','run','--parallel-mode','--branch','--source='+str(ROOT/'proof')]
  result=subprocess.run(cmd+[str(ROOT/'proof/grade.py'),str(p/'rubric.json'),str(p/'index.json'),'--root',str(p)],capture_output=True,text=True,timeout=45)
  return name,(result.returncode,json.loads(result.stdout))
class GradeCLI(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  # Four bounded independent CLI processes; each has its own temporary evidence root.
  with ThreadPoolExecutor(max_workers=4) as pool:cls.results=dict(pool.map(execute,CASES))
def build_case(name,expected):
 def test(self):
  rc,out=self.results[name]
  if expected=='INPUT_ERROR':self.assertEqual(rc,2);self.assertEqual(out['status'],'INPUT_ERROR')
  else:
   self.assertEqual(rc,0 if expected=='NO_RECORDED_MANDATORY_BLOCKER' else 1);self.assertEqual(out['gate_state'],expected)
   self.assertFalse(out['release_authorized']);self.assertFalse(out['product_qualified'])
 return test
for name,expected in CASES.items():setattr(GradeCLI,'test_case_'+name.replace('-','_'),build_case(name,expected))
