# Tracera Pass 09 — Effectivity Economics Checkpoint

**Status:** synthetic architecture evidence, not product verification.  
**Experiment:** `TRC-EXP-08-MATRIX-01`

## Matrix

512 ordinary-software configurations across:
- platform;
- browser family/version;
- feature flag;
- API schema;
- DB schema;
- dependency version;
- environment class;
- region.

Six criterion families produced 3,072 criterion×target judgments from 28 evidence seeds.

## Results

| Model | Safe reused judgments | Unknown | Forced rechecks | Unsafe reuse |
|---|---:|---:|---:|---:|
| Exact full configuration | 28 | 0 | 3,044 | 0 |
| Typed applicability | 2,304 | 768 | 768 | 0 |
| Typed + assumed-valid compatibility certificates | 3,072 | 0 | 0 | 0 |

These are synthetic results under constructed compatibility truth. They do **not** mean real software will achieve 100% reuse with certificates.

## Mutation controls

17 malformed evidence cases omitted one criterion-required applicability dimension.

A broken missing-as-wildcard evaluator would admit 3,648 target judgments across those mutants. All 17 controls therefore detect a false-admission path.

### Architecture implication

`UNKNOWN != wildcard` is promoted to a high-value invariant.

A criterion must declare which dimensions matter. Evidence must either:
- bind them;
- explicitly declare them irrelevant; or
- carry an admitted compatibility proof.

Silence is not applicability.

## What remains unresolved

Compatibility certificates are now the major risk:
- who/what can issue them;
- exact operation/criterion scope;
- transitivity;
- revocation;
- versioning;
- dependency changes;
- evidence that justifies the certificate itself.

Candidate-artifact equivalence and criterion-revision compatibility also remain outside this experiment.

## Decision

Keep the restricted typed applicability language for the next architecture iteration. Do not add arbitrary expression syntax yet.

Next falsification should attack certificate authority/scope and candidate equivalence, then move the surviving semantics into the real Rust vertical-slice repository/assessment contract.
