# Pass 38 — semantic execution-scope correction

Date 2026-09-30. Exactly Dino + Civis.

Dino remains frozen/ready for game-host developer handoff; no mutation.

Civis run36744041195 candidate adf8bf29e160d8e1e9e65de658e567da272391d0 compiled the lib-only semantic candidate successfully, but execution still invoked `cargo test -p civ-engine semantic_manifest_candidate_` without `--lib`. Cargo therefore linked unrelated integration tests, runner reached0MB disk and rust-lld bus-errored on fr_fr_civ_rts_004. Artifact11112177720 sha256 e1d16d183b0b90293644e8cd9a66d985d48e7d7560e5b94f6618f6f6966093c7 includes receipt/log. Classification: workflow execution-scope defect + runner exhaustion; semantic assertions remain unclassified.

Workflow corrected at88b350f45202e6473b655baad76bbd0691d8a1ab so both compile and execution use `cargo test -p civ-engine --lib semantic_`. This also executes the adapter/generation/reconciliation tests added after the original manifest-only filter, rather than silently excluding them.

Civis developer handoff remains conditional until this exact scope executes green or yields a semantic red.
