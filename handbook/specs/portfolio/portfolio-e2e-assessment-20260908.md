# Portfolio end-to-end assessment and forward plan

Prepared September 7 Pacific / September 8 UTC 2026. Mode: audit, research synthesis and planning. This document coordinates existing sources; it does not replace product-local specifications or the reconciled machine registers.

## Executive assessment

The portfolio has substantial policy, scope inventories, source audits, research captures, work breakdowns and pilot artifacts. Available evidence does not establish that every repository is optimally planned, implemented, tested, released or operated. The dominant problem is incomplete linkage and acceptance across those layers, compounded by mixed observation dates and unfinished authority decisions. More document volume alone will not close it.

The current audit is an end-to-end assessment of the program and its retained evidence, not a newly executed deep audit of every codebase. Missing evidence is listed as unknown; it is not proof that the implementation or tests do not exist.

## Past, present, target

| Period | Evidence and state | Consequence |
|---|---|---|
| September 1 imported plans | 146 owner-affiliated repository rows; competing portfolio-control and rationalization proposals | Preserve aliases, intent and proposals; do not enforce this as a current census or accept dispositions automatically |
| September 4-7 bounded audits | 33-repo chat2 dossiers and a separate 78-repo slice; static validation, limited source reviews and compatibility experiments | Join identities before calculating coverage; 33 + 78 is not a proven unique audited total |
| Earlier active pilot | Agentora Patch Review Workbench, frozen task and capture-supervisor plan; limited direct baseline and blocked comparison/capture gates | Resume from exact review findings and contract, not from unrelated repository activity |
| Session detour | External contribution candidates and their baseline tests were mistaken for portfolio progress | Exclude DeskcommCRM/token-monitor work from this program's completion evidence; preserve incident record |
| September 7 census receipt | 139 authenticated owner repositories; separate 14 organization-visible, 5 collaborator-visible and 99 local Git roots | Distinct scopes, not an additive project denominator; refresh before execution if identities or refs changed |
| Target | One traceable evidence chain per material capability and one scoped execution queue | Accept closure by contracts and results, not counts of artifacts, tests or repository names |

## Authoritative inputs

Current explicit sponsor instructions govern scope and action. Use `phenotype-portfolio-control` for broad policy and maturity definitions, `portfolio-reconciliation` for conflict resolution and normalized proposals, and actual product-local accepted contracts for behavior. Imported rationalization destinations remain hypotheses. Later reports may update evidence without automatically changing authority or permissions.

Sources relative to this Downloads directory:

- `phenotype-portfolio-control/02-COMPLETENESS-MODEL.md`: intent, product, specs, architecture, code, quality, evidence, operations, market and governance dimensions; G0-G6 gates.
- `phenotype-portfolio-control/04-SOTA-PILOT-CASE-STUDY-PROTOCOL.md`: fair comparison contract and evidence requirements.
- `portfolio-reconciliation/prompts/EXECUTION-ADDENDUM.md`: authority, provenance, dynamic census, execution and preservation constraints.
- `portfolio-reconciliation/data/work-queue.json`: 22 imported assessment-first work packages; no implicit execution authorization.
- `chat2-portfolio-audit-20260904/deep-validation.md`: qualified 33-dossier static integration review, not exhaustive runtime acceptance.
- `portfolio-slice-audit-2026-09-05/44-stage-dashboard.md` and `45-long-term-forward-wbs.md`: 78-row scope and later recovery/authority/pilot gates; reconcile report-specific differences before execution.
- `session-scope-audit-20260907.md`: recovered session ownership, detour effects, inventory limits and corrections.
- `session-pilot-crosswalk-20260907.md`: AgentAPI, Apisync and G3 evidence boundaries.

## Inventory and scope

