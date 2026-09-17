# Provisional repository-family map

## Status

This map routes the 146 repositories into investigation families. It is deliberately **not** the final target architecture.

A repository can eventually split across several targets or move families. The family lead must operate at capability/component level and preserve cross-family references.

## Immediate contradictions that override ordinary queue order

### FocalPoint / phenotype-apps

`phenotype-apps` currently presents itself as a substantial FocalPoint product and even uses an extraction-oriented default branch, while the current `FocalPoint` README describes “Phenotype-org dependency management.” This requires T4-level lineage recovery before either repo is treated as canonical.

### Planify / Planify2

Both repositories call the product Planify. `Planify` presents itself as an upstream Plane fork/candidate, while `Planify2` describes itself as the consolidated Plane fork. Compare ancestry, local patches, licenses, consumers, and release paths.

### Registry / specifications / enforcement

`phenotype-registry` declares an ecosystem index, but its own narrative says it is stale. `PhenoSpecs` declares cross-ecosystem ADR/spec authority and references an active `phenotype-org-governance` enforcement home that is not present under that exact active repository name in the current inventory.

### pheno shelf

`pheno` explicitly describes itself as a shelf containing independent repositories. Determine whether it should be a local workspace manifest, an operations/meta repo, or retired from public product framing.

### Execution family

`thegent`, `Agentora/agentkit`, `substrate`, `Tasken`, `Sidekick`, `PhenoProc`, and ShareCLI require semantic—not name-based—decomposition. Known role hypotheses should be tested, not discarded:

- thegent: labor/orchestration and agent execution.
- Agentora/agentkit: reusable framework/SDK.
- ShareCLI: OS-adjacent process and agent workload supervisor.
- Helios family: user clients and workbench surfaces.
- substrate/smaller runtimes: adapters or internal packages if no independent boundary remains.

## Families

## 01-governance-docs-registry-identity

**Initial semantic scope:** Repository/catalog authority, specs, conventions, documentation federation, design/identity, public portfolio projections.

**Primary adjudication question:** Resolve stale indexes, missing enforcement authority, central-vs-local spec ownership, and projection-versus-source distinctions.

**Repositories (14):** `.github`, `KooshaPari`, `pheno`, `phenoDesign`, `phenodocs`, `PhenoHandbook`, `PhenoSpecs`, `phenotype-landing`, `phenotype-registry`, `phenotype-traceability-spine`, `resume-all`, `zz-agslag-docs`, `zz-archive-phenotype-org-audits`, `zz-archive-phenotype-org-governance`

**Required first output:** capability union/intersection, authority conflicts, current/historical evidence coverage, consumer graph, and a proposed family disposition map.

## 02-enterprise-control-evidence-ledgers

**Initial semantic scope:** Strategy, governed delivery, agent labor, evidence, operational memory, research, repository and hardware ledgers.

**Primary adjudication question:** Recover AGSLAG authority, eliminate overlap among ledgers/Tracera, and preserve independent state ownership.

**Repositories (12):** `AgilePlus`, `Grapheon`, `hwLedger`, `Parpoura`, `RepoLedger`, `ResearchLedger`, `SessionLedger`, `thegent`, `Tracely`, `Tracera`, `zz-agslag`, `zz-agslag-dash`

**Required first output:** capability union/intersection, authority conflicts, current/historical evidence coverage, consumer graph, and a proposed family disposition map.

## 03-agent-runtime-orchestration-supervision

**Initial semantic scope:** Agent frameworks, labor orchestration, task/DAG runtimes, process supervision, execution adapters, quality harnesses.

**Primary adjudication question:** Separate SDK, labor control plane, OS-adjacent supervisor, provider adapter, and app-client responsibilities.

**Repositories (14):** `agentapi-plusplus`, `Agentora`, `context-mode-plusplus`, `no-mistakes`, `pheno-harness`, `PhenoCompose`, `PhenoProc`, `sharecli`, `Sidekick`, `substrate`, `substrate-adapters-bundle`, `Tasken`, `thegent-pr2-v2-uncommitted-2026-07-14`, `thegent-workspace`

**Required first output:** capability union/intersection, authority conflicts, current/historical evidence coverage, consumer graph, and a proposed family disposition map.

