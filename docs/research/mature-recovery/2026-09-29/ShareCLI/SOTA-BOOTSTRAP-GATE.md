# ShareCLI — SOTA, alternatives and bootstrap gate, pass 1

Research date2026-09-29. Internal source `4f01d0199e82b62bcf20399afcc102f58a10ad07`; registry source `85d7cd00cf59c379c05b740e8130a85b0d5bd31b`. **OPEN, architecture not frozen.** Primary documentation and author material were inspected; no vendor performance claim is treated as measured product evidence. Dynamic documentation URLs below are retrieval identities, not immutable source commits; missing version/health/license verification blocks final adoption.

## Source and competitor/prior-art matrix

| ID / source | Version/date and inspected extent | Factual claim supported | Interpretation, limit and decision consequence |
|---|---|---|---|
| SC-R01 https://github.com/F1bonacc1/process-compose | README feature/API section retrieved2026-09-29; exact source SHA not captured | Declares non-container process orchestration, recovery policies, liveness/readiness, CLI/TUI, authenticated REST option and MCP integration | Strong supervision/control baseline. Does not establish ShareCLI-specific global mediation, lease semantics or workload outcomes. Apache-2.0 indicated by repository UI; full license/dependency compatibility and maintenance history not reviewed. |
| SC-R02 https://bazel.build/remote/caching | Current documentation retrieved2026-09-29; action/cache model and known-issues sections | Separates action cache from content-addressed outputs and includes command/environment/input relationships; documents problems from concurrent file changes and tools outside tracked workspace | Learn/adapt explicit equivalence boundaries, not a promise that hashing anything makes arbitrary commands safe. No measured transferability to ShareCLI or exhaustive Bazel correctness proof. |
| SC-R03 https://pkg.go.dev/golang.org/x/sync/singleflight | Page displayed v0.23.0, published2026-08-31, with warning it is not latest module version; API/examples inspected | A Group suppresses concurrent calls sharing a key; duplicate callers share the result | Learn keyed in-flight suppression. It does not supply the correct semantic key or establish durable cross-process caching. BSD-3-Clause displayed; not a direct Rust dependency decision. |
| SC-R04 https://docs.kernel.org/accounting/psi.html | Current kernel documentation, original dateApril2018; pressure interface, threshold and cgroup sections | CPU/memory/I/O pressure observations and threshold notifications are available under stated kernel/configuration conditions | Integrate native Linux pressure signals before inventing an agent-count proxy as the only signal. It is observation, not automatic enforcement; macOS/Windows parity requires separate research. |
| SC-R05 https://www.buildbuddy.io/docs/remote-build-execution/ | Page reports updated2026-09-28; features/deployment options inspected | Vendor documents managed/on-prem remote execution, artifact caching, mTLS and action deduplication/merging | Direct attack on novelty of action merging. Scalability and benefit claims unbenchmarked here. Hosted/on-prem pricing, licensing and supported workload details remain unverified; no purchase recommended. |
| SC-R06 https://simon.peytonjones.org/build-systems-a-la-carte/ | Author publication page; ICFP2018, expanded JFP2020 link; abstract only | Authors present an executable comparative framework for decomposing and recombining build-system designs | Relevant intellectual framework for separating mechanisms. Not a benchmark of multi-agent CLI concurrency or general command caching. Full paper/code not inspected. |

No stars, feature counts or marketing superlatives are used as project-health or performance evidence. The exact candidate release/source lock, license text, transitive licenses, security history, maintainer activity, compatibility and integration cost still require explicit review.

## Best realistic replacement stack — current proposal

For the recovered owned-workstation workload, the baseline to beat is **process-compose for configured supervision and operator control, native OS resource controls/observations, and each supported tool's existing correct build/cache mechanism (Bazel for Bazel workloads), with no generic arbitrary-command result cache**. Existing shell/session tooling remains part of the user's environment rather than a new mandatory product subsystem. Compare BuildBuddy for eligible remote build actions when its deployment/cost constraints fit; it is not silently mandatory or free.

This composition deliberately does not claim to transparently mediate every externally launched vendor process. Where observation or intervention is required beyond configured supervision, inventory the actual gap and test it. A best alternative can leave a legitimate gap; it must not be crippled to make ShareCLI win. A concrete baseline installation, supported-platform matrix and paired workload comparison are still outstanding.

## Differentiation ledger

