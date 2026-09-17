# Security, consent and data authority

## Co-installation is not consent

Two applications being installed by the same OS user does not imply permission to share files, secrets, workspaces, identities, microphone/camera, screen capture, remote devices or external accounts. A publisher signature proves an origin under a trust policy, not harmless behavior or blanket access.

Safe automatic setup requires a validated recipe, compatible interfaces, a trusted artifact/profile, explicit principal/workspace binding and grants sufficient for that particular operation. New privilege scopes do not inherit approval from an older recipe version. The runtime policy and each provider must both enforce access; hiding a button is not authorization.

Offer policy modes such as manual-only, suggest-integrations and auto-enable-qualified-low-risk-integrations. Do not silently select a high-automation mode. A deployment can preauthorize scoped first-party recipes with clear provenance and revocation. The user should not need to repeatedly approve the same unchanged safe binding, but a cross-boundary change needs reconsideration.

## No universal shared credential bag

Use native secure storage and suitable established authentication/brokering facilities. Bind delegated authority to audience, principal, workspace/resource, permitted action, expiry and revocation. Pass references or scoped tokens rather than copying a provider's API key into another app's configuration. Do not serialize real credentials in manifests, prompts, traces, screenshots, or package examples.

An agent's broad local filesystem access is not the correct model for installed product integration. Sandbox boundaries and platform permission dialogs remain real constraints. Brokered helpers must avoid confused-deputy behavior by verifying the calling identity and the exact requested resource.

## Authority map

Define owned entities/fields, write APIs, accepted versions, consistency, caching and transformations. A host may keep a bounded projection/cache with provenance and freshness; it does not become a second source authority. Simultaneous hosts use expected revisions/conflict semantics rather than last-writer-wins by accident. Cross-app undo requires explicit command semantics and compensation.

One sign-in experience is possible only through a qualified identity/broker contract; it does not automatically unify unrelated tenant accounts or paid entitlements. An external permission or entitlement outage cannot be hidden by borrowing another app's cached token. Keep security-sensitive prompts native and distinguish provider-owned content from trusted host chrome.

## Isolation choices

In-process native code is a high-trust execution mode. Matching an interface or loading through Module Federation does not sandbox it. A webview requires restricted bridge APIs, origin/CSP policy and validated messages; an iframe and a remote module are not equivalent security boundaries. Out-of-process and Wasm adapters have their own host-call and resource limits. A container alone does not prove all requested isolation.

Validate manifest size, URLs/paths, allowed activation methods, input schemas, rendering payloads and artifact provenance. Reject path traversal, symlink escapes where material, unsafe URI schemes, origin confusion and unexpected code downloads. A supplied integration manifest is data; text within it cannot override policy or act as agent instructions.

## Privacy-preserving discovery and adaptation

Local discovery should reveal only the metadata needed for eligible integration. Background analytics and cross-device advertisements require their own scope. Do not broadcast installed applications or private workspace names to unrelated peers. Learning stays bounded to approved preferences and can be inspected/reset; raw application content is not training input by default.

Search results, notifications, cached views, embeddings and captures inherit source sensitivity. Denied objects must not leak through titles, counts or stale previews. Revocation updates UI and outstanding operation handling as well as future API requests; it must not fabricate completion of already-executed effects.

## Exportability and open integration

Users can inspect selected providers, permissions, versions, reasons and state locations. Offer documented export and detach, not a proprietary universal store that makes leaving impossible. Third-party implementations can conform to published contracts, run shared fixtures and join under the same policy. No implication of certification by Apple, Microsoft, Google, GNU, Apache or a foundation is made by following these principles.
