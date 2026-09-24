from __future__ import annotations
import copy,json,sys,unittest,tempfile,shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from validate_current_packets import validate_records

def inputs():
    return [json.loads((ROOT/p).read_text()) for p in ('portfolio/live-inventory-2026-09-16.json','portfolio/CURRENT-REPO-INDEX.json','records/current-repository-state.json')]

class CurrentPackets(unittest.TestCase):
    def test_actual(self):self.assertEqual(validate_records(*inputs(),ROOT),[])
    def mutate(self,change):
        a=inputs();change(a);self.assertTrue(validate_records(*a,ROOT))
    def test_missing_owner(self):self.mutate(lambda a:a[1]['entries'].pop())
    def test_duplicate_owner(self):self.mutate(lambda a:a[1]['entries'].append(copy.deepcopy(a[1]['entries'][0])))
    def test_wrong_count(self):self.mutate(lambda a:a[1].update(expected_count=999))
    def test_pair_allocation(self):self.mutate(lambda a:a[1]['entries'][0].update(owner_chats=2))
    def test_ten_seats(self):self.mutate(lambda a:a[2][0].update(owner_chat_count=10))
    def test_unknown_receipt(self):self.mutate(lambda a:a[1]['entries'][0].update(actual_chat_receipt='fabricated'))
    def test_fake_session(self):self.mutate(lambda a:a[2][0].update(owner_chat_id='fake'))
    def test_fake_heartbeat(self):self.mutate(lambda a:a[2][0].update(owner_chat_evidence='OBSERVED'))
    def test_stale_name(self):self.mutate(lambda a:a[1]['entries'][0].update(name='OLD'))
    def test_wrong_branch(self):self.mutate(lambda a:a[2][0].update(default_branch='WRONG'))
    def test_fake_native(self):self.mutate(lambda a:a[2][0].update(native_tests_run_by_this_audit=True))
    def test_fake_install(self):self.mutate(lambda a:a[2][0].update(installed_product_qualified=True))
    def test_unauthorized(self):self.mutate(lambda a:a[2][0].update(new_authority_granted=True))
    def test_fake_completion(self):self.mutate(lambda a:a[2][0].update(repository_completion='COMPLETE'))
    def test_bad_sha(self):self.mutate(lambda a:a[2][0].update(sampled_commit='main'))
    def test_missing_source(self):self.mutate(lambda a:a[2][0].update(sources=[]))
    def test_missing_next(self):self.mutate(lambda a:a[2][0].update(next_actions=[]))
    def test_fake_execution(self):self.mutate(lambda a:a[2][0]['next_actions'][0].update(status='COMPLETE'))
    def test_sibling_write(self):self.mutate(lambda a:a[2][0]['next_actions'][0].update(cross_repo_writes_authorized=True))
    def test_empty_acceptance(self):self.mutate(lambda a:a[2][0]['next_actions'][0].update(acceptance=''))
    def test_projection_change(self):self.mutate(lambda a:a[2][0].update(movement='not the published record'))
    def test_missing_state(self):self.mutate(lambda a:a[2].pop())
    def test_duplicate_state(self):self.mutate(lambda a:a[2].append(copy.deepcopy(a[2][0])))
    def test_path_escape(self):self.mutate(lambda a:a[1]['entries'][0].update(folder='../escape'))
    def test_prefix_not_dispatch(self):
        inv,idx,states=inputs();self.assertTrue(all(not e['name'].casefold().startswith('zz') for e in idx['entries']))
    def test_every_current_folder(self):
        inv,idx,states=inputs()
        for e in idx['entries']:
            with self.subTest(name=e['name']):self.assertTrue((ROOT/e['folder']/'AGENT-PROMPT.md').is_file())
    def test_empty_root_fails_missing_files(self):
        with tempfile.TemporaryDirectory() as tmp:self.assertTrue(validate_records(*inputs(),Path(tmp)))
