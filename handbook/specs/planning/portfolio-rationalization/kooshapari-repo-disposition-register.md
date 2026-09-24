# KooshaPari Repository Disposition Register

> **Status:** forensic audit pass 1 complete 2026-09-12. No irreversible action is authorized by this file alone.
> **Last updated:** 2026-09-12T23:08 PST

- Inventory: **146/146 owner repositories**
- GitHub metadata: **112 public**, **34 private**, **29 archived**, **117 not archived**
- Evidence: **108 E1 root-document reviews**, **19 E2 full forensic audits**, **38 E0 metadata-only hypotheses**
- Forensic disposition: **16 DELETE confirmed**, **3 HOLD pending resolution**, **0 already deleted**
- Recommended control surface: **63 managed**, **15 incubator/hold**, **13 frozen references**, **55 retire after gate**. The active agent-owned set is therefore **78**, not 146.

## Evidence legend

- **E0:** GitHub metadata/name/lifecycle only.
- **E1:** root documentation and declared role inspected.
- **E2:** code inventory, history, branches/tags, provenance, dependencies, consumers inspected.
- **E3:** clean build/test/lint/security/release verification reproduced.
- **E4:** controlled pilot against alternatives reproduced.
- **E5:** adoption/production/operational evidence.

## Forensic audit columns

- **Forensic Target:** where verified content should land after deletion.
- **Forensic Status:** Verified = E2 complete; Pending = investigation incomplete.
- **Commits:** total commit count at audit time.
- **Forensic Notes:** risk level, migration notes, special conditions.

## Register

