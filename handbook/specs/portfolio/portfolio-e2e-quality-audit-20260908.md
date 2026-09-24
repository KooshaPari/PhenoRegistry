# Portfolio end-to-end quality audit

Prepared 2026-09-08 from the existing read-only reports
`chat2-portfolio-audit-20260904/deep-validation.md` (observation
2026-09-05 Pacific), `validation-report.md` (2026-09-05 UTC), and
`portfolio-slice-audit-2026-09-05/44-stage-dashboard.md` and
`45-long-term-forward-wbs.md` (prepared 2026-09-07), plus the referenced
`pheno-portfolio-demos` evidence. This is a bounded quality crosswalk. It does
not claim every repository or product has been audited, and no builds or tests
were run for this report.

| Quality dimension | Actual evidence and scope/date | Gap / current disposition | Concrete acceptance gate |
|---|---|---|---|
| Unit | Apisync captured transcripts report 164 workspace tests (2026-09-05); Logify source-contract pilot reports 28/28 and then 6/6 after subscriber configuration; adapter bundle had zero-test shim binaries. | Captured results are not a fresh portfolio-wide unit baseline; many dossier tests were only inspected statically. | Re-run unit suites from pinned commits; retain command, environment, pass/fail totals, ignored tests, and artifact hash per affected component. |
| Integration | Logify adapter contract reached 6/6 in scratch; MCPForge focused replay did not complete; adapter bundle metadata/compile scratch path passed but doctests failed. | No broad cross-component integration or consumer journey is accepted. | Run one consumer-identical success/error/retry/shutdown journey with pinned source, dependency, schema, and rollback evidence. |
| Contract | 33 chat2 dossiers had required sections and source-path references; platform checks covered RepoLedger, ResilienceKit, Sidekick, Journeys, Tooling; contract categories are defined in MAIN00. | Capability matrices remain generic/unscored in places; static declarations do not prove runtime contracts. | For each selected contract, define inputs/outputs/errors/ordering and execute positive, negative, retry, and compatibility fixtures. |
| Real transport | AgilePlus MCP/gRPC health, dashboard, governance, and audit reads were captured as OPERATED evidence in Wave 04 (2026-09-05); teamcomm smoke directly called handlers. | Teamcomm transport framing/client serialization was not proven; Tracera/Plane consumption remains unproved. | Capture real socket/HTTP/MCP transport request and response traces, IDs, ordering, reconnect, malformed input, and rollback behavior. |
| E2E | Existing portfolio pilots include bounded Logify scratch behavior and Agentora/G1/G2/G3 media/transcript artifacts; reports explicitly distinguish static, claimed, reproduced, released, and operated evidence. | No portfolio-wide E2E acceptance; MCPForge replay blocked, Logify has no proven in-scope consumer, and Agentora capture gates remain separate. | Execute a named user journey from clean setup through result, failure/recovery, artifact export, and independent restore; retain unedited trace and manifest. |
| UI | Dossier navigation and 70 local Markdown targets passed validation (2026-09-05); pilot HTML/PDF/video bundles exist. | Navigation/file existence is not UI behavior; no browser interaction, visual regression, keyboard, or screen-reader run was validated here. | Browser-test critical flows at pinned browser/version with screenshots/traces, keyboard-only path, focus order, error states, and visual assertions. |
| Native framework behavior | Agentora and peer/framework claims are explicitly bounded; direct baseline cannot generalize to Agentora/LangGraph. MCPForge static module-path alignment is recorded. | No cross-framework native parity or framework-specific recovery proof. | Run the same frozen task through each named native adapter and retain native event IDs, side effects, failure behavior, and app/native attribution. |
| Accessibility | No qualifying accessibility execution evidence appears in the cited reports. | Unknown. | Perform WCAG-oriented keyboard, focus, semantics, contrast, zoom, reduced-motion, and screen-reader checks on the actual UI; retain results and defects. |
| Performance | Reports retain some pilot timing/context but no accepted portfolio performance baseline; placeholders and unmeasured forecasts are called out in Tooling. | No normalized latency/resource/throughput comparison. | Define workload, warm/cold policy, hardware, sample count, percentiles, CPU/memory/I/O, and failure thresholds; retain raw measurements. |
| Reliability | WBS requires restart/replay, retry, shutdown, rollback, and no-duplicate side effects; Argis restart/replay and rollback remain open. | No accepted crash recovery or durable-state reliability proof; historical claims are not reproduced. | Inject process death, timeout, duplicate resume, partial side effect, and sink failure; prove recovery, idempotency, continuity, and bounded loss. |
| Security | Static findings include wildcard CORS in RepoLedger and policy/authorization boundaries in ResilienceKit; no messages were sent and no deployment exposure probe was run. | No threat-model execution, authn/authz, secret-redaction, sandbox, dependency, or network-boundary acceptance. | Run authorized security tests for auth, CORS, injection, path/sandbox escape, secret handling, dependency provenance, and least-privilege transport. |
| Package | Package provenance report records mismatches: Apisync source 0.2.10 vs registry through 0.2.9; Benchora 0.2.1 vs audited 0.2.0; adapter bundle has duplicate names and unpinned historical canonical revision. | Publication, source-byte parity, signatures, and consumer compatibility are HOLD. | Select canonical package/version; reproduce metadata/build/tests/doctests, verify source and lockfile hashes, registry identity, signatures, and consumer install. |
| Install | Reports mention clean-install and package provenance as required gates, but no installation was performed by the cited validation lanes. | Unknown across the slice; no reproducible environment proof. | Install from a clean machine/container using pinned lockfiles and documented tools; verify executable/library bytes and offline fixture behavior. |
| Upgrade | No accepted upgrade rehearsal is evidenced. Apisync and other registry/source version mismatches remain unresolved. | Upgrade compatibility, migration steps, and downgrade path are unknown. | Test old-to-new upgrade with data/schema/API compatibility, dependency resolution, migration failure, and tested downgrade/rollback. |
| Restore | WBS P1/P3/P5/P6 repeatedly requires independent restore, `git fsck`/ref parity, source preservation, and tested rollback; current dashboard reports zero accepted cutovers. | Restore evidence is proposed or family-specific and incomplete; no portfolio-wide restore acceptance. | Restore from an immutable source/artifact manifest into a disposable target, verify refs/data/behavior/consumers, then prove failure leaves original intact. |
| Hosted CI | Reports explicitly state hosted workflow samples do not establish complete CI health; local checks must not be reported as hosted success. | No current hosted scheduler/check-run verification was performed in this audit. | Query the exact hosted workflow/check runs for the pinned commit; retain URLs/status/log evidence, required jobs, artifacts, and rerun policy. |

## Current quality posture

The evidence supports a **bounded static and selected-pilot checkpoint**. It does
not support product completion, release readiness, migration approval, archive or
deletion, consumer cutover, or an all-repository quality claim. The controlling
portfolio state remains 78/78 static inventory, zero accepted migration cutovers,
and zero archive/delete authorizations (`44-stage-dashboard.md:9-17`,
`45-long-term-forward-wbs.md:125-129`).

The highest-value next acceptance work is consumer-identical E2E execution,
package/install provenance, independent restore/rollback, real transport proof,
and hosted CI verification for each explicitly selected family. All gates remain
family-specific; a passing local test or populated media bundle cannot close
another family's gate.
