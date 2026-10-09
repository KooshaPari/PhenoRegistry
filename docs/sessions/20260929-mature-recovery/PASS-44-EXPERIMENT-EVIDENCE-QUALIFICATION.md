# Pass 44 — experiment evidence qualification

Date 2026-09-30.

## DeepSea archaeology
Portage receipt `6aa4b55ec4cf5d2c3c196d31daae6b6cdd593617`.

Targeted conversation retrieval did not recover the alias. It found a conflicting older 2026-08-09 record saying the relevant peer fork was not named DeepSea in the then-available evidence. That record separately recovered upstream Harbor GKE changes Portage wanted merged: exec keepalive, no K8s service-account token, per-environment ApiClient, root pods, content-addressed tags, startup-env propagation and DinD Compose.

These deltas are **not attributed to DeepSea** without provenance. Exact peer identity remains unresolved.

## Portage EXP-P1 task ladder
Receipt `d401f27ca3a452d5c3e096e21e58f8d292638740`.

Use a conformance ladder rather than one easy task:
A. separate-verifier-environment — expected Apple Container capability rejection because no-network is unsupported; tests honest preflight.
B. sidecar-artifacts — Compose sidecar/service-scoped artifact/collect-hook probe; expected to expose multi-service/materialization debt.
C. meaningful positive task — verifier+artifact, Docker-pass, compatible Apple capabilities, unchanged semantics. Hello-world cannot be product proof.

EXP-P1 requires honest negative capability behavior **and** a positive semantic-equivalence run.

## PhenoLab EXP-L1 baseline
Receipt `0c0f02a6639a2ce1454a3b3b7529a00cea023423`.

Historical Qwen evidence is useful but cannot freeze target thresholds:
- run-v5 header says 10 suites×25 tasks, but summary n=1/ok=1/1 and only mmlu-pro appears in per-suite breakdown;
- qwen-stock-vs-pheno-metal contains many projected values and no end-to-end Metal result.

This is exactly the evidence-identity failure the recovery doctrine is meant to catch.

Qwen3.5-0.8B remains the preferred subject candidate, but EXP-L1 requires a fresh live end-to-end baseline before TargetCondition freeze.

## Program consequence
Do not optimize against attractive historical numbers whose population/evidence identity is inconsistent. Product experiments must pre-qualify their baseline just as candidates are qualified.

Next:
1. identify Portage P1-C positive task by capability filtering;
2. define fresh Qwen baseline-run contract;
3. select EXP-M1 target/draft only after backend capability check;
4. continue DeepSea via git history/remotes if connector surfaces permit.
