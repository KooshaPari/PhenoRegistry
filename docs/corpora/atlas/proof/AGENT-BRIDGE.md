# Agent bridge: observation, action and proof are separate channels

## Purpose and access classes

An agent needs to understand the product, act through its public experience, inspect actual outcomes and locate regressions. No single tool grants complete observability. The adapter advertises only capabilities it can perform and proves its own health, instance binding and behavior.

| Class | Available leverage | Qualification rule |
|---|---|---|
| Owned/white box (Civis, owned GUI/CLI) | Domain API, engine instrumentation, controlled fixtures, state snapshots, trace/profiler hooks, accessibility and native capture | Internal checks supplement but never replace actual packaged user-path and rendered-output proof. |
| Gray box (Dino, WorldSphereMod and allowed mod/plugin paths) | Permitted mod SDK/hooks, bridge IPC, selected engine state, logs, public game files plus external input/capture | Reuse the existing game bridge; record base-game and mod identity and what remains inaccessible. |
| Black box (third-party application surface) | OS input, accessibility where exposed, screen/audio capture, process/log/file observers where authorized | Judge observable behavior; do not claim structural coverage of unavailable proprietary internals. |

CivicSurvival/CivicWarfare has owned mod code and a separate host game. Classify that boundary explicitly instead of calling the entire host white box. Native desktop, browser, terminal and media applications use the same evidence contract with different adapters.

## Three action channels

**Fixture control** creates a world, seeds data, positions an actor or stages a failure. It is useful test setup but cannot prove the UI action being tested.

**Semantic product commands** exercise the actual service/domain API and verify contracts efficiently. They must not be confused with a clicked button or physical input path.

**User-path actions** use the supported input route: OS keyboard/mouse/controller/PTY, or an explicitly declared accessibility/browser semantic action. Direct engine mutation is prohibited as a substitute for the user behavior being assessed. Clicking via an accessibility action is distinct from native pointer input; both can be required for different obligations.

A test may use all three, but records every switch. Setup changes are frozen before the target observation, except for deliberate fault/control operations. After input, observe dispatch, domain effect, rendered effect and persistence as applicable. 'Command accepted' is not 'operation completed'.

## Session handshake and correlation

Bind every run to product and repository IDs; source and artifact digests; base game/mod/asset versions; supported build flags; process ID and start identity; window/render target; session nonce; selected world/save; principal/workspace; adapter version; graphics/audio profile; and actual permissions. Verify a unique harmless challenge/observation to avoid acting on a stale window or wrong named pipe.

Commands carry operation IDs, deadline, expected state/version where supported, authorization context, and explicit idempotency semantics. Events and captures carry sequence, monotonic time, simulation tick, render/presentation frame and origin. These clocks differ; record the mapping rather than equating an ECS update with a displayed frame. A fresh image hash alone cannot establish freshness when the scene is static.

Required semantics: capability discovery, observe, user action, semantic action, fixture control, wait-for predicate, frame/clip/audio acquisition, metrics, read-only diagnostic buffers, artifact export and cancellation. Names are conceptual contract operations, not claims of existing endpoints. No adapter reports success for an unsupported method.

## Observation stack

- Semantic state: scene tree/ECS, objects, components, selection, resources, workflows and permissions where permitted.
- Actual output: final color frames or external window capture, video, audio, terminal output and accessibility structure.
- Diagnostics: logs, crashes, timing, draw-call/profile data and optional depth/normal/object-ID/motion buffers.
- Durability: saved data, migrated formats, restart/rejoin behavior, external side effects and produced artifacts.

Diagnostic buffers explain defects but do not replace final presentation. Internal state and rendered pixels can independently be wrong or stale. Cross-check them. For a visible feature, a log that its system initialized proves initialization only.

## Isolation and long runs

Use per-run writable data, output paths, ports/pipes, caches and save copies; lease any native device or window. Hidden means private and nondisruptive, not permission bypass. Separate persistent authorized account/entitlement identity from disposable test state. Do not clone auth tokens or bypass DRM/anti-cheat/mutex protections to manufacture concurrency. Use supported launch/session mechanisms, independent entitled identities or serialize tests when necessary.

Do not capture the operator's desktop, private browser or live microphone as a convenient default. Use allowlisted windows/displays and redacted derivative artifacts with restricted raw masters. Bound CPU, GPU, RAM, disk and networking; keep gaming/Ableton workloads protected. Distinguish software-rendered CI evidence from qualification on the supported hardware profile.

## Negative controls

Wrong window/pipe; stale nonce or capture; old binary; missing assets; no-op input; disabled input handler; unavailable bridge; scene transition destroying a hook; main-thread dispatch starvation; dropped acknowledgement; partial operation; process crash; save corruption; unauthorized action; cross-worker data access; unavailable GPU; headless logic without rendering; and injected known-bad visuals must produce honest failures or unresolved outcomes.

The bridge must fail before corrupting an unrelated instance. A lost acknowledgement triggers state reconciliation before retry. Never assume exactly-once external effects from transport delivery alone.

## Reuse

Inspect DINOForge GameControlCli and existing named-pipe protocol, Civis capture/playthrough scripts, native accessibility facilities, Playwright, Bevy screenshot/render-target support, Godot viewport capture and Unreal/Unity testing facilities. Wrap qualifying adapters instead of writing a new per-repository transport. Put shared interfaces/normalizers in their accepted shared owner; game-specific hooks stay with the game/mod. Primary sources are listed in SOURCES.md. No native bridge was executed by this amendment.