| # | Repository | Visibility | GH archived | Evidence | Family | Provisional recommendation | Target / authority | Confidence | Forensic Target | Forensic Status | Commits | Forensic Notes | First bounded task |
|---:|---|---|:---:|---|---|---|---|---|---|---|---:|---|---|
| 1 | `.github` | public | yes | E0-metadata-name | portfolio-governance | **absorb_then_archive** | KooshaPari profile + phenotype-fleet-ops | high | | | | | Inventory account-level templates; migrate only live profile/community/workflow assets; leave tombstone. |
| 2 | `agentapi-plusplus` | public | no | E1-root-docs | routing-provider | **absorb_then_archive** | substrate | high | | | | | Prove adapter/API parity and preserve upstream provenance before freezing this donor. |
| 3 | `Agentora` | public | no | E1-root-docs | agent-runtime | **canonical** | Agentora | high | | | | | Finish role charter, compatibility matrix, one Codex-class pilot, and measured framework comparison. |
| 4 | `AgilePlus` | public | no | E1-root-docs | delivery-control | **canonical_reset** | AgilePlus | high | | | | | Remove foreign DINO/shelf material; rebuild work-authority spec and executable traceability from evidence. |
| 5 | `Apisync` | public | no | **E2-forensic** | sdk-shared | **delete_confirmed** | phenotype-registry | high | phenotype-registry | Verified | | Absorbed, source preserved; published crate v0.2.10 retained | Choose the released Rust API toolkit identity; delete the contradictory API-sync/npm product fiction after history audit. |
| 6 | `argis-extensions` | public | no | E1-root-docs | routing-provider | **incubator** | argis-extensions | medium | phenotype-tooling | **HOLD** | | 144 unmerged branches; preserving SLO code; 495MB | Demonstrate a maintained Bifrost extension delta, one deployment journey, and two real consumers or absorb into substrate. |
| 7 | `AuthKit` | public | no | E1-root-docs | security-auth | **incubator** | AuthKit | medium | | | | | Resolve license, threat model, package identity, and two-consumer proof; otherwise absorb facades into domain owners. |
| 8 | `Benchora` | public | no | E1-root-docs | evidence-quality | **canonical** | Benchora | high | | | | | Use as the portfolio benchmark authority; add comparator schemas, immutable result bundles, and Tracera export. |
| 9 | `bifrost` | public | no | E1-root-docs | routing-provider | **upstream_reference** | bifrost | high | | | | | Add UPSTREAM/DELTA/SYNC/EXIT files; no first-party product claims without owned divergence evidence. |
| 10 | `BytePort` | public | no | E2-source-code | infra-product | **canonical** | BytePort | high | | | | | Full source-code audit: 387 commits, 61+ tests, 28 CI, 15 ADRs, PRD, SPEC. Consumer of NanoVMS via HTTP API. Score: 35/60. |
| 11 | `CivicSurvival-public` | public | no | E1-root-docs | product-game | **canonical** | CivicSurvival-public | high | | | | | Preserve public-client/closed-server boundary; add release evidence and player case-study metrics without fake buildability. |
| 12 | `Civis` | public | no | E1-root-docs | product-game | **canonical_reset** | Civis | high | | | | | Replace percent claims with reproducible game-loop evidence; reconcile 39-member scope and complete one playable vertical slice. |
| 13 | `clap-ext` | public | yes | **E2-forensic** | historical | **delete_confirmed** | phenotype-tooling | high | phenotype-tooling | Verified | 70 | Verified, absorbed | Verify tombstone/provenance and remove from actionable dashboards. |
| 14 | `cliproxyapi-plusplus` | public | no | E1-root-docs | routing-provider | **canonical_fork** | cliproxyapi-plusplus | high | | | | | Formalize owned deltas, upstream sync cadence, compatibility suite, and subscription-proxy benchmark. |
| 15 | `cockpit` | private | no | E1-root-docs | private-ops | **private_ops** | cockpit | high | | | | | Keep source-only; make RepoLedger its only state source and prohibit generated/runtime state in Git. |
| 16 | `Compound-Spheres-3D` | public | no | E1-root-docs | graphics-game | **canonical_fork** | Compound-Spheres-3D | high | | | | | Keep narrow WSM3D dependency boundary; automate upstream divergence and WorldSphere integration verification. |
| 17 | `Configra` | public | no | E1-root-docs | sdk-shared | **canonical** | Configra | high | | | | | Publish stable configuration contracts and prove adoption across at least two products. |
| 18 | `Conft` | public | yes | **E2-forensic** | historical | **delete_confirmed** | Configra | high | Configra | Verified | 166 | Low risk; self-tombstoned | Confirm no unique consumers; retain history only. |
| 19 | `context-mode-plusplus` | public | no | E0-metadata-name | agent-runtime | **upstream_reference** | context-mode-plusplus | medium | | | | | Document upstream pin and actual delta; upstream or archive if no material maintained difference. |
| 20 | `DataKit` | public | no | **E2-forensic** | sdk-shared | **hold** | phenotype-python-sdk | high | phenotype-python-sdk | **HOLD** | | ETL NOT in target; 877 lines on unmerged branch; recovering | Follow its own deprecation decision; verify no consumers and preserve migration map. |
| 21 | `Diffuse` | private | yes | E0-metadata-name | historical | **archive_normalize** | Diffuse | high | | | | | Retain history only; no active-agent ownership. |
| 22 | `Dino` | public | no | E1-root-docs | product-game | **canonical** | Dino | high | | | | | Treat DINOForge as a flagship platform; independently reproduce packages, installer, tests, and one live mod journey. |
| 23 | `DINOForge-UnityDoorstop` | public | no | E1-root-docs | product-game | **upstream_reference** | Dino dependency pin | high | | | | | Record exact upstream pin/license and consume as dependency; do not market unchanged upstream code as first-party. |
| 24 | `Eidolon` | private | no | E1-root-docs | device-automation | **canonical** | Eidolon | high | | | | | Make device/sandbox contract authoritative; reconcile extraction satellites and prove desktop+mobile+isolation journeys. |
| 25 | `Eventra` | public | no | E1-root-docs | events-state | **forensic_hold** | Eventra or restored phenoEvents | high | | | | | Do not archive into a nonexistent successor; locate parity, consumers, releases, and choose one real event-bus authority. |
| 26 | `eyetracker` | public | yes | E0-metadata-name | historical | **archive_normalize** | Eidolon research history | medium | | | | | Preserve useful experiments under Eidolon research/provenance; remove from actionable set. |
| 27 | `FocalPoint` | public | no | E1-root-docs | product-app | **forensic_hold** | one of FocalPoint / phenotype-apps | high | | | | | Recover branches and product history; select one canonical screen-time/dependency identity and redirect the loser. |
| 28 | `forgecode` | public | no | E1-root-docs | agent-cli | **canonical_lineage** | forgecode | high | | | | | Keep headless/performance lineage separate; benchmark against helios-cli before any convergence. |
| 29 | `Frostify` | public | no | E1-root-docs | historical-showcase | **historical_showcase** | Frostify | high | | | | | Keep visibly archived as a proven historical release; correct obsolete install links and preserve download evidence. |
| 30 | `ghostty` | public | no | E0-metadata-name | agent-workbench | **upstream_reference** | HeliosLab dependency/reference | medium | | | | | Document whether any maintained terminal delta exists; otherwise track upstream rather than operate a product fork. |
| 31 | `Grapheon` | private | no | E1-root-docs | trace-knowledge | **forensic_hold** | Grapheon or Tracera module | high | | | | | Prove an independent generic claim/provenance graph job and consumers; otherwise absorb into Tracera. |
| 32 | `helios-cli` | public | no | E1-root-docs | agent-cli | **canonical_lineage** | helios-cli | high | | | | | Keep UX-leading interactive lineage; produce shared task corpus and compatibility matrix with forgecode. |
| 33 | `HeliosLab` | public | no | E1-root-docs | agent-workbench | **canonical_reset** | HeliosLab | high | | | | | Replace configuration-workspace README with the human-approved desktop coding-workbench charter and executable prototype journey. |
| 34 | `HexaKit` | public | no | **E2-forensic** | sdk-shared | **delete_confirmed** | phenotype-registry | high | phenotype-registry | Verified | 727 | Monorepo branch merged | Extract domain crates to owners; retain only generators, project templates, schema validation, and migration tooling. |
| 35 | `hfscope` | private | no | E1-root-docs | ml-research | **forensic_quarantine** | hfscope or ResearchLedger | high | | | | | Time-box a code/history audit; either prove a usable model-analysis tool or archive its fragments into research history. |
| 36 | `homebrew-omniroute` | public | no | E0-metadata-name | routing-provider | **generated_surface** | OmniRoute release pipeline | medium | | | | | Generate formula from signed OmniRoute releases; archive if OmniRoute has no surviving release boundary. |
| 37 | `hwLedger` | public | no | E1-root-docs | asset-ledger | **canonical** | hwLedger | high | | | | | Resolve conflict with phenotype-omlx; keep hardware/fleet/capacity authority and export evidence to Tracera. |
| 38 | `kmobile` | private | no | E1-root-docs | device-automation | **absorb_then_archive** | Eidolon | high | | | | | Run shared mobile fixture corpus; migrate unique Rust capabilities to Eidolon, retain provenance, then freeze. |
| 39 | `KooshaPari` | public | no | E0-metadata-name | portfolio-brand | **canonical** | KooshaPari | high | | | | | Use as profile/portfolio front door generated from RepoLedger; no duplicate hand-maintained project truth. |
| 40 | `local-ops` | private | no | E1-root-docs | private-ops | **private_ops** | local-ops | high | | | | | Keep non-secret local automation sources; add executable inventory and disaster-recovery checks. |
| 41 | `localbase3` | public | no | E1-root-docs | marketplace-lab | **incubator** | localbase3 | medium | | | | | 60-day proof gate: one real provider, one buyer flow, settlement threat model, and deployable vertical slice or archive. |
| 42 | `Logify` | public | no | **E2-forensic** | observability | **hold** | PhenoObservability/logkit | high | PhenoObservability/logkit | **HOLD** | | Cherry-picking 9 fixes; target exists as repo not org | Verify byte/API parity and consumers, then enforce the already-declared absorption. |
| 43 | `MCPForge` | public | no | E1-root-docs | mcp | **conditional_canonical** | MCPForge | medium | | | | | Prove LSP-to-MCP delta, protocol-2026-07-28 compliance, interop tests, and at least one consumer. |
| 44 | `Melosviz` | public | no | E1-root-docs | product-app | **canonical** | Melosviz | high | | | | | Complete one local audio-to-visual live-performance journey, packaging, latency benchmark, and comparative case study. |
| 45 | `mobile-cli` | public | no | E1-root-docs | device-automation | **upstream_reference** | Eidolon comparison fixture | high | | | | | Pin upstream and use as comparator; migrate only uniquely valuable behavior after measured parity. |
| 46 | `mobile-mcp` | public | no | E1-root-docs | device-automation | **upstream_reference** | Eidolon comparison fixture | high | | | | | Pin upstream and use for MCP parity/security tests; avoid a parallel first-party roadmap. |
| 47 | `model-conductor-hub` | private | yes | E0-metadata-name | historical | **archive_normalize** | ResearchLedger history | high | | | | | Preserve model-routing research only; remove active ownership. |
| 48 | `nanovms` | public | no | E2-source-code | infra-runtime | **canonical** | nanovms or Eidolon sandbox runtime | high | | | | | Full forensic audit: 345 commits, 28 tiers (30 registered), 83 test files, 7 CI. Lifecycle pilot verified. Score: 39/60. |
| 49 | `NetWeave` | private | no | E1-root-docs | network-lab | **conditional_canonical** | NetWeave | medium | | | | | Prove a repeatable traffic-simulation workload, benchmark, package, and at least one internal consumer. |
| 50 | `no-mistakes` | public | no | E1-root-docs | upstream-contribution | **upstream_reference** | upstream kunchenguid/no-mistakes | high | | | | | Keep fork for contribution/experimentation; document only Koosha-authored delta and upstream PR status. |
| 51 | `OmniRoute` | public | no | E1-root-docs | routing-provider | **canonical_reset** | OmniRoute | high | | | | | Separate owned router product from upstream/vendor code; add DELTA, deterministic route tests, cost/latency/quality pilot. |
| 52 | `omniroute-rust` | private | yes | E0-metadata-name | historical | **archive_normalize** | OmniRoute history | high | | | | | Retain migration history only. |
| 53 | `Parpoura` | private | no | E1-root-docs | planning-history | **absorb_then_archive** | AgilePlus + ResearchLedger | high | | | | | Honor strict pause; migrate unique venture/spec research with provenance, then archive cleanly. |
| 54 | `phench` | private | no | E1-root-docs | portfolio-runtime | **conditional_canonical** | phench | medium | | | | | Prove project materialization/locking/sync as a narrow control plane; integrate RepoLedger rather than duplicate it. |
| 55 | `pheno` | public | no | E1-root-docs | portfolio-governance | **absorb_then_archive** | RepoLedger + local workspace config | high | | | | | Retire repo-of-repos shelf authority; preserve only local materialization manifests and history. |
| 56 | `pheno-harness` | private | no | E1-root-docs | evaluation-runtime | **decompose_and_narrow** | Benchora + OmniRoute + turboquant + ResearchLedger | high | | | | | Split benchmark authority, router configs, kernel research, and local serving; retain only a coherent operator testbed if needed. |
| 57 | `pheno-tracing` | public | no | E1-root-docs | observability | **absorb_then_archive** | PhenoObservability | high | | | | | Consolidate the trace port into the instrumentation owner unless independent package adoption is proven. |
| 58 | `phenoAI` | public | no | E1-root-docs | ml-research | **decompose_and_narrow** | ResearchLedger + turboquant + phenotype-omlx | high | | | | | Classify every artifact; move durable research/model work to specific owners and retire the generic AI umbrella. |
| 59 | `PhenoCompose` | public | no | E2-source-code | infra-runtime | **absorbed** | NanoVMS (absorbed) | high | | | | | Absorbed into NanoVMS. First commit: "unified NVMS with PhenoCompose integration". Bridge at integrations/pheno-compose/. No standalone action needed. |
| 60 | `PhenoContracts` | public | no | E1-root-docs | formal-verification | **conditional_canonical** | PhenoContracts | medium | | | | | Demonstrate real Kani/Prusti/Coq backends, package releases, and two consumers; otherwise move schemas to PhenoSpecs. |
| 61 | `phenoDesign` | public | no | E1-root-docs | historical | **archive_normalize** | product-local design systems / PhenoHandbook | high | | | | | Apply its declared archive state and preserve migration pointers. |
| 62 | `PhenoDevOps` | public | no | **E2-forensic** | portfolio-governance | **delete_confirmed** | phenotype-tooling | high | phenotype-tooling | Verified | 530 | | Dismantle the repo shelf; migrate only live shared operations or catalog metadata. |
| 63 | `phenodocs` | public | no | E1-root-docs | documentation | **generated_surface** | phenodocs | high | | | | | Keep as rendered federation only; generate navigation/status from RepoLedger and source docs from owners. |
| 64 | `PhenoFastMCP` | public | no | E1-root-docs | mcp | **upstream_reference** | PhenoFastMCP | high | | | | | Prove maintained framework delta against upstream FastMCP and current MCP spec or freeze as reference. |
| 65 | `phenoForge` | public | no | E1-root-docs | task-process | **absorb_then_archive** | Tasken | high | | | | | Verify Tasken contains every unique task-runner contract/benchmark; then enforce the recorded absorption. |
| 66 | `PhenoHandbook` | public | no | **E2-forensic** | documentation | **delete_confirmed** | phenotype-registry | high | phenotype-registry | Verified | 251 | Low risk | Own conventions/patterns only; eliminate project status and contract authority from the handbook. |
| 67 | `phenokits-commons` | public | no | E1-root-docs | sdk-shared | **decompose_and_archive** | domain owners | high | | | | | Recover concatenated Python/Go/utils/infra histories into correct owners; this cannot remain an authority. |
| 68 | `PhenoMCPServers` | public | no | E1-root-docs | mcp | **canonical** | PhenoMCPServers | high | | | | | Keep runnable server catalog; require protocol conformance, security manifests, ownership, and per-server release tests. |
| 69 | `PhenoObservability` | public | no | E1-root-docs | observability | **canonical_reset** | PhenoObservability | high | | | | | Narrow to instrumentation/runtime libraries; reconcile absorbed crates and remove evidence-product overlap with Tracera. |
| 70 | `PhenoPlugins` | public | no | E1-root-docs | plugin-runtime | **conditional_canonical** | PhenoPlugins | medium | | | | | Prove Agentora interoperability, ABI/manifest versioning, sandbox/security model, and multiple host consumers. |
| 71 | `PhenoProc` | public | no | E1-root-docs | task-process | **canonical** | PhenoProc | high | | | | | Keep process/IPC primitives distinct from Tasken; harden cross-platform behavior, safety invariants, and benchmarks. |
| 72 | `phenoResearchEngine` | private | no | **E2-forensic** | research-runtime | **delete_confirmed** | ResearchLedger | high | ResearchLedger | Verified | 93 | Low risk; self-tombstoned | Locate the claimed successor; preserve workflow/provenance contracts and retire the nonexistent-monorepo pointer. |
| 73 | `PhenoSpecs` | public | no | E1-root-docs | documentation | **canonical** | PhenoSpecs | high | | | | | Own cross-repo protocols and ADRs only; repo-local requirements remain with their products. |
| 74 | `phenotype-apps` | public | no | E1-root-docs | product-app | **forensic_hold** | one of phenotype-apps / FocalPoint | high | | | | | Resolve its collision with FocalPoint and giant mixed history; select one product identity and decompose unrelated apps. |
| 75 | `phenotype-fleet-ops` | public | no | E1-root-docs | fleet-assurance | **canonical** | phenotype-fleet-ops | high | | | | | Become sole shared CI/security/release/attestation authority; fix nonexistent-owner URLs and integrate RepoLedger state. |
| 76 | `phenotype-gateway` | public | no | **E2-forensic** | routing-provider | **delete_confirmed** | HexaKit | high | HexaKit | Verified | 90 | Low risk; already archived | It already declares archive; verify real successors and fix redirects before normalizing GitHub state. |
| 77 | `phenotype-gfx` | public | no | E1-root-docs | graphics-game | **incubator** | phenotype-gfx | medium | | | | | 90-day consumer gate: prove shared data contracts across at least two games; otherwise return modules to product owners. |
| 78 | `phenotype-go-kit` | private | no | E0-metadata-name | sdk-shared | **absorb_then_archive** | domain Go packages | high | | | | | Inventory modules and move each to its domain owner; retire language bucket. |
| 79 | `phenotype-go-sdk` | public | no | E1-root-docs | sdk-shared | **archive_normalize** | domain Go packages / HexaKit templates | high | | | | | Apply its explicit retirement; remove nonexistent successor links and preserve only genesis templates where appropriate. |
| 80 | `phenotype-infra` | public | no | E2-source-code | infra-runtime | **canonical_reset** | phenotype-infra | high | | | | | Own shared IaC only. Boundary confirmed (commit 67560d7): BytePort ejected from README. |
| 81 | `phenotype-infrakit` | private | no | **E2-forensic** | infra-runtime | **delete_confirmed** | HexaKit | medium | HexaKit | Verified | | All 9 crates migrated; private | Migrate unique IaC/config adapters to owners; retire generic infrastructure kit. |
| 82 | `phenotype-journeys` | public | no | E1-root-docs | evidence-quality | **canonical** | phenotype-journeys | high | | | | | Make hard assertions mandatory, add non-LLM validators, sign evidence bundles, and feed Tracera. |
| 83 | `phenotype-landing` | public | no | E1-root-docs | portfolio-brand | **canonical_collection** | phenotype-landing | high | | | | | Keep shared static-site deployment collection; generate product facts from RepoLedger to prevent drift. |
| 84 | `phenotype-omlx` | public | no | E1-root-docs | ml-runtime | **canonical_fork** | phenotype-omlx | high | | | | | Clarify fork delta, local-runtime boundary, and relationship to hwLedger; add reproducible model/hardware benchmarks. |
| 85 | `phenotype-python-sdk` | public | no | E1-root-docs | sdk-shared | **canonical_reset** | phenotype-python-sdk | high | | | | | Be a generated/released Python facade only; remove unresolved merge markers and domain logic; publish or stop claiming installability. |
| 86 | `phenotype-registry` | public | no | E1-root-docs | portfolio-governance | **generated_surface** | phenotype-registry | high | | | | | Generate human catalog from RepoLedger; prohibit hand-edited lifecycle authority. |
| 87 | `phenotype-router` | public | no | E1-root-docs | routing-provider | **conditional_canonical** | phenotype-router | high | | | | | Resolve library-only versus HTTP-product contradiction; prove package publication and real consumers or absorb into substrate. |
| 88 | `phenotype-teamcomm` | public | no | E1-root-docs | agent-runtime | **incubator** | phenotype-teamcomm | medium | | | | | Land protocol/persistence/CLI/MCP, integrate PhenoVCS locks, and prove two-agent collision avoidance before promotion. |
| 89 | `phenotype-tooling` | public | no | **E2-forensic** | fleet-assurance | **delete_confirmed** | phenotype-tooling (self) | high | phenotype-tooling | Verified | | Absorbed into target | Route CI/policy to fleet ops, benchmarks to Benchora, scaffolds to HexaKit; retain only coherent developer tooling if any. |
| 90 | `phenotype-traceability-spine` | public | no | E1-root-docs | trace-knowledge | **archive_normalize** | Tracera | high | | | | | Apply its own supersession decision after consumer/redirect verification. |
| 91 | `phenotype-unsloth-studio` | public | no | E1-root-docs | ml-runtime | **upstream_reference** | upstream Unsloth + local patches | high | | | | | Add exact upstream pin and delta inventory; maintain only deliberate local changes, not a shadow product identity. |
| 92 | `phenotypeActions` | private | no | **E2-forensic** | fleet-assurance | **delete_confirmed** | phenotype-fleet-ops | high | phenotype-fleet-ops | Verified | 124 | Low risk; private | Move reusable actions/workflows with history and tests; leave one fleet assurance surface. |
| 93 | `phenoUtils` | public | no | E0-metadata-name | sdk-shared | **decompose_and_narrow** | domain utility crates | high | | | | | Find consumers/co-change clusters; promote independently versioned utilities or absorb them—no generic dumping ground. |
| 94 | `PhenoVCS` | public | no | E1-root-docs | task-process | **canonical** | PhenoVCS | high | | | | | Finish safe worktree/airlock primitives, non-destructive invariants, and integration with teamcomm/agents. |
| 95 | `Pine` | public | no | E1-root-docs | platform-lab | **incubator** | Pine | medium | | | | | Time-box a smallest compatibility-layer vertical slice and compare against Wine/Proton/VM approaches; archive if no edge. |
| 96 | `Planify` | public | no | E1-root-docs | delivery-control | **upstream_reference** | Planify2 or upstream Plane | high | | | | | Freeze feature work; use only as comparator/donor until a branch/history parity decision chooses one fork. |
| 97 | `Planify2` | public | no | E1-root-docs | delivery-control | **conditional_canonical** | Planify2 | medium | | | | | Prove meaningful Plane divergence, reproducible install, migration from Planify, and a differentiated planning journey. |
| 98 | `PlayCua` | public | no | E1-root-docs | device-automation | **canonical_fork** | PlayCua | high | | | | | Keep as native CUA adapter under Eidolon; publish honestly and test platform adapters plus protocol conformance. |
| 99 | `PolicyStack` | public | no | E1-root-docs | fleet-assurance | **archive_normalize** | phenotype-fleet-ops | high | | | | | Apply declared migration after parity and redirect checks. |
| 100 | `portage` | public | no | E1-root-docs | evaluation-runtime | **upstream_reference** | portage | medium | | | | | Maintain as Harbor evaluation fork/reference with explicit upstream/delta and no duplicate benchmark authority. |
| 101 | `Project-Spyn` | public | yes | E0-metadata-name | historical | **archive_normalize** | Project-Spyn | high | | | | | Retain history only. |
| 102 | `QuadSGM` | private | no | E0-metadata-name | ml-research | **incubator** | QuadSGM | low | | | | | Require a reproducible paper/code benchmark, dataset provenance, and one clear research thesis before promotion. |
| 103 | `Quillr` | public | no | E1-root-docs | sdk-shared | **conditional_canonical** | Quillr | medium | | | | | Prove package distribution, protocol scope, benchmarks, and consumers; merge into Apisync if jobs are materially identical. |
| 104 | `RepoLedger` | public | no | E1-root-docs | portfolio-governance | **canonical** | RepoLedger | high | | | | | First priority: reconcile live GitHub state, own machine manifest/API, emit generated views, and fail on drift. |
| 105 | `ResearchLedger` | public | no | E1-root-docs | research-ledger | **canonical** | ResearchLedger | high | | | | | Own source/provenance/synthesis records; integrate SOTA snapshots, claims, and exports to Tracera. |
| 106 | `ResilienceKit` | private | no | E1-root-docs | sdk-shared | **archive_normalize** | phenotype-fleet-ops / product runbooks | high | | | | | Apply declared archive; preserve any unique resilience patterns with provenance. |
| 107 | `resume-all` | private | no | E1-root-docs | private-ops | **private_ops** | resume-all | high | | | | | Keep source-only recovery toolkit; verify every entry point and prevent secrets/runtime snapshots from entering Git. |
| 108 | `rich-cli-kit` | public | yes | **E2-forensic** | historical | **delete_confirmed** | phenoUtils | high | phenoUtils | Verified | 195 | Low risk; self-tombstoned | Retain history; migrate only proven reusable components. |
| 109 | `rust` | private | no | E0-metadata-name | historical | **forensic_quarantine** | archive or named target | low | | | | | Identify what the tiny private repo contains; rename/promote within one session or archive. |
| 110 | `SessionLedger` | public | no | E1-root-docs | session-ledger | **canonical** | SessionLedger | high | | | | | Keep narrow lossless capture/replay authority; verify privacy, format evolution, release channels, and Tracera export. |
| 111 | `sharecli` | public | no | E1-root-docs | agent-runtime | **canonical** | sharecli | high | | | | | Keep OS-level agent resource/coalescing runtime; independently verify package/release claims and contention benchmarks. |
| 112 | `Sidekick` | public | no | E1-root-docs | agent-runtime | **decompose_and_archive** | Agentora + substrate + communication owner | high | | | | | Split unrelated presence, cheap-routing, and messaging capabilities; preserve only independently justified components. |
| 113 | `Stashly` | public | no | **E2-forensic** | events-state | **delete_confirmed** | phenotype-registry | medium | phenotype-registry | Verified | 146 | Low risk | Narrow storage/state/cache contract, prove package/consumer adoption, and resolve naming/link drift. |
| 114 | `substrate` | public | no | E1-root-docs | routing-provider | **canonical** | substrate | high | | | | | Own agent-process dispatch gateway/TUI/adapters; define boundary against OmniRoute, router library, and Agentora. |
| 115 | `substrate-adapters-bundle` | public | yes | E0-metadata-name | historical | **archive_normalize** | substrate | high | | | | | Retain absorbed-adapter history only. |
| 116 | `Synthia` | public | yes | E0-metadata-name | historical | **archive_normalize** | Synthia | high | | | | | Retain history only. |
| 117 | `Tasken` | public | no | E1-root-docs | task-process | **canonical** | Tasken | high | | | | | Own task/DAG/scheduling semantics; prove phenoForge absorption and separate low-level process primitives from PhenoProc. |
| 118 | `thegent` | public | no | E2-source-code | developer-platform | **conditional_canonical** | thegent | high | | | | | Separate from NanoVMS cluster (REC-DEC-004). Has own apps/byteport/ with different stack. Independent dispatch/orchestration tool. |
| 119 | `thegent-pr2-v2-uncommitted-2026-07-14` | private | yes | E0-metadata-name | historical | **archive_normalize** | thegent history | high | | | | | Ensure unique uncommitted recovery was imported; retain frozen evidence only. |
| 120 | `thegent-workspace` | private | yes | E0-metadata-name | historical | **archive_normalize** | thegent history | high | | | | | Verify migration and keep frozen workspace evidence only. |
| 121 | `Tokn` | public | no | E1-root-docs | cost-ledger | **decompose_and_narrow** | Tokn accounting ledger + substrate/router | high | | | | | Keep token/cost/budget accounting; move provider-routing behavior to routing authorities. |
| 122 | `Tracely` | public | yes | E0-metadata-name | historical | **archive_normalize** | Tracera / PhenoObservability history | high | | | | | Retain provenance only. |
| 123 | `Tracera` | public | no | E1-root-docs | trace-knowledge | **canonical** | Tracera | high | | | | | Own evidence/trace graph; harden verifier, schema, provenance, queryability, and integrations with every ledger. |
| 124 | `turboquant` | public | no | E1-root-docs | ml-research | **canonical_research** | turboquant | high | | | | | Keep focused quantization research; require reproducible baselines, hardware matrix, artifacts, and paper-grade reports. |
| 125 | `vibe-kanban` | public | no | E1-root-docs | upstream-contribution | **upstream_reference** | upstream BloopAI/vibe-kanban | high | | | | | Honor "reference only"; archive/freeze fork and extract only attributed research into HeliosLab/AgilePlus. |
| 126 | `vibe-monitor` | public | no | E1-root-docs | routing-provider | **archive_normalize** | PhenoObservability or substrate runbooks | high | | | | | Empty duplicate scaffold; preserve spec if unique, then archive. |
| 127 | `vibeproxy` | public | no | E1-root-docs | routing-provider | **archive_normalize** | cliproxyapi-plusplus / substrate | high | | | | | Apply its own supersession decision after consumer scan. |
| 128 | `vibeproxy-monitoring` | public | no | E1-root-docs | routing-provider | **archive_normalize** | PhenoObservability or product-local ops | high | | | | | Duplicate empty scaffold; consolidate any unique rules and archive. |
| 129 | `vibeproxy-monitoring-unified` | public | no | E0-metadata-name | routing-provider | **archive_normalize** | PhenoObservability or product-local ops | high | | | | | Select no separate monitoring authority unless deployable assets and independent consumers exist. |
| 130 | `WorldSphereMod` | public | no | E1-root-docs | product-game | **canonical_fork** | WorldSphereMod | high | | | | | Keep flagship hard fork; automate live-game journey evidence, upstream divergence, and Compound-Spheres compatibility. |
| 131 | `zz-472-P2-Flame-War` | private | yes | E0-metadata-name | historical | **archive_normalize** | historical bundle | high | | | | | No active work; retain provenance only. |
| 132 | `zz-agslag` | private | yes | E0-metadata-name | historical | **archive_normalize** | AGSLAG current authority | high | | | | | Verify any unique source was migrated; retain frozen history. |
| 133 | `zz-agslag-dash` | private | yes | E0-metadata-name | historical | **archive_normalize** | AGSLAG / RepoLedger dashboard | high | | | | | Preserve unique dashboard history only. |
| 134 | `zz-agslag-docs` | private | yes | E0-metadata-name | historical | **archive_normalize** | AGSLAG docs | high | | | | | Preserve unique documents with provenance only. |
| 135 | `zz-archive-phenoData` | public | yes | **E2-forensic** | historical | **delete_confirmed** | zz-pheno | high | zz-pheno | Verified | 216 | Tombstoning now | Already historical; keep out of actionable set. |
| 136 | `zz-archive-PhenoProject` | public | yes | **E2-forensic** | historical | **delete_confirmed** | upstream | high | upstream | Verified | 177 | Fork | Already historical; keep out of actionable set. |
| 137 | `zz-archive-phenoRouterMonitor` | public | yes | E0-metadata-name | historical | **archive_normalize** | historical bundle | high | | | | | Already historical; keep out of actionable set. |
| 138 | `zz-archive-PhenoRuntime` | private | yes | **E2-forensic** | historical | **delete_confirmed** | zz-pheno | high | zz-pheno | Verified | 81 | Clean; private, already archived | Already historical; keep out of actionable set. |
| 139 | `zz-archive-phenotype-org-audits` | private | yes | E0-metadata-name | historical | **archive_normalize** | RepoLedger evidence imports | high | | | | | Retain immutable audit provenance; do not revive as authority. |
| 140 | `zz-archive-phenotype-org-governance` | private | yes | E1-root-docs | historical | **archive_normalize** | PhenoSpecs + PhenoHandbook | high | | | | | Retain decisions as evidence; current governance must be generated/enforced elsewhere. |
| 141 | `zz-archive-services` | private | yes | **E2-forensic** | historical | **delete_confirmed** | phenotype-router | high | phenotype-router | Verified | 19 | Tombstoning now | Already historical; keep out of actionable set. |
| 142 | `zz-atoms.tech` | private | yes | E0-metadata-name | historical | **archive_normalize** | historical product bundle | high | | | | | Retain private product history only; no active agents. |
| 143 | `ZZ-AtomsBot` | private | no | E1-root-docs | historical | **archive_normalize** | historical product bundle | high | | | | | Apply its strict freeze and GitHub archive state; security-review secrets/config before final closure. |
| 144 | `zz-GDK` | public | yes | E0-metadata-name | historical | **archive_normalize** | historical bundle | high | | | | | Already historical; keep out of actionable set. |
| 145 | `zz-KaskMan` | private | yes | E0-metadata-name | historical | **archive_normalize** | historical bundle | high | | | | | Already historical; keep out of actionable set. |
| 146 | `zz-RIP-Fitness-App` | public | yes | E0-metadata-name | historical | **archive_normalize** | historical bundle | high | | | | | Already historical; keep out of actionable set. |

