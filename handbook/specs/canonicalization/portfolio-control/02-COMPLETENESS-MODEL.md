# Completeness, traceability, and maturity model

## Core model

For each material capability `K`, track the vector:

\[
K = \langle I, P, S, A, C, Q, E, O, M, G \rangle
\]

| Dimension | Meaning |
|---|---|
| `I` Intent | Human sources, rationale, users, constraints, non-negotiables, supersession |
| `P` Product | User job, journey, value, scope, non-goals, success/failure |
| `S` Specification | Functional/non-functional requirements, contracts, acceptance criteria |
| `A` Architecture | HLD/ALD/LLD, ADRs, interfaces, data/state ownership, failure behavior |
| `C` Code | Reachable implementation, build inclusion, real integrations, migrations |
| `Q` Quality | Tests, static checks, security, compatibility, performance, packaging gates |
| `E` Evidence | Reproductions, benchmarks, demonstrations, pilots, real-use outcomes |
| `O` Operations | Installation, release, upgrade, observability, support, recovery, retirement |
| `M` Market/SOTA | Alternatives, baselines, differentiators, tradeoff and no-build decisions |
| `G` Governance | Authority, lifecycle, owner, budget, risk, decision and change control |

A repository is not complete because it has all filenames. It is complete only when every in-scope capability has the required dimensions at the required evidence level and no unresolved critical contradiction.

## Coverage states

Each cell uses one of:

| State | Definition |
|---|---|
| `U` Unknown | Not inspected or evidence unavailable |
| `0` Missing | Required representation is absent |
| `1` Claimed | Mentioned but not defined or evidenced |
| `2` Specified | Explicit contract and acceptance conditions exist |
| `3` Implemented | Reachable implementation appears present |
| `4` Verified | Machine-verifiable oracle passes with negative-control evidence |
| `5` Demonstrated | Representative end-to-end or comparative evidence exists |
| `6` Operated | Used in a real supported environment with operational evidence |
| `X` N/A | Not applicable, with rationale and reviewer |
| `D` Deferred | In horizon but explicitly deferred with owner and trigger |
| `R` Research | Feasibility unresolved; hypothesis and experiment exist |
| `S` Superseded | Historical record retained and successor identified |

Do not average these values into one flattering percentage. Report:

1. The weakest required dimension.
2. Critical gaps.
3. Coverage by capability.
4. Evidence confidence.
5. Gate reached.
6. Optional weighted score for prioritization only.

## Canonical capability record

Every significant product capability should have one canonical record or generated equivalent:

```yaml
id: CAP-AGENT-EXEC-001
name: bounded agent task execution
owner_repo: KooshaPari/thegent
user_jobs:
  - JOB-AGENT-001
intent_sources:
  - INT-0042
requirements:
  - FR-EXEC-001
  - NFR-RT-004
decisions:
  - ADR-EXEC-007
implementation:
  - repo: KooshaPari/thegent
    ref: <commit>
    paths:
      - crates/...
quality:
  - TEST-EXEC-001
  - BENCH-EXEC-003
evidence:
  - EVD-EXEC-019
operations:
  - RUNBOOK-EXEC-002
market_baselines:
  - ALT-OPENAI-AGENTS
  - ALT-LANGGRAPH
status:
  intent: 4
  product: 4
  specification: 4
  architecture: 3
  code: 3
  quality: 2
  evidence: 1
  operations: 1
  market: 3
  governance: 4
```

The record links artifacts; it does not duplicate their full prose.

## Maturity gates

### G0 — Identity and evidence recovered

Required:

- Repository identity, ref and history coverage recorded.
- Product/component/fork/archive role hypothesis.
- Available human intent preserved without fabrication.
- Current claims separated from historical and proposed claims.
- Canonical authority conflicts identified.
- Consumer and upstream discovery started.

A repository cannot enter broad improvement work before G0.

### G1 — Documentation and design closure

This is the user’s “everything not dependent on implementation” milestone.

Required where applicable:

- Clear problem, users, jobs, journeys, scope, non-goals, and value.
- Verbatim intent/provenance plus synthesized product contract.
- FR/NFR/system requirements with stable IDs and acceptance conditions.
- Domain model and data authority.
- HLD, explicitly defined ALD, LLD, state/failure/concurrency/security design.
- ADRs for material choices and rejected alternatives.
- SOTA and competitor/workflow analysis.
- Research hypotheses and experiments for unresolved feasibility.
- UX, API/protocol/schema, operations, migration, risk, and release design.
- WBS, DAG, PERT assumptions, work packages, and evidence gates.
- Traceability from source intent to planned verification.
- No critical contradictions among canonical documents.

G1 does not mean the software works.

### G2 — Red quality envelope

“Red” means the project has executable, meaningful oracles that can expose missing or incorrect behavior—not that every test is permanently failing.

Required:

