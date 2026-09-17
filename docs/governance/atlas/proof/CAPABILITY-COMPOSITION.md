# Capability-first composition: one product experience, several implementations

## The corrected abstraction

Two apps may contribute to the same user outcome without showing two apps, any embedded window, a plugin panel or a visible applet. A host can acquire a new command, transform, search source, persistence operation, runtime, renderer, evaluator or workflow step. Its own interface expresses the result. An embedded surface is one implementation option, not the definition of integration.

A Tracera capability can create or inspect real governed work through AgilePlus while Tracera renders the interaction in its own language. BytePort can use ShareCLI supervision and show deployment health without a second supervisor UI. Melosviz can acquire a qualified render/export provider, leaving the user in one editing workflow. A game can use a shared terrain or replay capability without exposing the library's brand. These are proposed examples, not implemented-product claims.

The proof is behavior with the provider present, absent, replaced, revoked and failed. A screenshot of a combined shell does not prove any of it. Conversely, a valid composition with zero UI mounts is not less federated.

## Composition planes

| Plane | Unit and obligation |
|---|---|
| Build/source | Use an owned or external package through a published contract; no casual source copy. |
| In-process | Direct calls, shared types and appropriate ownership for low overhead. |
| Runtime service | Scoped local IPC or network requests where lifecycle/isolation justifies them. |
| Data/document | Operate on authoritative objects using stable IDs and explicit read/write contracts. |
| Workflow | Compose results, cancellation, approvals, compensation and progress across capabilities. |
| Interaction | Host-rendered commands, tools, modes and semantics; accessible user behavior. |
| Surface | Optional native view, isolated web surface, remote pixels or bounded applet panel. |
| Deployment | Discover installed providers, reconcile versions/scopes and activate qualified bindings. |

These are not a maturity ladder. Use the least costly valid combination. Not every capability needs hot loading, a process, a registry, a universal database or network RPC. Optional dynamic resolution complements compile-time composition; it does not replace sound typed boundaries.

## Two-way engineering responsibility

Every substantial project change examines both directions: what existing capabilities should this implementation consume, and what useful capability can it expose for others? Search actual owned packages and accepted consumers, external libraries, upstream forks and relevant research. Prefer native facilities and mature implementations; then adaptation, narrow wrapping, upstream patching and small maintained deltas. New custom logic is justified by a recorded semantic or operational benefit, not a preference to own every line.

Least custom code is not fewest source lines at all costs. A short opaque expression, a slow generic layer or a dependency with an incompatible security model can raise total burden. Preserve accepted performance, numerical behavior, failure semantics, compatibility, privacy, resource and accessibility properties. Compare ecosystem-wide maintenance, not just local LOC. Avoid universal wrappers that duplicate a dependency's entire API.

Current supported consumers need real compatibility tests; committed future consumers need explicit contracts/spikes; plausible future consumers justify inexpensive seams, not speculative features. Unknown external consumers are not zero consumers. One owner chat is a write boundary, not a reasoning boundary. Coordinate shared package changes and migrations with their owners.

## Hexagonal and recursive constraints

Pure domain behavior stays independent from concrete UIs, engine bindings, providers and deployment. Ports express semantic operations, not incidental vendor APIs. Adapters explicitly translate error, retry, cancellation and data behavior. Architecture fitness checks validate dependency direction and prohibited imports. Consumer-driven contract tests validate adapters. Fake adapters support narrow tests; real adapters must qualify integration and installed E2E.

A composite can expose a reduced interface and participate at the next level. Recursive identity does not imply recursive full-shell nesting or unrestricted permission inheritance. Distinguish installation graphs, service dependency graphs, data authority and user perspective. Discovery metadata is not consent; learned suggestions are not execution permission. Headless provider changes must remain diagnosable even when the integrated experience hides the component boundaries.

## Required witness

First demonstrate a zero-mount capability contribution through an existing host command. Verify that the underlying real object or result changes, both sources agree, the host remains coherent, a revoked permission fails correctly, no optional peer breaks the standalone host, and uninstall/detach preserves authoritative data. Then try a second consumer so the port is not secretly one hardcoded pair. Do not build another mandatory App Center before this works.
