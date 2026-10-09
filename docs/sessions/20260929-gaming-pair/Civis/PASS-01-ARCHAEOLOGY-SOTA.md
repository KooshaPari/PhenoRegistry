# Civis — archaeology, alternatives and bootstrap pass 1

Date 2026-09-29. Source **b3cd62a7394878cc64d024fbfcfd398b8bb88bf1**; registry **85d7cd00cf59c379c05b740e8130a85b0d5bd31b**. Research draft; architecture freeze BLOCKED.

## Authority correction before architecture

The February PRD describes deterministic headless CivLab with many clients. The current `docs/guides/emergence-charter.md` explicitly corrected that on May29, and `docs/adr/ADR-determinism-dropped.md` is Accepted as recorded, dated May30. Global bit-identical replay and seed-only reproducibility are not required; persistence restores actual state. The May31 scope note excludes multiplayer/co-op/spectator from v1 and includes actor rigging/animation. Original decision-author transcript remains unrecovered; no later explicit authorized reinstatement was found. Generic later descriptions do not automatically reverse this specific correction.

The initial recovery assumption that global deterministic replay was the spine is **falsified**. RNG stream position only blocks an explicitly opted-in replay contract, not automatically the entire game. Do not invent a mandatory deterministic research mode to reconcile stale prose.

Current intended horizon includes physical/material/planet/genomic substrate and emergent life, sentience, psyche, culture/language, diverse markets/polities, architecture and agent/user intervention. Scientific realism and 'disk primarily bounds 20mi maps' are unvalidated claims, not accepted empirical facts.

Additional sources: current `docs/research/RESEARCH_INDEX.md`, blob `d5436a1a05ca1c0a99ff3c73072278544e585b68`, fully read. It indexes Cities Skylines, WorldBox, Empire at War, Call to Arms, Dwarf Fortress/RimWorld, Songs of Syx, Manor Lords, Civ/Old World, Spore/Black & White and Bevy teardowns plus RND001..016. Counts/competitor claims inside the index are author assertions, not independently revalidated. Reuse and audit that corpus rather than duplicating it. Histories include April25 correction from civic-infra fiction and June10 integrated emergence/charter work; full useful history is not exhausted.

Civis `vendor/phenodocs` exact gitlink: **35e0e90a19dfd93ce4e1a81210ade92088b2bbbc**. This resolves the full pin previously open in source ledger C-S10; source contents and contract imports still unreviewed.

## Primary-source research register

Accessed 2026-09-29. Read extents, not latest-version or project-health certification.

| ID / primary source | Version / extent | Established fact | Interpretation and limitation |
|---|---|---|---|
| C-EXT-01 https://www.superworldbox.com/ | Current official product overview (page labels0.51.4; release identity not verified) | God powers, world/life creation and civilizations are marketed product capabilities | Strong gameplay absent-product baseline; feature existence/quality claims need hands-on comparison, not vendor prose alone |
| C-EXT-02 https://mesa.readthedocs.io/stable/ | Stable documentation overview; exact package version not resolved | Apache2 agent-based modeling framework with agents/spaces, visualization and data collection | COMPOSE for research baseline or focused submodel validation; not a drop-in single 3D living-world game. `/latest` was4.0.0a0 alpha, not stable recommendation |
| C-EXT-03 https://bevy.org/news/bevy-0-18/ | Official0.18 release article, Jan13 2026 | Existing engine provides rendering/UI/camera/plugin machinery | INTEGRATE pinned engine; custom engine not justified. This is not a check that0.18 is latest or all selected features run on target hardware |
| C-EXT-04 https://docs.wasmtime.dev/examples-deterministic-wasm-execution.html | Current official deterministic-Wasm execution guide | Host imports, NaNs, relaxed SIMD, resource behavior and interruption policy affect reproducibility | Apply only where a subsystem explicitly opts in. Wasm admission should still enforce permissions/resource isolation; determinism is not a global Civis admission criterion |
| C-EXT-05 https://www.jasss.org/23/2/7.html | Grimm etal2020 ODD second update, DOI10.18564/jasss.4259; HTML method/limitations read | Structured model descriptions connect entities, schedules, submodels, rationale and evaluation | ADAPT for rule/model dossiers. Describing a model does not establish societal realism or gameplay value |
| C-EXT-06 https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md | Statement v1 | Artifact digest and predicate identity envelope | ADAPT evidence subjects; trusted issuer and actual behavioral observations remain separate |
| C-EXT-07 https://slsa.dev/spec/v1.2/provenance | Approved1.2 provenance overview | Build/source provenance concerns artifact production and origin | COMPOSE build identity with gameplay/model validation. Never infer scientific/gameplay correctness from a build attestation |

Remaining research families: artificial life/open-ended evolution and emergence criteria; calibrated agent models/pattern-oriented validation; economics/markets/social-network models; spatial streaming/multi-resolution conservation; physics/fluids/chemistry libraries; state persistence/event sourcing; native UI/accessibility and game testing; plugin sandboxing; asset/animation/audio tooling and licenses; actual competitor teardown evidence; current package health/security and integration costs. Existing in-repo research is a source family, not a completed SOTA gate.

## Best realistic alternatives / existence gate

