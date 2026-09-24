# Implementation backlog — v0.3

All items remain `not_started`. This package authorizes planning/evidence work, not deployment or account mutation.

## WP-01 — Recover source and resolve ownership

**Priority:** P0  
**Depends on:** none  
**Requirements:** FR-DEP-001, FR-DEP-007, FR-DEP-024

**Exit evidence:** Source export indexed in this package; remaining work is canonical owner, approved check-run mapping, actual settings and missing artifact-body reconciliation.

## WP-02 — Read-only host and entitlement inventory

**Priority:** P0  
**Depends on:** WP-01  
**Requirements:** FR-DEP-002, FR-DEP-004, FR-DEP-008

**Exit evidence:** Installed runtime/version/capability records and per-repository plan/settings snapshot; no mutation.

## WP-03 — Specify trusted promotion boundary

**Priority:** P0  
**Depends on:** WP-01, WP-02  
**Requirements:** FR-DEP-006, FR-DEP-009, FR-DEP-010, FR-DEP-011, FR-DEP-012, FR-DEP-013

**Exit evidence:** Reviewed gate/state-machine contract with negative fixtures and actual credential boundary.

## WP-04 — Prove one disposable local service

**Priority:** P1  
**Depends on:** WP-02, WP-03  
**Requirements:** FR-DEP-003, FR-DEP-005, FR-DEP-016, FR-DEP-017, FR-DEP-018

**Exit evidence:** Exact-version Podman/WSL service evidence, restart/failure/resource tests and a measured runtime comparison.

## WP-05 — Qualify one private ingress and one SSE path

**Priority:** P1  
**Depends on:** WP-04  
**Requirements:** FR-DEP-014, FR-DEP-015, FR-DEP-019

**Exit evidence:** Positive/negative identity tests, origin bypass check, full-chain streaming and bounded failover traces.

## WP-06 — Prove stateful recovery and adapter boundaries

**Priority:** P1  
**Depends on:** WP-04  
**Requirements:** FR-DEP-020, FR-DEP-021, FR-DEP-022, FR-DEP-023

**Exit evidence:** Restored disposable data, migration decision, single state writer, digest-controlled update flow.

## WP-07 — Integrate approved docs and evidence

**Priority:** P1  
**Depends on:** WP-05, WP-06  
**Requirements:** FR-DEP-024

**Exit evidence:** Atomic or staged cross-repository PR plan, regenerated index links, complete receipts and remaining-limitations statement.

## WP-08 — Repair shared workflow and verification contracts

**Priority:** P0  
**Depends on:** WP-01  
**Requirements:** FR-DEP-027, FR-DEP-029, FR-DEP-034

**Exit evidence:** Supported pinned workflow paths, exact emitted checks, explicit secrets and a disposable invocation receipt.

## WP-09 — Implement local delivery profiles and nightly predicate

**Priority:** P0  
**Depends on:** WP-02, WP-08  
**Requirements:** FR-DEP-025, FR-DEP-026, FR-DEP-033

**Exit evidence:** Local dev placement, schedule truth table, offline catch-up, target serialization and negative ingress proof.

## WP-10 — Qualify provider artifact, service bindings and recovery

**Priority:** P0  
**Depends on:** WP-09  
**Requirements:** FR-DEP-028, FR-DEP-030, FR-DEP-031

**Exit evidence:** Immutable tested image observation, emulator-vs-service action tests, stateful rollback/restore and provider source-mode fixtures.

## WP-11 — Integrate compaction-safe source intake into existing evidence owner

**Priority:** P1  
**Depends on:** WP-01  
**Requirements:** FR-DEP-032

**Exit evidence:** Idempotent provenance import with original hashes/ranges and explicit author/evidence classes; no second global ledger.

## WP-12 — Reconcile current owners and historical local-cloud branches

**Priority:** P0  
**Depends on:** WP-01  
**Requirements:** FR-DEP-035, FR-DEP-036, FR-DEP-044

**Exit evidence:** Current owner/module map plus accepted/rejected contract diff from historical BytePort local-cloud branches; no blind branch resurrection.

## WP-13 — Specify and qualify local node daemon and capability inventory

**Priority:** P0  
**Depends on:** WP-12, WP-02  
**Requirements:** FR-DEP-037, FR-DEP-042

**Exit evidence:** Versioned node identity/capability contract, private enrollment flow and read-only inventory receipts on at least one disposable or non-impacting node.

## WP-14 — Implement resource reservation, modes and preemption fixtures

**Priority:** P0  
**Depends on:** WP-13  
**Requirements:** FR-DEP-038, FR-DEP-039, FR-DEP-043

**Exit evidence:** Admission/preemption truth tables covering interactive, creator/audio, gaming, LLM, idle and stateful negative cases with no foreground starvation claim beyond measured fixtures.

## WP-15 — Bind CI artifacts to local lifecycle management

**Priority:** P0  
**Depends on:** WP-08, WP-13  
**Requirements:** FR-DEP-040, FR-DEP-041

**Exit evidence:** Immutable artifact build receipt, node pull/observation, health transition and daemon/workload rollback on a disposable service.

## WP-16 — Unify GUI API CLI SDK and agent automation contract

**Priority:** P1  
**Depends on:** WP-12  
**Requirements:** FR-DEP-045, FR-DEP-046

**Exit evidence:** Same plan/apply/observe operation demonstrated through API and at least two clients without hidden surface-specific state.

## WP-17 — Converge audit and scorecard systems into Assessment Dossiers

**Priority:** P1  
**Depends on:** WP-01  
**Requirements:** FR-DEP-047, FR-DEP-048

**Exit evidence:** One real repository dossier where Phase A inventory leaves scores unknown and Phase B executes qualified measurements; legacy scorecard mapped as a profile rather than copied truth.

## WP-18 — Recover and integrate Emergent Garden Wave 5 authority

**Priority:** P0  
**Depends on:** WP-01  
**Requirements:** FR-DEP-049, FR-DEP-050

**Exit evidence:** Exact PR-81 payload preserved, reconciled against current main, package/tests rerun, landed or explicitly superseded, and projection status corrected.

## WP-19 — Inventory reviewer providers and enforce zero-spend broker policy

**Priority:** P0  
**Depends on:** WP-01  
**Requirements:** FR-DEP-051, FR-DEP-052, FR-DEP-053, FR-DEP-056, FR-DEP-057

**Exit evidence:** Live provider capability/quota snapshot, cash-spend=false enforcement, risk-tier dispatch fixtures, and deterministic gates proven independent of semantic-review outages.

## WP-20 — Reconcile historical review backlog

**Priority:** P0  
**Depends on:** WP-19  
**Requirements:** FR-DEP-054, FR-DEP-055

**Exit evidence:** Sample merged/open PR backlog classified finding-by-finding; surviving defects linked to remediation PRs and stale/fixed/duplicate findings have evidence-backed dispositions.

## WP-21 — Measure reviewer marginal yield and tune provider routing

**Priority:** P1  
**Depends on:** WP-19, WP-20  
**Requirements:** FR-DEP-058

**Exit evidence:** Per-provider unique-valid-finding, duplicate, false-positive, remediation, latency and quota-efficiency report sufficient to justify or reject a sixth default semantic reviewer.
