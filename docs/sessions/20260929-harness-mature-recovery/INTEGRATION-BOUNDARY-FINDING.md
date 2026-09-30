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