# Pass 36 — infrastructure isolation

Date 2026-09-30. Exactly Dino + Civis.

Dino host-independent candidate remains frozen green at candidate50d677b8b1074a4b27f12374cd9b252b14d9b83f run36717763618; no further mutation in this pass.

Civis repaired bridge candidate8a7747f71d496ac6cbb5ed45f5908ca519da4e82 run36738029757 progressed beyond the previous SaveBundleError type failures, then failed while linking unrelated engine integration test gameplay_loop_depth. Runner reported 0 MB free disk and ld terminated with signal7 Bus error. Artifact11109845632 sha256 afd1c6daad4a2e68df89652d5a3d5cda94ae9223d94c55bd22a58e87659903ac contains receipt only. Classification: CI resource/build-scope failure, zero semantic credit.

Semantic candidate tests are crate-lib test modules, so experiment workflow is narrowed to `cargo test -p civ-engine --lib semantic_` for compile and execution. This avoids linking the unrelated full integration-test fleet and improves evidence subject precision. Candidate head adf8bf29e160d8e1e9e65de658e567da272391d0 pending fresh run.

No third product.
