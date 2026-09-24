# Reuse-first platform lowering

The semantic contract is cross-platform; the execution and visual adapters are platform-specific where needed. Keep the matrix current with actual OS/SDK versions and packaging/entitlement constraints. These researched sources establish available mechanisms, not that the portfolio has already integrated them. See [sources](SOURCES.md).

| Mechanism | Useful part | Important limit / proposed role |
|---|---|---|
| Apple ExtensionFoundation + ExtensionKit | Declared extension points, discovery, XPC, optional extension UI and sandbox policy | Version/entitlement-specific; not universal embedding of any arbitrary installed app. Prototype native host/extension behavior on the supported Macs. |
| Windows app extensions + app services | Package-catalog discovery, lifecycle events, two-way service integration | Documented app-extension path requires package identity. Keep unpackaged behavior explicit. |
| OLE in-place activation | Established host/container presentation with contextual menus and embedded objects | Windows-specific historical mechanism; valuable UX precedent, not universal modern core. |
| XDG Desktop Portals + D-Bus | User-mediated scoped desktop resources, document handles, service activation | Portal availability depends on environment/backend. Portals are not an arbitrary UI compositor. |
| OSGi capability resolver / Apache Felix | Explicit requirements, providers, transitive resolution, dynamic service lifecycle | Excellent reference/reuse candidate where its runtime fits; do not add a JVM to every Rust app without need. |
| VS Code / Eclipse Theia | Commands, context predicates, views, service and host extension models | Existing domains have specific APIs and lifecycle. Theia distinguishes compile-time extensions from runtime plugins; do not pretend all are interchangeable. |
| Module Federation | Dynamic remote module loading and dependency coordination in web hosts | Not security, permission, lifecycle or domain-semantic proof. Use only with matching web runtime/trust profile. |
| WIT / WebAssembly Component Model | Typed import/export boundaries and composition of components into components | Interfaces do not specify behavior; components do not offer arbitrary cross-component shared-memory semantics. Select for suitable portable isolated computation. |
| Native direct calls / qualified ABI | Lowest-overhead local composition | ABI/version/ownership and trust must be explicit. No forced network round trip for same-process work. |
| Window/video remoting | Compatibility fallback for applications with no semantic integration | A picture is not a native semantic applet. Declare degraded accessibility, focus, clipboard, DPI/HDR and latency behavior. |

## Surface strategy

Prefer a native or host-native contribution adapter using a shared domain API. For simple inspectors/forms, evaluate a constrained declarative view model rendered natively by each host. For complex surfaces, use a dedicated qualified native adapter or isolated webview/canvas with the required input/accessibility bridge. Do not handroll an entire universal UI toolkit merely to make every app look similar.

Maintain explicit conformance tiers: linked launch, contextual handoff, embedded surface, native semantic contribution, and full workflow federation. A lower tier can be useful. It cannot claim a higher tier because its panel shares the color palette.

## Locality and rendering

A Swift UI subtree cannot be assumed embeddable inside arbitrary Tauri/GTK/WinUI/Bevy windows with no adapter. An installed app requires exposed contracts or a maintained integration adapter. An engine/rendering surface may need its own event loop, device/context, process and output transport. The runtime negotiates a valid path or advertises a lower integration tier.

Use PhenoFabric's existing locality work when a surface/service actually crosses processes, VMs or devices. The federation layer chooses the capability and perspective; transport should not decide who owns product data. Shared GPU resources, audio clocks, input capture and color conversion retain their technical qualification requirements. No universal AV1 or zero-copy assumption belongs in the federation contract.

## Build and distribution

Standalone and integrated modes should share authoritative implementation packages and tests. Version the contribution SDK and integration recipes independently where useful, while recording tested combinations. Reuse supported package/discovery systems and existing app release pipelines. Avoid a central deployment that replaces all applications merely to enable one integration.

Every installed host/provider combination needs real package installation, process identity, permission and update testing—not only source-tree module tests. Keep upstream licenses, attribution, maintained patches, entitlement requirements and an exit path visible. Reuse our own capabilities as upstreams before copying them per host; choose an external facility where it better satisfies the contracts.
