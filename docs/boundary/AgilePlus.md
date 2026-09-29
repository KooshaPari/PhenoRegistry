---
repo: "AgilePlus"
product_id: "PRD-AGILEPLUS"
role: governed-specification-and-work-execution-engine
status: active
last_boundary_review: 2026-09-29
contract: AGP-MATURE-V1
---

# Boundary — AgilePlus

## In scope

- repository/project work identity and scope;
- intake, triage and backlog;
- specification/research/planning;
- work-package DAGs and lifecycle;
- resource claims, leases, worktrees and execution isolation;
- agent dispatch, monitoring, retry and receipts;
- review loops and escalation;
- governance contracts, evidence requirements and progression gates;
- validation, shipping, rollback and retrospectives;
- immutable execution/audit history;
- CLI/API/gRPC/MCP/dashboard execution surfaces;
- external PM/source sync where configured;
- reciprocal Tracera product-context federation.

## Out of scope

| Fact/capability | Canonical owner |
|---|---|
| Mature product identity/intent/hierarchy | Tracera |
| Product dissatisfaction and product-stage assessment | Tracera |
| Source content and Git object truth | source repository/Git |
| Measurement/test result truth | producing verifier |
| Generic agent runtime identity | agent-runtime owner |

## Key rule

**Work completion is not product acceptance.** AgilePlus reports what work was specified, attempted, reviewed, gated and completed. Tracera decides what that means for accepted product state using independently admissible evidence.

## Stale prior boundary

The July 17 registry boundary described AgilePlus primarily as a 94-crate mega-workspace with ARCHIVE_ONLY/proposed spine disposition. That snapshot is retained as historical evidence but is not the current product boundary.
