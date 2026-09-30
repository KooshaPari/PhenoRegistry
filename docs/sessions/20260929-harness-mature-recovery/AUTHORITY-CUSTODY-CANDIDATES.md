# Authority and custody decision candidates — pass 1

Date: 2026-09-30. These are architecture candidates supported by current evidence; destructive migrations are not authorized here.

## AgilePlus
HeliosLite currently mounts an internal `forge_agileplus` command engine implementing a 31-pillar scorecard, sprint records and velocity prediction. The broader ecosystem already assigns AgilePlus durable development-effort/work-package responsibility. Candidate decision: **external authority, Helios projection/adapter only**. Preserve useful UI/CLI projection code, but do not let Helios own a divergent scorecard schema, sprint truth or completion reducer.

## Tracera
HeliosLite mounts `forge_tracera` as opt-in best-effort telemetry. Its bridge intentionally ignores submit/flush failures and disables itself on invalid configuration. Candidate decision: **observability sink may remain best-effort; acceptance evidence may not use this path.** Product evidence integration needs acknowledged receipts and exact subject/candidate/criterion identity, with collector failure explicitly non-green.

## Pine/native shell
HeliosLite contains `forge_pheno_shell` and Windows Terminal configuration utilities; KCode/upstream have native Windows machinery. Candidate decision: **Pine owns translation/compatibility semantics; runtimes own adapters and native process execution.** Do not grow shell-detection/completion utilities into a competing translation platform.

## Agentora/SDK
Both ecosystems have SDK-like surfaces and current upstream KCode already has harness/SDK APIs. Candidate decision: **do not infer general Agentora replacement from a client SDK.** General agent framework custody remains external until consumer/API analysis proves consolidation.

## Runtime/product acceptance
Neither CLI owns accepted product truth. Runtime sessions, telemetry and task completion are observations. External accepted contract + independent grader + evidence policy decide product acceptance.

These candidates should become ADRs only after source/consumer contradiction review. They are designed to minimize duplicate authorities while retaining useful projections.