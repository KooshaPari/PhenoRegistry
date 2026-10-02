# Integration boundary finding — do not count absent Pheno/Pine code as fork differentiation

Date: 2026-09-30.

Direct current-source searches in both active primary repositories found no named `Pine`, `PhenoShared`, `Tracera`, or `AgilePlus` integration surfaces. A name search cannot prove semantic absence, but it does falsify any claim that those named integrations are already an implemented differentiator.

## Contract consequence
Treat these as **external consumer/adapter boundaries** until evidence proves core modification is necessary:
- Pine: command/path/env/PTY/process/cancellation compatibility profile for native Windows/POSIX-oriented workflows.
- Tracera: accepted product/requirement/evidence graph exchange, not ownership of coding-worker runtime.
- AgilePlus: durable development effort/work-package integration, not product-state authority.
- PhenoShared/Agentora: shared capability/SDK contracts only where actual consumers and stable exported APIs exist.

Do not add direct dependencies merely to make differentiation exist. First define a versioned interface and prove a thin adapter cannot satisfy the journey. Only then may a core retained patch be justified.

This keeps the three lifetimes separate: worker runtime, durable development effort, and accepted product state.
## Correction after mounted-interface trace — 2026-09-30
Evidence falsified the earlier name-search implication for HeliosLite. Frozen HeliosLite main entrypoint imports and initializes `TraceraTelem`; startup/end/error telemetry is mounted in `forge_main::main`. It also dispatches an `Agileplus` top-level command through `forge_agileplus::commands::Cli::run_command`. `forge_sharecli` includes explicit composition tests with `forge_tracera`.

Therefore Tracera and AgilePlus are **implemented/mounted integration surfaces in HeliosLite**, not merely future adapter candidates. Their authority is still constrained:
- Tracera telemetry/events are evidence/observations and must not become product-state acceptance authority merely because they are emitted by the runtime.
- AgilePlus command integration is a durable-development/work-management surface; its presence does not make worker runtime state canonical durable effort by itself.
- ShareCLI↔Tracera tests prove envelope composition/store round-trip, not production HTTP delivery or product acceptance.

The earlier broad statement that named Pine/PhenoShared/Tracera/AgilePlus integrations were not mounted is superseded for **HeliosLite Tracera and AgilePlus only**. Pine and the other named boundaries remain evidence-driven until mounted source is established.