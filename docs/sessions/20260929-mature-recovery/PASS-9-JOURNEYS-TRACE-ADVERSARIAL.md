# Pass 9 — journeys, stage projections, trace matrices and adversarial contract review

Date 2026-09-30.

This pass deliberately does more than add requirements. It tests whether the current semantic models can explain complete actor outcomes and hostile lifecycle/configuration cases.

## Portage

Journey/stage head: `949b63ed753c8a633d1161abbd1f0c0a298a9f8f`.
Trace head: `6f1c73db4a5aa70a29cdf872fba3d24e1950eeca`.
Adversarial-review head: `3156adb08112e8e8e9e62d4af25c7af889af4b01`.

Ten mature journeys now cover qualified install/profile, task import, subject declaration, execute/assess, failure diagnosis, evidence inspection, regrade, comparison, recovery and stable export. CVP requires one real benchmark family with pass/fail/invalid evidence through the mature identity spine.

Current shape finding: the highest-risk incomplete chain is **EvaluationSubject → Trial → Assessment → EvidenceEnvelope → ConsumerExport**. This is why raw parser/test progress cannot establish a usable product.

Adversarial review exposed distinct semantic candidates around dataset membership revision, criterion-level assessment/aggregation, human adjudication supersession, and evidence payload retention/redaction.

## PhenoMLX

Journey/stage head: `fa53c3fb6347df23b0104dc634ec3b9e34a03e5f`.
Trace head: `8ca98cc1fe4e961d0e1e8ca05f0610ad0dc1713b`.
Adversarial-review head: `77da21e6016a9a8b6bfa7071ca81f54f8673653b`.

Twelve mature journeys now cover candidate install, profile discovery, launch, inference, identity/resources, cancel, unload, restart, qualification, extension comparison, update/rollback and evidence export. CVP explicitly requires lifecycle closure and a negative/unsupported profile; custom kernel is not required.

Current shape finding: **RuntimeProfile → RuntimeInstance → request/resource state → QualificationAssessment** is not yet a coherent durable identity chain.

Adversarial review exposed realized/effective configuration, distributed deployment topology, external cache connectors, cache isolation domain, quantization calibration/draft-model lineage and operating-condition scope as distinct semantic additions.

## PhenoLab / PhenoLM

Journey/stage head: `e78c543554aa07777ae4a822bd49001af5afe396`.
Trace head: `f3a09450208256b8bff26cc063e1c5109d862a8d`.
Adversarial-review head: `dba4eede0443bd0c630e4fa9f220bdb6fc0ab100`.

Fifteen mature journeys now cover subject registration, assignment/baseline, data/trace versioning, optimizer selection, candidate proposal, execution, feedback, independent assessment, comparison, decision/promotion, rollback, worker replacement, learning-artifact mining, organization optimization and model adaptation.

Existing `promotion_decision` is useful: two consecutive green windows + explicit human approval + non-mutating eligibility. But it is only a partial L-J10 primitive because it does not itself bind candidate/evidence/policy or create a durable PromotionRecord.

Current shape finding: **SystemSubject → Candidate → Trial → independent Assessment → Comparison → Decision/PromotionRecord** is not represented as one coherent identity chain.

Adversarial review added important semantics: replacement comparison vs causal attribution, candidate lineage/protected surfaces, partition contamination/rotation, conflicting assessments, post-promotion observation/demotion, explicit feedback-only runs, oscillation metrics only over comparable observations, and training-artifact lineage.

## Stage-position consequence

No product currently qualifies even for its proposed CVP. This is a journey-closure statement, not a percentage:
- Portage has meaningful runner/verifier primitives but lacks the complete accepted evidence identity/export chain and native invalid-evidence witness execution.
- PhenoMLX has extensive research/runtime pieces but lacks a qualified install/profile/lifecycle/evidence vertical witness.
- PhenoLab has rich benchmark/garden primitives but lacks the durable candidate/independent-assessment/promotion spine and currently contains direct false-green authority defects.

## Gate movement

W8 journeys: **v0 established**.
Stage projections: **v0 established, unaccepted**.
Bidirectional trace: **targeted v0, not comprehensive**.
Adversarial semantic review: **first pass completed; it found valid missing semantics, so ontology/obligation freeze remains OPEN**.

Next execution should promote/reconcile the valid adversarial candidates, deepen implementation mapping around the three missing identity chains, and design the first vertical witness contracts. Requirement expansion follows those semantics rather than a quota.