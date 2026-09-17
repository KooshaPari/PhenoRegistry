> **v1.4:** federation can have zero peer UI mounts. Features, results, workflows and headless services are the primary composition units. See [capability-first clarification](../proof/CAPABILITY-COMPOSITION.md).

# Seamless experience means shared interaction, not shared wallpaper

## One host grammar

The host owns its navigation hierarchy, toolbar placement, command palette, focus policy, accessible structure and primary task vocabulary. An extension supplies bounded contributions, not a second menu bar and sidebar wrapped in another window. The same task remains recognizably the same task in either perspective; words can be contextualized without changing its semantics.

A contribution declares a stable command/view ID, target object kinds, accepted slot types, context predicate, enablement predicate, help, permission need and unavailable/error behavior. Context predicates control discoverability, not authorization. The provider rechecks permission and preconditions when the command executes.

Slots include detail inspector, contextual panel, primary task view, inline editor, preview, result card, command, context menu, search provider, notification and headless operation. A host advertises supported versions, allowed isolation modes, layout constraints and lifecycle. Unknown slots do not become arbitrary HTML injection points.

## Shared context, distinct authority

Pass explicit object references, schema/version, workspace/principal, selection, permitted actions and bounded navigation state. Avoid global mutable 'current project' variables, filesystem-path identity, and implicit sharing of every selected object with every app. Different Windows/macOS/Linux sessions may map to the same person only through an explicit trusted identity relation, not matching usernames.

Deep links resolve stable objects, then choose a compatible installed host under user preference. A link may open a work item in AgilePlus or its integral surface in Tracera without duplicating the underlying record. Deleted, forbidden, migrated and incompatible targets have distinct explanations. Back/forward history does not bounce between top-level application launchers.

## Focus and command routing

Exactly one focus owner handles an input event in a view. Resolve shortcut conflicts through explicit host precedence and user overrides; retain accessibility and platform shortcuts. Relative mouse capture, IME, pen, drag/drop and clipboard require declared support for specialist surfaces. A remote/pixel surface cannot claim native accessibility or text semantics it does not expose.

Opening another app does not steal an existing editing session or cancel its work. Commands carry stable operation IDs and expected versions. UI retries cannot repeat non-idempotent actions with a new operation ID. A global command palette does not imply a global undo stack: commands advertise local undo, compensating action or irreversibility, and the UI explains partial multi-owner outcomes.

## Settings, search and notifications

Provide one contextual settings entry with namespaced ownership, precedence and effective-value explanation. App-local settings do not silently become workspace-wide settings. A shared search view performs permission-filtered queries and deduplicates by authoritative object ID; it does not merge all databases or leak private result counts/snippets. Search/backend failure remains visible without blanketing the whole host.

Deduplicate notifications by operation and audience. Show a single status/progress surface for shared work, with authoritative owner available in details. Avoid duplicate trays, sign-in dialogs and progress bars. Errors should identify the failed capability and safe recovery action without requiring the user to understand repository boundaries.

## Native quality and visual restraint

Preserve platform-appropriate keyboard behavior, menus, drag/drop, touch/pen, high-DPI scaling, screen-reader semantics and OS-level lifecycle. Reuse the accepted design tokens and editable asset lineage. Theme conformance does not justify hiding provenance or impersonating another publisher. Integrated areas may expose unobtrusive provider details in an inspector, permissions page or troubleshooting view while remaining part of the primary experience.

The desired richness is purposeful: layered/2.5D/3D assets, smooth transition, good materials and contextual motion where they clarify an action. Supply reduced-motion, reduced-transparency, high-contrast and static/low-power fallbacks. Do not place an always-running 3D canvas behind routine tables. GPU/CPU/audio budgets and cold/warm paths must be profiled with actual foreground contention.

Screenshots are evidence of pixels, not proof of interaction. Native accessibility checks, keyboard journeys, wrong-context commands, multiwindow behavior and failure recovery must accompany the visual review. No universal millisecond budget is invented here: each selected profile declares and measures its own frame/input/startup/RAM/energy limits relative to standalone baselines.

## Standalone, embedded and app-center modes

The same capability may have a full standalone experience and several embedded views. Share domain logic and use host adapters; do not fork the feature implementation per host. A full standalone shell is not the default embedded contribution. A provider can offer a compact inspector without exposing all its settings and unrelated features.

CLI-only tools contribute actual typed operations, job status, results and optional inspectors. A host can render those surfaces without turning the tool into an invented GUI product. CLI stdout remains a machine contract: no extra banners or UI-control escapes in JSON/MCP output. VHS captures actual standalone and host-mediated command journeys.

## Concrete 'feels like one app' acceptance

Select an object in A; invoke a contributed B action without copying IDs, ports or credentials; see appropriate progress and errors; edit through the real B authority; undo or compensate where declared; search for the object once; open the same object from B with equivalent state; use keyboard and assistive technology; restart and recover. At no stage should the user need to understand a repository boundary just to complete the qualified workflow.
