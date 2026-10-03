"""Synthetic acceptance-predicate experiment, NOT a game/product grader.

Run with Python 3.10+: python evidence_gate_experiment.py [receipt.json]
Trust boundary: policy, accepted run ID, approved verifier build and raw artifacts
are supplied by an independently authenticated collector. Authentication,
signatures, protected policy storage and application behavior are NOT tested.
"""
from __future__ import annotations
import copy
import hashlib
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
import platform
import sys
from typing import Any

IDENTITY = ("product", "subject", "contract", "candidate", "configuration", "environment", "verifier", "verifier_version", "run_id")
OUTCOMES = {"pass", "fail", "skip", "error", "missing"}

def stamp(value: Any) -> datetime:
    if not isinstance(value, str):
        raise ValueError("timestamp is not a string")
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("timestamp lacks timezone")
    return parsed.astimezone(timezone.utc)

def evaluate(policy: dict[str, Any], receipt: dict[str, Any], artifacts: dict[str, bytes], now: datetime) -> dict[str, Any]:
    """Fail closed on malformed identity, missing evidence and contradictory results.

    This deliberately returns no average/percentage. The narrow synthetic gate
    closes only when every externally required criterion passes. A worker ID is
    deliberately not part of product/evidence identity.
    """
    errors: list[str] = []
    try:
        expected = policy["identity"]
        required = policy["criteria"]
        if not isinstance(required, list) or not required or any(not isinstance(x, str) or not x for x in required) or len(set(required)) != len(required):
            raise ValueError("policy criteria must be unique, nonempty strings")
        if set(expected) != set(IDENTITY) or any(not isinstance(expected[k], str) or not expected[k] for k in IDENTITY):
            raise ValueError("policy identity incomplete")
        ttl = policy["max_age_seconds"]
        if type(ttl) is not int or ttl <= 0:
            raise ValueError("invalid policy evidence lifetime")
        rows = receipt["results"]
        if not isinstance(rows, list) or not rows:
            raise ValueError("empty or malformed result set")
        seen: set[str] = set()
        for number, row in enumerate(rows):
            label = f"row:{number}"
            if not isinstance(row, dict):
                errors.append(f"{label}:malformed")
                continue
            criterion = row.get("criterion")
            if not isinstance(criterion, str) or criterion not in required:
                errors.append(f"{label}:unknown-criterion")
                continue
            label = criterion
            if criterion in seen:
                errors.append(f"{label}:duplicate-or-conflicting")
            seen.add(criterion)
            for key in IDENTITY:
                if row.get(key) != expected[key]:
                    errors.append(f"{label}:wrong-{key}")
            status = row.get("outcome")
            if not isinstance(status, str) or status not in OUTCOMES or status != "pass":
                errors.append(f"{label}:not-pass")
            if row.get("collector_status") != "complete":
                errors.append(f"{label}:collector-incomplete")
            if type(row.get("executed_cases")) is not int or row["executed_cases"] <= 0:
                errors.append(f"{label}:no-executed-cases")
            observed = stamp(row.get("observed_at"))
            if observed > now or now - observed > timedelta(seconds=ttl):
                errors.append(f"{label}:future-or-stale")
            artifact_id = row.get("artifact_id")
            digest = row.get("artifact_sha256")
            raw = artifacts.get(artifact_id) if isinstance(artifact_id, str) else None
            if not isinstance(raw, bytes) or not raw or not isinstance(digest, str) or hashlib.sha256(raw).hexdigest() != digest:
                errors.append(f"{label}:missing-or-wrong-artifact")
        for criterion in required:
            if criterion not in seen:
                errors.append(f"{criterion}:missing")
    except (KeyError, TypeError, ValueError, OverflowError) as error:
        errors.append(f"malformed:{type(error).__name__}:{error}")
    return {"gate": "pass" if not errors else "blocked", "reasons": sorted(set(errors)), "scope": "synthetic-predicate-only"}

def fixture() -> tuple[dict[str, Any], dict[str, Any], dict[str, bytes], datetime]:
    now = datetime(2026, 9, 29, 12, 0, tzinfo=timezone.utc)
    identity = dict(zip(IDENTITY, ("synthetic-product", "synthetic-journey", "synthetic-contract-v1", "synthetic-candidate-v1", "synthetic-config-v1", "synthetic-environment-v1", "synthetic-grader", "prototype-v1", "synthetic-run-001")))
    policy = {"identity": identity, "criteria": ["positive-behavior", "negative-control", "recovery"], "max_age_seconds": 3600}
    artifacts = {criterion: json.dumps({"synthetic": True, "criterion": criterion}).encode() for criterion in policy["criteria"]}
    rows = [{**identity, "criterion": criterion, "outcome": "pass", "collector_status": "complete", "executed_cases": 1, "observed_at": "2026-09-29T11:59:00Z", "artifact_id": criterion, "artifact_sha256": hashlib.sha256(artifacts[criterion]).hexdigest()} for criterion in policy["criteria"]]
    return policy, {"worker_attempt": "attempt-A", "results": rows}, artifacts, now

