# Pilot repair and negative-test guide

**Disposition: preserve the recovered pilot as historical evidence; repair only in the current canonical owner under separately authorized scope.** No file under `evidence/session/` is an install script.

## Repair sequence

| Order | Repair | Required evidence before closure |
|---|---|---|
| 1 | Resolve current shared workflow owner and caller revision | Immutable repository/ref, relevant consumers, owner/ADR; do not infer repository absence from one 404 |
| 2 | Put a reusable workflow at a supported path and declare its interface | Platform-semantic validation and actual disposable caller resolution, not YAML parse alone |
| 3 | Repair CI context identity and dependency coverage | Actual observed check contexts/trusted producer IDs for the exact candidate; full required result matrix |
| 4 | Implement the local-dev delivery profile and exact trigger | One-commit deferral, two-commit eligibility, scheduled single-commit eligibility, safe offline/lease behavior |
| 5 | Separate source build/test from privileged apply | Build credentials cannot deploy; candidate cannot rewrite the verifier/approval policy; spoofing fixtures rejected |
| 6 | Bind tested artifact to target source mode | Immutable binary/image identity observed after deployment; no `:latest` or mismatched `commitId` shortcut |
| 7 | Make health and provider observation fail closed | Missing URL, stale status, wrong candidate, wrong route and unknown response shape do not pass |
| 8 | Implement recovery and data compatibility | Prior healthy candidate, approved recovery action, restored application/data invariants and independent receipt |
| 9 | Import receipts and update readiness | File/commit/platform/runtime/data/acceptance states separately recorded; no report-count-based completion |

## Historical regression fixtures

The extracted evidence intentionally retains defects. A test that confirms a fixture contains an invalid nested path is a **test of the audit fixture**, not a repaired deployment. Do not modify the fixture until it passes; create a new corrected implementation and compare the two.

| Fixture | Negative case to preserve | Test objective |
|---|---|---|
| E007/E009 | Nested reusable workflow path | Reject a platform-invalid reference despite syntactically valid YAML |
| E008/current CI declarations | `ci/lint` versus `ci / lint` | No silent context normalization or substitution |
| E009/E010 | Source checkout tested, image tag used, deploy sent `commitId` | Require source-mode-specific immutable provenance |
| E009 | Live-equals-HEAD as the only predicate | Demonstrate that one-commit push is not the requested `>1` threshold |
| E009 | Missing health base URL exits zero | Unknown observation must fail closed |
| E007/E010 | `/health` and `/healthz` disagreement | Resolve one profile-defined contract; do not guess either works |
| E007/E009 | Service ID not explicitly forwarded | Validate inputs and actual environment secret availability without revealing values |
| E009 | Build/test command receives provider-credential environment | Enforce privilege separation or explicitly documented fully trusted code path |
| E009 | Nonzero failure exit with no recovery action | A failed workflow is not a rollback receipt |
| E010 | Scratch database and static auth defaults | Refuse durable-fallback qualification without actual durable data/auth binding |
| E011/E016 | Untracked/modified file versus production-ready summary | Distinguish persistence/commit/execution/observation/acceptance |

## What the included tests do

The pure scheduling tests exercise a proposed predicate and its malformed/unknown/offline cases. The snapshot tests verify a handful of literal audit observations and source hashes. Contract tests verify the proposed OpenAPI’s structural references, mandatory precondition headers and absence of client self-approval fields. They do not emulate GitHub’s complete workflow compiler, execute Render deployments, prove token isolation, or recover a database.

The 34 operational tests in [the acceptance catalog](11-acceptance-tests.md) still require the actual host/provider/runtime under an authorized disposable profile. Keep those statuses `not_run` until execution receipts exist.

## Provider qualification must use response fixtures

Capture redacted actual service, active-deployment, list-page, create-deploy, status and recovery responses for the selected API version. Include empty, paginated, unauthorized, rate-limited, failed, unknown and schema-changed cases. Validate parsing with those fixtures and follow pagination where the endpoint requires it. A fixed `limit=20` does not prove the active record was found. Conversely, an unobserved alternate response structure should not be asserted as a confirmed production bug. [S038; S039; S051]

## Exact acceptance states

`declared` means intent exists. `written` means a successful file-write receipt exists. `read_back` means expected bytes were observed. `committed` requires an immutable revision. `resolved` means consumers and platform reference the intended producer. `executed` requires a real run. `observed_healthy` requires intended candidate and application health. `recovery_verified` requires a recovery drill. `accepted` requires the actual approving authority.

Not every profile needs every state, but omitting one requires a profile-specific reason. A static-site release and a stateful service need different recovery evidence. None of these states is established by a task list changing to “completed.”

## Gate against another misleading closure

The receiving agent should return exact changed revisions, linked requirements, test names/results, actual unresolved blockers and an explicit statement of which environment was untouched. Keep asynchronous provider states open until observed. Do not merge an API producer and consumer in the wrong order or claim a shared workflow exists upstream based on local files. Preserve the current user scope: plans and doc formalization do not authorize any of these target-system changes by themselves.
