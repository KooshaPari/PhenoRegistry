# Pass 34 — machine store/UI contracts + Portage semantic fork delta

Date 2026-09-30.

## PhenoMLX
Profile-store event schema `f366251532738b5f62929d0a7744e1854ee27318`.

Machine schema now encodes immutable Profile, append Qualification, append/supersede Support and time-scoped Capacity events. This operationalizes the storage-neutral contract without choosing a database.

## PhenoLab
Experiment resource envelope schema `48b517a0a9043df963656bd9ca1093fa40d28989`.
Current journey map `ac18d67a03d73a201793d837228796eecfb52a8a`.

None of UJ-01..09 is fully closed today. Current strongest surfaces are EvaluationReport/evidence, garden ledger, comparison/reporting and dashboards. Missing mature surfaces are unified experiment creation, candidate review, typed Assessment review, Decision authorization, complete resume and semantic negative-learning retrieval.

This confirms the next UI work should compose existing evidence/ops surfaces rather than replace them.

## Portage
Semantic fork delta `98021f1294e027d32c0ce92862b24f3a667edf3d`.

Preserved upstream-diff evidence measured a huge fork (488 commits ahead, 3,717 files, ~369k insertions). Mature-first classification now separates:
- KEEP: subject/evidence compatibility semantics and still-real adapters;
- UPSTREAM/REUSE: generic Harbor execution/environment/agent/reward/viewer features;
- ADAPTER: benchmark/harness/provider shape conversion;
- HISTORICAL: plans/scratch/co-located unrelated scorecards/parallel generic execution;
- REMOVE-CANDIDATE: dead duplicates, scratch/archive, superseded generic execution subject to caller/publication check.

Critical correction: **fork change volume is not product identity**. The old statement that Portage's identity is agent/environment extension reflected file-count divergence, not accepted mature differentiation.

## Source denominator
No family is promoted CLOSED yet:
- PhenoMLX schema is future contract, not current store implementation.
- PhenoLab current journey map proves gaps.
- Portage fork delta still needs current caller/use relevance and package publication.

Next:
1. schema/oracle tests for the new PhenoMLX store events;
2. machine UJ trace and minimal CVP interaction contract for PhenoLab;
3. current Portage delta/caller classification of major adapter families;
4. native VS-01 evidence remains decisive.
