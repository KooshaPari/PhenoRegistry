# Execution receipt 2 — implementation candidates and archaeology correction

Date: 2026-09-29. Program: HARNESS-MATURE-20260929. Status: OPEN.

## Separate implementation candidates

HeliosLite draft PR #322 is an implementation candidate based on source `536a25cac1dc21ac97bbc86c7e9af74bd5932780`. Current observed head: `57c1762cd003bba2609b196f682ed89ac5b4484a`. It changes benchmark acceptance semantics and adds adversarial tests; it is deliberately not on the specification branch.

KCode draft PR #14 is an implementation candidate based on source `046ea2af5e01e84449f65d086510b51152360215`. Current observed head: `ad7700ea3c1b93f668bfb28c48da58d2112ba6f3`. It extends the existing Ping/Pong protocol with backward-compatible responder identity: runtime version, git hash, PID and SHA-256 of the actual daemon executable. It preserves the existing bool ping API via a richer `ping_identity` call and adds a native server test. This is runtime artifact identity, not cryptographic attestation of trustworthiness.

KCode issue #13 now legitimately tracks the program and PRs #12/#14 reference it. The prior governance failure was not bypassed.

## HeliosLite baseline evidence

Platform Tests on implementation head `57c1762...` failed on unrelated existing surfaces:
- macOS: `forge_lsp` watcher reload/debounce tests failed; generated CI formatting drift also reported.
- Windows: `forge_ci` release-tag test failed; generated CI formatting drift also reported.
Large preceding Rust test cohorts were green. These logs do not implicate the new benchmark oracle code, but a failing platform workflow remains a failing workflow and is not relabeled green.

The dedicated Harness Recovery Eval Oracle workflow remains the required source-bound verdict for H-F001..H-F004 at the time of this receipt. Do not close those findings merely because unrelated cohorts passed.

## Source denominator

Complete recursive Git trees were fetched without truncation:
- HeliosLite frozen source: 1,895 entries / 1,512 blobs.
- KCode frozen source: 2,539 entries / 2,142 blobs.

Repository-local SOURCE-INVENTORY.json files preserve family counts. Counts are path inventory only, not semantic-resolution percentages.

## Archaeology correction

Evidence falsified the assumption that KCode's only material line was frozen master. Remote branch `fix/tui-focus-paste-panic-master` is 2,111 commits ahead and 136 behind frozen master. However its manifest/README identify an upstream-style jcode 0.88.0 line; current inspected upstream is 0.89.2, while fork master is 0.85.1-k1.1.1. Therefore the branch is classified as a material upstream-sync/fix lineage, not automatically the accepted KCode successor.

The correct existence comparison is now stronger: current upstream + retained fork-specific obligations versus frozen fork master/current implementation, rather than a strawman old upstream.

HeliosLite also has material preservation/journey/release-provenance/packaging branches. These must be mined for unique obligations but not resurrected wholesale.

## Research update

SOTA pass 3 records MCP Tasks 2026-07-28, durable workflow prior art, OPA policy bundle/decision receipt patterns, and SLSA provenance. Architecture consequence: keep worker transport/session state separate from durable effort and accepted product evidence; integrate existing provenance/policy/task concepts where justified rather than growing either CLI into a generic workflow platform.

No product existence, architecture freeze, merge or 100% gate is awarded by this receipt.
