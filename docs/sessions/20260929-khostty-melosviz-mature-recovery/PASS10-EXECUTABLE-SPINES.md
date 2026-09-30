# Pass 10 — executable vertical spine and wrapper/native evidence

Observed 2026-09-30. Exactly two products.

## Melosviz

Experimental PR #302 reached its first clean exact-head implementation run. Workflow run 45 (36751162085) at df72dcd80ecd39d17f4fa6e8733e00574226f360 passed:
- focused M-E02 scene/selector/result/cache/assembly contract;
- mounted real CLI + bridge FFmpeg journey;
- broader conductor/bridge regression suite;
- web StudioConsole behavioral tests + bundle;
- Electrobun Director Console webview bundle.

The experiment failure sequence was itself audited rather than erased: an escaped-newline test-patch corruption first hid the intended R2 mutation/reset; after repair, a historical provenance assertion still required clip.mp4 although its fixture now emitted a real WAV. Both were corrected without weakening the semantic contract.

This proves the deterministic video_export vertical spine on the tested Linux/FFmpeg environment. It is not full M-E02 acceptance.

### Held-out generative evidence blocker

SceneCacheKey does not mandate backend execution configuration. ComfyUI adapter already obtains a prompt_id and completed /history/{prompt_id} entry, but returns only downloaded file paths. That discards the backend execution identity before provenance/cache/result construction. Official ComfyUI server API also exposes prompt/history, model lists/metadata, object info, workflow templates, features and system stats.

Next generative cache/evidence contract: preserve prompt_id + canonical submitted-workflow hash + output descriptors + adapter revision + deployment/model/custom-node identity. Backend history is execution evidence, not independent acceptance. Until that is implemented and adversarially tested, generative cache reuse remains blocked.

## Khostty

K-E03 run 19 advanced beyond setup and built both candidate/upstream native artifacts, but comparison gate still failed for two experiment-infrastructure/product-packaging reasons:
- candidate Rust downstream binary still could not locate libghostty-vt.so.0 even when the exact shared library was supplied; direct C with explicit rpath executed. This demonstrates the wrapper crate's build-script rpath is not sufficient for downstream runtime deployment.
- upstream harness invocation used a library-origin token outside the harness's declared enum, so no upstream JSON receipt was produced.

The harness now explicitly configures the platform loader path for the execution witness and records that runtime loader configuration is required. Workflow now uses the declared upstream-ghostty origin. New exact run 23 at aeede977... is active. This does not erase the packaging burden; a pass would establish API execution under explicit deployment configuration, not self-contained distribution.

### K-E02 threading gate

Source review blocks a naive server mount. AppHost says connection handlers run off the app thread and its mutex does not protect app-thread concurrency. Surface.queueIo is an existing IO-thread route but private. K-E02 is therefore phased: app-thread/mailbox bridge first, server lifecycle second, native adversarial journey third. Direct Server.bind with cross-thread raw app access is an automatic fail.

## Handoff state

- Melosviz deterministic M-E02 spine: experimentally demonstrated; generative evidence/cache identity subproblem READY FOR EXPERIMENTAL DEV HANDOFF.
- Khostty K-E02a app-thread bridge: READY FOR EXPERIMENTAL DEV HANDOFF.
- Khostty K-E03: active exact comparison experiment, not accepted.
- Neither repository: READY FOR GENERAL DEV HANDOFF.
