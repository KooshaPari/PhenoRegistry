# Executed validation and its limits

**v1.4 / September 16, 2026.** These results validate the documentation/reference artifacts. They do not certify a native application, game, bridge, installed product, real UI mockup, product grade or human approval.

## Completed runs

The complete inherited-plus-new suite passed **393 tests**. This includes 238 inherited reference tests and 155 new tests: 146 numerical-grader tests and 9 amendment-contract tests. The final unified run completed in 48.120 seconds. The count refers to discovered test methods, not 393 independent product behaviors.

| Grader suite | Methods | Lines | Branches |
|---|---:|---:|---:|
| unit | 53 | 87.71% (157/179) | 89.13% (82/92) |
| integration | 49 | 87.71% (157/179) | 90.22% (83/92) |
| e2e | 44 | 93.85% (168/179) | 88.04% (81/92) |

The measurement target is **only `proof/grade.py`**. No source lines are excluded. Unit tests isolate acquisition; integration tests use real temporary receipt/payload files; E2E tests launch the actual grading CLI as a child process. E2E child coverage files are combined only within that E2E suite, never with unit or integration. Synthetic fixtures are labelled. Thresholds do not certify semantic quality or real producer behavior.

Negative cases include missing evidence, wrong source/artifact/profile, stale/future receipts, invalid counts, altered or missing payloads, absent real-user action routes, missing required modality, synthetic/live mismatch, model-only critical qualification, duplicate outcomes and high-score/failed-critical cases. JSON parsing and path/digest cases exercise additional failure boundaries.

## Reproduce reference checks

From the `docs/` directory with the existing validation dependencies installed in an isolated environment:

```bash
python scripts/validate_package.py .
python -m unittest discover -s tests -v
python proof/grade.py proof/examples/grade/rubric.json \
  proof/examples/grade/index.json \
  --root proof/examples/grade
```

The last command intentionally returns **exit 1** with the synthetic result `84.11% / C - BLOCKED`. That is the expected example, not a broken validator and not a real repository grade. CLI exit 0 never grants release authority.

For independent instrumentation use `coverage run --branch --source=proof -m unittest discover -s tests -p test_grade_unit.py` and the equivalent integration pattern with separate `COVERAGE_FILE` values. E2E sets `PROOF_CLI_COVERAGE=1` so actual child commands run under parallel-mode coverage; combine only their matching suite prefix before reporting `proof/grade.py`. Native JSON reports and logs are in [validation/](validation/).

## PDF and package

The 19-page additive PDF was rendered and visually inspected. The original v1.3 archive is preserved unchanged and bound by checksum. Final packaging checks validate relative file links, IDs, JSON/schema examples, traceability, work DAGs, archive integrity and exact delta reconstruction. Those final records accompany the archive; they are not a universal secret scanner, external-URL validator, image oracle or native test report.

## Trust boundary

The scorer checks supplied record structure, arithmetic, identity/freshness and local payload digests. It does not verify signatures, authenticate the producer/approver, inspect actual pixels, execute a native product, discover every requirement, or establish qualitative truth. Fabricated but self-consistent input can still be false. Integrate trusted native adapters and independent calibrated oracles before accepting production scores. The file reader assumes trusted quiescent inputs and is not a hostile concurrent-filesystem sandbox.

Do not copy reference coverage numbers into any product scorecard. No user research, model calibration study, new product screenshots, deployed bridge, agent-session state or lifecycle transition was performed.
