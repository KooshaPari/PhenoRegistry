"""Parser/arithmetic/admission unit tests; receipts supplied through a mock reader."""
import sys,tempfile,unittest,json
from pathlib import Path
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'proof'))
import grade as g
from test_support import CASES,make_case,save_case,mutate
class GradeUnit(unittest.TestCase):
 def test_duplicate_keys(self):
  with self.assertRaises(ValueError):g.strict_json(b'{"a":1,"a":2}')
 def test_nan(self):
  with self.assertRaises(ValueError):g.strict_json(b'{"a":NaN}')
 def test_numeric_overflow(self):
  with self.assertRaises(ValueError):g.strict_json(b'{"a":1e999}')
 def test_nested_nonfinite(self):
  with self.assertRaises(ValueError):g.strict_json(b'{"a":[1e999]}')
 def test_json_size_limit(self):
  with self.assertRaises(ValueError):g.strict_json(b' '*(g.MAX_JSON_BYTES+1))
 def test_timezone_required(self):
  with self.assertRaises(ValueError):g.utc('2026-09-16T12:00:00')
 def test_empty_payload(self):
  with tempfile.TemporaryDirectory() as td:
   p=Path(td);(p/'empty').write_bytes(b'')
   with self.assertRaises(ValueError):g.secure_payload(p,'empty','a'*64,99)
 def test_absolute_payload(self):
  with tempfile.TemporaryDirectory() as td:
   with self.assertRaises(ValueError):g.secure_payload(Path(td),'/etc/passwd','a'*64,99)
 def test_large_payload(self):
  with tempfile.TemporaryDirectory() as td:
   p=Path(td);(p/'big').write_bytes(b'abcdef')
   with self.assertRaises(ValueError):g.secure_payload(p,'big','a'*64,2)
def build_case(name,expected):
 def test(self):
  with tempfile.TemporaryDirectory() as td:
   p=Path(td);r,rs=make_case(p);mutate(name,p,r,rs);raw,ix=save_case(p,r,rs)
   # Freeze artifacts in memory and isolate transport. Safety-path tests remain real integration tests.
   store={str(x.relative_to(p)):x.read_bytes() for x in p.rglob('*') if x.is_file()}
   def read(root,name,digest,max_bytes):
    if '..' in Path(name).parts or name not in store:raise ValueError('unavailable payload')
    b=store[name]
    if not b or g.hashlib.sha256(b).hexdigest()!=digest:raise ValueError('invalid payload')
    return b
   with patch.object(g,'secure_payload',side_effect=read):
    if expected=='INPUT_ERROR':
     with self.assertRaises((ValueError,g.jsonschema.ValidationError)):g.grade(r,ix,p,raw)
    else:self.assertEqual(g.grade(r,ix,p,raw)['gate_state'],expected)
 return test
for name,expected in CASES.items():setattr(GradeUnit,'test_case_'+name.replace('-','_'),build_case(name,expected))