| Classification | Claim | Evidence/attack and disposition |
|---|---|---|
| Commodity/contested | Supervision, restart, health checks, CLI/TUI/API/MCP control | SC-R01 already documents substantial coverage; not sufficient differentiation |
| Commodity/contested | Artifact caching and action deduplication | SC-R02/03/05 cover pieces; distinguish declared build actions from generic CLI work |
| Falsified as a broad novelty claim | Sharing duplicate work or having a process-control API is itself new | Existing documented primitives/products defeat that argument; not claiming full product equivalence |
| Falsified unsafe interpretation | HEAD+status or argv equality proves reusable output | SC-F01 / SC-EXP-001 source-derived counterexample; no cryptographic collision is involved |
| Candidate differentiation | One usable operator experience across heterogeneous agent workload detection, bounded control and safe work-sharing adapters | Product thesis only; actual integration reach and user benefit unverified |
| Unverified | Better foreground responsiveness/resource efficiency without incorrect results or greater operating burden | Needs measured baseline/candidate trials, native negative controls and supported OS evidence |
| Unverified | Recovery/coordination across worker replacement and worktree/filesystem strategies is materially better than composition | Donor parity, lease correctness and comparative experiments outstanding |

## Bootstrap decision ledger (all provisional)

| Capability | Options considered | Current disposition / why custom might remain | Next decision evidence |
|---|---|---|---|
| Process lifecycle/UI/API | USE, INTEGRATE, ADAPT process-compose; existing local supervisor; FORK only if demonstrated incompatible extension | Compare integration before maintaining a second generic supervisor. Custom value must be agent-aware policy/UX, not commodity mechanics | Public lifecycle and identity tests; compatibility with recovered no-vendor-binary-replacement detection intent |
| Repeated work | USE tool-native caches; COMPOSE action cache/CAS; LEARN singleflight; REJECT unconditional generic result reuse | Custom semantic adapter/evidence boundary may be necessary where existing tools cannot express it. Do not hand-roll cache mechanics by default | Changed-input/tool/env/principal fixtures, poisoning tests, cost of fingerprinting, native throughput/foreground impact |
| Queue/admission | INTEGRATE OS primitives; ADAPT durable lease/generation semantics; compare existing local orchestration | Custom policy only if baseline cannot represent accepted contention/ownership behavior | Crash/orphan/live-owner and clock/priority/fairness tests; not a cosmetic rank patch |
| Resource signals | USE Linux PSI; evaluate native platform APIs separately | Custom policy interprets signals, not reinvents measurement | Privilege/configuration matrix, missing/stale collector behavior, platform parity |
| FUSE/worktrees/mesh | USE filesystem libraries; ADAPT recovered donor semantics; COMPOSE eligible tool caches | Preserve intended outcomes, but custom interception only where measured benefit justifies compatibility/security burden | Full donor revisions, actual mount/path semantics, optional/required mode, crash/conflict experiments |
| Evidence/grader interface | COMPOSE existing run/artifact tooling; BUILD narrowly scoped product adapters | Product-specific subject identity and negative controls remain necessary; a new general task platform does not follow | Independent policy selection and non-empty exact-candidate receipts |

## Academic evidence matrix

| Paper | Exact task | Dataset / sample | Baseline / metric / evaluator | Establishes / does not establish |
|---|---|---|---|---|
| Mokhov, Mitchell, Peyton Jones, Build systems a la carte, ICFP2018 | Abstract: executable framework comparing and recombining build-system designs | Not extracted from abstract; do not invent dataset or n | Full baselines/metrics/evaluation not inspected; author abstract is not independent evaluation | Supports a decomposition research direction only; does not establish ShareCLI throughput, correctness, OS parity or ROI |

Full-text study and current academic work on incremental computation, hermetic execution, coordination/fencing, scheduling and workload interference are **not complete**. No paper-derived numerical benefit is claimed.

## Remaining gate and experiment program

Pin candidate versions/commits; review licenses and health; inspect deeper API/data/storage/failure semantics; test configured supervision plus cache baseline; compare actual authorized equivalent reads; run wrong-scope/stale/poisoned/mutation and crash controls; validate detection-to-mediation reach; verify supported OS and packaging. Architecture cannot freeze until high-risk alternatives and native experiments close. The later pilot compares product, best supported alternative and status quo on correctness, false greens, time/cost, intervention, recovery and usability; it is separate from this gate.
