# Known Issues and Evidence Limits

- Benchora artifact is hosted and pinned at [`65ccb502`](https://github.com/KooshaPari/Benchora/blob/65ccb50288e3ddfa0f537aef80c82c1a26553244/audits/ci-exceptions/2026-09-08-pr107-scorecard-repair-plan.md); its earlier local temporary/unpublished status is historical.
- Historical `668ceed` is not current proof: stated snapshot has scorecard `32/88`, Sonar fail, and queued Infisical.
- ResearchLedger #81 `5ada3d8` is published; `fbf2d0d` and active list-support tests are unpublished. No latest completion claim is made.
- The authoritative WBS remains in ResearchLedger; this packet does not replace it.
- The project-owned specification for `researchledger-corpus-audit-routing` exists. Live registration is verified via CLI (2026-09-12T09:02:25Z): CLI specify succeeded with state transition Created -> Specified on the live daemon DB, and CLI list independently confirmed ID3 slug in `specified` state. No blind duplicate enqueue was submitted. The earlier `get_feature` `NOT_FOUND` responses are historical from the supported operation returning not-found before registration; they do not apply to the current CLI-verified registration. MCP read timed out; governance completion and MCP transport remain unverified open gates.
- Historical registry catalog contradictions remain preserved pending separate authorization.
