# Portage — SOTA/bootstrap pass 1

Observed 2026-09-29; target source `7593f02f9b370edbbbf447d44c17645db3d19316`. **Architecture/existence gate OPEN.** Official documentation was read; exact external implementation versions, licenses and native integration results remain unqualified. No source is treated as an empirical performance proof.

## Best realistic absence stack, provisional

Current upstream Harbor with supported task/agent/environment extensions, isolated verification and artifact-based regrading; an established experiment/trace store where needed; PhenoLab or equivalent tooling for study-level decisions. Inspect is a serious alternative where its task/solver/scorer model better matches the work. Compare a composed, idiomatic stack—not an intentionally impoverished upstream configuration.

| Capability / primary source | Evidence actually inspected | Bootstrap hypothesis | Unresolved technical/integration cost |
|---|---|---|---|
| Execution/isolation: https://docs.harborframework.com/core-concepts/tasks/separate-verifier | Separate verifier environment, explicit artifact transfer and image/config choices | USE DIRECTLY or INTEGRATE upstream; retain fork only for identified delta | Task compatibility, credential/network isolation, image provenance, dependency flakiness and mounted caller behavior |
| Replay: https://docs.harborframework.com/core-concepts/jobs/regrade | Recorded artifacts can be graded into a new trial without rerunning the agent; prerequisites are explicit | USE DIRECTLY / ADAPT evidence binding | Required artifact completeness, task identity, versioned policy and downstream result semantics |
| Scoring: https://inspect.aisi.org.uk/scorers.html | Extensible scorers and metrics with multiple matching/grading approaches | INTEGRATE or LEARN FROM, based on task semantics | Task conversion, invalid-reference behavior, scorer isolation, held-out validation and imported result fidelity |
| Trace/experiments: https://langfuse.com/docs/evaluation/overview | Online/offline evaluations, datasets and comparisons | COMPOSE where a general trace/comparison service is needed | Deployment/retention, ACLs, export semantics, operating cost, privacy and exact version |
| Provenance: https://www.w3.org/TR/prov-overview/ | Standard provenance framework discovery | LEARN FROM / ADAPT vocabulary, not invent every provenance relation | Authorization is additional policy; a valid provenance graph does not certify truth |

## Differentiation attack

Commodity/contested: generic task execution, isolated grading, artifact replay and result viewing. A uniqueness argument resting only on those is falsified by available upstream documentation. Candidate differentiation: particular model × harness × swarm competency coverage, strict consumer-bound evidence semantics or necessary owned-fork governance. Those remain **unverified**, not claimed unique. No external user or benchmark pilot establishes an advantage here.

BUILD CUSTOM requires an accepted obligation, demonstrated upstream/adapter shortfall, costed maintenance and a falsifying experiment. FORK requires a concrete delta ledger and feasible upstream-sync burden. REJECT a solution only after evaluating the best realistic composition and its constraints. No competitor is rejected on marketing impressions; no custom subsystem is approved by default.

## Required next research passes

Pin the upstream merge-base/current candidate and enumerate actual owned deltas; inspect task/job/trial models, storage, regrade and failure semantics; evaluate ATIF and consumer contracts; audit licenses/security/project health and commercial operating burden; inspect representative benchmark literature and scoring validity. Then run repo experiment P-X01 with a bounded deterministic task, adversarial evidence and real persistence. The first pass has not exhausted major capabilities or closed the existence gate.
