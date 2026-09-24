from __future__ import annotations
import copy
from datetime import datetime,timezone,timedelta
import importlib.util
import json
import math
from pathlib import Path
import random
import shutil
import sys
import tempfile
import unittest
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
import pep
import demo_loop

class KernelTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='pep-tests-')
        self.root=Path(self.temp.name)
        self.b=self.root/'bundle'
        shutil.copytree(ROOT/'examples/executed-toy-loop/after',self.b)
    def tearDown(self):self.temp.cleanup()
    def get(self,p):return pep.load_json(self.b/p)
    def put(self,p,v):
        (self.b/p).write_text(json.dumps(v,indent=2,allow_nan=False)+'\n',encoding='utf-8')
    def mod(self,p,key,value):
        x=self.get(p);x[key]=value;self.put(p,x)
    def assignment(self,fn):
        a=self.get('assignment.json');fn(a);self.put('assignment.json',a)
        digest=pep.file_digest(self.b/'assignment.json')
        self.mod('assessment.json','assignment_digest',digest)
        for p in (self.b/'results').glob('*.json'):
            self.mod(str(p.relative_to(self.b)),'assignment_digest',digest)
    def summary(self):return pep.summarize_bundle(self.b)
    def resultmod(self,key,value):self.mod('results/R-I-RESTORE.json',key,value)
    def test_01_good_example_passes_bounded_gate(self):
        s=self.summary();self.assertEqual(s['mandatory_gate_state'],'PASS');self.assertEqual(s['assessed_pass_rate'],1)
    def test_02_bad_example_rejects_success_narrative(self):
        s=pep.summarize_bundle(ROOT/'examples/executed-toy-loop/before');self.assertEqual(s['mandatory_gate_state'],'FAIL')
    def test_03_demo_runs_actual_good_and_noop_variants(self):
        self.assertEqual(demo_loop.run(self.root/'demo')['before_gate'],'FAIL')
    def test_04_catalog_counts(self):
        c=pep.validate_catalog(pep.load_json(ROOT/'catalog/catalog.json'))
        self.assertEqual((c['domains'],c['pillars'],c['candidate_entries']),(18,108,1080))
    def test_05_stale_pass_unknown(self):
        self.resultmod('evidence_state','STALE');s=self.summary();self.assertEqual(s['weights']['unknown_weight'],1);self.assertEqual(s['mandatory_gate_state'],'BLOCKED')
    def test_06_expired_pass_unknown(self):
        t=self.get('assessment.json')['as_of'];self.resultmod('expires_at',t);self.assertEqual(self.summary()['mandatory_gate_state'],'BLOCKED')
    def test_07_future_result_rejected(self):
        self.resultmod('observed_at','2099-01-01T00:00:00Z')
        with self.assertRaises(pep.ValidationError):self.summary()
    def test_08_zero_assertions_not_pass(self):
        r=self.get('results/R-I-RESTORE.json');r['observation']['assertions_executed']=0;self.put('results/R-I-RESTORE.json',r)
        self.assertEqual(self.summary()['mandatory_gate_state'],'BLOCKED')
    def test_09_waiver_not_pass(self):
        self.resultmod('review_status','WAIVED');self.assertEqual(self.summary()['weights']['unknown_weight'],1)
    def test_10_missing_qualification_unknown(self):
        self.resultmod('qualification_ids',[]);self.assertEqual(self.summary()['mandatory_gate_state'],'BLOCKED')
    def test_11_rejected_positive_control_unknown(self):
        self.mod('qualifications/Q-TOY.json','positive_control_passed',False);self.assertEqual(self.summary()['weights']['unknown_weight'],2)
    def test_12_rejected_negative_control_unknown(self):
        self.mod('qualifications/Q-TOY.json','negative_control_passed',False);self.assertEqual(self.summary()['weights']['unknown_weight'],2)
    def test_13_revoked_qualification_unknown(self):
        self.mod('qualifications/Q-TOY.json','status','REVOKED');self.assertEqual(self.summary()['mandatory_gate_state'],'BLOCKED')
    def test_14_evidence_tampering_rejected(self):
        (self.b/'raw/observations.json').write_text('{}')
        with self.assertRaises(pep.ValidationError):self.summary()
    def test_15_wrong_subject_rejected(self):
        self.resultmod('subject_digest','sha256:'+'1'*64)
        with self.assertRaises(pep.ValidationError):self.summary()
    def test_16_wrong_epoch_rejected(self):
        self.resultmod('epoch_id','E-OTHER')
        with self.assertRaises(pep.ValidationError):self.summary()
    def test_17_assignment_changed_without_rebinding_rejected(self):
        a=self.get('assignment.json');a['instances'][0]['weight']=999;self.put('assignment.json',a)
        with self.assertRaises(pep.ValidationError):self.summary()
    def test_18_result_assignment_digest_rejected(self):
        self.resultmod('assignment_digest','sha256:'+'2'*64)
        with self.assertRaises(pep.ValidationError):self.summary()
    def test_19_catalog_digest_rejected(self):
        self.mod('assessment.json','catalog_digest','sha256:'+'3'*64)
        with self.assertRaises(pep.ValidationError):self.summary()
    def test_20_duplicate_instances_rejected(self):
        self.assignment(lambda a:a['instances'].append(copy.deepcopy(a['instances'][0])))
        with self.assertRaises(pep.ValidationError):self.summary()
    def test_21_duplicate_obligation_keys_rejected(self):
        self.assignment(lambda a:a['instances'][1].update(obligation_key=a['instances'][0]['obligation_key']))
        with self.assertRaises(pep.ValidationError):self.summary()
    def test_22_unknown_criterion_rejected(self):
        self.assignment(lambda a:a['instances'][0].update(criterion_id='PEP-99-99-99'))
        with self.assertRaises(pep.ValidationError):self.summary()
    def test_23_zero_weight_rejected(self):
        self.assignment(lambda a:a['instances'][0].update(weight=0))
        with self.assertRaises(pep.ValidationError):self.summary()
    def test_24_negative_weight_rejected(self):
        self.assignment(lambda a:a['instances'][0].update(weight=-1))
        with self.assertRaises(pep.ValidationError):self.summary()
    def test_25_boolean_weight_rejected(self):
        self.assignment(lambda a:a['instances'][0].update(weight=True))
        with self.assertRaises(pep.ValidationError):self.summary()
    def test_26_weight_overflow_rejected(self):
        self.assignment(lambda a:[i.update(weight=1e308) for i in a['instances']])
        with self.assertRaises(pep.ValidationError):self.summary()
    def test_27_unresolved_applicability_separate(self):
        self.assignment(lambda a:a['instances'][0].update(applicability='UNRESOLVED'))
        s=self.summary();self.assertEqual(s['weights']['unresolved_applicability_weight'],1);self.assertFalse(s['applicability_complete']);self.assertEqual(s['mandatory_gate_state'],'BLOCKED')
    def test_28_gate_cannot_exclude_required_member(self):
        self.assignment(lambda a:a['instances'][0].update(applicability='NOT_APPLICABLE',applicability_decision_ref='D-NA'))
        with self.assertRaises(pep.ValidationError):self.summary()
    def test_29_na_needs_decision(self):
        def change(a):
            a['gates']=[];a['instances'][0].update(applicability='NOT_APPLICABLE',applicability_decision_ref=None)
        self.assignment(change)
        with self.assertRaises(pep.ValidationError):self.summary()
    def test_30_proposed_assignment_blocks(self):
        self.assignment(lambda a:a.update(status='PROPOSED',scope_review_status='PENDING',scope_review_ref=None))
        self.assertEqual(self.summary()['mandatory_gate_state'],'BLOCKED')
    def test_31_no_gate_is_not_evaluated(self):
        self.assignment(lambda a:a.update(gates=[]));self.assertEqual(self.summary()['mandatory_gate_state'],'NOT_EVALUATED')
    def test_32_missing_result_is_unknown(self):
        m=self.get('assessment.json');m['result_ids'].remove('R-I-RESTORE');self.put('assessment.json',m);(self.b/'results/R-I-RESTORE.json').unlink()
        self.assertEqual(self.summary()['weights']['unknown_weight'],1)
    def test_33_manifest_cannot_hide_existing_result(self):
        m=self.get('assessment.json');m['result_ids'].remove('R-I-RESTORE');self.put('assessment.json',m)
        with self.assertRaises(pep.ValidationError):self.summary()
    def test_34_duplicate_result_manifest_id_rejected(self):
        m=self.get('assessment.json');m['result_ids'].append(m['result_ids'][0]);self.put('assessment.json',m)
        with self.assertRaises(pep.ValidationError):self.summary()
    def test_35_competing_effective_results_contested(self):
        r=self.get('results/R-I-RESTORE.json');r['id']='R-FORK';r['verdict']='FAIL';self.put('results/R-FORK.json',r)
        m=self.get('assessment.json');m['result_ids'].append('R-FORK');self.put('assessment.json',m)
        s=self.summary();self.assertEqual(s['weights']['unknown_weight'],1)
    def test_36_explicit_supersession_resolves_branch(self):
        r=self.get('results/R-I-RESTORE.json');r.update(id='R-NEW',verdict='FAIL',supersedes=['R-I-RESTORE']);self.put('results/R-NEW.json',r)
        m=self.get('assessment.json');m['result_ids'].append('R-NEW');self.put('assessment.json',m)
        self.assertEqual(self.summary()['weights']['fail_weight'],1)
    def test_37_supersession_cycle_rejected(self):
        r=self.get('results/R-I-RESTORE.json');r.update(id='R-NEW',supersedes=['R-I-RESTORE']);self.put('results/R-NEW.json',r)
        self.resultmod('supersedes',['R-NEW']);m=self.get('assessment.json');m['result_ids'].append('R-NEW');self.put('assessment.json',m)
        with self.assertRaises(pep.ValidationError):self.summary()
    def test_38_cross_instance_supersession_rejected(self):
        self.resultmod('supersedes',['R-I-CORRUPT'])
        with self.assertRaises(pep.ValidationError):self.summary()
    def test_39_evaluator_mismatch_rejected(self):
        self.resultmod('evaluator_digest','sha256:'+'f'*64)
        with self.assertRaises(pep.ValidationError):self.summary()
    def test_40_qualification_scope_mismatch_rejected(self):
        self.mod('qualifications/Q-TOY.json','scope_instance_ids',['I-CORRUPT'])
        with self.assertRaises(pep.ValidationError):self.summary()
    def test_41_missing_measurement_binding_unknown(self):
        self.assignment(lambda a:a['instances'][0].update(measurement_binding_ref=None))
        self.assertEqual(self.summary()['mandatory_gate_state'],'BLOCKED')
    def test_42_wrong_measurement_binding_rejected(self):
        self.mod('measurement-bindings/MB-I-RESTORE.json','criterion_id','PEP-01-01-01')
        with self.assertRaises(pep.ValidationError):self.summary()
    def test_43_error_cannot_be_product_pass(self):
        self.resultmod('execution','ERROR')
        with self.assertRaises(pep.ValidationError):self.summary()
    def test_44_empty_evidence_cannot_pass(self):
        self.resultmod('evidence_ids',[]);self.assertEqual(self.summary()['weights']['unknown_weight'],1)
    def test_45_relative_path_escape_rejected(self):
        with self.assertRaises(pep.ValidationError):pep.safe_file(self.b,'../other.json')
    def test_46_absolute_path_rejected(self):
        with self.assertRaises(pep.ValidationError):pep.safe_file(self.b,'/etc/passwd')
    def test_47_windows_path_escape_rejected(self):
        with self.assertRaises(pep.ValidationError):pep.safe_file(self.b,'C:/Windows/file')
    def test_48_symlink_evidence_rejected(self):
        p=self.b/'raw/link.json'
        try:p.symlink_to(self.b/'raw/observations.json')
        except OSError:self.skipTest('host does not permit symlink creation')
        with self.assertRaises(pep.ValidationError):pep.safe_file(self.b,'raw/link.json')
    def test_49_duplicate_json_keys_rejected(self):
        p=self.root/'bad.json';p.write_text('{"x":1,"x":2}')
        with self.assertRaises(pep.ValidationError):pep.load_json(p)
    def test_50_nan_json_rejected(self):
        p=self.root/'bad.json';p.write_text('{"x":NaN}')
        with self.assertRaises(pep.ValidationError):pep.load_json(p)
    def test_51_timezone_required(self):
        with self.assertRaises(pep.ValidationError):pep.parse_time('2026-09-10T12:00:00')
    def test_52_schema_unknown_keyword_rejected(self):
        with self.assertRaises(pep.ValidationError):pep.validate_shape({}, {'unevaluatedProperties':False})
    def test_53_schema_unknown_field_rejected(self):
        r=self.get('results/R-I-RESTORE.json');r['claim_everything_done']=True
        with self.assertRaises(pep.ValidationError):pep.validate_record(r)
    def test_54_operational_placeholders_rejected(self):
        d=pep.load_json(ROOT/'templates/intent.template.json');d['record_status']='OPERATIONAL'
        with self.assertRaises(pep.ValidationError):pep.validate_record(d)
    def test_55_templates_have_valid_shapes(self):
        for p in (ROOT/'templates').glob('*.json'):
            with self.subTest(file=p.name):pep.validate_record(pep.load_json(p))
    def test_56_all_profiles_valid(self):
        for p in (ROOT/'profiles').glob('*.json'):
            with self.subTest(file=p.name):pep.validate_record(pep.load_json(p))
    def test_57_init_does_not_overwrite(self):
        dst=self.root/'new';pep.init_assessment(dst,'cli','example')
        self.assertEqual(pep.summarize_bundle(dst)['mandatory_gate_state'],'NOT_EVALUATED')
        with self.assertRaises(pep.ValidationError):pep.init_assessment(dst,'cli','example')
    def test_58_inspection_is_bounded(self):
        d=self.root/'inspect';d.mkdir()
        for n in range(5):(d/f'{n}.txt').write_text('secret contents not read')
        out=pep.inspect_metadata(d,2);self.assertEqual(len(out['files']),2);self.assertTrue(out['truncated'])
        self.assertNotIn('secret',json.dumps(out))
    def test_59_inspection_skips_generated_directories(self):
        d=self.root/'inspect';(d/'node_modules').mkdir(parents=True);(d/'node_modules/private.js').write_text('x')
        out=pep.inspect_metadata(d);self.assertEqual(len(out['files']),0);self.assertIn('node_modules/',out['excluded_or_unreadable'])
    def test_60_outbox_cannot_claim_delivery_without_receipt(self):
        d=pep.load_json(ROOT/'templates/outbox.template.json');d.update(state='DELIVERED',receipt_ref=None)
        with self.assertRaises(pep.ValidationError):pep.validate_record(d)
    def test_61_canonical_object_key_order_invariant(self):
        self.assertEqual(pep.value_digest({'a':1,'b':2}),pep.value_digest({'b':2,'a':1}))
    def test_62_current_fail_noncompensating(self):
        self.resultmod('verdict','FAIL');self.assignment(lambda a:a['instances'][1].update(weight=9999))
        self.assertEqual(self.summary()['mandatory_gate_state'],'FAIL')
    def test_63_random_weighted_totals_match(self):
        rng=random.Random(12)
        for _ in range(30):
            p,f=rng.randint(1,100),rng.randint(1,100)
            self.assignment(lambda a:a['instances'][0].update(weight=p))
            self.assignment(lambda a:a['instances'][1].update(weight=f))
            self.resultmod('verdict','PASS');self.mod('results/R-I-CORRUPT.json','verdict','FAIL')
            self.assertAlmostEqual(self.summary()['assessed_pass_rate'],p/(p+f))
    def test_64_undefined_denominator_not_perfect(self):
        dst=self.root/'empty';pep.init_assessment(dst,'bootstrap','example')
        out=pep.summarize_bundle(dst);self.assertIsNone(out['assessed_pass_rate']);self.assertIsNone(out['assessment_coverage'])
    def test_65_unknown_evidence_record_rejected(self):
        self.resultmod('evidence_ids',['EV-NOT-THERE'])
        with self.assertRaises(pep.ValidationError):self.summary()
    def test_66_invalid_expiry_order_rejected(self):
        self.resultmod('expires_at','2000-01-01T00:00:00Z')
        with self.assertRaises(pep.ValidationError):self.summary()
    def test_67_deterministic_reduction(self):self.assertEqual(self.summary(),self.summary())
    def test_68_source_kind_mismatch_rejected(self):
        self.mod('evidence/EV-OBS.json','role','QUALIFICATION')
        with self.assertRaises(pep.ValidationError):self.summary()

if __name__=='__main__':unittest.main(verbosity=2)
