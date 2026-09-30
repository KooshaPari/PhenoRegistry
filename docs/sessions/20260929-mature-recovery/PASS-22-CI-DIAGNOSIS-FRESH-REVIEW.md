# Pass 22 — CI diagnosis + fresh-review-style contract attack

Date 2026-09-30.

## CI blockers are now differentiated

### PhenoLab
Historical owner-handoff evidence already conclusively identifies an **account-level GitHub Actions billing/spending restriction**. Jobs are rejected before starting; zero-step failures are queue/billing failures, not test failures. Repository changes cannot clear this.

The same handoff records substitute local evidence on prior revisions, but it is not environment-equivalent to hosted CI and does not cover current recovery heads.

Therefore hosted native evidence remains externally blocked until account billing is resolved. Stop treating repeated Actions reruns as useful work.

### Portage
Different failure class: jobs actually start and reach `Install dependencies`, then fail. Workflow installs `uv sync --all-packages --all-extras --locked` before any test, while the root project defines a huge all/cloud/provider/ML optional dependency surface.

This is a CI architecture reliability risk even without the exact dependency error log. Recovery tests are dependency-light but held hostage by universal all-extras installation.

Analysis receipt: Portage `e56dab590a645ba33011e2b15588de85e9bcc5f1`.

No production workflow mutation was made because exact failing package/log is unavailable and CI policy is separate from architecture semantics.

## Fresh-review-style attack

A reviewer stance assuming the contracts wrong was applied after all prior prototypes.

### Portage
No foundational new identity. Clarification: actual credential/account binding belongs to Attempt/Environment evidence, not only public subject config, because credentials may rotate between retries.

Review `b1f383ff4928261e097e69d3f1bc9929038b5b1d`; delta `0c1a302abef820958db3e53a7ade64b258e77b46`.

### PhenoMLX
No foundational rewrite. New valid case: engine auto-tuning/effective runtime config may change after launch without requested config changing. Acceptance evidence must bind effective config via RealizedProfile/RuntimeGeneration or RuntimeObservationEpoch fingerprint.

Review `e51f09f726f0ea96d1f60e9dc0fdc49496d1f4d5`; delta `cd08c4ab495c5990a00f26005e3ba29e5dcbc33e`.

### PhenoLab
No foundational rewrite. Hardening:
- AcceptancePolicy identity includes grader implementation/version/code digest, not thresholds alone.
- concurrent/conflicting Decisions need append-only supersession/resolution.
- target application state is separate from Decision/PromotionRecord; target rejection does not rewrite experimental truth.
- separation-of-duties may be required by risk class.

Review `624e9b33b500ea92ece1aa2bcacb8fb0b962b302`; delta `24efe9a9fc0f1298d2908f999ae0847470d41167`.

## Baseline outlook

Semantic instability is now low: repeated attacks yield hardening clarifications rather than new product identities.

Still, this is **not the final independent/fresh completion review** because it is performed by the same ongoing program and native vertical evidence remains missing.

Next work can now:
1. consolidate the current contract + deltas into a clean candidate baseline document per repo;
2. expand semantic decomposition/quality overlays from that stable spine while marking baseline as provisional;
3. prepare implementation-ready vertical-slice packages, but gate production handoff on the native architecture experiments where required;
4. close source-coverage ledgers further and quantify coverage only by resolved rows, not product completion.
