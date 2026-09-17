# Runtime architecture and explicit contracts

## Distinct planes

| Plane | Responsibility | Authority boundary |
|---|---|---|
| Package/discovery adapters | Observe approved installed artifacts and capability manifests | Do not execute arbitrary package hooks to discover metadata |
| Resolver and composition planner | Match requirements, versions, trust, scopes, locality and resources | Produces a proposed plan, not new permission |
| Policy and grants | Decide whether a binding may activate and execute | Provider still enforces scope on every operation |
| Service activation | Start or lease the needed provider instance lazily | Avoid full application startup for a single capability |
| Experience host adapters | Mount views and route commands/context coherently | Host chrome and focus are not data ownership |
| State/data adapters | Resolve object handles, versions and transformations | Exactly one declared writer authority per entity/field contract |
| Diagnostics | Explain selected providers, failures and drift | Observation does not authorize mutation |

Reuse qualified native extension catalogs, IPC, registries and parsers. A shared library can implement neutral contracts; installations hold their own scoped runtime binding state. This must not become hardcoded portfolio data inside AgilePlus or PhenoDocs. An installation/runtime capability catalog is useful infrastructure, not the portfolio's product-truth registry.

## Inputs and negotiated output

An installation manifest identifies product/package/artifact version, publisher, allowed activation endpoints, provided and required capabilities, supported host surfaces, platform profile, owned state, lifecycle, resource constraints and extension recipes. A recipe is declarative and versioned, naming match conditions, context mapping, contributions, permission requirements and failure/detach policy. It is not arbitrary install-time code.

A composition plan pins package/contract versions and artifact identities; binds consumer capabilities to providers; records principal/workspace scope, approved grants, transport/isolation, service instance keys, surfaces, startup dependencies, rollout/recovery and expiration/revalidation conditions. Synthetic examples in this amendment illustrate shape only. A signed plan or matching schema cannot prove behavioral compatibility by itself.

Compatibility has at least five parts: type/interface compatibility, semantic behavior, lifecycle/error behavior, security/resource requirements and host-surface support. A matching string such as `tasks` is insufficient. Probe declared handshake/conformance fixtures before activation. Missing required capabilities yield a concrete unresolved plan, not a null provider or successful empty output.

## Resolution order

Filter by visibility/trust/platform first, then by version and semantic contract, then by required scopes and resources. Prefer the user's valid pinned provider. Otherwise use approved workspace policy and tested recipes, with deterministic tie-breaking and explicit ambiguity where choices matter. Do not equate newest, local, cheapest, largest or first-discovered with always best.

Do not recompute all pairwise integrations continuously. Index typed capability offers; maintain affected bindings incrementally; retain known-good plans when inputs are unchanged; invalidate only dependent plans when packages, policy or contracts change. Explicitly report incomplete observations. Optional capability discovery must not materialize every UI view or load every implementation.

## Host-relative composition

A perspective record identifies the host application/window, root context, selected recipe set, view layout and user customizations. A binding record identifies the provider, consumer, contract and execution scope. A service lease identifies the actual instance and references. These are different records so opening a second perspective does not automatically duplicate a job or shift the data authority.

Two hosts can use one provider instance only where identity, configuration, trust, isolation, resource and tenancy scopes agree. Identical command text does not make computations safely shareable. A conflicting scope creates separate instances or fails according to policy, never leaks data to save memory.

## Recursion and cycles

Composites re-export only an intentional bounded contract, including required dependencies and failure behavior. A product-level applet need not reveal internal provider names. A composite can be embedded by another host while retaining the underlying child provenance.

Visual mounting and strict startup prerequisites must be acyclic in the initial implementation. Cross-calling workflows may contain cycles only through explicit asynchronous/event protocols with origin, correlation, deduplication and hop/rate bounds. Reciprocal perspectives are not reciprocal full-shell embedding. Stable instance IDs and reentrancy rules stop an A panel inside B from recursively mounting all of A's B panels.

## Locality and fast paths

Do not convert every boundary to RPC. Same-process qualified components can use direct calls; same-OS processes can use appropriate IPC/shared-memory/handles; VM paths can use qualified shared-memory/device interfaces; LAN/WAN paths use negotiated transport and serialization. Preserve existing PhenoFabric locality and deadline goals without pretending arbitrary code or views can be remotely placed.

Security boundaries justify unavoidable copies and checks. Zero-copy is a measured implementation property of a specific route, not a promise inferred from a shared-memory field. Heavy rendering/audio/GPU providers activate only for demanded work and remain under resource admission; background discovery is event-driven and bounded.

## Shared failure domains

A minimal local broker is a possible implementation choice, not an excuse for a single fragile mandatory daemon. Define what survives broker restart: existing safe connections, known-good bindings, no new grants, and reconnect identity. No unbounded auto-restart storm. Expose a disabled-integration mode so the host's independent functions remain usable while debugging a provider.
