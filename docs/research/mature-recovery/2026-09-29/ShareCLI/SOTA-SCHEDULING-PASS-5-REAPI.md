# ShareCLI SOTA pass 5 — action identity, CAS, in-flight dedup

Date: 2026-10-01.

## REAPI / Bazel

The Remote Execution API models a reproducible Action using digests for:
- Command;
- complete input-root Directory/CAS tree;
- execution properties/timeout and related identity-bearing configuration.

ActionResult is separately cacheable. CAS stores content by digest; ActionCache maps action identity to result.

Important semantic distinction: an execution request may skip cache lookup yet still be merged with another in-flight execution of the same action.

This directly validates ShareCLI's v1.2 separation:
- EquivalenceDecision::InFlight;
- EquivalenceDecision::Durable;
- ResultArtifact/CAS-like immutable subject;
- adapter-defined complete input identity.

Decision:
**ADAPT REAPI action/CAS semantics where workload adapters can provide reproducibility.**
Do not attempt universal REAPI identity for arbitrary opaque commands.

## Buck2

Buck2 can use REAPI-compatible services and independently configures:
- remote execution engine;
- ActionCache;
- CAS;
- digest algorithm;
- execution platform/properties;
- local+remote hybrid execution;
- remote-cache behavior;
- resource units and gang workers.

Implications:
- execution location, cache eligibility and action identity are independent dimensions;
- adapter execution properties may participate in identity;
- ResourceVector/Placement can include remote resource units/gang requirements;
- existing REAPI services (BuildBarn/BuildBuddy/EngFlow-compatible) are possible providers rather than ShareCLI-owned infrastructure.

## Bootstrap consequence

For reproducible adapter families:
`Invocation -> adapter ActionIdentity -> InputRootDigest -> EquivalenceDecision -> InFlightGroup / ActionCache -> ExecutionProvider -> ResultArtifact`.

For opaque/unqualified work:
`Invocation -> BYPASS sharing -> scheduler only`.

The scheduler may still pack/queue opaque work based on ResourceVector without claiming semantic equivalence.

## Falsified shortcut

Hashing command-line arguments plus cwd/time/git metadata is not a substitute for an adapter-qualified complete input/action identity.

## Next implementation consequence

SC-WP-A04 should eventually support an optional structured ActionIdentity/CAS subject from adapters rather than only a string key. This is additive Tier-A evolution; legacy generic modes remain transition scope.
