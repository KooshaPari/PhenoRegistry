# Capability-first composition

Source: INT-006. This is a proposed implementation contract, not a live engine state.

## PROOF-13-01 — Composition without mounted UI
Qualify composed behavior with no requirement to mount a peer UI.

Acceptance: A host command uses a real provider with zero UI mounts and retains a coherent result.

## PROOF-13-02 — Consumed and consumable
Assess both available providers and current/credible future consumers before significant implementation.

Acceptance: A proposed handroll without owned/external alternatives or consumer impact remains incomplete.

## PROOF-13-03 — Semantic preservation
Preserve accepted behavior, error/cancellation/state/resource and consumer contracts when replacing code.

Acceptance: A faster or shorter replacement that breaks a critical consumer is rejected.

## PROOF-13-04 — Correct lowering
Select compile-time, direct-call, IPC, network or UI adapters according to actual constraints.

Acceptance: A valid in-process provider is not forced through an unnecessary network layer.

## PROOF-13-05 — Boundary fitness
Enforce domain dependency direction and real adapter contracts.

Acceptance: A prohibited UI/transport dependency introduced into the domain fails the architecture check.

## PROOF-13-06 — Independent activation
Peer discovery, permissions, absence, replacement and detach are explicit.

Acceptance: Revoked authority or absent optional peer does not silently trigger privileged fallback.

## PROOF-13-07 — Stable authority
Composed UX does not silently merge data owners, identities or lifecycle obligations.

Acceptance: Two host perspectives reference one authoritative object and reject duplicate mutation.

## PROOF-13-08 — DD proof paths
Use pure tests, real adapter tests and actual user journeys as distinct complementary layers.

Acceptance: Mocked provider success cannot satisfy a required live integration.
