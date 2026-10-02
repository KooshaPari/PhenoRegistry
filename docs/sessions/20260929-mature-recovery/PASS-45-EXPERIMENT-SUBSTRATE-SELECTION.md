# Pass 45 — experiment substrate selection

Date 2026-09-30.

## Portage P1-C
Receipt 692d7c36d5af99cec5540b9552fa11aded9d9c99.

Positive ladder:
- C0 reward-kit-example: nested programmatic grading, useful Apple Container smoke but not enough for product proof.
- C1 DeepSWE tomlkit table-converters: real pinned repository feature task. Current prebuilt ECR image may be x86-only, making it a strong multi-arch materialization stress case. It becomes positive proof only if the environment can be rebuilt/represented for arm64 without changing task/verifier semantics.

P1-A/B remain negative capability/materialization probes.

## PhenoLab fresh Qwen baseline
Receipt ba93eb99933745b8d0b8b16e56ab46d0c514ba54.

Target cannot freeze until a fresh baseline has exact model/tokenizer/harness/backend/hardware/workload identity, real population count, live evidence, appropriate repeats, quality and real streaming metrics. Header/manifest/per-task/aggregate population must agree.

## PhenoMLX EXP-M1 substrate
Receipt 0a2ca7fdc9e1fe2f7911fc5ebcb4fd3fa717dcf7.

PhenoLab already owns speculative experiment orchestration through specdec_trial.py, the current decode acceleration matrix, compatibility/quarantine policy and engine matrix. Do not duplicate this harness in PhenoMLX.

Typed relation:
- PhenoLab = target-driven experiment program/orchestration/evidence/learning.
- PhenoMLX = runtime mechanism implementation, realized state and low-level measurement/qualification.

No ownership relation.

First EXP-M1 can validate acceptance telemetry/prediction using n-gram/MTP/engine-native modes before requiring a new trained draft model. Exact target/draft pair remains gated on current compatibility and runnable artifacts.

## DeepSea
Conversation archaeology confirms the name remains unresolved/conflicting; no guessed repo. Recovered upstream GKE delta remains separately sourced.

## Next
1. inspect reward-kit and DeepSWE arm64 materialization feasibility more deeply;
2. machine-schema fresh Qwen baseline manifest;
3. map PhenoLab speculative trial outputs against EXP-M1 required measurements;
4. recover peer fork from git remotes/history if available;
5. runtime execution remains environment-dependent.