## Forensic audit summary (2026-09-12)

### DELETE confirmed (16 repos)

| Repository | Evidence | Target | Commits | Risk | Special |
|---|---|---|---:|---|---|
| Conft | E2 | Configra | 166 | low | Self-tombstoned |
| rich-cli-kit | E2 | phenoUtils | 195 | low | Self-tombstoned |
| phenoResearchEngine | E2 | ResearchLedger | 93 | low | Self-tombstoned |
| phenotype-gateway | E2 | HexaKit | 90 | low | Already archived |
| phenotype-infrakit | E2 | HexaKit | N/A | low | All 9 crates migrated; private |
| Stashly | E2 | phenotype-registry | 146 | low | |
| phenotypeActions | E2 | phenotype-fleet-ops | 124 | low | Private |
| zz-HexaKit | E2 | phenotype-registry | 727 | low | Monorepo branch merged |
| PhenoHandbook | E2 | phenotype-registry | 251 | low | |
| Apisync | E2 | phenotype-registry | N/A | low | Published crate v0.2.10 preserved |
| zz-archive-phenoData | E2 | zz-pheno | 216 | low | Tombstoning now |
| zz-archive-PhenoRuntime | E2 | zz-pheno | 81 | low | Private, already archived |
| zz-archive-PhenoProject | E2 | upstream | 177 | low | Fork |
| zz-archive-services | E2 | phenotype-router | 19 | low | Tombstoning now |
| PhenoDevOps | E2 | phenotype-tooling | 530 | low | |
| zz-clap-ext | E2 | phenotype-tooling | 70 | low | Absorbed |

### HOLD pending resolution (3 repos)

| Repository | Evidence | Target | Issue |
|---|---|---|---|
| DataKit | E2 | phenotype-python-sdk | ETL NOT in target; 877 lines on unmerged branch |
| Logify | E2 | PhenoObservability/logkit | Cherry-picking 9 fixes; target exists as repo not org |
| zz-argis-extensions | E2 | phenotype-tooling | 144 unmerged branches; preserving SLO code; 495MB |

### Tombstoning in progress

- **zz-archive-phenoData**: tombstoning now (deletion pending)
- **zz-archive-services**: tombstoning now (deletion pending)

## Non-negotiable caveat

Every row is a **decision hypothesis**. Before archive, deletion, destructive rewrite, or package deprecation, an assigned agent must complete the migration/closure gate in the master plan and commit evidence at an immutable SHA.