## 04-coding-agent-clients-workbenches

**Initial semantic scope:** Desktop and terminal coding-agent clients, headless automation, terminal/workbench forks, orchestration frontends.

**Primary adjudication question:** Validate distinct Helios roles, upstream lineage, and shared framework/runtime extraction.

**Repositories (7):** `cockpit`, `forgecode`, `ghostty`, `helios-cli`, `HeliosLab`, `portage`, `vibe-kanban`

**Required first output:** capability union/intersection, authority conflicts, current/historical evidence coverage, consumer graph, and a proposed family disposition map.

## 05-provider-routing-proxies-gateways

**Initial semantic scope:** LLM/provider routing, gateways, compatibility proxies, provider forks, monitoring and distribution.

**Primary adjudication question:** Determine one product authority, explicit fork/adapters, monitoring home, and protocol/performance differentiation.

**Repositories (13):** `bifrost`, `cliproxyapi-plusplus`, `homebrew-omniroute`, `OmniRoute`, `omniroute-rust`, `phenoAI`, `phenotype-gateway`, `phenotype-router`, `vibe-monitor`, `vibeproxy`, `vibeproxy-monitoring`, `vibeproxy-monitoring-unified`, `zz-archive-phenoRouterMonitor`

**Required first output:** capability union/intersection, authority conflicts, current/historical evidence coverage, consumer graph, and a proposed family disposition map.

## 06-mcp-frameworks-servers-clients

**Initial semantic scope:** MCP frameworks, server collections, mobile adapters, tooling and runtime integration.

**Primary adjudication question:** Separate framework, server implementations, routing/runtime, SDK, and app-specific adapter layers.

**Repositories (4):** `MCPForge`, `mobile-mcp`, `PhenoFastMCP`, `PhenoMCPServers`

**Required first output:** capability union/intersection, authority conflicts, current/historical evidence coverage, consumer graph, and a proposed family disposition map.

## 07-foundations-sdks-libraries-plugins

**Initial semantic scope:** Reusable libraries, protocols, config, auth, data, events, observability, plugins, SDKs, templates and utility fragments.

**Primary adjudication question:** Find real consumers, compress one-consumer fragments, avoid universal shared dumps, and preserve stable public contracts.

**Repositories (28):** `Apisync`, `argis-extensions`, `AuthKit`, `clap-ext`, `Configra`, `Conft`, `DataKit`, `Eventra`, `HexaKit`, `Logify`, `pheno-tracing`, `PhenoContracts`, `phenokits-commons`, `PhenoObservability`, `PhenoPlugins`, `phenotype-gfx`, `phenotype-go-kit`, `phenotype-go-sdk`, `phenotype-python-sdk`, `phenoUtils`, `PhenoVCS`, `Pine`, `PolicyStack`, `Quillr`, `ResilienceKit`, `rich-cli-kit`, `Stashly`, `Tokn`

**Required first output:** capability union/intersection, authority conflicts, current/historical evidence coverage, consumer graph, and a proposed family disposition map.

## 08-devtools-ops-deployment-platform

**Initial semantic scope:** Build/evaluation tooling, delivery/deployment products, infra, CI/actions, journeys, team communication and PM frontend.

**Primary adjudication question:** Separate user-facing products from internal ops, resolve Planify lineage, and consolidate reusable automation.

**Repositories (12):** `Benchora`, `BytePort`, `local-ops`, `PhenoDevOps`, `phenotype-infra`, `phenotype-infrakit`, `phenotype-journeys`, `phenotype-teamcomm`, `phenotype-tooling`, `phenotypeActions`, `Planify`, `Planify2`

**Required first output:** capability union/intersection, authority conflicts, current/historical evidence coverage, consumer graph, and a proposed family disposition map.

## 09-compute-inference-fleet-virtualization

**Initial semantic scope:** Hardware capacity, inference, model training/studio, quantization, virtualization, fleet/network and remote capacity.

**Primary adjudication question:** Define hwLedger/NVMS/fabric authority and distinguish product, runtime, fork, experiment and fleet operations.

