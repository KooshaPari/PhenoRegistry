"""Dossier-layer tests. Do not interpret these as product/evaluator certification."""
from __future__ import annotations
from pathlib import Path
import copy,json,shutil,sys,tempfile,unittest
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
import dossier
pep=dossier.pep

class DossierTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='dossier-test-')
        self.addCleanup(self.temp.cleanup)
        self.path=Path(self.temp.name)/'dossier'
    def copied(self,name='04-polished-dashboard'):
        shutil.copytree(ROOT/'examples'/name,self.path);return self.path
    def mutate(self,relative,fn):
        p=self.path/relative;x=pep.load_json(p);fn(x);p.write_text(dossier.dumps(x));return x
    def test_all_eight_dossiers_consistent(self):
        self.assertEqual(len(dossier.case_dirs()),8)
        for p in dossier.case_dirs():self.assertEqual(dossier.verify(p)['status'],'CONSISTENT')
    def test_102_scoped_rows_not_102_new_criteria(self):
        self.assertEqual(sum(len(dossier.build_model(p)['rows']) for p in dossier.case_dirs()),102)
    def test_dashboard_spans_18_domains(self):
        m=dossier.build_model(ROOT/'examples/04-polished-dashboard')
        self.assertEqual(len({r['domain'] for r in m['rows']}),18)
    def test_executed_before_fails(self):
        self.assertEqual(dossier.build_model(ROOT/'examples/01-restoration-before')['evidence_summary']['mandatory_gate_state'],'FAIL')
    def test_executed_after_passes_only_fixture(self):
        m=dossier.build_model(ROOT/'examples/02-restoration-after')
        self.assertEqual(m['evidence_summary']['mandatory_gate_state'],'PASS')
        self.assertEqual(m['dossier']['example_class'],'EXECUTED_FIXTURE')
    def test_fictional_premises_get_zero_evidence_credit(self):
        for p in dossier.case_dirs()[2:]:
            m=dossier.build_model(p)
            self.assertEqual(m['evidence_summary']['assessment_coverage'],0.0)
            self.assertEqual(m['evidence_summary']['mandatory_gate_state'],'BLOCKED')
            self.assertIsNotNone(m['illustrative_summary'])
    def test_assumed_dashboard_failures_remain_visible(self):
        m=dossier.build_model(ROOT/'examples/04-polished-dashboard')
        self.assertGreater(m['illustrative_summary']['counts']['FAIL'],0)
        self.assertTrue(any(g['status']=='FAIL' for g in m['illustrative_summary']['gates']))
    def test_illustrative_cannot_mark_review_accepted(self):
        self.copied();self.mutate('results/R-I-01.json',lambda x:x.update(review_status='ACCEPTED'))
        with self.assertRaisesRegex(pep.ValidationError,'PROPOSED'):dossier.build_model(self.path)
    def test_illustrative_cannot_claim_local_execution_origin(self):
        self.copied();self.mutate('evidence/EV-SCENARIO.json',lambda x:x.update(origin='LOCAL_OBSERVATION'))
        with self.assertRaisesRegex(pep.ValidationError,'masquerade'):dossier.build_model(self.path)
    def test_illustrative_cannot_relabel_as_executed_fixture(self):
        self.copied();self.mutate('dossier.json',lambda x:x.update(example_class='EXECUTED_FIXTURE'))
        with self.assertRaisesRegex(pep.ValidationError,'source digest'):dossier.build_model(self.path)
    def test_example_cannot_relabel_as_operational(self):
        self.copied();self.mutate('dossier.json',lambda x:x.update(record_status='OPERATIONAL'))
        with self.assertRaises(pep.ValidationError):dossier.build_model(self.path)
    def test_subject_descriptor_tamper_rejected(self):
        self.copied();self.mutate('subject.json',lambda x:x.update(subject_key='other-subject'))
        with self.assertRaisesRegex(pep.ValidationError,'subject identity'):dossier.build_model(self.path)
    def test_raw_evidence_tamper_rejected(self):
        self.copied();self.mutate('raw/scenario.json',lambda x:x.update(product_execution_performed=True))
        with self.assertRaisesRegex(pep.ValidationError,'evidence digest'):dossier.build_model(self.path)
    def test_rehashed_fiction_still_requires_fiction_label(self):
        self.copied();self.mutate('raw/scenario.json',lambda x:x.update(product_execution_performed=True))
        self.mutate('evidence/EV-SCENARIO.json',lambda x:x.update(digest=pep.file_digest(self.path/'raw/scenario.json')))
        with self.assertRaisesRegex(pep.ValidationError,'fictional-premise'):dossier.build_model(self.path)
    def test_assignment_byte_tamper_rejected(self):
        self.copied();p=self.path/'assignment.json';p.write_text(p.read_text()+' ')
        with self.assertRaisesRegex(pep.ValidationError,'assignment digest'):dossier.build_model(self.path)
    def test_html_drift_rejected(self):
        self.copied();p=self.path/'ASSESSMENT.html';p.write_text(p.read_text().replace('broken outcome','complete outcome'))
        with self.assertRaisesRegex(pep.ValidationError,'view drift'):dossier.verify(self.path)
    def test_markdown_drift_rejected(self):
        self.copied();p=self.path/'ASSESSMENT.md';p.write_text(p.read_text()+'\nInvented acceptance.\n')
        with self.assertRaisesRegex(pep.ValidationError,'view drift'):dossier.verify(self.path)
    def test_yaml_drift_rejected(self):
        self.copied();p=self.path/'views/assessment.yaml';p.write_text(p.read_text()+'# changed\n')
        with self.assertRaisesRegex(pep.ValidationError,'view drift'):dossier.verify(self.path)
    def test_render_deterministic(self):
        p=ROOT/'examples/04-polished-dashboard'
        self.assertEqual(dossier.expected_views(p),dossier.expected_views(p))
    def test_render_changes_only_views(self):
        self.copied();before=dossier.inputs(self.path);dossier.render(self.path)
        self.assertEqual(before,dossier.inputs(self.path))
    def test_jsonl_carries_each_source_digest(self):
        p=ROOT/'examples/04-polished-dashboard'
        for line in (p/'views/records.jsonl').read_text().splitlines():
            r=json.loads(line);self.assertEqual(r['source_byte_digest'],pep.file_digest(p/r['source_path']))
    def test_duplicate_json_keys_rejected(self):
        self.copied();p=self.path/'dossier.json';s=p.read_text();p.write_text(s.replace('"kind": "dossier"','"kind": "dossier", "kind": "dossier"'))
        with self.assertRaisesRegex(pep.ValidationError,'duplicate'):dossier.build_model(self.path)
    def test_missing_row_note_rejected(self):
        self.copied();self.mutate('dossier.json',lambda x:x['row_notes'].pop())
        with self.assertRaisesRegex(pep.ValidationError,'exact instance'):dossier.build_model(self.path)
    def test_unknown_finding_evidence_rejected(self):
        self.copied();p=next((self.path/'findings').glob('*.json'))
        self.mutate(str(p.relative_to(self.path)),lambda x:x.update(evidence_refs=['MISSING']))
        with self.assertRaisesRegex(pep.ValidationError,'unresolved'):dossier.build_model(self.path)
    def test_unlisted_finding_rejected(self):
        self.copied();f=next((self.path/'findings').glob('*.json'));shutil.copyfile(f,self.path/'findings/extra.json')
        with self.assertRaisesRegex(pep.ValidationError,'file set mismatch'):dossier.build_model(self.path)
    def test_symlink_output_directory_rejected(self):
        self.copied();shutil.rmtree(self.path/'views');(self.path/'views').symlink_to(Path(self.temp.name),target_is_directory=True)
        with self.assertRaisesRegex(pep.ValidationError,'symlink'):dossier.render(self.path)
    def test_html_escapes_script_text(self):
        m=dossier.build_model(ROOT/'examples/04-polished-dashboard');m=copy.deepcopy(m)
        m['dossier']['title']='<script>alert(1)</script>'
        output=dossier.body_html(m)
        self.assertNotIn('<script>',output);self.assertIn('&lt;script&gt;',output)
    def test_markdown_escapes_html_tags(self):
        m=copy.deepcopy(dossier.build_model(ROOT/'examples/04-polished-dashboard'))
        m['dossier']['title']='<script>alert(1)</script>'
        self.assertNotIn('<script>',dossier.report_md(m))
    def test_service_unknown_applicability_not_hidden(self):
        m=dossier.build_model(ROOT/'examples/05-service-blocked-deployment')
        self.assertFalse(m['evidence_summary']['applicability_complete'])
        self.assertEqual(m['illustrative_summary']['counts']['UNRESOLVED'],1)
    def test_service_has_no_fake_receipt(self):
        p=ROOT/'examples/05-service-blocked-deployment/outbox/OUTBOX-SCENARIO-001.json'
        x=pep.load_json(p);self.assertIsNone(x['receipt_ref']);self.assertEqual(x['attempt_count'],0)
    def test_outbox_wrong_payload_rejected(self):
        self.copied('05-service-blocked-deployment')
        self.mutate('outbox/OUTBOX-SCENARIO-001.json',lambda x:x.update(payload_digest='sha256:'+'1'*64))
        with self.assertRaisesRegex(pep.ValidationError,'payload'):dossier.build_model(self.path)
    def test_grader_revision_preserves_subject(self):
        before=dossier.build_model(ROOT/'examples/07-grader-before');after=dossier.build_model(ROOT/'examples/08-grader-after')
        self.assertEqual(before['assignment']['subject_digest'],after['assignment']['subject_digest'])
        self.assertNotEqual(before['assessment']['assignment_digest'],after['assessment']['assignment_digest'])
        self.assertEqual(after['dossier']['lineage']['change_class'],'EVALUATOR_CORRECTION')
    def test_blank_template_not_evaluated(self):
        p=ROOT/'master/blank-assessment';m=dossier.build_model(p)
        self.assertEqual(m['dossier']['record_status'],'TEMPLATE')
        self.assertEqual(m['evidence_summary']['mandatory_gate_state'],'NOT_EVALUATED')
    def test_yaml_roundtrip_if_parser_available(self):
        try:import yaml
        except ImportError:self.skipTest('Optional independent YAML parser not installed.')
        for p in dossier.case_dirs():
            self.assertEqual(yaml.safe_load((p/'views/assessment.yaml').read_text()),pep.load_json(p/'views/assessment.json'))
    def test_no_invented_git_or_signing_identities(self):
        for p in dossier.case_dirs():
            d=pep.load_json(p/'dossier.json');r=pep.load_json(p/'views/build.json')
            self.assertIsNone(d['subject_identity']['source_revision']);self.assertTrue(r['generated_build_receipt_is_not_signed'])
            self.assertIsNone(r['report_commit']);self.assertIsNone(r['registry_commit'])

if __name__=='__main__':unittest.main(verbosity=2)
