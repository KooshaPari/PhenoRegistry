"""Reference schema/consistency tests, not native product integration tests."""
from pathlib import Path
from copy import deepcopy
import importlib.util
import json
import unittest
import hashlib
from graphlib import TopologicalSorter
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('fedcheck',ROOT/'federation/check_plans.py')
fed=importlib.util.module_from_spec(spec);spec.loader.exec_module(fed)
class FederationTests(unittest.TestCase):
    def setUp(self):
        self.ms=json.loads((ROOT/'federation/examples/manifests.json').read_text())
        self.p=json.loads((ROOT/'federation/examples/perspective-a.json').read_text())
    def bad(self):self.assertEqual(fed.validate_plan(self.ms,self.p)['status'],'INVALID')
    def test_valid_forward(self):self.assertFalse(fed.validate_plan(self.ms,self.p)['errors'])
    def test_valid_reverse(self):
        p=json.loads((ROOT/'federation/examples/perspective-b.json').read_text());self.assertFalse(fed.validate_plan(self.ms,p)['errors'])
    def test_no_permission_claim(self):
        r=fed.validate_plan(self.ms,self.p);self.assertFalse(r['activation_authorized']);self.assertFalse(r['grant_authenticity_checked']);self.assertFalse(r['product_behavior_verified'])
    def test_missing_field(self):del self.p['workspace'];self.bad()
    def test_unknown_field(self):self.p['auto_merge_all_data']=True;self.bad()
    def test_fake_live_result(self):self.p['runtime_result']={'pass':True};self.bad()
    def test_fake_approval(self):self.p['authorization_receipt']='approved-by-agent';self.bad()
    def test_non_synthetic(self):self.p['synthetic']=False;self.bad()
    def test_duplicate_product(self):self.ms[1]['product_id']=self.ms[0]['product_id'];self.bad()
    def test_duplicate_manifest(self):self.ms[1]['id']=self.ms[0]['id'];self.bad()
    def test_digest_mismatch(self):self.p['package_locks'][0]['artifact_sha256']='c'*64;self.bad()
    def test_unknown_lock(self):self.p['package_locks'][0]['manifest_id']='SYN-UNKNOWN';self.bad()
    def test_unlocked_provider(self):self.p['package_locks'].pop();self.bad()
    def test_unknown_provider(self):self.p['bindings'][0]['provider']='SYN-UNKNOWN';self.bad()
    def test_unknown_primary(self):self.p['primary_app']='SYN-UNKNOWN';self.bad()
    def test_wrong_principal(self):self.p['bindings'][0]['principal']='SYN-OTHER';self.bad()
    def test_wrong_workspace(self):self.p['bindings'][0]['workspace']='SYN-OTHER';self.bad()
    def test_missing_grant_ref(self):self.p['bindings'][0]['grant_references']=[];self.bad()
    def test_contract_mismatch(self):self.p['bindings'][0]['semantic_contract']='SYN-WRONG';self.bad()
    def test_unknown_capability(self):self.p['bindings'][0]['capability']='SYN-UNKNOWN';self.bad()
    def test_owner_substitution(self):self.p['bindings'][0]['data_authority']='SYN-APP-A';self.bad()
    def test_offer_unknown_owner(self):self.ms[1]['state_authorities']=[];self.bad()
    def test_duplicate_binding(self):
        b=deepcopy(self.p['bindings'][0]);b['instance_scope']='SYN-DIFFERENT';self.p['bindings'].append(b);self.bad()
    def test_unknown_dependency(self):self.p['bindings'][0]['depends_on']=['SYN-UNKNOWN'];self.bad()
    def test_startup_cycle(self):self.p['bindings'][0]['depends_on']=[self.p['bindings'][0]['id']];self.bad()
    def test_wrong_host(self):self.p['mounts'][0]['host']='SYN-APP-B';self.bad()
    def test_bad_slot(self):self.p['mounts'][0]['slot_id']='SYN-UNKNOWN';self.bad()
    def test_unqualified_adapter(self):self.p['mounts'][0]['adapter']='web-module';self.bad()
    def test_unknown_surface_binding(self):self.p['mounts'][0]['binding_id']='SYN-UNKNOWN';self.bad()
    def test_unknown_parent(self):self.p['mounts'][0]['parent_mount']='SYN-UNKNOWN';self.bad()
    def test_mount_cycle(self):self.p['mounts'][0]['parent_mount']=self.p['mounts'][0]['id'];self.bad()
    def test_requirements_and_scenarios(self):
        r=json.loads((ROOT/'federation/requirements.json').read_text());t=json.loads((ROOT/'federation/acceptance-scenarios.json').read_text())
        ids={x['id'] for x in r};self.assertEqual(len(ids),len(r));self.assertEqual(ids,{y for x in t for y in x['requirement_ids']})
        self.assertTrue(all(x['status']=='PLANNED_NOT_EXECUTED' and not x['actual_evidence_ids'] for x in t))
    def test_all_existing_owner_packets(self):
        index=json.loads((ROOT/'portfolio/CURRENT-REPO-INDEX.json').read_text());o=json.loads((ROOT/'federation/owner-map.json').read_text())
        self.assertEqual({x['repository_id'] for x in index['entries']},{x['repository_id'] for x in o})
        for x in index['entries']:self.assertTrue((ROOT/x['folder']/'FEDERATION.md').is_file())
    def test_federation_work_dag(self):
        w=json.loads((ROOT/'federation/work-packages.json').read_text());self.assertEqual(len(w),len(list(TopologicalSorter({x['id']:x['depends_on'] for x in w}).static_order())))
        self.assertTrue(all(x['mutation_authorized'] is False and not x['completion_evidence'] for x in w))
    def test_exact_intent_digest(self):
        p=json.loads((ROOT/'intent/INT-005-provenance.json').read_text());self.assertEqual(hashlib.sha256((ROOT/'intent'/p['path']).read_bytes()).hexdigest(),p['sha256'])
if __name__=='__main__':unittest.main()
