# Pass 8 — W6/W7 semantic obligations and invariants

Date 2026-09-30.

The first semantic obligation slice now exists in all three product repositories. Requirement count remains an output; these documents are DRAFT and ineligible as accepted grading denominators.

## Shared invariant layer

All three obligation documents reference a common v0 semantic invariant set rather than cloning generic concerns per feature:

- authority ≠ confidence;
- exact evidence identity;
- missing/skipped/collector/verifier failure ≠ pass;
- historical evidence stays historical;
- worker/durable effort/product lifetimes are distinct;
- append/supersede history;
- implementation cannot weaken its own grader for credit;
- scope delta ≠ engineering delta;
- infrastructure failure ≠ subject behavioral failure;
- bidirectional provenance/validation trace;
- retry/restart attempt lineage;
- explicit comparability/incomparability.

This is W7's first shared-constraint layer, not final policy.

## Portage

Head `d3e80fbefac4d081f9a93605905912b3a08a3a6a`.

First obligations cover EvaluationSubject identity, TaskContract identity, Trial vs Assessment, non-vacuous verifier evidence, fail-closed required artifacts, verifier identity, retry/attempt lineage, consumer export, comparability and upstream-delta justification.

High-risk mapping: inspected `VerifierResult` only carries optional rewards; exact candidate/task/verifier/evidence identity must come from another layer or is absent. Parser defects remain mapped to the non-vacuous evidence obligation.

## PhenoMLX

Head `f6aef0bcb3f1fa7a5793a9360f4b8140c6413ebd`.

First obligations cover exact RuntimeProfile, profile-scoped support/incompatibility, clean candidate-resolving installation, correct invocation, matched qualification, complete memory accounting, quality hard gates, lifecycle/cache isolation, bootstrap-before-custom, negative-result preservation and evidence-backed capacity/fit.

High-risk mapping: current launcher is a development integration over an external app/repository environment, not yet a self-identifying qualified RuntimeProfile. The web-port defect maps directly to invocation correctness.

## PhenoLab

Head `ca5211d7fe92c41f3ce999ecf9fb5a89ad67abae`.

First obligations cover typed SystemSubject, frozen Assignment, durable experiment/worker separation, feedback vs acceptance, actual policy invocation, fail-closed evidence, stale-result prevention, candidate identity, holdout partitioning, optimizer composition, multidimensional hard-gated comparison, durable promotion/rollback, negative learning artifacts and organization/topology interventions.

New mapping findings:
- `Trail.commit()` freezes transition addition but not metadata; TournamentRunner writes `trail.meta["output"]` after commit. Whole-trail immutability is therefore only partial.
- convenience `run_tournament(n=...)` does not forward n into TournamentRunner.
- TournamentRunner still bypasses `self.verifier`.
- scalar `final_score/cumulative_delta` cannot by itself represent the mature multi-objective/hard-gate comparison.

## Gate movement

W6 semantic decomposition: **STARTED, far from exhaustive**.
W7 shared invariants: **v0 established, unaccepted**.
High-risk implementation mapping: **started alongside obligations**.
No product has an accepted denominator or completion percentage.

Next:
1. expand obligations by ontology capability only where distinct semantics exist;
2. define first-class journeys and stage closure dependencies;
3. build trace rows obligation ↔ source ↔ implementation ↔ oracle/evidence;
4. attack the v0 ontologies/obligations for missing lifecycle/configuration cases before accepting them.
