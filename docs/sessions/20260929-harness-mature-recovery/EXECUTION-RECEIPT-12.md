# Execution receipt 12 — product effect hooks plus KCode macOS trust candidate

Date: 2026-09-30. Program remains OPEN.

## Product-integrated effect recovery
HeliosLite #333 head `d18b37b45e06919baaf97b2de3e978588d578e01`: optional ToolExecutor effect adapter; Write only; focused wrapper tests for intent -> dispatch -> confirm and committed effect + failed confirmation -> UNCERTAIN. Ordinary execution without adapter unchanged. CI queued.

KCode #20 head `0f1a2f5a7d80328661ff4438549d55cd60bfc488`: optional Registry effect adapter; Write only; real WriteTool isolated-filesystem tests for normal ordering and committed file + failed durable confirmation -> UNCERTAIN. Effect adapter propagation through Registry clone/WeakRegistry was corrected before CI. CI queued.

Neither candidate yet performs attempt-B reconciliation. They establish product execution seams only.

## KCode K-F002 macOS trust mutation
Direct source comparison confirms the frozen fork's startup-time `self_heal_macos_code_signature` is not present in current upstream. Upstream removes quarantine in install flow; frozen KCode strips provenance/quarantine and force ad-hoc re-signs the current executable on every macOS startup. This is a fork-specific supply-chain/runtime-identity risk.

KCode issue #21 and draft PR #22 now isolate this risk. Candidate `a9daae12bb102047b3bbb708e516a841af686036` makes startup repair explicit opt-in through `JCODE_MACOS_STARTUP_REPAIR`; normal startup is non-mutating while the historical repair path remains available for controlled local/dev recovery. macOS-native compile/policy workflow is queued.

Still required for K-F002: signed release before/after digest/signature evidence, read-only executable, unavailable xattr/codesign, repeated launch, installer interaction and final accepted release policy. No release policy is silently changed by the specification program.

## Queue state
Standalone contract jobs and product-hook jobs remain runner-queued. Queued is not green.

No merge, retirement, rebase, architecture freeze or completion gate is awarded.