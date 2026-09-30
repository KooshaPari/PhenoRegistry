# Pass 24 — both implementation candidates isolated

Date 2026-09-30. Exactly Dino + Civis.

## Dino

Draft implementation candidate PR491: https://github.com/KooshaPari/Dino/pull/491
- base: spec/mature-recovery-20260929
- branch: experiment/generation-store-20260930
- current head52903db408d257c8d4864094265a95fe2720f959
- production-shaped Runtime.Generation.GenerationStore plus four isolated integration-candidate tests
- no ModPlatform/live-consumer wiring yet
- experiment workflow now includes pull_request trigger against spec branch because push-only runs were not visible through the PR-filtered run evidence API; no execution receipt yet.

## Civis

Exact expanded spec candidate d990d704e4850ef2760fcf3faa12af512586944a qualified in run36711269740:20 tests =11 prototype/guard greens vs9 unchanged production reds. Artifact11094234183 sha256 bba6a17e1f4c41774d79d93ffde1fc6d914a578c81686f7a2f1dd2bbcc2e3426. This run includes tutorial/religious-profile/active-caravan state in the semantic manifest prototype.

Draft implementation candidate PR1569: https://github.com/KooshaPari/Civis/pull/1569
- base: spec/mature-recovery-20260929
- branch: experiment/semantic-save-manifest-20260930
- production-shaped semantic_state_manifest module and isolated tests
- does NOT wire CivSaveBundle or migrate format
- dedicated experiment workflow run36712033274 queued at receipt.

This is the first point where both products have separate spec truth and bounded implementation candidates. Neither candidate is merge-ready or product-accepted.
