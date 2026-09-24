# Initial central decision queue

These are investigation decisions, not accepted outcomes.

## DEC-ECO-001 — What system owns live repository facts and what system owns curated ecosystem roles?

- **Status:** INVESTIGATING
- **Scope:** `RepoLedger`, `phenotype-registry`, `GitHub inventory`
- **Evidence required:** current implementation; write paths; consumers; generation workflows; conflict behavior
- **Provisional hypothesis:** RepoLedger/live observer owns GitHub facts; phenotype-registry owns curated roles and generated maps.

## DEC-ECO-002 — Where do product-local specs end and cross-product contracts begin?

- **Status:** INVESTIGATING
- **Scope:** `AgilePlus`, `PhenoSpecs`, `product repositories`, `phenotype-traceability-spine`
- **Evidence required:** current schemas; consumer workflows; duplicate documents; lifecycle authority
- **Provisional hypothesis:** Product-local intent/specs stay local and are lifecycle-managed by AgilePlus; cross-product contracts/RFCs remain central.

## DEC-ECO-003 — What is the active enforcement authority?

- **Status:** BLOCKED
- **Scope:** `.github`, `phenotypeActions`, `PhenoDevOps`, `phenotype-tooling`, `zz-archive-phenotype-org-governance`
- **Evidence required:** current workflows; policy sources; exceptions; consumers; historical migration
- **Provisional hypothesis:** One active policy owner plus reusable workflows/projections; archived references must be corrected.

## DEC-ECO-004 — Which repository is canonical for FocalPoint?

- **Status:** INVESTIGATING
- **Scope:** `FocalPoint`, `phenotype-apps`, `zz-RIP-Fitness-App`, `eyetracker`
- **Evidence required:** intent lineage; branch ancestry; capability matrix; build/release reproduction; consumers
- **Provisional hypothesis:** Undecided; requires T4 forensic recovery.

## DEC-ECO-005 — Which repository is canonical for Planify and how should the Plane fork be maintained?

- **Status:** INVESTIGATING
- **Scope:** `Planify`, `Planify2`, `AgilePlus`
- **Evidence required:** upstream bases; local patch sets; license; consumers; release/deploy paths
- **Provisional hypothesis:** One strategic fork target; other becomes provenance/redirect after migration.

## DEC-ECO-006 — What is the current role of pheno?

- **Status:** INVESTIGATING
- **Scope:** `pheno`, `local workspace tooling`, `phenotype-registry`
- **Evidence required:** actual tracked tree; consumer workflows; local shelf use; public product claims
- **Provisional hypothesis:** Meta/workspace manifest or retire; not a generic product authority.

## DEC-ECO-007 — What is the canonical strategy/capital authority after archived AGSLAG generations?

- **Status:** INVESTIGATING
- **Scope:** `zz-agslag`, `zz-agslag-dash`, `zz-agslag-docs`, `Parpoura`, `AgilePlus`, `RepoLedger`, `hwLedger`
- **Evidence required:** human intent; accepted architecture; historical code/docs; current consumers
- **Provisional hypothesis:** Restore/create an explicit AGSLAG authority or publish a formal supersession.

## DEC-ECO-008 — How should the agent execution family be layered?

- **Status:** INVESTIGATING
- **Scope:** `thegent`, `Agentora`, `substrate`, `Tasken`, `Sidekick`, `PhenoProc`, `sharecli`, `agentapi-plusplus`
- **Evidence required:** capability union; consumers; pilots; co-change; runtime boundaries; history
- **Provisional hypothesis:** thegent labor/orchestration; Agentora SDK if justified; ShareCLI independent supervisor; others absorb or narrow.

## DEC-ECO-009 — How should the Helios app/CLI/framework family be partitioned?

- **Status:** INVESTIGATING
- **Scope:** `HeliosLab`, `forgecode`, `helios-cli`, `Agentora`, `ghostty`
- **Evidence required:** historical consolidation branch; user journeys; upstream lineage; shared code; pilots
- **Provisional hypothesis:** Desktop workbench, terminal CLI, headless harness, reusable framework can remain distinct only if contracts are enforced.

## DEC-ECO-010 — What is the minimal coherent provider routing/gateway/fork topology?

- **Status:** INVESTIGATING
- **Scope:** `OmniRoute`, `bifrost`, `cliproxyapi-plusplus`, `vibeproxy`, `phenotype-router`, `phenotype-gateway`, `phenoAI`
- **Evidence required:** upstreams; protocols; original patches; consumers; performance/reliability pilot
- **Provisional hypothesis:** One product-facing router plus explicit upstream-derived adapters/forks and one observability home.

## DEC-ECO-011 — Which tiny/generic foundations deserve independent repositories?

- **Status:** INVESTIGATING
- **Scope:** `Configra`, `Logify`, `phenoUtils`, `PhenoContracts`, `HexaKit`, `phenokits-commons`, `PhenoVCS`, `SDKs`, `Kits`
- **Evidence required:** real consumers; release histories; co-change; API stability; license/security boundaries
- **Provisional hypothesis:** Compress into a small number of package homes; retain only stable multi-consumer contracts.

## DEC-ECO-012 — What repository boundaries implement the distributed compute/data/I-O fabric vision?

- **Status:** PROPOSED
- **Scope:** `hwLedger`, `sharecli`, `nanovms`, `NetWeave`, `phenotype-fleet-ops`, `localbase3`, `future fabric`
- **Evidence required:** existing implementations; consumer map; SOTA; prototype experiments; real-time/scale requirements
- **Provisional hypothesis:** New product/runtime repo may be justified, with existing repos providing adapters/ledgers rather than absorbing the whole vision.

