# Khostty SOTA / bootstrap gate — pass 6

Research date: 2026-09-29. Frozen Khostty subject `a29aa9c6553d9f42aa68e2919116c0f6d53f329d`. Current upstream comparator `ghostty-org/ghostty@f9e82709360d97b2246718f774c544de0f16787b`.

## Result: both headline product deltas are now contested prior art

Khostty's repository-level differentiation cannot rest on either 'Ghostty with agent control' or 'Ghostty on Windows'. Both have substantive same-family implementations.

### Agent control baseline — Ghoztty

Pinned `dzearing/ghoztty@fd3838acfa834c29e99616cdc8500c0208a13a09`, MIT root license.

Source-inspected capabilities include:
- named/idempotent windows and panes;
- working directory + command launch;
- PTY child input via `+send-keys`, not parser/display injection;
- screen/scrollback text via `+read`;
- explicit and caller-derived target identity (`GHOZTTY_IPC_SOCKET`, `GHOZTTY_PANE_ID`);
- stale weak-reference pruning in target registry;
- owner-only `0600` local Unix socket on macOS implementation;
- lifecycle/list/rearrangement/state/banner/reload operations;
- documented agent-owned PTY/session persistence architecture for app replacement/crash recovery.

Not independently established here: complete cross-platform parity, all README claims, performance, security threat-model completeness, or long-term maintenance. The persisted-session document contains its own unfinished/unmeasured criteria.

**Bootstrap disposition for Khostty IPC: ADAPT/LEARN FROM existing implementation first. BUILD CUSTOM only for accepted unmet structured-state/search/event/auth/cross-platform requirements.**

### Native Windows baseline — shiweis/ghostty-windows

Pinned `shiweis/ghostty-windows@119b9270c8585fa3ae6969c353767fab5a32e438`, direct MIT fork of `ghostty-org/ghostty`. Created 2026-03-18; pinned head pushed 2026-09-02.

Source inspection, not README alone, finds:
- ~2.5k-line Win32 App implementation with window classes/message loop/config/global hotkeys/taskbar etc.;
- ~2.4k-line Window implementation with tabs/splits/window state;
- ~3.1k-line Surface implementation with WGL, core surface, keyboard/mouse/IME/search/palette/scrollbar integration;
- ConPTY/core Ghostty integration and PowerShell shell integration;
- Win32 test harnesses under `test/win32/`.

Its GitHub-hosted `Windows CI` workflow runs `zig build test -Dapp-runtime=win32 -Dtarget=x86_64-windows-gnu` on `windows-latest`, then builds the full app. Run `33633427282` on the pinned head completed SUCCESS on 2026-09-02. This is external-project self-verification, not our independent acceptance run, but it materially exceeds a scaffold claim.

Current-upstream compare: 241 commits ahead / 345 behind, merge base `20abdb50a6216c450d6d4d010c41c7edf5ab15b2`. Its implementation strength therefore comes with substantial rebase/merge debt.

Upstream PR `ghostty-org/ghostty#12167` was closed unmerged. Comments identify contribution-vouch process, review size, unsettled Windows UI/toolkit direction, and especially long-term maintainer ownership as blockers. Early external testing reported AltGr and kitty-image issues; later fork work claims fixes/features. Upstream non-merge is therefore a convergence/maintenance warning, not a technical falsification of the Win32 path.

Current upstream Ghostty itself still has no Windows application runtime at `f9e827…`; release documentation says Windows remains long-term while libghostty already supports Windows.

**Bootstrap disposition for Windows: ADAPT/PORT the strongest existing Win32 delta onto the desired current base first. A new Khostty Windows implementation must prove a specific unmet obligation or materially lower maintenance burden.**

## Updated best realistic product-absent architecture

Rather than 'use another generic terminal', the strongest composition is now:

```text
upstream/current Ghostty core
  + mature Win32 runtime delta where Windows native GUI is required
  + Ghoztty-class thin control layer where agent terminal control is required
  + direct upstream libghostty for embedding
  + Khostty-owned conformance / language wrappers only where experiments prove net value
```

This stack is deliberately compositional. It can borrow/adapt code/concepts rather than use one stale fork wholesale.

## What can still justify Khostty

Candidate surviving thesis is **a carefully maintained integration/distribution layer over upstream Ghostty and proven external deltas**, not invention of those deltas:
- current-upstream rebasing and conflict discipline;
- a coherent supported Windows build/distribution where alternative forks drift;
- one consistent auth/identity/control policy across supported platforms if accepted;
- tested safe language bindings if they substantially reduce integration cost;
- conformance/evidence gates that catch upstream/fork regressions;
- clean installation/release/update/support experience.

Those are operational/integration claims. They require comparative evidence; sunk work does not establish them.

## K-E02/K-E03 experiment implications

K-E02 control: Ghoztty is primary same-family control baseline. Khostty is allowed to be unsupported at frozen source. Compare child-effect correctness, target identity, inspection/events, authorization, controller/app replacement and maintenance delta.

K-E02 Windows: compare adapting `shiweis/ghostty-windows@119b927…` (or an isolated Win32 delta rebased to current upstream) against Khostty's own scaffold and a thin libghostty host. Do not spend an experiment rebuilding tabs/splits/IME/ConPTY from scratch before this comparison.

K-E03 embedding: direct upstream libghostty is the baseline; Khostty wrappers must prove safe ergonomics/consumer value while the manifest primitive remains correctly attributed upstream.

## Existence gate disposition

**OPEN, but monolithic feature-novelty thesis is falsified.** A full Khostty fork survives only if integration/support economics or accepted cross-surface invariants beat the compositional alternative. Otherwise retain useful verification/wrapper assets and reduce fork ownership.

Primary source references:
- https://github.com/dzearing/ghoztty/tree/fd3838acfa834c29e99616cdc8500c0208a13a09
- https://github.com/shiweis/ghostty-windows/tree/119b9270c8585fa3ae6969c353767fab5a32e438
- https://github.com/ghostty-org/ghostty/pull/12167
- https://ghostty.org/docs/install/release-notes/1-3-0
