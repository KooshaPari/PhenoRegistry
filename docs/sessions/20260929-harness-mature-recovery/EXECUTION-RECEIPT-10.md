# Execution receipt 10 — product-integrated effect seams pinned

Date: 2026-09-30. Program remains OPEN.

## Contract CI
External Effect Recovery Contract jobs for both spec branches are still runner-queued at this receipt. Queued is not green. The diagnostic uses real subprocess death and fsync'd receipt/effect files but remains contract-level, not runtime integration.

## HeliosLite seam
Source tracing pins the common integration point at `ToolExecutor::execute` immediately above `call_internal`. H-F008 remains: Write/Patch/Remove/Shell/Fetch can commit before a durable effect receipt. Product-integrated experiment design adds an optional versioned effect context/adapter to ToolCallContext rather than instrumenting each service or abusing conversation metadata. First fixture is a deterministic write-like operation with crash before dispatch, after write/before confirm, and after confirm.

## KCode seam
Source tracing pins the common boundary at Registry dispatch / the central turn caller around `registry.execute`. Existing ToolContext already carries tool_call_id; it is correlation evidence, not an idempotency guarantee. Existing ToolUse-before-execute and ToolResult-after-execute persistence stays intact; the effect ledger complements it. First fixture can reuse isolated WriteTool/Registry tests and must include a non-queryable negative control.

## Architecture constraint
Durable effort/effect authority remains outside disposable worker sessions. Neither runtime should grow a duplicate general workflow engine. Ordinary sessions may remain backward-compatible without an adapter; a workflow that explicitly requires durable-effect safety must fail before dispatch if the required adapter is unavailable.

## Existence pressure
Current upstream jcode's external-provider registration architecture further supports moving the owned ForgeCode provider toward upstream contribution/external runtime adapter. Golden semantic fidelity tests remain required before any migration decision.

No production effect-recovery implementation has been claimed yet.