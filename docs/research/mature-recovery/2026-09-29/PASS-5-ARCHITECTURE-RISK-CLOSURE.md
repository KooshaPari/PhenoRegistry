# Pass 5 — architecture-risk closure transition

Date: 2026-09-30.

## ShareCLI

Exact native run `36686200573`, job `109792530472`, establishes four distinct incorrect-reuse classes through the real Hypervisor:

1. Git mode: changed file bytes with stable HEAD/status shape → stale result replayed.
2. Args mode: same argv in different workspaces → first workspace result replayed.
3. Git mode: relevant environment change → old environment result replayed.
4. Time mode: external state change → old external-state result replayed.

These failures falsify the architecture hypothesis that one generic arbitrary-command durable cache can be made correct merely by selecting one of the recovered key modes. The product-local architecture candidate now defaults unknown equivalence to execution/bypass and moves optimization behind explicit semantic adapters/tool-native caches. In-flight duplicate suppression is a separate decision from durable replay.

This is a meaningful architecture-gate delta, not merely four bug tickets.

## BytePort

BP-F03 remains exact native reproduced. The first BP-F04 probe was invalid and is explicitly rejected. A corrected GORM callback injects Project-create failure only after provider deployment remains reachable. In the full red package run it did not fail while BP-F03 did, but an isolated workflow has been added so BP-F04 receives its own criterion receipt; that workflow is pending.

Product-local architecture candidate now favors:
- BytePort-owned Project/SourceSnapshot/ManifestRevision/DeploymentIntent/Operation/evidence/reconciliation;
- delegated established build engine returning immutable BuildArtifact identity/provenance;
- NanoVMS/runtime behind a provider adapter.

BytePort-owned generic build engine remains an alternative to falsify; provider-owned source build is currently unsupported by inspected NanoVMS boundary/API evidence.

## Why this changes the forward program

The next implementation work is no longer “fix cache key” or “replace project.UUID with sandbox ID.”

For ShareCLI, the next experimental object is the equivalence-adapter boundary and queue/lease ownership semantics.

For BytePort, the next experimental object is the tiny immutable source→manifest→artifact→runtime fixture plus durable operation/reconciliation behavior.

Production fixes that bypass these identities are premature and should not be accepted merely because they make the first negative tests green.

No completion percentage. Source denominator, full mature obligations, independent review and architecture experiments remain open.