The retained authenticated owner snapshot contains 139 repositories, 30 private and 17 archived. Of 146 imported names, 111 matched directly and 27 resolved through GitHub redirects. Eight returned 404; a 404 does not prove deletion. One local homebrew-omniroute backup retains a historical commit; no successor is proven by that alone. The 99 local roots include worktrees and preserved sources. Repository IDs, Git common directories, remotes and source refs must be joined before counting independent repositories.

The complete program retains original/fork/private/archive/local-only identities while prioritizing active capabilities. Organization or collaborator visibility does not itself make a repository an owned implementation target. No further work on external contribution candidates belongs in this queue without a separate assignment.

## Current completeness by dimension

| Dimension | Present evidence | Unclosed requirement |
|---|---|---|
| Intent | Verbatim-source packages, doctrine and session correction | Per-capability provenance and supersession; earliest session recovery is partial |
| Product/jobs | Family hypotheses, dossiers, pilot proposals | Accepted user jobs, non-goals and maintained role for each retained product |
| Specifications | Completeness model, schemas, local designs | Requirement-to-oracle mapping and contradiction review against current source |
| Architecture | Family maps and authority alternatives | Accepted writers, current consumers, schema/API/ABI and failure contracts |
| Implementation | Pinned static findings and isolated examples | Current default/release-build reachability and actual integrated behavior |
| Quality | Test sources, captured results, qualified independent reviews | Meaningful negative controls, real transport/E2E, selected CI jobs and artifact tests |
| Evidence/pilots | Direct baseline, transcripts, limited compatibility work | Fair comparable runs, immutable manifests, retained failures and independent review |
| Operations | Packaging/release proposals and selected provenance observations | Install/upgrade/rollback, signed artifact identity, restore and real-use evidence |
| SOTA/research | Prior alternative captures and narrowed hypotheses | Current primary-source verification and semantic comparison for material families |
| Governance | Reconciliation kit, stable aliases, decisions and queue | Accepted domain owners and applied work leases; no synthetic global percentage |

## Quality infrastructure contract

For each relevant capability record the exact test command, selected source revision, fixture/config/toolchain hashes, execution environment, exit status, raw output, reviewer and remaining limit. Tests that are absent, skipped or blocked cannot satisfy a required gate. A well-justified N/A needs a scoped rationale.

| Layer | Required proof |
|---|---|
| Build/static | Locked toolchain/dependencies; default and release targets compile; real lint/type/static checks propagate failure |
| Unit/property | Boundary, malformed-input and state invariants; mutation or negative controls demonstrate failure detection |
| Contract | API/schema/CLI/ABI compatibility, version negotiation and backward-compatible errors |
| Integration | Actual database, queue, filesystem and process boundaries; restart and concurrency behavior |
| Transport | Real socket/HTTP/stdio framing, serialization, truncation, cancellation and backpressure; direct handler calls are insufficient |
| E2E | Installed product completes a representative user job through its real interfaces, with success and recovery paths |
| UI/native | Supported platform, focus/input routing, accessibility, error/empty/loading states and capture isolation |
| Performance | Declared workload and resource budget, cold/warm runs, repetitions, tails and correctness floors |
| Reliability | Timeout, retries, idempotency, disconnect, crash recovery, partial-write and resource-exhaustion handling |
| Security/supply chain | Threat-model-specific permission boundaries, secret handling, dependency/provenance checks and denied-action tests |
| Packaging | Published or staged package maps to source and passes clean install/uninstall/upgrade smoke |
| Data/recovery | Schema migration, preserved data/refs, independent restore and tested rollback |
| Hosted CI | Exact commit, selected jobs, result/skip semantics and failure propagation; local passing tests do not prove hosted CI |
| Operations | Dogfood period with user tasks, interventions, failures, support and maintenance cost |

Do not run all suites across all repositories indiscriminately. First inventory entrypoints and CI selection; then execute the smallest checks that answer a declared gate on a pinned source. Expand when failures or changed scope justify it.

## Research and pilot plan

