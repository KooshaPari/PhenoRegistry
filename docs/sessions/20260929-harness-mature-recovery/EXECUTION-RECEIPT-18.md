# Execution receipt 18 — separate-process oracle executable; persistence denominator deepened

Date: 2026-09-30. Program remains OPEN.

## Attempt replacement oracle
Both specification branches now contain an executable separate-process `attempt_replacement_oracle.py` and targeted workflow. It creates genuinely separate Attempt-A/Attempt-B processes and durable disk state. Cases assert committed-effect reconciliation without redispatch, known-absence single retry, conflicting-state fail closed, corrupt receipt rejection, changed effect-ID rejection and repeated-B no redispatch. The new workflows are queued; no green is claimed yet.

## Product hooks
HeliosLite #333 Platform Tests and performance are in progress; other checks including focused Effect Recovery Hook remain queued. KCode #20 remains queued. Runner starvation is treated as missing evidence, not failure or success.

## Source coverage — persistence
HeliosLite H-S10 is now deeper: forge_dbd write-side serialization preserves ToolCallId/ToolResult and compression compatibility; its daemon exposes framed mutation protocol, queue depth/health and SQLite quick_check reachability. forge_repo enforces workspace ownership and read-only attached legacy history. Still open: actual mount precedence between write/read-era surfaces, queue crash/ack atomicity, schema/migration ordering/rollback and complete migration tests.

KCode K-S13 is now deeper: session persistence explicitly salvages torn/glued journal entries, continues after corrupt lines, schedules a clean full checkpoint, retains forensic backups and refuses destructive empty checkpoints over non-empty transcripts. This is strong transcript recovery evidence, but it does not close external-effect truth K-F008. Broader schema/import/compaction/concurrency/migration work remains open.

No source family is marked fully resolved merely from these samples.