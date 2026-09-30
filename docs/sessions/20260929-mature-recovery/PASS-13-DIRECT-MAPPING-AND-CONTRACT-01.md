# Pass 13 — direct structural mapping + mature contracts v0.1

Date 2026-09-30.

Recursive Git tree traversal corrected the connector-search blind spots and materially reduced speculative implementation scope.

## Portage

Direct tree/file reads confirm current Harbor-native trial/job/result/artifact/regrade/trajectory/viewer machinery.

Key corrections:
- TrialResult already binds UUID, task id/checksum, TrialConfig, AgentInfo/model/provider, verifier result/environment mode, exceptions/timing/steps.
- ArtifactManifestEntry explicitly records ok/failed/empty/skipped.
- Regrade preserves source trial, seeds recorded outputs/artifacts, requires separate verifier and fails when artifact coverage cannot be verified.
- JobStats distinguishes completed/errored/running/pending/cancelled/retries.

Therefore Portage should not rebuild these. Remaining thesis is a thin compound-subject + strict acceptance/evidence/authority/export layer over Harbor.

Mapping receipt `97d3b03fdf9bef3f837bb5353c5567a48588c9d1`.
Mature-contract v0.1 `cf87031d74a42da943da3a49dfcc18e2e40e829a`.

## PhenoMLX

Direct tree reveals actual backend interface, cockpit capacity/eval/assignment machinery, extensive perf-core runtimes/kernels and candidate-provenance/evaluation envelopes.

Corrections:
- backend adapter seam is implemented at basic generation level;
- capacity UI exists but is a params×dtype heuristic/default-24GiB hint, not qualified admission;
- cockpit EvaluationReport preserves useful evidence labels but derives UI OK from status/pass score and is not acceptance authority;
- historical candidate provenance is strong: exact head/artifact hashes, compile-only state, unknown device fingerprint, evidence_complete=false and blocked promotion are explicitly preserved.

Thus mature work should generalize the good provenance/profile discipline and constrain experimental breadth, not canonize every perf-core subsystem.

Mapping `c8af03a96b84689dbcf66ebb0858597484d285c5`.
Contract `9334b280a02100ad410bfac82cfa6ee4b1f7b350`.

## PhenoLab

Existing primitives reconcile cleanly into a thin typed identity/control spine rather than rewrite: dataset/manifests, Trail, BaseOptimizer, risky-action gate, garden gates, ledger, retention preview, promotion eligibility and reports.

Candidate CVP architecture is typed Assignment/SystemSubject/Candidate identities around an external/current runner, existing gates into a new independent Assessment, existing promotion eligibility into new durable Decision/PromotionRecord and append-only durable experiment state.

Mapping `39c30452ed5106084c81ca7ed3367904551af330`.
Contract `3740cfcc283d3370a3745572bf6f2139a0de1646`.

## Program consequence

All three now have coherent mature-contract v0.1 candidates. They are **not accepted/frozen**.

Next gate is an explicit contract review:
1. reconcile each v0.1 against all current obligations/journeys and identify omissions/contradictions;
2. run a second adversarial architecture interpretation attack against the consolidated contract;
3. resolve blocking ambiguities;
4. if it survives, promote ontology/contract to candidate baseline and continue exhaustive semantic decomposition/quality overlays;
5. native architecture experiments remain blockers before specification/design completion.

No implementation WPs or completion percentage yet.