Research is organized by material capability family, with per-repository applicability links. Retain old captures as historical. For each family refresh primary-source versions, architecture, licensing, support boundaries and meaningful alternatives, including direct/manual/no-framework and composed baselines. Broad discovery and a small executable shortlist are different deliverables. Requested breadth must be measured without padding aliases or failed requests as successful comparisons.

Before running a pilot freeze user job, target and alternatives, inputs, oracle, must-pass floors, expected advantage, resource/tuning budgets, repetitions, failure policy, and measurements. Include setup effort, maintainability, interoperability and operations, not latency alone. A result may justify an internal strategic component without a public novelty claim. Inconclusive or losing results must remain possible outcomes.

Agentora's current recovered plan has five failed capture-protocol review gaps and separate attempt-budget, pinned-dependency and capture-isolation constraints. AgentAPI's retained live message round-trip failed. Apisync's captured test results need source/package provenance reconciliation. G3's inspection is not provider execution or migration acceptance. Existing media does not upgrade these results.

## Infrastructure target

The requested direction is OCI-oriented operation through Podman and Apple Container, with the intended Windows WSLC backend identified explicitly. Do not silently translate WSLC into WSL2. Runtime identity and image-format portability do not establish equal CLI/API, network, volume, build, resource, or cleanup behavior.

Use nanovms as an existing capability/adapter candidate subject to source and consumer inspection. Audit current consumers before introducing a second runtime interface. Migration acceptance must cover image digest/architecture, create/start/exec, stdin/exit status, dynamic ports, mounts and persistence, cancellation, logs, labels, limits, health, cleanup and orphan detection. Windows behavior requires Windows evidence. Colima's existing state must be inventoried and safely cut over after parity; a new Docker socket dependency is not the target architecture.

The broader infrastructure horizon also retains compute/data/I/O placement, hardware capacity, GPU/platform constraints, audio/video/input routing, clocks, isolation and observability. Those research mechanisms must be separated from already demonstrated runtime support. Capture and benchmarking must respect foreground interactive workloads.

## Forward WBS

IDs below coordinate existing work; they do not replace REC-W or product-local task IDs. Owners are responsibility roles until a bounded worker lease names an executor. No calendar estimate is defensible for the whole portfolio before remaining work is sized.

| ID | Work and output | Dependency | Exit gate / owner |
|---|---|---|---|
| E01 | Join source inventories, aliases, Git IDs/common dirs and 33/78 audit scopes into existing records | Retained census | Explicit coverage and unresolved identities; census owner; maps to REC-W-001 |
| E02 | Map prompts, accepted specs, decisions, generators and stronger local authorities | E01 for repo assignment | No-loss source crosswalk; documentation owner; REC-W-002/004 |
| E03 | Attach capability vectors and current source/test/CI/package receipts | E01, bounded local scope | Each cell has scoped evidence or unknown/N/A; repo auditor |
| E04 | Resolve material cross-family writer/consumer conflicts | E02 and relevant E03 evidence | Versioned decision with consumer and rollback obligations; portfolio/family adjudicator |
| E05 | Refresh family research and freeze pilot contracts | Product job and relevant E04 only | Primary-source register, exclusions, oracle and fair shortlist; research owner |
| E06 | Audit OCI consumers and stage runtime parity specification | Runtime source/consumer scope | Podman/Apple/Windows capability matrix and tested migration plan; infrastructure owner |
| E07 | Specify/repair meaningful quality envelope for selected closure slice | Accepted requirements, scoped E03 | Negative controls and real CI selection; quality owner |
| E08 | Implement bounded requirements and independently verify | E07 and relevant contracts | Required checks pass on pinned default/release build; implementer plus separate verifier |
| E09 | Execute paired representative pilots | E05, stable runnable slice | Raw results, failure cases, analysis and disposition recommendation; pilot owner |
| E10 | Package and prove install/upgrade/restore/E2E | E08 and applicable platform dependencies | Artifact-level supported-platform proof; release owner |
| E11 | Operate bounded dogfood and measure support burden | E10 | Real task and incident evidence; product/operator owner |
| E12 | Propose accepted role, consumer cutover or retirement | Relevant E04/E09/E10/E11 | Preservation, independent restore, rollback and action-specific approval; adjudicator |

