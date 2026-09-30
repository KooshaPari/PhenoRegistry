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