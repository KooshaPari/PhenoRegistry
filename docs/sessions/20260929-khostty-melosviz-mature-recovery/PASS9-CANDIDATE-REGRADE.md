# Pass 9 — experimental candidate execution and adversarial re-grade

Observed 2026-09-30. Exactly two products.

## Melosviz M-E02

Experimental branch PR #302 is a substantial implementation candidate, not part of the canonical spec branch. Independent recovery review treated it as untrusted and inspected exact push workflows.

Run history exposed real defects in the experiment itself:
- run 37 failed the R2 selector test;
- source review showed the candidate selector code was present, and the failure was traced to literal escaped-newline text inside the test patch, which commented out the intended R2 mutation and call reset;
- after repairing the test corruption, run 43 passed the focused contract and mounted CLI+bridge FFmpeg journey but failed one broader historical test that still hard-coded clip.mp4 after its fixture was deliberately converted to a real decodable WAV;
- after aligning that assertion to the real fixture, **run 45 on exact candidate df72dcd80ecd39d17f4fa6e8733e00574226f360 succeeded across backend contract, mounted CLI/bridge FFmpeg, broader conductor/bridge regressions, web behavioral/build, and Electrobun webview bundle.**

This establishes a deterministic video_export vertical spine on the tested Linux/FFmpeg configuration: two same-backend scenes, distinct scene-indexed artifacts, real decodable media, final assembly, structured bridge results, selective R2 rerender with complete-timeline reconstruction, and produced-vs-accepted UI language.

It does NOT close M-E02 globally. Recovery-controller held-out review found SceneCacheKey does not require renderer/model/workflow/custom-node/tool version identity; generative partial-rerender can therefore reuse stale media after backend configuration changes unless optional cache_extra happens to encode it. This directly fails a pass-8 held-out negative control. External reviewer-controlled product-media grading, real generative backend execution, creative/beat quality and real application persistence restart also remain open.

Disposition: **DETERMINISTIC VERTICAL SPINE EXPERIMENTALLY DEMONSTRATED; FULL M-E02 BLOCKED.**

## Khostty K-E03

Experimental PR #9 is also untrusted until exact native evidence passes.

Run 17 at 1edff1a... built an exact candidate native library and recorded SHA-256 e76a6b74b498b29c6c8c6f8cbbbbb9e5cbf59de8e34d0af0b2d8f4889aa717d8. Direct C create/write/resize/render/search/snapshot-restore executed successfully; ABI/FFI tests passed; missing-library fail-closed and Rust lifetime misuse controls passed. Rust wrapper execution failed only at runtime loader resolution: it requested libghostty-vt.so.0 while the workflow had supplied a static .a. Because that critical check failed, upstream comparison was skipped and verdict remained FAIL_EXPERIMENT.

Recovery controller changed only experiment infrastructure: Linux comparison now supplies the emitted shared object, candidate/upstream harness steps preserve both receipts even if one side fails, and a final step requires both receipts PASS. New exact push run 19 at 1860db9... is executing. No wrapper/product acceptance is awarded while it is incomplete.

Disposition: **USEFUL PARTIAL NATIVE EVIDENCE; K-E03 STILL BLOCKED ON TWO-ARTIFACT COMPARISON.**

## Handoff

Melosviz can now hand a developer agent the generative backend cache/evidence-identity subproblem without reopening scene identity/assembly/UI fundamentals. Khostty K-E03 remains an active experiment; K-E02 native agent-server mounting remains separate.

Neither repository is READY FOR GENERAL DEV HANDOFF.
