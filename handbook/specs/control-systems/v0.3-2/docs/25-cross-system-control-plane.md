# Cross-system control plane

These four workstreams should share primitives without collapsing their domain authorities.

| System | Canonical object | Scheduler/control concern | Evidence concern |
|---|---|---|---|
| BytePort/local cloud | desired deployment + observed target state | placement, lifecycle, resource budget | artifact/target/health/recovery receipt |
| Assessment | Assessment Dossier | applicability and measurement execution | qualified observations/verdicts |
| ResearchLedger corpus | source/claim record + bounded projection | research work packages | provenance, source revision, experiment evidence |
| Review control | normalized review finding + review run | provider quota/risk dispatch | finding adjudication/remediation receipt |

## Shared primitives to reuse

- stable subject/candidate identity;
- immutable or append/supersede evidence;
- plan versus apply separation;
- idempotency and leases;
- capability discovery instead of assumption;
- budgets as explicit policy objects (CPU/VRAM, money/credits, review quota, research scope);
- event streams and receipts;
- exact revision binding;
- unknown/blocked distinct from fail/pass;
- a human/agent/automation-neutral API surface.

The mistake to avoid is a "mega ledger" that owns all four domains. Share schemas and evidence conventions while keeping ResearchLedger, Assessment Dossiers, deployment state and review findings under their real owners.

## Priority order

1. **Authority recovery:** current owners, closed-unmerged research branch, historical BytePort contracts, review backlog identity.
2. **Control contracts:** local-node capabilities/QoS, review provider state, Assessment Dossier staging.
3. **One narrow executable slice each:** one disposable local service; one real assessment dossier; PR-81 salvage; one historical review backlog sample.
4. **Metrics and adaptation:** resource interference, provider yield/quota efficiency, assessment instrument quality, research experiment outcomes.
5. **Only then broaden coverage.**

This ordering intentionally attacks the contradictions first: we should not automate a control plane whose authority is ambiguous, score evidence before applicability is settled, restart research that already exists on an unmerged branch, or spray review calls before quotas are modeled.
