# ResearchLedger corpus audit routing and review repair

Feature slug: `researchledger-corpus-audit-routing`.

This project-owned specification tracks the registry routing packet originally delivered by PR #550 and its forward repair. ResearchLedger retains the authoritative corpus WBS and implementation ownership.

## Requirements

- Route only VERIFIED destinations; preserve unresolved and unlinked evidence distinctions.
- Link the exact hosted ResearchLedger WBS and inventory revisions and the hosted Benchora owner artifact. Temporary/unpublished Benchora observations are historical.
- Verify Infisical access without printing environment values or uploading secret files.
- Preserve the current workflow trigger boundary: credentialed verification runs on explicit dispatch, reusable invocation, or matching main/master pushes, not pull requests.
- Require fresh hosted checks and review for the forward repair; historical checks are not current proof.

## Tracking status

Live feature registration is verified via CLI on 2026-09-12. The supported `specify` call succeeded with state transition Created -> Specified on the verified live daemon DB (2026-09-12T09:02:25Z). A subsequent supported `list` call independently confirmed ID3 slug `researchledger-corpus-audit-routing` in `specified` state. No blind duplicate enqueue was submitted; the CLI actually persisted. The earlier `get_feature` `NOT_FOUND` responses are historical from the supported operation returning not-found before registration; they do not apply to the current CLI-verified registration. MCP read timed out and remains unverified. Governance completion and MCP transport remain unverified open gates.

## Acceptance

- The WBS and inventory links resolve at `8822aa14baef2a964288076645edcc493c338688`.
- Infisical child output contains no fetched environment dump and no secret artifact is uploaded.
- Hosted validation and reviewer acceptance are recorded for the repair commit.
- Live feature registration remains an explicit open gate until read back successfully.