```text
E01 identity -> E02 intent/authority -> E04 decisions
   |                 |                    |
   +-> E03 evidence -+-> E07 quality -> E08 implementation -> E10 artifact E2E -> E11 use
                     +-> E05 research -> E09 pilot ----------------------------+-> E12
E06 OCI compatibility supplies only the platform edges actually required.
```

Keep one control slice, one product closure slice, one consolidation/forensic slice within review capacity. Blocked tasks retain owner and wakeup conditions but release execution slots. Do not make an unrelated standalone product wait for a full portfolio platform rebuild. Do not reopen known complete checks without changed evidence.

## Completion and optimality

The correct target is defensible, measurable planning with explicit tradeoffs. Universal optimality is not established by this audit. Measure first successful user outcome, accepted capability coverage, unresolved critical requirements, maintenance burden, contract-change impact and operational cost. Report the weakest required gate and critical blockers rather than averaging them away.

The three bounded lane reports are now reconciled below. This completes the program-level synthesis; current-code coverage, comprehensive family research, test execution and operational certification remain distinct work. The audit must never be presented as proof that all portfolio repositories are done.

## Integrated lane findings and handoff

- [Planning audit](portfolio-e2e-planning-audit-20260908.md): source precedence, existing task namespaces and traceability gaps. Its FWP steps are decompositions of this document's E01-E12 work, not another independently dispatched backlog. The 78-row observation slice is distinct from the historical 63+15 scenario even though their totals match.
- [Quality audit](portfolio-e2e-quality-audit-20260908.md): scoped evidence and concrete acceptance across quality layers. Captured AgilePlus transport observations are historical receipts, not current engine status. No live AgilePlus state was inferred from files in this synthesis. Claims of zero accepted cutovers are limited to the reviewed packets, not the entire portfolio history.
- [Infrastructure audit](portfolio-e2e-infra-audit-20260908.md): NanoVMs source supports Podman, Apple Container and WSLC candidates; local Podman 6.1.1 lacks a machine/socket and Apple Container 1.0.0 has a stopped API server. Colima/Docker responds. These are September 7 observations, not guarantees of continuing availability.

WSLC is present in NanoVMs: `pkg/runtime/probe.go` prefers `container.exe` then `wslc.exe`; `internal/adapters/containers/containers.go` defaults to `wslc.exe`; the general Windows adapter detects `wsl.exe`. Resolve this naming/adapter contract with authoritative Windows evidence. Do not discard the WSLC direction or silently substitute WSL2. Podman setup was already authorized by the sponsor; no additional consent is needed merely because the install was interrupted. This pass remained audit-only.

Fresh primary-source research, September 8 UTC:

- [OCI overview](https://opencontainers.org/about/overview/) distinguishes image, runtime and distribution specifications. Inference: OCI compliance alone does not establish Docker CLI/API interchangeability.
- [Apple Container README](https://github.com/apple/container/blob/main/README.md) documents OCI-compatible images and an Apple-silicon/macOS runtime. Local lifecycle conformance still needs execution evidence.
- [Podman machine documentation](https://docs.podman.io/en/stable/markdown/podman-machine.1.html) documents VM management for macOS and Windows. Installing the client alone does not prove a working local engine.

These three sources validate runtime architecture assumptions only; they do not complete portfolio-wide SOTA research.

The next bounded execution packages should be selected from existing task IDs: finish identity/coverage joins without serializing all useful work behind eight unavailable identities; attach missing source/config/run receipts to one owned pilot; resolve Agentora's failed protocol review under its existing task contract; stage the NanoVMs capability/parity matrix before runtime removal. Preserve current attempt, offline, capture and destructive-action gates until their specific conditions change.
