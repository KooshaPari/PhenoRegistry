# Pass 19 — handoff boundary and expanded semantic controls

Date2026-09-30. Exactly Dino + Civis.

## Developer handoff status

Both products are **ready for bounded experimental developer-agent work**, but neither is ready for production integration handoff.

Dino experimental handoff: generation facade/builder/consumer acknowledgement prototypes only. Production gate requires all generation prototype controls green plus consumer semantics and native-host plan.

Civis experimental handoff: semantic state-manifest/v6 encoding experiments only. Production gate requires expanded semantic controls green, full future-affecting state classification, legacy/migration/atomicity policy and mounted save authority.

Product-local `DEVELOPER-HANDOFF-GATE.md` files define concrete WPs.

## Expanded Civis controls

Beyond the three reproduced failures, recovery tests now probe:
- high-level control-policy kind separately from economy PolicyInput;
- market prices/state continuity;
- deletion of metadata from a freshly written current-format bundle, which must not silently downgrade to legacy.

The semantic manifest prototype was extended to policy kind and market prices. These additions remain candidate semantics until runner results and state-authority review.

## Targeted SOTA

Dino pass2 uses Kubernetes Server-Side Apply only as conceptual prior art for manager ownership/conflict/omission-removal and TUF snapshot metadata for consistent-generation views. Neither is proposed as a dependency.

Civis pass2 distinguishes Wasmtime compiled module/component serialization from product semantic runtime-state persistence. Wasmtime resource handles have instance/store ownership semantics; Civis must own mod artifact identity and compatible guest-state reconstruction rather than treating compiled-component serialization as a save solution.

## Catalog safety

Civis current audit is incorporated as supporting evidence, not as mature denominator. Synthetic ranges, dead bindings and collisions remain quarantined.
