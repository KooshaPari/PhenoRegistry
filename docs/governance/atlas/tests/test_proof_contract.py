"""Amendment consistency, not game/UI/native product testing."""
from pathlib import Path
import json,unittest,hashlib,sys
from graphlib import TopologicalSorter
import jsonschema
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'federation'))
import check_plans
class ProofContract(unittest.TestCase):
 def test_all_owners(self):
  ix=json.loads((ROOT/'portfolio/CURRENT-REPO-INDEX.json').read_text())['entries'];rows=json.loads((ROOT/'proof/owner-map.json').read_text())
  self.assertEqual({r['repository_id'] for r in rows},{r['repository_id'] for r in ix})
  for r in ix:self.assertTrue((ROOT/r['folder']/'PROOF-AND-GRADE.md').is_file())
  self.assertTrue(all(r['actual_grade'] is None and r['actual_evidence']==[] for r in rows))
 def test_capability_only_no_mounts(self):
  ms=json.loads((ROOT/'federation/examples/manifests.json').read_text());p=json.loads((ROOT/'federation/examples/capability-only.json').read_text());self.assertEqual(p['mounts'],[])
  out=check_plans.validate_plan(ms,p);self.assertEqual(out['errors'],[]);self.assertFalse(out['activation_authorized'])
 def test_requirements_scenarios(self):
  r=json.loads((ROOT/'proof/requirements.json').read_text());s=json.loads((ROOT/'proof/scenarios.json').read_text())
  self.assertEqual({x['id'] for x in r},{i for x in s for i in x['requirement_ids']})
  self.assertTrue(all(x['actual_evidence_ids']==[] for x in s))
 def test_dag(self):
  w=json.loads((ROOT/'proof/work-packages.json').read_text());self.assertEqual(len(w),len(list(TopologicalSorter({x['id']:x['depends_on'] for x in w}).static_order())))
 def test_prompt_integrity(self):
  p=json.loads((ROOT/'intent/INT-006-provenance.json').read_text());self.assertEqual(p['sha256'],hashlib.sha256((ROOT/'intent'/p['path']).read_bytes()).hexdigest())
 def test_schemas(self):
  for p in (ROOT/'proof/schemas').glob('*.json'):jsonschema.Draft202012Validator.check_schema(json.loads(p.read_text()))
 def test_example_grade_arithmetic(self):
  p=json.loads((ROOT/'proof/examples/grade/result.json').read_text());self.assertEqual(p['score_percent'],84.11);self.assertEqual(p['letter_grade'],'C');self.assertEqual(p['gate_state'],'BLOCKED');self.assertFalse(p['product_qualified'])
 def test_design_not_approved(self):
  p=json.loads((ROOT/'proof/examples/design-record.json').read_text());self.assertIsNone(p['approval_reference']);self.assertEqual(p['review_status'],'proposed')
 def test_bridge_not_executed(self):
  p=json.loads((ROOT/'proof/examples/bridge-session.json').read_text());self.assertEqual(p['evidence_ids'],[]);self.assertEqual(p['status'],'PLANNED_NOT_EXECUTED')
