# Dino — archaeology, alternatives and bootstrap pass 1

Date 2026-09-29. Source **17119051e782b32615413049c1c3cd207f0b540e**; registry **85d7cd00cf59c379c05b740e8130a85b0d5bd31b**. Research draft, architecture freeze BLOCKED. Product-local source ledger owns inspected extents and findings.

## Internal recovery

Current README and runtime namespaces identify DINOForge as a general-purpose mod platform for Diplomacy is Not an Option, not a single content conversion. Retrieved March10 user intent prioritizes that framework. The earliest matched foundation commit `a0d42051e0e62d758397ba56987b0f17ae550ae0` (March9 local / March10 UTC) independently records declarative content, extensible registries, domain plugins and wrap-over-handroll. Its claims of completed prior research and approval are author assertions, not an exhaustive source review. Next matched commit `a3146aa46718d0e5a798cd2a8eb986a20b5052a0` describes early reverse-engineering/PackLoader tooling. These are useful lineage anchors, not all history.

Additional actual caller inspected: `src/Runtime/RuntimeDriver.cs:1-335`, blob `f4024a7b69d2b83d1bf94a77616e9bcaca9b3736`. Initialize starts InitializeRoutine; the routine constructs ModPlatform and calls its Initialize. Thus the null-schema integration is not inferred merely from an unused class name. The complete Plugin-to-driver startup and scene transition chain still needs inspection/native execution.

Observed `ModPlatform.cs:220-440` passes null schema validator; `ContentLoader.cs:1-220` documents skip-on-null and forwards it to registry import. Scope-limited finding: compiler validation cannot qualify all mutable runtime ingress. Parsing, version compatibility and dependency checks remain present. Inspect RegistryImportService and alternate ingress guards before calling this an end-to-end reproduced exploit.

## Primary-source research register

All sources accessed 2026-09-29. Versions below are what the pages identify, not claims that they are the newest installable release. Full code/license/health audits remain open.

| ID / primary source | Version and inspected extent | Established fact | Interpretation / limitation / decision consequence |
|---|---|---|---|
| D-EXT-01 https://docs.bepinex.dev/articles/user_guide/installation/index.html | v5.4.21 docs installation overview, build c17cd01 | Installation depends on host/platform/architecture | USE DIRECTLY subject to the exact supported DINO host matrix; do not infer v5 supports all IL2CPP hosts |
| D-EXT-02 https://docs.bepinex.dev/master/articles/user_guide/installation/index.html | master installation overview, build f6050e7 | Mono and IL2CPP have different installation/runtime paths | INTEGRATE a pinned compatible loader; newer docs do not justify untested runtime upgrade |
| D-EXT-03 https://github.com/NeighTools/UnityDoorstop | upstream README v4/legacy-v3 description | Early managed entry differs by Mono/IL2CPP; v4 README identifies LGPL2.1, legacy v3 CC0 | INTEGRATE existing retained fork after exact binary/source/license binding. Early entry does not mean Unity world/UI is ready. No account-fork license conclusion yet |
| D-EXT-04 https://github.com/pardeike/Harmony | repository overview only | Runtime .NET/Mono patching prior art exists | USE/INTEGRATE narrowly when needed, not replace ECS-native semantic adapters without measurement; detailed patch lifecycle/compatibility review open |
| D-EXT-05 https://github.com/devopsdinosaur/dno-mods | master README/tree overview | Existing DINO-specific mods/recipes offer realistic absent-product baseline | LEARN FROM; copying/forking BLOCKED pending explicit license/permission review. Public visibility is not permission |
| D-EXT-06 https://github.com/ebkr/r2modmanPlus | develop README, MIT-labelled repo | Profiles, configuration, enabling/disabling, sharing and updating are existing manager capabilities | COMPOSE/ADAPT only after proving DINO integration. Do not claim it is an already compatible DINO replacement |
| D-EXT-07 https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md | Statement v1 format | Immutable subjects/digests and predicate type provide an evidence envelope | ADAPT identity envelope, not its syntax as proof of gameplay or trusted issuer |
| D-EXT-08 https://slsa.dev/spec/v1.2/provenance | Approved SLSA1.2 provenance overview | Provenance distinguishes artifact origin/build/source processes | COMPOSE build receipt with separate behavioral evidence. v1.1 page was retired; current1.2 checked. No SLSA level certified |

Failed acquisition: Factorio official lifecycle URL attempted but unavailable via reader. Foundation message cites Factorio/RimWorld/Satisfactory/Minecraft DX as prior research; that message is NOT a substitute for retrieving those lifecycle APIs and technical contracts. Additional needed research includes host game official mod/support terms, package dependency algebra and rollback, asset formats/import libraries, safe YAML/schema handling, modern mod managers, update/TUF/Sigstore alternatives, accessibility and automated game testing. No negative competitor conclusion is drawn from a failed search.

