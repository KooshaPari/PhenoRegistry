# Pass 7 — minimum repair contracts

Observed 2026-09-30. Product sources remain frozen; exactly two product programs.

## Melosviz

Source tracing falsifies selective rerender as implemented. The constructor stores `_only_scenes` but no later source reads it. `render(..., only_scenes=...)` also never uses its parameter beyond signature/docstring. CLI generate passes selection into the constructor. Therefore a direct/edit rerender request can still dispatch the whole storyboard.

This joins the prior double-iteration defect: conductor loops scenes and whole-spec adapters loop scenes again. Existing identity does not need reinvention: `scene_index` already flows through events, provenance, cache, direct/partial-rerender APIs, bridge schemas and exports. The immediate repair contract is:
1. one effective validated scene selector;
2. one owner of scene iteration;
3. scene-indexed/ordered results;
4. scene_type only selects adapter;
5. structured results feed bridge/UI/assembly;
6. independent media oracle remains outside candidate authority.

No UUID/global identity system is authorized by this finding.

## Khostty

Wrapper inspection narrows the differentiation thesis. Rust/Go/Python/WASM are fork-owned wrapper surfaces over inherited `libghostty-vt` C semantics. Candidate value is idiomatic ownership/lifetime/error/ABI checking and packaging:
- Rust documents RAII, unsafe confinement, typed lifetime rules and non-Send/Sync handles.
- Go owns opaque handles with Close/finalizer and cgo calls.
- Python uses cffi and compares declarations/enums to the library's inherited type manifest.
- WASM uses the inherited manifest for target-dependent layout/memory helpers.

K-E03 should compare wrapper safety/ergonomics/maintenance against direct upstream C integration, not re-benchmark inherited VT correctness as Khostty value. A successful wrapper could be separable/upstreamable even if the broader fork is rejected.

## Handoff state

Both remain READY FOR EXPERIMENTAL IMPLEMENTATION, NOT GENERAL DEV HANDOFF. Melosviz M-E02 contract is now bounded enough to implement after preserving the baseline failure. Khostty K-E03 is bounded as a Rust-first wrapper experiment; K-E02 still needs a native-capable checkout.
