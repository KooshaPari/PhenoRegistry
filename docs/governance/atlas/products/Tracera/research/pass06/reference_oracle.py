"""Research-only model: identity-bound grading, not the Tracera implementation.

Uses SQLite only to retain synthetic observations across worker/restart boundaries.
No cryptographic verification, sandboxing, network or production integration.
Run: python reference_oracle.py --output reference-results.json
"""
from __future__ import annotations
import argparse
import hashlib
import json
import platform
import sqlite3
import tempfile
from dataclasses import asdict, dataclass, replace
from pathlib import Path


@dataclass(frozen=True)
class Subject:
    product: str = "shop"
    baseline: str = "b1"
    candidate: str = "sha256:build-a"
    configuration: str = "linux-basic-flag-off"
    expectation: str = "criterion-v1"
    evaluation: str = "run-current"


@dataclass(frozen=True)
class Observation:
    event: str
    criterion: str = "persist"
    status: str = "passed"
    subject: Subject = Subject()
    verifier: str = "trusted-native-checker"
    observed_at: int = 95
    worker: str = "agent-a"


BINDINGS = tuple(Subject.__dataclass_fields__)
STATUSES = {"passed", "failed", "unknown", "inconclusive", "stale", "skipped", "error"}


def assess(subject: Subject, required: tuple[str, ...], observations: list[Observation],
           *, now: int = 100, ttl: int = 10, ignore: frozenset[str] = frozenset()) -> dict:
    """Grade one frozen evaluation, not the highest historical attempt score.

    'ignore' enables deliberate broken variants in this experiment only.
    Verifier membership assumes prior trusted admission; it is NOT authentication.
    """
    if not required or len(required) != len(set(required)) or ttl < 0:
        return {"state": "not_assessable", "ratio": None, "criteria": {}}
    if any(not getattr(subject, key) for key in BINDINGS):
        return {"state": "not_assessable", "ratio": None, "criteria": {}}
    states = {}
    for criterion in required:
        relevant = [o for o in observations if o.criterion == criterion
                    and all(key in ignore or getattr(o.subject, key) == getattr(subject, key)
                            for key in BINDINGS)
                    and ("verifier" in ignore or o.verifier == "trusted-native-checker")]
        if not relevant:
            states[criterion] = "unknown"
            continue
        results = {o.status for o in relevant}
        if any(o.observed_at > now for o in relevant) or not results <= STATUSES:
            state = "inconclusive"
        elif all(now - o.observed_at > ttl for o in relevant):
            state = "stale"
        elif "passed" in results and "failed" in results:
            state = "inconclusive"
        elif "failed" in results:
            state = "failed"
        elif results & {"error", "inconclusive"}:
            state = "inconclusive"
        elif results & {"unknown", "skipped"}:
            state = "unknown"
        elif "stale" in results or any(now - o.observed_at > ttl for o in relevant):
            state = "stale"
        else:
            state = "verified"
        states[criterion] = state
    values = set(states.values())
    order = ("failed", "inconclusive", "stale", "unknown", "verified")
    state = next(s for s in order if s in values)
    return {"state": state, "ratio": sum(v == "verified" for v in states.values()) / len(required),
            "criteria": states}


def open_store(path: Path) -> sqlite3.Connection:
    db = sqlite3.connect(path)
    db.executescript("""
    CREATE TABLE IF NOT EXISTS observations(event TEXT PRIMARY KEY, body TEXT NOT NULL);
    CREATE TRIGGER IF NOT EXISTS no_update BEFORE UPDATE ON observations
    BEGIN SELECT RAISE(ABORT, 'append-only'); END;
    CREATE TRIGGER IF NOT EXISTS no_delete BEFORE DELETE ON observations
    BEGIN SELECT RAISE(ABORT, 'append-only'); END;
    CREATE TABLE IF NOT EXISTS work(id TEXT PRIMARY KEY, status TEXT NOT NULL);
    """)
    return db


def append(db: sqlite3.Connection, observation: Observation) -> None:
    body = json.dumps(asdict(observation), sort_keys=True, separators=(",", ":"))
    old = db.execute("SELECT body FROM observations WHERE event=?", (observation.event,)).fetchone()
    if old:
        if old[0] != body:
            raise ValueError("conflicting replay")
        return
    db.execute("INSERT INTO observations VALUES (?, ?)", (observation.event, body))


def load(db: sqlite3.Connection) -> list[Observation]:
    result = []
    for (body,) in db.execute("SELECT body FROM observations ORDER BY event"):
        fields = json.loads(body)
        fields["subject"] = Subject(**fields["subject"])
        result.append(Observation(**fields))
    return result


