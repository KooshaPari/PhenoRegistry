# Execution receipt 24 — Helios mounted interface families separated

Date: 2026-09-30. Program remains OPEN.

## Recovery freeze point
Helios #333 latest exact head `0e95f160...` is rerunning after formatting/dead-code cleanup; Cargo Deny is green and Platform Tests in progress. Recovery remains classified QUALIFIED_CANDIDATE_PRIMITIVE / REACHABILITY_OPEN pending exact-head regression evidence. No further speculative adapter API is being added without a consumer.

## Mounted interfaces
Frozen Helios `forge_main::run` proves several top-level surfaces are directly mounted before normal ForgeAPI/UI startup: AgilePlus commands, LSP commands and ShareCLI commands each dispatch and return/serve independently. The normal path separately handles config validation, accessibility audit, worktree selection and UI/ForgeAPI initialization.

Architecture consequence: these early-exit subcommands are distinct product journeys/authority paths. They cannot be assumed to inherit agent/tool runtime recovery, conversation persistence, evidence or hook semantics merely because they share one binary. Source ledger H-S08 now records this and requires exhaustive TopLevelCommand/MCP/noninteractive/stream-json/feature-binary reachability mapping.

## KCode
KCode recovery primitive remains exact-head green; active work is retained-patch/existence reduction rather than expanding the fork.

No completion or merge verdict.