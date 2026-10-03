# Pass 6 — finite denominators, live experiments, and narrowed architecture gates

Observed 2026-09-30. Exactly two product subjects remain: Khostty and Melosviz. PhenoRegistry is evidence/research index only.

## Handoff state

| Product | Experimental handoff | Ready now | General dev |
|---|---|---|---|
| Khostty | **READY FOR PARALLEL EXPERIMENTAL IMPLEMENTATION** | K-E02 native/control; K-E03 linked embedding/CI | BLOCKED |
| Melosviz | **READY FOR PARALLEL EXPERIMENTAL IMPLEMENTATION** | M-E01 mounted baseline; M-ESEC bridge security | BLOCKED |

M-E02 awaits M-E01 result evidence. M-E03 awaits M-E02 result-contract review. No merge/release is authorized.

## Structural source denominators

Melosviz frozen main: every top-level Git tree recursively enumerated with untruncated API responses. Product-local inventories contain 688 exact blob rows. Tracked-file enumeration is CLOSED; semantic/history/conversation/external-source denominator remains OPEN.

Khostty frozen source: every top-level tree enumerated untruncated. Product-local inventories preserve 2,117 raw A+B rows with 62 overlapping paths and zero object conflicts, yielding 2,055 unique non-fuzz paths. The unchanged test tree has a separate 4,014-blob fuzz family including 4,002 corpus seeds. Those seeds are not 4,002 obligations. Tracked-file enumeration is CLOSED; semantic/history/authority/external denominator remains OPEN.

## Khostty architecture narrowing

Exact merge-base ownership now separates inherited substrate from fork candidates:
- top-level: 43 identical, 13 added, 6 modified, no top-level removed entries;
- macOS, test, include, examples and several packaging/vendor trees are wholly identical;
- Windows runtime is fork-added;
- ten new JSON-agent files are fork-added;
- current public `apprt.ipc` is the upstream 253-line three-action IPC relocated into `ipc/mod.zig`; it becomes textually identical to baseline after import-path normalization;
- selected terminal C/API implementation is inherited;
- the new JSON server/AppHost is not mounted into normal app startup at the frozen source.

`SURVIVING-DIFFERENTIATION-GATE.md` makes Windows, control, wrappers/WASM, conformance, benchmarks and CI/distribution survive or fail independently. Same-family Ghoztty and a substantial external Windows Ghostty fork materially contest both headline feature-existence claims.

Live experimental draft Khostty #8 is candidate-bound to a frozen-base branch and forces a native libghostty-vt build plus Rust integration-test sentinels; its hosted run must be inspected before K-E03 earns evidence.

Khostty main moved two commits after the frozen source, only in PyPI/release-operation files. Those are post-snapshot state, not silently included in the product analysis.

## Melosviz architecture narrowing

Mounted source tracing now establishes a coherent defect cluster:
- orchestrator iterates scenes while ComfyUI/C4D/UE adapters also iterate the full/matching spec, enabling repeated N×N work and identity collapse;
- bridge generate scans flat `out/scene_*` while actual adapter output is nested under scene-type directories; its existing test pre-creates the flat fixture with subprocess mocked;
- Electrobun release desktop can mark every scene done from CLI return; web/bridge can mark real nested output missing;
- selective rerender is non-operative, positional identity bases disagree, job IDs are not durable, cache identity omits render-affecting references;
- events/cache/provenance files are not a durable authoritative product-state ledger;
- direct web StudioConsole has no bearer capability, so authenticated public bridge mode is currently incompatible with that surface, while the release Electrobun proxy does attach bearer headers.

`MOUNTED-SPINE-CONTRACT.md` defines the candidate experimental spine: stable scene revision identity, one iteration owner, typed attempt/artifact/acceptance states, scene-keyed results, accepted ordered assembly subjects, complete cache dependency identity, and durable product truth independent of workers.

`DURABLE-STATE-ALTERNATIVES.md` sets direct SQLite as the architecture-to-beat for the current single-host product, not an accepted decision; M-E03 must compare it against an atomic file journal under the same restart/corruption oracle before selecting storage.

Live experimental drafts:
- Melosviz #301: diagnostic-only M-E01 reproduction of whole-spec repeated dispatch + bridge layout mismatch.
- Melosviz #300: M-ESEC fail-closed non-loopback/public bind and protected Studio/render/debug routes. Review found direct authenticated web incompatibility; do not weaken server policy or put bearer tokens in URLs. M-E03 owns an authenticated web transport or an explicit later scope decision.

## Authority status

Library and memory searches still did not recover the primary original “Programmable Music Visualizers” user transcript or primary Khostty product-decision message. Exact-phrase searches resolve to derived repository documents/assistant-era artifacts. Historical acceptance claims remain imported attributions, not independently reproduced user authority. Current user authorization of this recovery/experimental program is explicit.

## Completion status

No scalar product/spec percentage is issued. Neither product has:
- complete semantic source resolution;
- fully closed SOTA/alternatives architecture;
- a general developer handoff;
- complete mature requirement/journey/quality denominator;
- complete implementation mapping and evidence graph;
- fresh independent completeness attack;
- post-build comparative pilot.

Increasing certainty by falsifying an architecture assumption may make a product look “less complete”; that is expected and preferable to false progress.
