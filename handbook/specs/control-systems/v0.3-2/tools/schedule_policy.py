#!/usr/bin/env python3
"""Pure scheduling reference; eligibility is NOT deployment authorization.

No network, provider, shell, clock or credential operations are performed. Callers
must obtain inputs from trusted observations and independently enforce CI and
promotion authority. See docs/17-lifecycle-and-delivery-profiles.md.
"""
from __future__ import annotations
from dataclasses import asdict, dataclass
from typing import Literal
import argparse
import json
from pathlib import Path

Event = Literal['push', 'schedule', 'manual', 'resume']
Outcome = Literal['noop', 'defer', 'blocked', 'queue_latest', 'coalesce', 'eligible']

@dataclass(frozen=True)
class ScheduleInput:
    candidate_key: str
    observed_healthy_key: str | None
    new_eligible_commits: int | None
    event: Event
    target_qualified: bool
    lineage_verified: bool
    target_online: bool = True
    lease_available: bool = True
    scheduled_tick_due: bool = False
    force_requested: bool = False
    force_authorized: bool = False
    bootstrap_authorized: bool = False

@dataclass(frozen=True)
class Decision:
    outcome: Outcome
    reason: str
    may_advance_watermark: bool = False
    authorizes_deployment: bool = False


def evaluate(value: ScheduleInput) -> Decision:
    """Return a scheduling decision after validating the input shape.

    A watermark advances only in the real controller after healthy observation,
    never inside this function. Even an eligible result still requires checks,
    approval, a fenced lease, and an exact target-generation precondition.
    """
    if not isinstance(value, ScheduleInput):
        raise TypeError('Expected ScheduleInput')
    if not isinstance(value.candidate_key, str) or not value.candidate_key.strip():
        raise ValueError('candidate_key must be a nonempty immutable identity')
    if value.observed_healthy_key is not None and (
        not isinstance(value.observed_healthy_key, str) or not value.observed_healthy_key.strip()
    ):
        raise ValueError('observed_healthy_key must be a nonempty identity or null')
    if value.event not in ('push', 'schedule', 'manual', 'resume'):
        raise ValueError('Unsupported event')
    n = value.new_eligible_commits
    if n is not None and (type(n) is not int or n < 0):
        raise ValueError('new_eligible_commits must be a nonnegative integer or null')
    for name in ('target_qualified', 'lineage_verified', 'target_online',
                 'lease_available', 'scheduled_tick_due', 'force_requested',
                 'force_authorized', 'bootstrap_authorized'):
        if type(getattr(value, name)) is not bool:
            raise ValueError(f'{name} must be a boolean')
    if value.scheduled_tick_due and value.event not in ('schedule', 'resume'):
        raise ValueError('A due scheduled tick belongs to a schedule/resume event')
    if value.bootstrap_authorized and value.event != 'manual':
        raise ValueError('Bootstrap is a separately authorized manual decision')
    if value.force_requested and not value.force_authorized:
        return Decision('blocked', 'unauthorized_force')
    if value.candidate_key == value.observed_healthy_key:
        return Decision('noop', 'candidate_already_observed_healthy')
    if not value.target_qualified:
        return Decision('blocked', 'target_unqualified')
    first = value.observed_healthy_key is None
    if first and not value.bootstrap_authorized:
        return Decision('blocked', 'missing_success_watermark_requires_bootstrap')
    if not first and (not value.lineage_verified or n is None):
        return Decision('blocked', 'lineage_or_change_count_unknown')
    due = (first and value.bootstrap_authorized) or value.scheduled_tick_due or (
        n is not None and n > 1
    ) or (value.force_requested and value.force_authorized)
    if not due:
        return Decision('defer', 'threshold_not_met_and_no_tick_or_force')
    if not value.target_online:
        return Decision('queue_latest', 'eligible_target_offline')
    if not value.lease_available:
        return Decision('coalesce', 'environment_writer_busy')
    return Decision('eligible', 'eligible_for_independent_ci_policy_and_authorization')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input_json', type=Path)
    args = parser.parse_args()
    try:
        payload = json.loads(args.input_json.read_text(encoding='utf-8'))
        if not isinstance(payload, dict):
            raise ValueError('Input JSON must be an object')
        result = evaluate(ScheduleInput(**payload))
    except (OSError, TypeError, ValueError) as exc:
        parser.exit(2, f'Invalid scheduling input: {exc}\n')
    print(json.dumps(asdict(result), indent=2))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
