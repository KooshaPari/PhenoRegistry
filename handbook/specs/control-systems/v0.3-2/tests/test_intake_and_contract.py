from copy import deepcopy
from pathlib import Path
import hashlib
import json
import re
import sys
import unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
from index_forge_export import index_bytes

class IntakeTests(unittest.TestCase):
    def fixture(self):
        cid='12345678-1234-1234-1234-123456789abc'
        k_cid='conversation'+'_id'
        k_msg='mess'+'ages'
        k_ct='cont'+'ent'
        meta={k_cid:cid,'title':'fixture','is_compressed':1,'message_count':1}
        ctx={k_cid:cid,k_msg:[{'message':{'text':{'role':'User',k_ct:'An inert test prompt'}}}]}
        text='# Fixture\n\n## Conversation '+cid+' (.forge.writes.db)\n\n### Database metadata\n```json\n'+json.dumps(meta)+'\n```\n\n### Readable message text\n\n#### Message 1\n\nAn inert test prompt\n\n### Complete decoded context (lossless JSON representation)\n`````json\n'+json.dumps(ctx)+'\n`````\n'
        return text.encode()
    def test_fixture_counts_once(self):
        m,i=index_bytes(self.fixture());self.assertEqual(m['message_count_decoded'],1);self.assertEqual(m['compressed_conversations'],1);self.assertFalse(m['raw_included']);self.assertEqual(len(i),1)
    def test_parser_deterministic(self):self.assertEqual(index_bytes(self.fixture()),index_bytes(self.fixture()))
    def test_windows_line_endings(self):
        a,ai=index_bytes(self.fixture());b,bi=index_bytes(self.fixture().replace(b'\n',b'\r\n'))
        self.assertEqual(ai,bi);self.assertEqual(a['source_lines'],b['source_lines']);self.assertNotEqual(a['source_sha256'],b['source_sha256'])
    def test_reject_truncated_context(self):
        with self.assertRaises(ValueError):index_bytes(self.fixture().split(('"'+'mess'+'ages"').encode())[0])
    def test_reject_missing_sections(self):
        with self.assertRaises(ValueError):index_bytes(b'# not a Forge export')
    def test_reject_duplicate_identity(self):
        with self.assertRaises(ValueError):index_bytes(self.fixture()+self.fixture())
    def test_reject_message_enumeration_drift(self):
        with self.assertRaises(ValueError):index_bytes(self.fixture().replace(b'#### Message 1',b'#### Message 2'))
    def test_released_intake_summary(self):
        m=json.loads((ROOT/'evidence/session/intake-manifest.json').read_text());i=json.loads((ROOT/'evidence/session/conversation-index.json').read_text())
        self.assertEqual(len(i),81);self.assertEqual(sum(x['message_count_decoded'] for x in i),4588)
        self.assertEqual(m['conversation_count'],len(i));self.assertEqual(sum(bool(x['compressed_flag']) for x in i),81)
        self.assertEqual(sum(m['role_counts'].values()),4588)
    def test_released_derivative_hashes(self):
        entries=json.loads((ROOT/'evidence/session/evidence-index.json').read_text());self.assertEqual(len(entries),16)
        for x in entries:
            p=(ROOT/x['bundled_path']).resolve();self.assertTrue(p.is_relative_to(ROOT))
            self.assertEqual(hashlib.sha256(p.read_bytes()).hexdigest(),x['sha256'])
    def test_historical_invalid_workflow_reference(self):
        s=(ROOT/'evidence/session/E007.md').read_text();self.assertIn('.github/workflows/reusable/nightly-dev-deploy.yml@main',s)
    def test_historical_context_spacing(self):
        s=(ROOT/'evidence/session/E008.md').read_text();self.assertIn('"ci/lint"',s);self.assertNotIn('"ci / lint"',s)
    def test_historical_no_rollback_api(self):
        s=(ROOT/'evidence/session/E009.md').read_text();self.assertNotIn('/rollback',s);self.assertNotIn('rollback)',s)
    def test_historical_fail_open_health(self):
        s=(ROOT/'evidence/session/E009.md').read_text();self.assertRegex(s,r'Could not resolve service URL[^\n]*\n[^\n]*exit 0')

class ContractTests(unittest.TestCase):
    def setUp(self):self.api=json.loads((ROOT/'contracts/control-api.openapi.json').read_text())
    def test_design_only_without_server(self):
        self.assertEqual(self.api['x-status'],'proposed_not_implemented');self.assertNotIn('servers',self.api)
    def test_all_internal_refs_resolve(self):
        def walk(x):
            if isinstance(x,dict):
                if '$ref' in x:
                    self.assertTrue(x['$ref'].startswith('#/'));a=self.api
                    for part in x['$ref'][2:].split('/'):a=a[part]
                    self.assertIsInstance(a,dict)
                for v in x.values():walk(v)
            elif isinstance(x,list):
                for v in x:walk(v)
        walk(self.api)
    def test_unique_operation_names(self):
        ids=[v['operationId'] for item in self.api['paths'].values() for v in item.values()]
        self.assertEqual(len(ids),len(set(ids)))
    def test_privileged_operations_require_precondition_and_idempotency(self):
        for p in ['/v1/authorizations','/v1/deployments','/v1/recoveries']:
            headers=self.api['paths'][p]['post']['parameters']
            self.assertEqual({x['name'] for x in headers},{'If-Match','Idempotency-Key'});self.assertTrue(all(x['required'] for x in headers))
    def test_no_self_declared_approver_in_request(self):
        s=self.api['components']['schemas']['AuthorizationRequest'];self.assertFalse(s['additionalProperties'])
        self.assertTrue({'approved','issuer_principal','actor'}.isdisjoint(s['properties']))
    def test_global_auth_required(self):self.assertEqual(self.api['security'],[{'bearerAuth':[]}])
    def test_unknown_is_explicit(self):
        s=self.api['components']['schemas'];self.assertIn('unknown',s['Operation']['properties']['state']['enum']);self.assertIn('unknown',s['Observation']['properties']['state']['enum'])

if __name__=='__main__':unittest.main()