**Player goal:** WorldBox is a realistic existing god-simulation baseline, not an intentionally weak comparison. **Research/modeler goal:** Mesa + established models + notebooks/analysis is a practical baseline for explicit social/economic experiments. **Native 3D authoring goal:** pinned Bevy plus appropriate existing plugins and domain models avoids writing a graphics engine. WorldBox and Mesa are not a unified shared-world stack; interoperability and manual transfer costs must be counted rather than concealed.

| Differentiation | Status | Direct attack / next evidence |
|---|---|---|
| God powers, world creation, evolving societies | COMMODITY / CONTESTED | Existing games address much of this; need user outcome comparison |
| ABM framework, charts and model experiments | COMMODITY / CONTESTED | Mesa/established model tooling already exists |
| Global deterministic replay as Civis's unique core | FALSIFIED AS CURRENT OBLIGATION | Explicit charter/ADR drops it; optional local contracts do not resurrect it globally |
| Coupled physical-to-social emergence with legible intervention and retained world continuity | CANDIDATE DIFFERENTIATION | Prove coupling instead of fixed scripted labels, show interpretable effect and honest limits, then compare user value |
| Reality-like predictive society from physics-like rules | UNVERIFIED; no scientific claim admitted | Calibration/validation datasets, model assumptions, uncertainty and held-out patterns missing |
| Very large world is disk-bound rather than compute-bound | UNVERIFIED | Workload/hardware/active-cell/agent/LOD/performance experiment required |

Existence gate remains **OPEN**. No engine rewrite, five-client expansion, new general ABM framework or multiplayer implementation is justified merely by accumulated source. A single usable, state-faithful, inspectable journey is the candidate next proof; mature scope is retained as projections, not erased.

## Bootstrap decisions, provisional

| Capability | Disposition | Custom justification / constraints |
|---|---|---|
| Engine/rendering/UI/animation/audio | USE DIRECTLY / INTEGRATE existing pinned ecosystem | Product UX and domain visualization custom; backend duplication requires evidence. Exact crates/assets/licenses/health remain to audit |
| Materials/fluids/planet/genomes | LEARN FROM / ADAPT / COMPOSE before BUILD CUSTOM | Choose model fidelity and conservation first; a domain-specific coupling layer may be necessary, a fresh general physics engine is not presumed |
| Economy/psyche/culture/polity models | ADAPT established models, custom coupled rules only when justified | Record authored rules vs measured emergent patterns and calibration limits; names/events are not proof of emergence |
| Spatial streaming and simulation LOD | COMPOSE storage/chunk primitives plus domain transfer rules | Identity, conservation and cross-boundary causality on promote/demote need experiments; graphics LOD is not simulation LOD |
| Save/load | COMPOSE mature serialization/storage/transaction primitives | Custom exhaustive authoritative-state manifest/migrations may be needed; mixed sidecars and interrupted replace must not silently become valid saves |
| Mod sandbox | INTEGRATE existing runtime | Capability/resource denial, host API/version and state restoration are domain contracts; no handrolled VM/crypto |
| Scenario/command/observation interface | ADAPT existing transports; custom domain semantics | One authoritative world identity across standalone/server/client modes; JSON-RPC reachability alone is not acceptance |
| Model description and evaluation | ADAPT ODD plus task-specific experiments | Separate scientific validity, software correctness and subjective gameplay value |
| Evidence/grading | COMPOSE provenance standards with domain oracles | Policy independence and candidate/configuration identity are not optional |

## Academic evidence matrix — first admitted source, not a quota

**C-EXT-05 (Grimm etal2020):** task = improve clarity/replication/structural-realism description of ABMs; design = methodological protocol update plus discussion/bibliometric context; dataset = literature/use experience, not Civis scenarios; sample size = no controlled Civis sample, bibliometric absolute N not extracted; baseline = earlier ODD protocol conceptually, not a head-to-head game benchmark; metric = no product performance metric; evaluator = authors/protocol analysis and scholarly review, no independent Civis evaluator; limitations = complex models, incomplete code-level detail, long descriptions and continued ambiguity; establishes = a reusable model-reporting structure; does not establish = emergence from our code, calibrated society predictions, performance, usability or superiority over WorldBox/Mesa. Date published2020-03-31. No effect size or numerical benchmark is invented.

Dino has no qualified academic benchmark in this cycle. More papers must be selected by unresolved capability questions, not to inflate this matrix.

## Architecture experiment contracts

- Save interruption: fault after each output step and during replacement. The previous committed snapshot must remain restorable, or an explicit unrecoverable state must be surfaced without silently accepting a mixed save. Caller safeguards remain uninspected.
- Save classification: genuine supported legacy fixtures must load under explicit migration; damaged current-format fixtures missing metadata/sidecars must not masquerade as correct restoration. Validate spec/model/world/tick identities and source bytes preserved on failed load.
- Cross-mode world identity: an action to civ-server must not qualify a separate standalone world; reconnect/restart keeps durable world truth, not a worker lease.
- Emergence ablation: change/remove a claimed causal coupling while retaining display labels. Grader must detect lost behavior; seeing a `faction`/`sentience` label alone is not a pass. Statistical controls are necessary where outputs vary; no requirement for identical future random trajectories.
- LOD transfer: promote/demote active regions while tracking conserved quantities and entity/event ownership; compare against a high-resolution reference over a declared workload and tolerance. Tolerances require acceptance, not arbitrary values now.

Native execution of these experiments: **NOT RUN**. No high-risk architecture unknown is closed by this research pass.
