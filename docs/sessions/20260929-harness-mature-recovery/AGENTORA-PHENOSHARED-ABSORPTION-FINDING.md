# Agentora / PhenoShared absorption finding — 2026-09-30

## Verdict

**NOT PROVEN ABSORBED.**

PhenoShared contains contradictory historical records:
- older absorption plans/justifications claim Agentora -> pheno / capability absorption;
- current projects/Agentora.json says historic ABSORB claims are not supported by source-level migration proof and sets KEEP_STANDALONE_PENDING_BOUNDARY_REVIEW;
- PhenoAgent was separately absorbed into Agentora (crates/pheno-agent) and PhenoShared contains copies/descendants of PhenoAgent and other runtime/support crates;
- presence of those fragments does not establish Agentora API/behavior/lifecycle parity.

Therefore the canonical harness program must treat live Agentora as a first-class donor/current implementation surface until an obligation-by-obligation parity audit proves otherwise.

## Required parity audit

Compare Agentora against PhenoShared/other claimed destinations for agent lifecycle; skills/tools registry; memory/checkpoint semantics; message routing/task dispatch; cancellation/backpressure; provider/model ports; approvals/policy hooks; event/stream semantics; retries/recovery; tracing/replay; daemon/process runtime; public SDK contracts; build/release membership; active consumers.

Classify each PRESENT_EQUIVALENT / PRESENT_CHANGED / PARTIAL / ABSENT / SUPERSEDED / REJECTED.

Do not design the new Freyr/canonical harness API by extending HeliosCLI's current harness_interfaces until this audit and external SOTA decomposition are complete.
