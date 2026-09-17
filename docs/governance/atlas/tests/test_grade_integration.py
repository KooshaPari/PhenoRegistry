"""Filesystem integration of the reference grader; not native product testing."""
import sys,json,tempfile,unittest,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'proof'))
import grade as g
from test_support import CASES,make_case,save_case,mutate
class GradeIntegration(unittest.TestCase):
 def test_no_certification(self):
  with tempfile.TemporaryDirectory() as td:
   p=Path(td);r,rs=make_case(p);raw,ix=save_case(p,r,rs);out=g.grade(r,ix,p,raw)
   for k in ['product_qualified','producer_authenticity_verified','oracle_truth_verified','approval_authenticity_verified','release_authorized']:self.assertFalse(out[k])
 def test_high_score_still_blocked(self):
  with tempfile.TemporaryDirectory() as td:
   p=Path(td);r,rs=make_case(p);r['categories'][0]['weight']=1;r['categories'][1]['weight']=99;rs[0]['earned_units']=0;raw,ix=save_case(p,r,rs);out=g.grade(r,ix,p,raw)
   self.assertEqual(out['score_percent'],99);self.assertEqual(out['letter_grade'],'A');self.assertEqual(out['gate_state'],'BLOCKED')
 def test_unknown_bound_not_confidence(self):
  with tempfile.TemporaryDirectory() as td:
   p=Path(td);r,rs=make_case(p);rs.pop(0);raw,ix=save_case(p,r,rs);out=g.grade(r,ix,p,raw)
   self.assertEqual(out['unknown_perfect_arithmetic_bound'],[30,100]);self.assertFalse(out['bound_is_confidence_interval'])
 def test_bad_fingerprint(self):
  with tempfile.TemporaryDirectory() as td:
   p=Path(td);r,rs=make_case(p);raw,ix=save_case(p,r,rs);ix['rubric_sha256']='f'*64
   with self.assertRaises(ValueError):g.grade(r,ix,p,raw)
 def test_symlink_payload(self):
  with tempfile.TemporaryDirectory() as td:
   p=Path(td);r,rs=make_case(p);a=p/rs[0]['artifacts'][0]['path'];data=a.read_bytes();a.unlink();(p/'linked.json').write_bytes(data);a.symlink_to(p/'linked.json');raw,ix=save_case(p,r,rs)
   self.assertEqual(g.grade(r,ix,p,raw)['gate_state'],'UNASSESSED')
def build_case(name,expected):
 def test(self):
  with tempfile.TemporaryDirectory() as td:
   p=Path(td);r,rs=make_case(p);mutate(name,p,r,rs);raw,ix=save_case(p,r,rs)
   if expected=='INPUT_ERROR':
    with self.assertRaises((ValueError,g.jsonschema.ValidationError)):g.grade(r,ix,p,raw)
   else:
    out=g.grade(r,ix,p,raw);self.assertEqual(out['gate_state'],expected)
    self.assertGreaterEqual(out['score_percent'],0);self.assertLessEqual(out['score_percent'],100)
 return test
for name,expected in CASES.items():setattr(GradeIntegration,'test_case_'+name.replace('-','_'),build_case(name,expected))
