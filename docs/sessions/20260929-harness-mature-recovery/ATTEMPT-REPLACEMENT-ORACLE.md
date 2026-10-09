# Attempt-A / Attempt-B process-death oracle

Date: 2026-09-30. Applies to both primary products. This is the next product-integration gate after the qualified standalone state machine.

## Fixture process model

The test harness owns a temporary durable-effort directory outside the worker process:
- `effect.json` — atomic durable receipt;
- `target.txt` — downstream write target;
- `attempts.jsonl` — append-only attempt/reconciliation evidence.

Attempt A is a child process. Attempt B is a fresh child process; no in-memory state is shared.

## Attempt A

1. Load assigned stable effect ID / tool-call ID from fixture input.
2. Persist INTENT_RECORDED.
3. Persist DISPATCHED.
4. Execute the product's real Write path through its effect hook.
5. At a test-only crash barrier after the file effect but before durable confirmation, terminate the process without cleanup.

Expected durable state: receipt cannot honestly be CONFIRMED. Target file contains expected content.

## Attempt B

1. Load the same durable effort + effect ID from disk.
2. Observe prior state as DISPATCHED/UNCERTAIN.
3. Invoke the product's Write reconciliation helper **before** any Registry/ToolExecutor redispatch.
4. Matching target content => persist RECONCILED_SUCCESS.
5. Exit without invoking Write again.

Oracle: target mutation counter/fixture proves one committed write; receipt history proves attempts A and B; no second dispatch exists.

## Negative controls

- Delete target before B => RETRY_ALLOWED, then B may dispatch once and confirm.
- Replace target with conflicting content => STILL_UNCERTAIN; B exits non-zero/no write.
- Corrupt/unreadable receipt => fail closed/no write.
- Change effect/tool-call ID => must not reconcile the old effect as the new one.
- Run B twice after RECONCILED_SUCCESS => neither run redispatches.

## Product-specific binding

KCode: Attempt A must use Registry + real WriteTool with ToolContext.tool_call_id. Attempt B invokes the same reconciliation primitive that a future durable-effort adapter would use.

HeliosLite: Attempt A must use ToolRegistry/ToolExecutor with ToolCallFull.call_id propagated into ToolCallContext. Because adapter injection is not yet mounted in production, the test may use a test-only registry/executor construction, but it must exercise the real Write service and stable call-ID path. Production reachability remains a separate trace row.

## Closure rule

H-F008/K-F008 move from BLOCKING to QUALIFIED_CANDIDATE only after this process-death test passes on an exact candidate. They do not become fully closed until the adapter is reachable in the intended durable workflow and independent review attacks the retry/reconciliation policy.