def run() -> dict[str, Any]:
    cases: list[dict[str, Any]] = []
    def check(name: str, mutate: Any, expected: str = "blocked") -> None:
        policy, receipt, artifacts, now = fixture()
        mutate(policy, receipt, artifacts)
        result = evaluate(policy, receipt, artifacts, now)
        cases.append({"case": name, "expected": expected, "actual": result["gate"], "matched": result["gate"] == expected, "reasons": result["reasons"]})
    check("valid_nonempty_identity_bound_fixture", lambda p,r,a: None, "pass")
    check("worker_replacement_preserves_evidence_identity", lambda p,r,a: r.update(worker_attempt="attempt-B"), "pass")
    for key in IDENTITY:
        check(f"wrong_{key}", lambda p,r,a,k=key: r["results"][0].update({k: "different"}))
        check(f"missing_{key}", lambda p,r,a,k=key: r["results"][0].pop(k))
    for outcome in ("fail", "skip", "error", "missing", "green", "", None, {}):
        check(f"not_an_explicit_pass_{outcome!r}", lambda p,r,a,o=outcome: r["results"][1].update(outcome=o))
    for count in (0, -1, True, "1"):
        check(f"invalid_executed_count_{count!r}", lambda p,r,a,c=count: r["results"][0].update(executed_cases=c))
    check("empty_results", lambda p,r,a: r.update(results=[]))
    check("missing_result", lambda p,r,a: r["results"].pop())
    check("duplicate_pass", lambda p,r,a: r["results"].append(copy.deepcopy(r["results"][0])))
    check("conflicting_observation", lambda p,r,a: r["results"].append({**r["results"][0], "outcome": "fail"}))
    check("unknown_criterion", lambda p,r,a: r["results"][0].update(criterion="unaccepted"))
    check("worker_cannot_reduce_external_policy", lambda p,r,a: (r.update(criteria=["positive-behavior"]), r.update(results=r["results"][:1])))
    check("empty_external_policy", lambda p,r,a: p.update(criteria=[]))
    check("duplicate_policy_criterion", lambda p,r,a: p["criteria"].append(p["criteria"][0]))
    check("collector_error", lambda p,r,a: r["results"][0].update(collector_status="error"))
    check("historical_pass", lambda p,r,a: r["results"][0].update(observed_at="2026-09-28T11:00:00Z"))
    check("future_dated_pass", lambda p,r,a: r["results"][0].update(observed_at="2026-09-30T11:00:00Z"))
    check("naive_timestamp", lambda p,r,a: r["results"][0].update(observed_at="2026-09-29T11:00:00"))
    check("invalid_timestamp", lambda p,r,a: r["results"][0].update(observed_at="not-a-time"))
    check("missing_raw_artifact", lambda p,r,a: a.pop("positive-behavior"))
    check("empty_raw_artifact", lambda p,r,a: a.update({"positive-behavior": b""}))
    check("tampered_raw_artifact", lambda p,r,a: a.update({"positive-behavior": b"different bytes"}))
    check("wrong_digest", lambda p,r,a: r["results"][0].update(artifact_sha256="0"*64))
    check("malformed_result", lambda p,r,a: r["results"].__setitem__(0, None))
    result = {"experiment": "gaming-pair-evidence-predicate-v1", "data_kind": "SYNTHETIC", "observed_at": datetime.now(timezone.utc).isoformat(), "python": platform.python_version(), "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), "native_products_executed": [], "independent_review": False, "tested_cases": len(cases), "matched_cases": sum(case["matched"] for case in cases), "cases": cases, "not_established": ["Dino/Civis behavior, native builds or tests", "accepted completeness of either product contract", "trusted issuer authentication or signatures", "policy storage protection or branch protection", "full malformed-input fuzz robustness", "cryptographic anti-forgery", "proof against an authenticated collector lying"]}
    return result

if __name__ == "__main__":
    result = run()
    output = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("experiment-receipt.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: result[key] for key in ("experiment", "tested_cases", "matched_cases", "source_sha256")}, indent=2))
    sys.exit(0 if result["tested_cases"] == result["matched_cases"] else 1)
