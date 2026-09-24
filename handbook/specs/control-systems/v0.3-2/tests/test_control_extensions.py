import json
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
class ControlExtensionTests(unittest.TestCase):
    def test_node_example_is_non_admitting(self):
        d=json.loads((ROOT/'examples/local-node.unqualified.json').read_text())
        self.assertEqual(d['trust_state'],'unqualified')
        self.assertFalse(d['admission']['accepting_work'])
    def test_review_example_forbids_cash_spend(self):
        d=json.loads((ROOT/'examples/review-provider.unqualified.json').read_text())
        self.assertFalse(d['cash_spend_allowed'])
        self.assertFalse(d['auto_refill'])
    def test_new_requirements_have_tests(self):
        d=json.loads((ROOT/'machine/docset.json').read_text())
        req={r['id']:r for r in d['requirements']}
        tests={t['id']:t for t in d['acceptance_tests']}
        for n in range(35,59):
            rid=f'FR-DEP-{n:03d}'; tid=f'AT-DEP-{n:03d}'
            self.assertIn(rid,req); self.assertIn(tid,tests); self.assertIn(tid,req[rid]['acceptance_test_ids'])
    def test_emergent_and_review_work_packages_exist(self):
        d=json.loads((ROOT/'machine/docset.json').read_text())
        ids={w['id'] for w in d['work_items']}
        self.assertTrue({'WP-18','WP-19','WP-20','WP-21'} <= ids)
if __name__=='__main__': unittest.main()