- Reproducible toolchain and dependency lock.
- Build/type/format/lint/static-analysis entry points.
- Characterization tests for preserved behavior.
- Acceptance and contract test skeletons bound to FR/NFR IDs.
- Negative controls or mutation evidence showing the suite can fail.
- Security/supply-chain checks appropriate to the threat model.
- Performance/scale/reliability benchmark harnesses with declared workloads.
- Packaging/install/upgrade smoke harnesses.
- CI actually selects and propagates failures from these checks.
- Known gaps produce explicit failing/ignored-with-contract outcomes, not unconditional success.

G2 can be reached before implementation is green.

### G3 — Green implementation closure

Required:

- In-scope requirements implemented in reachable default/release builds.
- No critical feature is represented only by a mock, fixture, disabled flag, disconnected branch, or README.
- G2 suite passes under representative supported environments.
- Migrations, backward compatibility, failures, and rollback are tested.
- Performance/resource floors are met or exceptions are accepted.
- Release artifact—not merely source checkout—passes smoke and journey tests.
- No critical unsupported “shipped” claim remains.

### G4 — Pilot and competitive evidence

Required for user-facing products, developer products, and major frameworks:

- A representative pilot/problem is selected.
- Closest alternatives solve the same bounded job.
- Environment, inputs, acceptance oracle, and measurement boundaries are controlled.
- Developer and user experience are measured as well as runtime performance.
- Must-not-lose floors and must-win wedge are evaluated.
- Tradeoffs and counterexamples are reported.
- Raw evidence and reproduction instructions are retained.
- Product disposition is revisited if no defensible advantage or distinct job remains.

Libraries and internal foundations can satisfy G4 with consumer/adoption and integration-leverage evidence rather than a public product pilot.

### G5 — Productization and operability

Required:

- Installable/publishable artifact.
- Accurate quickstart and first-value journey.
- Versioning, compatibility, support, upgrade, rollback, and deprecation policy.
- Observability and incident/recovery procedures.
- Security disclosure and provenance/SBOM/release controls.
- Supported platform matrix with actual evidence.
- User-facing errors and documentation are fit for intended audience.
- One credible case study or operational dogfood record.

### G6 — Ecosystem integration and terminal disposition

Required:

- Canonical role and authority registered.
- Dependency direction and consumers are known.
- Duplicate capability claims are removed or explicitly layered.
- Cross-repo contracts and IDs are stable.
- Migration/compatibility bridges are complete or time-bounded.
- Public positioning matches implementation and lineage.
- Repository is in a terminal state from the charter.

## Repository-level completion

A repository’s gate is constrained by the least mature critical capability:

\[
Gate(repo) = \min_{K \in CriticalCapabilities(repo)} Gate(K)
\]

Supporting or deferred capabilities do not block the same way if their status and product claims are honest.

## Project, product, and program views

The same capability graph supports different projections:

- **Project view:** planned work, resources, dependencies, schedule, risks.
- **Product view:** user jobs, journeys, value, market, adoption, support.
- **Program view:** multiple projects/products, governance, portfolio outcomes, cross-repo dependencies.
- **System view:** components, protocols, runtime, data, security, failures.
- **Operational view:** deploys, releases, incidents, SLOs, cost.
- **Evidence view:** tests, traces, pilots, provenance, confidence.
- **Economic view:** maintenance cost, resource allocation, opportunity cost, realized value.

Do not force each view into each repository. Store authoritative records where they belong and render repo-specific projections.

## Quality completeness catalog

The quality layer may need:

- Unit, property, fuzz, mutation, snapshot/golden, integration, contract, E2E/journey, compatibility, migration, concurrency/race, fault/chaos, load, soak, latency, throughput, memory/resource, thermal, security, dependency, license, secrets, provenance, accessibility, docs/link/schema, packaging, installer, upgrade, rollback, release-artifact, and observability tests.

Only applicable classes are required. Every `X` needs a rationale. A project with 5,000 unit tests can remain incomplete if its only important journey is untested.

## Machine-verifiable representation rule

A concern is machine-verifiable when there is a deterministic or statistically defined oracle with:

- inputs and environment;
- expected property or threshold;
- failure semantics;
- reproducibility;
- negative control;
- evidence retention;
- linkage to the requirement.

Some user-value and architectural decisions cannot be fully automated. Their machine-verifiable portion should be automated, while the remaining human judgment has an explicit review rubric and evidence.

## Documentation superset rule

The portfolio baseline is a **capability contract**, not a folder-destruction template.

If a repository already has richer systems—such as device-level prompt captures, structured provenance, generated spec registries, executable notebooks, or superior review workflows:

1. Preserve them.
2. Identify their canonical role and format.
3. Map them into the common capability/traceability schema.
4. Add only missing coverage.
5. Generate compatibility projections if central tooling expects a standard path.
6. Never replace higher-fidelity sources with an impoverished summary.

## Completion report minimum

Each repository report must state:

- Gate reached.
- Gate blockers.
- Critical capability vectors.
- Unsupported claims.
- Current and historical evidence coverage.
- Proposed repository disposition.
- First smallest closure slice.
- Exact commands and artifacts.
- What was not inspected or executed.
