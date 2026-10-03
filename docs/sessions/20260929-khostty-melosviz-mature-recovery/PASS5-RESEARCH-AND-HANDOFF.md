# Pass 5 — executable evidence and bounded developer handoff

Observed 2026-09-29. Exactly two products remain in scope. Registry is supporting research, not product #3.

**Both products: READY FOR EXPERIMENTAL IMPLEMENTATION. Neither: READY FOR GENERAL DEV HANDOFF.**

## Frozen subjects and durable product-local evidence

| Product | Source analyzed | Latest pass-5 specification/evidence commit | Draft |
|---|---|---|---|
| Khostty | `a29aa9c6553d9f42aa68e2919116c0f6d53f329d` | `c39856ef3f07d688dd45dc26e8f937bfc0420271` | https://github.com/KooshaPari/Khostty/pull/7 |
| Melosviz | `1aec20a2ba41a01ed557d1c7f63f9a0089f842cf` | `78ad6b0775eb60a429e661bba6a688c1b56592ec` | https://github.com/KooshaPari/Melosviz/pull/297 |

The detailed handoffs are `docs/specs/mature-recovery-20260929/DEVELOPER-HANDOFF.md` in each product. Each names allowed work packages, dependencies, write scopes, commands, forbidden shortcuts, evidence receipts and blockers. Product-local `pass5/EXPERIMENT-RECEIPT.json` separates the measured subjects below. No implementation candidate, merge, release or deployment was nominated.

## 1. Khostty: source evidence falsified an earlier differentiation claim

The earlier fork-delta ledger proposed ABI/type-manifest work as a potentially genuine contribution. Exact Git blobs now establish inheritance:

| File | Frozen Khostty blob | Upstream merge-base blob |
|---|---|---|
| `include/ghostty/vt/types.h` | `059bc5c8fd5cf971eb02611ab1033f906963b42f` | `059bc5c8fd5cf971eb02611ab1033f906963b42f` |
| `src/terminal/c/types.zig` | `4184de8227ec74cbe1d5e4aad5978d206138de2b` | `4184de8227ec74cbe1d5e4aad5978d206138de2b` |

Merge base: `d4c88d8069912b653d707191388ca98e24751f12`. The implementation was read directly through both Khostty and `ghostty-org/ghostty` at that revision. Relevant immutable upstream source: https://github.com/ghostty-org/ghostty/blob/d4c88d8069912b653d707191388ca98e24751f12/src/terminal/c/types.zig . Its opening comment identifies the embedded ABI metadata returned by `ghostty_type_json`.

**Decision consequence:** USE the inherited primitive; do not award fork differentiation for it. Wrapper-specific ownership, error handling and consumer integration still require independent analysis. Khostty's fork-delta ledger was amended rather than leaving the incorrect attribution active.

### Native status strengthened from 'not observed' to a source fact

Two complete files were copied into the sandbox and their Git object IDs verified exactly:
- `src/apprt/windows/App.zig`: `7e677fb91431e6d19f4347f1fd352e3a341d5df9`.
- `src/apprt.zig`: `67dd08c54744b947b0cb236c08ed0c542b3e8076`.

The Windows runtime is selectable, but its App init/registerWindowClass/run bodies return Unimplemented. Exported `apprt.ipc` selects the legacy mod. This is not just missing GUI screenshot evidence. It does not prove a complete call graph or claim that Zig/native execution occurred. `pass5/check_snapshots.py` replays the exact snapshot/hash/static checks and writes a fresh receipt.

## 2. Ghoztty research progressed from an unpinned lead

Pinned comparator: `dzearing/ghoztty@fd3838acfa834c29e99616cdc8500c0208a13a09`.
- README blob `4d1efb4d5fbab5d10428d496dca15f048907c237`, inspected lines 1–230.
- LICENSE blob `0a07a66cd1ad6ea35cc3b8150e2c37702fe5989d`, full read, root MIT.
- README documents named/idempotent `+new-window`, `+split`, `+close`, cwd and command flags, and a Unix-socket approach.

Sources: https://github.com/dzearing/ghoztty/blob/fd3838acfa834c29e99616cdc8500c0208a13a09/README.md and https://github.com/dzearing/ghoztty/blob/fd3838acfa834c29e99616cdc8500c0208a13a09/LICENSE .

These remain documentary claims, not a native bake-off. No complete project-health, dependency-license or runtime assessment is claimed. A successful no-op closing an absent named target can be valid idempotency. Do not force an alternative to mimic every Khostty return code; compare intended effects, stale-instance safety and real workflow outcomes.

## 3. Melosviz: actual isolated function probes executed

