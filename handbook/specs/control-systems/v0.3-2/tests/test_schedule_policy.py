from dataclasses import replace
from pathlib import Path
import sys
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from schedule_policy import ScheduleInput, evaluate

class ScheduleTests(unittest.TestCase):
    def setUp(self):
        self.base = ScheduleInput('candidate-new', 'candidate-observed', 2, 'push', True, True)
    def run_case(self, outcome, **kw):
        result=evaluate(replace(self.base, **kw))
        self.assertEqual(result.outcome,outcome)
        self.assertFalse(result.authorizes_deployment)
        self.assertFalse(result.may_advance_watermark)
        return result
    def test_two_commits_eligible(self): self.run_case('eligible')
    def test_one_commit_waits(self): self.run_case('defer',new_eligible_commits=1)
    def test_zero_commits_waits(self): self.run_case('defer',new_eligible_commits=0)
    def test_single_commit_tick(self): self.run_case('eligible',event='schedule',scheduled_tick_due=True,new_eligible_commits=1)
    def test_config_only_tick(self): self.run_case('eligible',event='schedule',scheduled_tick_due=True,new_eligible_commits=0)
    def test_schedule_is_not_implicitly_due(self): self.run_case('defer',event='schedule',new_eligible_commits=1)
    def test_same_candidate_noop(self): self.run_case('noop',candidate_key='candidate-observed',new_eligible_commits=0)
    def test_unknown_lineage_blocked(self): self.run_case('blocked',lineage_verified=False)
    def test_unknown_count_blocked(self): self.run_case('blocked',new_eligible_commits=None)
    def test_unknown_lineage_even_with_tick(self): self.run_case('blocked',lineage_verified=False,event='schedule',scheduled_tick_due=True)
    def test_unqualified_target_blocked(self): self.run_case('blocked',target_qualified=False)
    def test_force_does_not_qualify_target(self): self.run_case('blocked',target_qualified=False,force_requested=True,force_authorized=True)
    def test_force_does_not_qualify_lineage(self): self.run_case('blocked',lineage_verified=False,force_requested=True,force_authorized=True)
    def test_missing_baseline_is_not_implicit_bootstrap(self): self.run_case('blocked',observed_healthy_key=None)
    def test_bootstrap_authorized_manually(self): self.run_case('eligible',event='manual',observed_healthy_key=None,bootstrap_authorized=True,new_eligible_commits=None,lineage_verified=False)
    def test_force_not_bootstrap(self): self.run_case('blocked',observed_healthy_key=None,force_requested=True,force_authorized=True)
    def test_authorized_force(self): self.run_case('eligible',event='manual',new_eligible_commits=1,force_requested=True,force_authorized=True)
    def test_unauthorized_force(self): self.run_case('blocked',event='manual',force_requested=True)
    def test_authorization_without_request_not_force(self): self.run_case('defer',event='manual',new_eligible_commits=1,force_authorized=True)
    def test_offline_coalesces_latest(self): self.run_case('queue_latest',target_online=False)
    def test_busy_writer_coalesces(self): self.run_case('coalesce',lease_available=False)
    def test_no_eligible_work_offline(self): self.run_case('defer',target_online=False,new_eligible_commits=1)
    def test_resume_due_single_commit(self): self.run_case('eligible',event='resume',scheduled_tick_due=True,new_eligible_commits=1)
    def test_invalid_numbers(self):
        for n in (-1, 1.5, True, '2'):
            with self.subTest(n=n), self.assertRaises(ValueError):evaluate(replace(self.base,new_eligible_commits=n))
    def test_invalid_flags(self):
        with self.assertRaises(ValueError):evaluate(replace(self.base,target_online='true'))
    def test_invalid_event(self):
        with self.assertRaises(ValueError):evaluate(replace(self.base,event='random'))
    def test_invalid_key(self):
        with self.assertRaises(ValueError):evaluate(replace(self.base,candidate_key=' '))
    def test_tick_on_push_rejected(self):
        with self.assertRaises(ValueError):evaluate(replace(self.base,scheduled_tick_due=True))
    def test_bootstrap_on_push_rejected(self):
        with self.assertRaises(ValueError):evaluate(replace(self.base,observed_healthy_key=None,bootstrap_authorized=True))
    def test_input_type_rejected(self):
        with self.assertRaises(TypeError):evaluate({})

if __name__=='__main__':unittest.main()
