from copy import deepcopy
import json
from pathlib import Path
import sys
import unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
from validate_docset import ValidationError,validate_payload,validate_tree
from analyze_logs import analyze

class DocsetTests(unittest.TestCase):
    def setUp(self):
        self.data=json.loads((ROOT/'machine/docset.json').read_text())
        self.sources=json.loads((ROOT/'machine/sources.json').read_text())
    def test_valid_payload(self):
        self.assertEqual(validate_payload(self.data,self.sources)['requirements'],58)
    def test_duplicate_id(self):
        self.data['requirements'].append(deepcopy(self.data['requirements'][0]))
        with self.assertRaises(ValidationError):validate_payload(self.data,self.sources)
    def test_unknown_source(self):
        self.data['findings'][0]['source_ids']=['S-NOT-REAL']
        with self.assertRaises(ValidationError):validate_payload(self.data,self.sources)
    def test_missing_evidence_definition(self):
        self.data['acceptance_tests'][0].pop('evidence_required')
        with self.assertRaises(ValidationError):validate_payload(self.data,self.sources)
    def test_orphan_test(self):
        self.data['requirements'][0]['acceptance_test_ids']=['AT-NOT-REAL']
        with self.assertRaises(ValidationError):validate_payload(self.data,self.sources)
    def test_nonbidirectional_test(self):
        self.data['acceptance_tests'][0]['requirement_ids']=[]
        with self.assertRaises(ValidationError):validate_payload(self.data,self.sources)
    def test_operational_pass_not_claimed(self):
        self.data['acceptance_tests'][0]['status']='passed'
        with self.assertRaises(ValidationError):validate_payload(self.data,self.sources)
    def test_invented_trio_rejected(self):
        self.data['unresolved']['exact_ci_trio']=['lint','test','build']
        with self.assertRaises(ValidationError):validate_payload(self.data,self.sources)
    def test_unapproved_adr_not_promoted(self):
        self.data['decisions'][1]['status']='accepted_user_constraint'
        with self.assertRaises(ValidationError):validate_payload(self.data,self.sources)
    def test_no_production_approval_status(self):
        self.data['status']='approved_for_production'
        with self.assertRaises(ValidationError):validate_payload(self.data,self.sources)
    def test_work_cycle(self):
        self.data['work_items'][0]['depends_on']=['WP-07']
        with self.assertRaises(ValidationError):validate_payload(self.data,self.sources)
    def test_unknown_work_dependency(self):
        self.data['work_items'][0]['depends_on']=['WP-UNKNOWN']
        with self.assertRaises(ValidationError):validate_payload(self.data,self.sources)
    def test_missing_work_coverage(self):
        self.data['work_items'][1]['requirement_ids']=['FR-DEP-002']
        with self.assertRaises(ValidationError):validate_payload(self.data,self.sources)
    def test_source_tree_and_metrics(self):
        self.assertEqual(validate_tree(ROOT)['status'],'passed')
    def test_observed_log_counts(self):
        result=analyze(ROOT/'evidence/source-excerpt.md')
        self.assertEqual(result['counts']['terminal_traces'],316)
        self.assertEqual(result['counts']['unique_combo_ids'],316)
        self.assertEqual(result['counts']['decisions_histogram']['99'],192)
        self.assertEqual(result['counts']['empty_completion_warnings'],1)
        self.assertEqual(result['counts']['upstream_error_before_content_warnings'],5)
        self.assertEqual(result['counts']['zero_model_sync_reports'],18)
        self.assertEqual(result['explicit_fallback_events'][0]['reported_duration_ms'],83173)
        self.assertEqual(result['explicit_fallback_events'][0]['reported_fallbacks'],32)
        self.assertEqual(result['unparsed_terminal_lines'],[])
    def test_metrics_make_no_rate_claim(self):
        result=analyze(ROOT/'evidence/source-excerpt.md')
        self.assertNotIn('error_rate',result)
        self.assertNotIn('retry_count',result['counts'])

if __name__=='__main__':unittest.main()
