# Primary sources and reuse map

Consulted September 16, 2026. Documentation demonstrates available mechanisms, not portfolio implementation or vendor-wide quality. No external PDF was used in this amendment. Current native SDK/package prerequisites must be checked before implementation.

## FED-S01 — Apple: Adding support for app extensions

https://developer.apple.com/documentation/extensionfoundation/adding-support-for-app-extensions-to-your-app

Custom extension points, discovery, XPC, scope and UI support through ExtensionKit. Platform/SDK/entitlement constraints apply; not arbitrary app embedding.

## FED-S02 — Apple: App Extensions

https://developer.apple.com/documentation/appkit/app-extensions

Native extension contexts and supported extension surfaces; a limited contract, not whole-app fusion.

## FED-S03 — Microsoft: Create app extensions for Windows App SDK apps

https://learn.microsoft.com/en-us/windows/apps/develop/launch/app-extensions

Package-catalog discovery, host/provider roles and install/update lifecycle. This documented path requires MSIX identity.

## FED-S04 — Microsoft: Implementing In-Place Activation

https://learn.microsoft.com/en-us/windows/win32/com/implementing-in-place-activation

OLE demonstrates embedded object interaction and context-sensitive composite menus. Windows-specific precedent; not the proposed universal runtime.

## FED-S05 — OSGi Core 8: Resolver Service

https://osgi.github.io/osgi/core/service.resolver.html

Requirement/capability wiring, transitive resolution, contexts and diagnostic failures; reuse ideas or implementation where appropriate.

## FED-S06 — Apache Felix Framework

https://felix.apache.org/documentation/subprojects/apache-felix-framework.html

Existing OSGi R8 core implementation. Candidate only where language/runtime/operational costs fit.

## FED-S07 — XDG Desktop Portal: For App Developers

https://flatpak.github.io/xdg-desktop-portal/docs/for-app-developers.html

Desktop-resource integration with user-controlled permissions; not general GUI federation.

## FED-S08 — XDG Desktop Portal: Documents

https://flatpak.github.io/xdg-desktop-portal/docs/doc-org.freedesktop.portal.Documents.html

Scoped document access and permission revocation; portal deletion removes an entry, not the underlying file.

## FED-S09 — VS Code: Commands

https://code.visualstudio.com/api/extension-guides/command

Command contributions, context conditions, enablement and lazy activation; useful host-adapter reference.

## FED-S10 — Eclipse Theia: Extensions and Plugins

https://theia-ide.org/docs/extensions/

Different compile-time and runtime extension models; headless and frontend lifecycle must not be conflated.

## FED-S11 — Module Federation: Runtime API

https://module-federation.io/guide/runtime/runtime-api

Dynamic web remote-module and shared-dependency APIs; not a sandbox or data-authority contract.

## FED-S12 — WebAssembly Component Model: Worlds

https://component-model.bytecodealliance.org/design/worlds.html

Import/export boundaries and host/component roles; type surfaces do not establish behavior.

## FED-S13 — WebAssembly Component Model: Components

https://component-model.bytecodealliance.org/design/components.html

Recursive component composition; component memories are not exported/imported as shared memory.

## FED-S14 — Microsoft: Extensibility overview

https://learn.microsoft.com/en-us/windows/apps/develop/launch/extensibility-overview

Combines extension discovery and app services; optional package and service models have different purposes.

## FED-S15 — Eclipse Theia: Composing Applications

https://theia-ide.org/docs/composing_applications/

Existing configurable application composition and reuse; not necessary to build a new IDE shell for every product.
