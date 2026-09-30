# Pass 32 — caller inventory, persistence/API/UI mapping, statistical fixtures

Date 2026-09-30.

## Portage

Caller inventory `439273157781fa42a1a62b6e37cbc01ade4b016c`.

No in-repo caller was returned for portage-trial/portage_trial/portage_metrics by connector search, but this connector has known search blind spots. Direct source proves the package exists and the historical pheno-harness adapter targets Harbor task layout rather than portage-trial API.

Therefore portage-trial remains a REMOVE/ADAPT candidate, **not deletion-authorized**. Reliable local recursive caller inventory + publish history or explicit caller migration is required.

## PhenoMLX

Request/persistence map `17ef15520936f4dc25694c2cde88596508aaaaac`.

The generic Python BackendBase remains thin generate/is_available without durable request/profile state. KernelRegistry provides strong immutable extension evidence. Historical runtime envelopes provide strong file evidence. No general RuntimeProfile/SupportEnvelope store is established.

Important process control: unrelated AgilePlus SQLite/storage crates co-located in the repository are not automatically PhenoMLX storage. Co-location does not imply subsystem ownership.

## PhenoLab

Durable/API/UI map `e2a78cfdc21b13255de258503628aa6d9308fcad`.

Real current surfaces:
- append-only garden JSONL durable primitive;
- EvaluationReport interchange;
- static bench/suites web UI;
- Grafana/Prometheus cockpit and demo dashboards.

No mature dedicated experiment-management API was found. Existing UI is benchmark/ops observability, not Assignment→Candidate→Assessment→Decision UX.

Statistical policy fixtures `b718147ad11019ff464cab394f62610b5eed75c5` encode replicate completeness, uncertainty/no-forced-winner, practical equivalence and causal-attribution downgrade controls.

## Strict denominator

No source family moves to CLOSED:
- Portage caller/publish history incomplete.
- PhenoMLX generic profile persistence absent/open.
- PhenoLab API/UI mature journey mapping confirms gaps rather than closure.

Prior CLOSED fractions remain unchanged.

## Next
1. Portage: use GitHub package/release/history metadata to bound publish/caller authority where available.
2. PhenoMLX: formalize minimal append/versioned profile store contract for VS-01 rather than selecting a database prematurely.
3. PhenoLab: define mature experiment-management API/UI journey contract from baseline, explicitly distinct from existing dashboards.
4. continue native VS-01 gate.
