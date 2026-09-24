# Registry unavailable or partial delivery

Keep completed local evidence at its owner. Create a PENDING outbox record only for an intended authorized delivery, with payload digest and idempotency key. A failed request becomes BLOCKED with actual error and next retry condition; no receipt is present until a real destination accepts the correct payload.

Retry transport rather than rerunning assessment. Verify acknowledgement, scope, digest and destination identity. Detect duplicate delivery by the stable key. Conflicting revisions require the actual destination's compare-and-swap/merge semantics, not a fabricated successful response. Persist raw allowed receipts separately from rendered dashboards.

Report local acceptance and global registration separately. When new integration becomes available, replay queued events under current authority and retain original observation timestamps. Do not copy portfolio records into the tool implementation repository. Do not publish private evidence merely to make an unavailable private destination look complete.
