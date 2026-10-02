# Pass 10 — semantic falsification

Date 2026-09-30.

The explicit adversarial review succeeded in falsifying all three v0 ontologies. They are preserved as historical drafts; each repo now has ONTOLOGY-V1 with valid counterexamples incorporated.

## Portage

Valid missing dimensions: authorization/principals; secret/evidence retention/redaction/disposal; duplicate/out-of-order result delivery; immutable external dependency identity; criterion-level/partial assessment; cancellation-vs-late-evidence race; imported external observations.

v1 adds Principal, AuthorityGrant, EvidenceLifecyclePolicy, DeliveryEvent, DependencySet, CriterionAssessment and ImportedObservation plus terminal/idempotency rules.

Falsification commit `dbaa89b136a44dc15a99104a738ef2b61441e366`; v1 `1762ba58bcc77a304e79d2c50dfc06bc3f20b2b8`.

## PhenoMLX

Valid missing dimensions: distributed placement/topology; requested-vs-realized fallback; remote/disaggregated cache identity and tenant isolation; rolling/hot-swap runtime generations; partial streams; instantaneous admission vs general support; thermal/power operating state; support deprecation; remote-provider observability limits.

v1 adds DeploymentTopology, PlacementPlan, RequestedProfile, RealizedProfile, StateStore, CacheDomain, RuntimeGeneration, StreamArtifact/terminal states, CapacitySnapshot, AdmissionDecision, OperatingState, support lifecycle and ObservabilityLevel.

Falsification `fe8006690d118f3fdb85405b132c2530cd247ab3`; v1 `e6138c5d7cd62c3a968fcbcb2332146258445bcb`.

## PhenoLab

Valid missing dimensions: concurrent candidate/rebase lineage; assignment-policy epochs; adaptive holdout leakage through repeated feedback; provider/environment drift; replacement win vs causal attribution; pre-evaluation optimizer capability safety; post-promotion evidence aging/regression; rollback dependency viability; authorized human override semantics; declared vs realized dynamic organizations; imported/federated experiments; replicate/uncertainty semantics.

v1 adds CandidateLineage, AssignmentEpoch, EvaluatorRole, AcceptanceQueryBudget, EnvironmentEpoch, OptimizerCapabilityPolicy, ReplicateSet, CausalAttribution, ObservationWindow, richer RollbackPlan, Declared/RealizedOrganization and ImportedExperiment.

Falsification `cf22c986657cfbe600f3959af60c063c4cb6105f`; v1 `1bcaf013dd965858463dd2d706dd1d58fa7003e7`.

## Consequence

The program must now derive obligations for these new semantic dimensions and update journeys/trace matrices. The falsification gate is **working**: v0 was not defended merely because substantial documentation already existed.

This is not the final independent/fresh review; it is same-program adversarial review. Final completion still requires a genuinely fresh reviewer to attack the later accepted candidate.

No completion percentage or ontology freeze yet.
