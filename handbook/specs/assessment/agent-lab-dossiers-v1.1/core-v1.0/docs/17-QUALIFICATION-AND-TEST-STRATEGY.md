# Qualification and test strategy

## Executed in this handoff

The local Python test suite exercises reference record parsing, schema subsets, binding integrity, digest mismatch, result freshness, effective-result conflicts, supersession cycles, scope weights, unresolved applicability, critical gates, placeholder rejection, bounded metadata inspection and no-overwrite initialization. The exact results and environment are in `qualification/VALIDATION-REPORT.md` and its machine-readable companion.

The toy loop executes an intentionally incorrect restoration function that returns success without restoring data, and a valid function that restores intact data and rejects a corrupted backup. It records actual synthetic observations. The former fails and the latter passes two bounded predicates. This is not an agent-driven real-repository repair.

## Qualification levels

Schema-valid is not semantically correct. Digest-matching is not authenticated. An accepted qualification record is not proof the tests ran unless a trusted collector establishes that fact. A local test suite is not a deployment, cross-platform certification, exhaustive security audit or validation of user benefit.

## Required real adapters

For each activated product method, provide actual valid and invalid fixtures, limits, ownership, permissions, command/action capture, observation parsing, assertion semantics and the claim it can support. Include runner errors, timeouts, skipped tests, truncated output, wrong artifacts, stale caches and expected permission denials. Add traceable contract tests for adapters rather than changing the core status model to suit one vendor.

## Independent paths

Where the risk warrants it, store protected fixtures and raw evidence outside builder write authority. Check actual external effects through a separate path. Merely using another prompt or model is not sufficient. An evaluator that always fails also fails qualification; false-negative controls matter.

## Release checks

Validate schema syntax using the shipped bounded checker and, when available, an independent Draft 2020-12 validator. Validate all generated templates and profiles. Check exact catalog counts and duplicate IDs. Test code, inspect package links, verify source provenance descriptions, build and extract the ZIP, verify every file against its manifest, and rerun tests from the extracted copy. Record unsupported or untested claims as limits rather than green checks.