def run() -> dict:
    results = []
    def check(name: str, actual, expected) -> None:
        results.append({"name": name, "actual": actual, "expected": expected, "pass": actual == expected})
    s = Subject()
    good = Observation("e-good")
    check("missing proof", assess(s, ("persist",), [])["state"], "unknown")
    check("exact qualifying proof", assess(s, ("persist",), [good])["state"], "verified")
    for field in BINDINGS:
        wrong = replace(good, subject=replace(s, **{field: "other"}))
        check("reject wrong " + field, assess(s, ("persist",), [wrong])["state"], "unknown")
    check("missing configuration is not wildcard", assess(s, ("persist",), [replace(good, subject=replace(s, configuration=""))])["state"], "unknown")
    check("untrusted producer", assess(s, ("persist",), [replace(good, verifier="worker-claimed")])["state"], "unknown")
    for status, expected in (("unknown", "unknown"), ("stale", "stale"), ("skipped", "unknown"),
                             ("error", "inconclusive"), ("failed", "failed")):
        check("explicit " + status, assess(s, ("persist",), [replace(good, status=status)])["state"], expected)
    check("old evidence", assess(s, ("persist",), [replace(good, observed_at=50)])["state"], "stale")
    check("future timestamp", assess(s, ("persist",), [replace(good, observed_at=101)])["state"], "inconclusive")
    check("conflicting current results", assess(s, ("persist",), [good, replace(good, event="e-fail", status="failed")])["state"], "inconclusive")
    old = replace(good, subject=replace(s, evaluation="run-old"))
    check("collector error cannot reuse old green", assess(s, ("persist",), [old, replace(good, status="error")])["state"], "inconclusive")
    check("empty denominator", assess(s, (), [good])["ratio"], None)
    check("duplicate denominator", assess(s, ("persist", "persist"), [good])["state"], "not_assessable")
    check("missing mandatory criterion", assess(s, ("persist", "recover"), [good]),
          {"state": "unknown", "ratio": 0.5, "criteria": {"persist": "verified", "recover": "unknown"}})
    check("worker substitution", assess(s, ("persist",), [replace(good, worker="human-b")]), assess(s, ("persist",), [good]))
    mutants = []
    for field in (*BINDINGS, "verifier"):
        wrong = replace(good, verifier="worker-claimed") if field == "verifier" else replace(good, subject=replace(s, **{field: "other"}))
        bad = assess(s, ("persist",), [wrong], ignore=frozenset({field}))
        mutants.append({"removed_guard": field, "bad_state": bad["state"], "detected": bad["state"] != "unknown"})
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "proof.sqlite"
        db = open_store(path)
        db.execute("INSERT INTO work VALUES ('wp-1','done')")
        check("work done grants no proof", assess(s, ("persist",), load(db))["state"], "unknown")
        append(db, good); append(db, good)
        check("idempotent replay", db.execute("SELECT COUNT(*) FROM observations").fetchone()[0], 1)
        conflict = False
        try:
            append(db, replace(good, status="failed"))
        except ValueError:
            conflict = True
        check("conflicting replay rejected", conflict, True)
        protected = False
        try:
            db.execute("UPDATE observations SET body='{}'")
        except sqlite3.IntegrityError:
            protected = True
        check("retained proof append-only", protected, True)
        db.commit(); db.close()
        db = open_store(path)
        check("proof survives restart", assess(s, ("persist",), load(db))["state"], "verified")
        db.execute("DELETE FROM work"); db.commit()
        check("proof independent of work retention", assess(s, ("persist",), load(db))["state"], "verified")
        db.execute("BEGIN")
        append(db, replace(good, event="rolled-back", status="failed"))
        db.rollback()
        check("rollback leaves no partial observation", [o.event for o in load(db)], ["e-good"])
        db.close()
    ok = all(r["pass"] for r in results) and all(m["detected"] for m in mutants)
    return {"experiment": "TRC-EXP-EVIDENCE-BINDING-01", "scope": "synthetic_reference_model_only",
            "product_test_generation": "deferred", "product_verified": False,
            "python": platform.python_version(), "sqlite": sqlite3.sqlite_version,
            "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "checks": results, "mutation_controls": mutants, "success": ok,
            "limitations": ["Not Tracera Rust/runtime proof", "No cryptographic verifier authentication",
                            "No cross-engine, load, concurrency or migration benchmark",
                            "Exact configuration match only; safe evidence reuse/subsumption unresolved",
                            "Conservative precedence is experimental, not an accepted final oracle"]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = run()
    text = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    print(json.dumps({"success": report["success"], "checks": len(report["checks"]),
                      "mutation_controls": len(report["mutation_controls"]), "product_verified": False}))
    raise SystemExit(0 if report["success"] else 1)