## Best realistic absent-product stack

For a bounded pack: existing compatible BepInEx + upstream/retained Doorstop + narrow Harmony or existing DINO/ECS recipes + rights-cleared content + isolated installation/profile/deployment scripts. Add r2modman only when a supported DINO adapter is demonstrated. This stack already boots plugins and can modify the game; it does not automatically supply DINOForge's declarative semantic registry or verification interface. Compare the cost of that missing glue honestly against maintaining DINOForge.

| Claim | Status after attack | Evidence needed next |
|---|---|---|
| We uniquely load mods / patch .NET / offer profiles | FALSIFIED as generic differentiation | Existing loaders/managers provide these primitives |
| We make DINO domain content declarative and composable across packs | CANDIDATE DIFFERENTIATION | Two semantically different packs on the same supported host; no pack-specific engine branch; dependency/conflict controls |
| Agents can reliably author, install, observe and recover a real DINO pack | UNVERIFIED DIFFERENTIATION | Same-host action-to-state evidence and independent controls; compiler output alone insufficient |
| Current large test/milestone counts mean mature usable product | REJECTED AS EVIDENCE | Current installed player journey, restart and scene-transition evidence |
| Unified asset workflow saves net effort and respects rights | UNVERIFIED | Source/license/transformation lineage, import failure behavior, measured operator effort vs tools already available |

Existence gate: **OPEN**. A bounded framework proof is justified as a hypothesis test, not by sunk work. A bespoke loader, cryptosystem, generic package manager, or second gameplay engine is not justified by this pass. Continue only on DINO-specific semantics and a safe observable spine until alternatives are qualified.

## Bootstrap decision ledger

| Capability | Proposed disposition | Why custom, if any | Open integration / health / licensing gate |
|---|---|---|---|
| Process entry, patches | USE DIRECTLY / INTEGRATE | No new loader/patch engine | Exact game/Unity/backend/OS/loader/binary versions; retained fork deltas; notices |
| Schema parsing and validation | COMPOSE existing YAML/schema tools | Domain schemas and DINO semantic compatibility are custom | Runtime/CLI parity; unknown fields; failure atomicity; library version/health |
| Dependency/conflict ordering | ADAPT proven resolution semantics | DINO activation side effects need domain transaction | Semver/ranges, cycle handling, missing dependency, hot-reload graph, rollback proof |
| ECS mapping and scene lifecycle | BUILD CUSTOM narrow adapter | Existing generic loaders do not define DINO components or scene ownership | Host version compatibility, root resurrection, main-thread dispatch, stale world handles |
| Profiles/install/update UX | COMPOSE / ADAPT | Only DINO-specific target detection and diagnostics | DINO manager support, canonical paths, crash rollback, user save preservation |
| Asset processing | USE/COMPOSE before new pipeline | Pack semantics/provenance integration only | Formats, tool versions, cache correctness, source/redistribution license per asset |
| Agent-facing observe/action interface | ADAPT machine-interface infrastructure; custom domain commands | Must expose actual game state and accepted actions rather than file existence | Authorization, install/session identity, observation completeness, stale operations |
| Acceptance evidence | COMPOSE standard provenance with custom domain oracles | Game effects require domain criteria | Trusted collector, policy protection, verifier versioning and negative controls |

No library adoption, upgrade, fork or license decision has been executed. Each unresolved technical/health/license gate is a blocker to freezing that architectural choice.

## Academic evidence and experimental coverage

No Dino-specific academic performance study was qualified in this pass. Do not use a paper count as a gate. Remaining tasks: identify research on automated game testing, stateful hot-reload transactions, metamorphic testing and gray-box instrumentation; record task/dataset/sample/baseline/metric/evaluator/limitations before importing a result. Industry documentation above establishes API/lifecycle alternatives, not benchmark superiority.

## Highest-risk experiments

1. Same pack bytes through compiler, direct runtime load and hot reload; schema-invalid but parse-valid content must not activate unnoticed. Confirm prior active registry and live game state survive rejection.
2. Boot -> menu -> playable scene -> return -> reload; instrument exact installed binary, pack digests and world generation. A screenshot from another install or stale bridge must fail qualification.
3. Interrupt activation/update and remove dependencies/assets. Demonstrate bounded recovery and preservation of user saves/last accepted configuration.
4. Compare one real pack workflow against the absent stack, with author effort, player success, breakage and maintenance recorded. This is a later empirical pilot, not a replacement for design research.

All remain NOT RUN against the native host. No architecture high-risk unknown is marked closed by documentation.
