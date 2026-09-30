# Pass 28 — PhenoLab boundary correction propagated

Date 2026-09-30.

Direct user correction supersedes the false relationship introduced in Passes 14–27:

**Tracera is a product/feature graph + traceability product.**
**PhenoLab/PhenoLM is LLM-oriented experimentation/R&D.**
They have no normative product-authority/canonical-state relationship.

## Why the error happened

PhenoLab contains substantial real Tracera trace-store/dual-write integration. The recovery program incorrectly promoted implementation integration into product authority. This violated the program's own rule: implementation evidence is not automatically accepted intent.

## Corrected artifacts

PhenoLab boundary correction `688c739bd2ce4ffe3ded121ca1a50691edce7602`.
Registry correction `0f300c9ddd5dc77cdb2ffe84f1319d24fe28b07d`.
PhenoLab baseline v2 `5381d2f9c3c7fe262618f3bac6d5be3d8f33d8cc`.
VS-01 amendment `e95488f7150bd9e9d8915dbc7cdda664c7243a68`.
Normative supersession index `27059864d2fdc648f03749e644548cc854a63863`; registry copy `25826442be241b92b6be2540eedd5d83363b030a`.
Corrected v2 trace `d972102f6142b270f7f551540b7bd7c3a62b0df2`.
VS-02 fixtures `179025fe9b1548085a7db50e587e1f0c9093cc4b`.

## Correct semantics

PhenoLab owns experiment/R&D state through durable Decision/LearningArtifact.

External application is optional and generic. If an experiment applies an intervention, `TargetApplication(target_ref)` may refer to a repo/worktree, model/adaptation artifact, harness/runtime config, deployment, etc.

Tracera adapters remain optional telemetry/trace-store integrations only.

## Superseded prior conclusions

Any prior statement that:
- Tracera owns PhenoLab canonical product state,
- PromotionRecord bridges into Tracera by default,
- Tracera is a PhenoLab completion blocker,
- PhenoLab is subordinate to Tracera,
is invalid.

## Process finding

This is an important source-authority failure caught by direct user review. Future archaeology must explicitly distinguish **integration edge** from **product ownership/authority edge** in the relation type itself.

Add a general review control: no cross-repo integration may be promoted to normative ownership/authority without direct intent or accepted architecture evidence.
