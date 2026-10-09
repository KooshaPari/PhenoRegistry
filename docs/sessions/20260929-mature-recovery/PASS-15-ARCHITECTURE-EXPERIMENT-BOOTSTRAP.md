# Pass 15 — architecture experiment bootstrap

Date 2026-09-30.

This pass advances all three v0.2 architecture gates in one cycle. It does not claim runtime/product validation.

## Portage

Experiment package `027ec1bc4e70b60e1feb14305dda6facbb80e32b` specifies ten thin-layer fixtures over native Harbor TrialResult/ArtifactManifest/regrade behavior.

A self-contained prototype test at `ac9ae36fe093cf3af76453a883213f0b6bfa568d` demonstrates the proposed semantic layer can:
- derive compound subject identity without replacing Harbor AgentConfig;
- block green reward when a required artifact failed;
- block acceptance when a required criterion is invalid.

This is architecture-feasibility evidence only. It does not prove actual Harbor hook coverage or native integration.

Additional source finding: TrialConfig already contains model, skills, MCP servers, env/kwargs, resource/network and task ref/git identity. Compound subject identity can likely be a canonical projection over native config plus missing role/memory/organization/runtime references, not a duplicate configuration system.

## PhenoMLX

Experiment package `ec220a78b370063bb16f8be02483c627b6156917`.

Current source already has MLX, Metal, llama.cpp, vLLM, SGLang and TensorRT-LLM adapters. Static BackendCapabilities normalize broad flags, while GenerateResponse usually lacks exact engine/model/build/profile identity. This is direct evidence that a typed profile envelope addresses a real current ambiguity.

Self-contained profile prototype `a0699024eb4905c2bac9059e6b5ee40a663706b5` demonstrates:
- requested engine and realized fallback have distinct profile identity;
- hot swap/runtime generation changes identity;
- opaque mechanism facts can remain explicitly unknown rather than fabricated.

No engine/model performance claim is made. Real two-engine phase remains required.

## PhenoLab / PhenoLM

Experiment package `376458be6fb9da03fd942b59390de480f3a607cb` specifies a complete narrow vertical plus ten adversarial cases and GEPA composition subexperiment.

Self-contained identity prototype `2ba6e3fdaeeae575400f6490759790c7188d95d0` demonstrates:
- material candidate intervention changes identity and invalidates old assessment binding;
- acceptance-policy/hard-gate change creates a different AssignmentEpoch;
- missing evidence cannot accept;
- critical failure cannot average away.

This prototype is designed to wrap existing garden gates/promotion/risky-action/ledger primitives rather than replace them.

## Interpretation

The semantic architecture hypotheses are **implementable at small wrapper/envelope scale** in isolation. This materially lowers the risk that v0.2 requires a rewrite.

It does not close the architecture gate because integration matters:
- Portage must prove actual Harbor extension/gateway hooks and native false-green fixtures.
- PhenoMLX must run two real pinned engines/profiles and show the abstraction preserves useful differences.
- PhenoLab must wire one real runner + existing gates + durable records, execute false-green cases and worker replacement.

## Next work in same program

1. Check CI receipts for prototype commits; production CI blockers must not be confused with prototype semantics.
2. Build explicit experiment result ledgers with PASS/FAIL/NOT_RUN per fixture.
3. Reconcile source coverage ledgers now that architecture/product boundary has narrowed.
4. Produce v0.2 obligation-to-contract coverage check and candidate baseline criteria.
5. If prototypes expose no semantic contradiction, begin the first vertical-slice contract packages while keeping implementation changes bounded and separate.

No product is at specification/design completion.