**Repositories (10):** `hfscope`, `localbase3`, `model-conductor-hub`, `nanovms`, `NetWeave`, `phenotype-fleet-ops`, `phenotype-omlx`, `phenotype-unsloth-studio`, `rust`, `turboquant`

**Required first output:** capability union/intersection, authority conflicts, current/historical evidence coverage, consumer graph, and a proposed family disposition map.

## 10-applied-civic

**Initial semantic scope:** Civic knowledge/simulation/survival products.

**Primary adjudication question:** Clarify private/full versus public surfaces, shared domain core, independent product jobs and release boundaries.

**Repositories (2):** `CivicSurvival-public`, `Civis`

**Required first output:** capability union/intersection, authority conflicts, current/historical evidence coverage, consumer graph, and a proposed family disposition map.

## 11-applied-focus-productivity-mobile

**Initial semantic scope:** Focus/productivity, device/mobile control and related historical products.

**Primary adjudication question:** Resolve FocalPoint authority, extract product-specific mobile code from generic tooling, and validate real platform constraints.

**Repositories (7):** `eyetracker`, `FocalPoint`, `kmobile`, `mobile-cli`, `phenotype-apps`, `PlayCua`, `zz-RIP-Fitness-App`

**Required first output:** capability union/intersection, authority conflicts, current/historical evidence coverage, consumer graph, and a proposed family disposition map.

## 12-applied-worlds-games-graphics

**Initial semantic scope:** Game/world simulation, modding, graphics, sphere/terrain and related forks.

**Primary adjudication question:** Map common engines/assets, product/mod/plugin distinctions, licensing and independent user communities.

**Repositories (7):** `Compound-Spheres-3D`, `Dino`, `DINOForge-UnityDoorstop`, `Project-Spyn`, `QuadSGM`, `WorldSphereMod`, `zz-GDK`

**Required first output:** capability union/intersection, authority conflicts, current/historical evidence coverage, consumer graph, and a proposed family disposition map.

## 13-applied-creative-media

**Initial semantic scope:** Music/media/creative and historical generative experiments.

**Primary adjudication question:** Decide which are independent products, portfolio case studies, reusable engines, or archives.

**Repositories (5):** `Diffuse`, `Eidolon`, `Frostify`, `Melosviz`, `Synthia`

**Required first output:** capability union/intersection, authority conflicts, current/historical evidence coverage, consumer graph, and a proposed family disposition map.

## 14-legacy-archive-or-unknown-discovery

**Initial semantic scope:** Archived historical systems, named experiments, recovery snapshots, unclear small repos and prior brand generations.

**Primary adjudication question:** Recover intent and provenance, identify stranded capabilities, then tombstone, absorb, or retain as explicit labs/archives.

**Repositories (11):** `phench`, `phenoForge`, `phenoResearchEngine`, `zz-472-P2-Flame-War`, `zz-archive-phenoData`, `zz-archive-PhenoProject`, `zz-archive-PhenoRuntime`, `zz-archive-services`, `zz-atoms.tech`, `ZZ-AtomsBot`, `zz-KaskMan`

**Required first output:** capability union/intersection, authority conflicts, current/historical evidence coverage, consumer graph, and a proposed family disposition map.


## Cross-family relations to model

- A product may consume a foundation without belonging to the literal central ecosystem.
- A strategic fork may be operationally independent while semantically part of a product family.
- A documentation portal is a projection, not necessarily authority.
- A ledger may preserve independent durable state while sharing identifiers/events.
- A lab may graduate into a product or several packages.
- An app-specific component should not be generalized into a foundation without demonstrated second consumers.
- A package can move without the entire source repository moving to one target.

## Current → transition → target mapping form

Every component ultimately receives:

| Field | Meaning |
|---|---|
| Current owner | repo/ref/path |
| Current claim | what docs/manifests say |
| Observed capability | what static/executable evidence supports |
| Historical source | origin/extraction/fork lineage |
| Consumers | verified dependents |
| Target authority | proposed repo/path |
| Disposition | retain/absorb/split/etc. |
| Compatibility | API/package/config/data/URL plan |
| Migration wave | dependency-ordered work |
| Evidence gate | proof required before cutover |
| Source terminal state | active/fork/bridge/archive/retire |

The machine-readable map is `manifests/provisional-clusters.json`.