Python 3.13.5, Linux x86_64, FFmpeg/FFprobe 7.1.5. The source functions were copied from frozen orchestrator blob `549e70a5741f43546af3d068b5444d54d47affc2`, omitting comments/docstrings. Full source was not downloadable into this sandbox, so evidence explicitly says EXTRACTED_FUNCTION_EXECUTION and full_blob_verified=false.

Observed:
- 64 zero bytes named `.mp4`: helper reports no rejection, independent FFprobe rejects it.
- Nonempty malformed WAV: helper reports no rejection, independent FFprobe rejects it.
- Cache `NEW!`, destination `OLD!`, both four bytes: materialization returns destination while OLD! remains.
- Positive diagnostic controls: zero-byte file rejected; zero-frame WAV rejected; different-size destination replaced.

These are three reproduced function-level defects plus three controls, NOT a passing product suite or a full CLI invocation. `pass5/probe_source.py --repo <checkout>` is ready to hash the complete frozen source, verify executable AST equality and replay those exact functions. This stricter mode is not claimed executed here.

FFprobe documentation inspected: https://ffmpeg.org/ffprobe.html . Its stream/frame inspection and positive exit on unrecognized input support reusing it as a primitive; the tool alone does not authenticate product identity or assess creative quality.

## 4. The media oracle is now code, not another specification

Product-local `pass5/oracle.py` and `selftest_oracle.py` generate actual small three-scene lossless FFV1/PCM media and evaluate independent expected policies. Version `mv-oracle-0.2-experimental` had **28/28 expected selftest outcomes**: two valid R1/R2 cases pass, invalid cases fail, and an unavailable collector blocks.

Controls cover wrong candidate/contract/configuration/revision/run, skipped collection, missing/duplicated/reordered scenes, placeholder/plan-only output, digest mismatch, garbage media, valid wrong scene, wrong final ordering/audio, wrong video presentation time, delayed audio timestamps, path escape, empty/malformed evidence, empty expected denominator and stale R1 against R2.

An active self-review found that decoded audio bytes alone miss a playback-time offset. The verifier was amended to check audio-frame timestamps and sample continuity; an actual delayed-audio file is now rejected. This is useful adversarial self-review, NOT the fresh independent reviewer required by the completion gate.

Code identity: oracle Git blob `ac59f69a6b495a10c1e28a0306305422b94f9371`; selftest blob `abd75d24ecba3383a62e9368dd0771607a6c3a48`. Both were checked against the sandbox-tested bytes after publication.

Limits: no product CLI/GUI/GPU rendering service was executed; the fixture is tiny/lossless rather than a real music-video quality benchmark; R2 tests evidence semantics, not actual application restart/persistence. Receipt identity fields are checked against expected values but are not authenticated. A reviewer-controlled execution witness and separate grader authority remain necessary. No verifier selftest contributes to product completion.

## 5. Source-denominator tooling

`tools/source_inventory.py` uses exact Git commits and a complete NUL-delimited tree listing, preserves removed baseline paths and file modes/object identities, and initializes all six semantic-resolution fields to false. It refuses moving refs and writes outside the candidate checkout with exclusive creation.

Nine synthetic-repository controls passed, including newline filenames, symlinks, added/modified/inherited/removed files and preventing enumeration from becoming semantic resolution. This is an inventory-tool selftest only. Neither complete product tree was inventoried here; conversations/PR history/external standards would remain separate families even after tree enumeration.

## 6. Authority/provenance correction

This pass's memory retrieval returned earlier assistant summaries for the claimed April 18 Melosviz acceptance and September Khostty objective. A second search specifically excluding recovery summaries returned no primary conversation. Prior wording 'direct user acceptance recovered' therefore lacks independently reproduced primary evidence in this pass.

Reclassify those claims as imported historical attributions pending the primary user message. The existing ADR/intent docs still matter, and no inference that the user never accepted them follows. Current user authorization for these two recovery programs and bounded experimental work remains explicit. Do not use a PR section named 'User description' or assistant memory summary as proof of a human product decision without attribution validation.

## 7. Handoff and remaining blockers

Ready independently now: K-E01 source/ownership/caller inventory and M-E01 full-source/probe/mounted-baseline reproduction. They may run in parallel in separate worktrees. Dependent native/embedding K-E02/E03 and Melosviz repair/consumer M-E02/E03 require the return evidence and contract dependencies specified in each handoff.

General developer handoff remains blocked by semantic source closure, original authority/supersession, complete mature contract/journeys/quality/traces, completed SOTA decisions/high-risk experiments, real mounted product evidence and independent review. Existing CI was not modified to enforce catalog quarantine; that remains a separate enforcement task. No new paid services, merges or releases occurred.
