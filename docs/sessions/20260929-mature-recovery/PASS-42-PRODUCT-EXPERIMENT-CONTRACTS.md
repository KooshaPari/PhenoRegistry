# Pass 42 — corrected product experiment machine contracts

Date 2026-09-30.

## New experiment schemas

Portage portable TaskEnvironmentDefinition `ec17c5a4a3193ede151ceed3ac9492c6160a1273`.
It describes OS/ISA, materialization kind, services and required primitives without requiring Docker. Dockerfile/OCI/provider image are possible materializers, not the ontology.

PhenoMLX speculative qualification experiment `40808b14889c7868b31fb343fc191271210eb370`.
It binds exact target/draft/workload/baseline, predeclared expected acceptance/speedup/falsification, measurements and quality/practical-speedup acceptance.

PhenoLab intervention/progress `1e43445422f2f0926f246b838ae4a323dc836a07`.
It binds intervention layers/changes/expected effect plus multidimensional target position. Delta/velocity/confidence are nullable; insufficient observations must not manufacture slope/asymptote claims.

## Product-experiment traces

Portage `383f216689462a2ce70a6ac096e49ad757559b82`.
PhenoMLX `89daa7bf0b288628b16965e51dfb825b1bd3fe8a`.
PhenoLab `6cfff80858d4be806b3c9aec58e5b00444d870ca`.

Every vNext obligation now declares whether it is PRODUCT, INFRA, EXISTENCE or later-stage and the acceptable evidence class. This prevents old INFRA-01 receipts from satisfying restored product obligations.

## Key architecture movement

Portage: Harbor already has BaseEnvironment; EXP-P1 should attack TaskEnvironmentDefinition/materialization and missing native/non-Docker adapters first.

PhenoMLX: EXP-M1 is now pre-registered enough to prevent post-hoc success criteria for speculative qualification. The exact mechanism remains replaceable if research finds a better candidate.

PhenoLab: progress is target-relative rather than candidate-count-relative. A valid failed program can close EXP-L1 if it exhausts/stops correctly and preserves trustworthy negative learning.

## Next
1. add conformance/adversarial fixtures for the three new schemas;
2. recover DeepSea peer fork;
3. deepen Unsloth history/persistence/plugin falsification;
4. identify a concrete Portage benchmark suitable for EXP-P1;
5. identify a concrete PhenoLab model+harness+target suitable for EXP-L1 without choosing an artificially easy target.
