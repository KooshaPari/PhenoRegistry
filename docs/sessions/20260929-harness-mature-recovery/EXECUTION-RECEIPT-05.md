# Execution receipt 5 — exact candidate qualification and false-green rejection

Date: 2026-09-30. Program remains OPEN.

## HeliosLite #322
Exact candidate `8451b952ef26f0720ee5e87d25eda6da1bc38700` has successful Harness Recovery Eval Oracle run 36627763151. Job 109609022604 reports 8 tests, 8 pass, 0 fail. Exact-head Platform Tests, CVP, Cargo Deny, Trufflehog, Trunk Check, CodeQL, Performance Benchmarks and all listed CI workflows also completed successfully.

H-F001 through H-F004 are now RESOLVED FOR THIS CANDIDATE. Historical source findings remain part of the audit trail. This does not close overall specification/design or product maturity.

## KCode #14
Workflow run 36627882343 completed success, and cargo check compiled the touched crates. However its intended targeted cargo test executed `running 0 tests` with 1,257 filtered out because the selector combined a partial name with `--exact`. The apparent green was therefore rejected as behavior evidence.

Candidate head `5a15dd86a685e60f03de64806c913ea544549793` removes the mismatched exact selector and makes the workflow fail if zero tests execute or if the named daemon identity test does not report ok. Corrected run 36673339535 is in progress at receipt time.

This is a concrete MACE negative-control success: a skipped/empty effective check did not receive product credit even though the workflow itself was green.

## Gate consequence
HeliosLite high-risk oracle experiment is partially closed on an exact candidate; KCode daemon identity remains compile-qualified but behavior-unqualified pending the corrected nonzero test. Source, existence, journey, full trace and independent-review gates remain open for both.
## Follow-up correction on KCode targeted evidence
Corrected run 36673339535 reached a clean cargo check but the targeted test command exited 101. Its workflow used command substitution under `set -e`, so the captured test output was lost before printing. Candidate `54b0e012734428e84479a25c2e5b2d4ed27dc754` changes the evidence harness to retain output and exit status before adjudication. A fresh run is in progress. The failed run remains a failure; no behavioral credit is awarded.

## Existence-gate narrowing
Further current-upstream source inspection falsified additional broad KCode differentiation: upstream has substantial server version/git identity and stale client/server handling, provider/subscription/account breadth, and first-class native Windows x64/ARM64 support. The Windows/Pine question is now specifically POSIX-oriented native workflow semantics without making PowerShell/CMD/WSL the normal substrate, not generic Windows support.
