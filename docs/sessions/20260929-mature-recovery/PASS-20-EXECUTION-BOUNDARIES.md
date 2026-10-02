# Pass 20 — real execution-boundary bridges

Date 2026-09-30.

## CI receipts

Portage Python jobs for the prior persistence head completed failure at **Install dependencies** on Ubuntu and Windows; every test step was skipped. This is repeatable infrastructure/setup failure and still provides no oracle pass/fail.

PhenoLab CI/mutation jobs completed failure with no recorded steps, repeating its pre-execution runner/infrastructure problem.

No native green is inferred.

## Portage

TrialResult acceptance bridge `452285b5256d24c261fa24eebf83c51e60a2eb33`; mapping `1584951aa336f188183fa7fdb8cb645571db0312`.

Harbor TrialResult already supplies UUID, task ID/checksum, agent/model, verifier result, exception/timing/config. Portage envelope can project rather than duplicate.

New lifecycle insight: Harbor JobStats retry update removes previous aggregate contribution before adding new result. That is fine for latest statistics but cannot serve as canonical acceptance history. Portage must preserve Attempt/Assessment history separately while Harbor stats remain projection.

## PhenoMLX

Backend availability/version receipt `6dfa1e548f1a4ecf58317ebe82a3d0bc4798fd6c`; mapping `440028a7a9c16efbfd1a8079dfc72ae5b1743bbd`.

Real adapter availability/version can be captured as environment observation. Static BackendCapabilities remain source facts; availability/version remain environment facts; real profile qualification still requires workload evidence.

## PhenoLab

EvaluationReport→Assessment bridge `910bf6eb925f084668c72f5394dccb5d0d0e0245`; mapping `a2abcc6a6cf91dd48812c9536bdd049fa4b4ec2e`.

Major scope reduction: current EvaluationReport v0.5 canonicalization/evidence contract already provides producer head/dirty state, model revision, dataset provenance, synthetic/substitute flags, evidence labels and hash-chain semantics. Recovery bridge reuses real validate_evidence_label and only lets live-verified, non-synthetic, non-substitute evidence enter acceptance eligibility.

Therefore PhenoLab should not invent a second TrialEvidence interchange format. Typed Candidate/Assignment/Environment bindings wrap/reference EvaluationReport, then existing gates produce Assessment and promotion policy feeds Decision.

## Baseline outlook

Architecture is now well supported by:
- source archaeology;
- SOTA alternatives;
- semantic falsification;
- isolated identity tests;
- cross-object state machines;
- real class integration;
- persistence/restart;
- execution-boundary adapters.

But **candidate baseline is still blocked** by native/runtime architecture experiments, not semantic incoherence:
- Portage actual Harbor thin extension execution + package/existence/fork gates;
- PhenoMLX two real engines/common model + support/qualification evidence;
- PhenoLab real runner-generated EvaluationReport through typed Candidate→Assessment→Decision plus worker replacement and target bridge.

Next: assemble a formal candidate-baseline review packet with evidence dimensions and exact PASS/BLOCKED state, then continue the three remaining native verticals as far as available infrastructure permits.
