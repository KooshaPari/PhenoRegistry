# Khostty alternatives and bootstrap gate — pass 1

Research retrieved 2026-09-29. Internal source: Khostty a29aa9c6553d9f42aa68e2919116c0f6d53f329d. Status: EXISTENCE / ARCHITECTURE GATE OPEN. Official documentation establishes available concepts, not a benchmark or installed compatibility qualification.

## Evidence-backed competitors and primitives

| Source / inspected extent | Fact established | Version / limitations | Provisional disposition |
|---|---|---|---|
| WezTerm CLI: https://wezterm.org/cli/cli/index.html ; command list and pane targeting | Existing commands cover pane text, activation, send-text, spawning, splitting and zoom; explicit pane selection is available | Mutable documentation, binary version not frozen; no local cross-platform test or embedding equivalence demonstrated | USE DIRECTLY or INTEGRATE for an automation baseline |
| cmux API: https://cmux.com/docs/api ; macOS CLI, socket protocol and access modes | Existing Ghostty-oriented workspace/pane control over local JSON messages, plus machine-facing workspace operations | macOS page; process-based access policy is not proof of equivalent threat coverage; source/license pin pending | USE DIRECTLY for macOS baseline; LEARN FROM capability/identity model |
| kitty: https://sw.kovidgoyal.net/kitty/remote-control/ ; remote commands and authorization | Scriptable terminal control and scoped remote-control permissions already exist | Mutable docs; no product-specific security or platform qualification | USE DIRECTLY / LEARN FROM permission boundaries |
| Microsoft pseudoconsole: https://learn.microsoft.com/en-us/windows/console/creating-a-pseudoconsole-session ; session creation and communication lifecycle | A native pseudoconsole session uses communication channels and separately launched client processes | Documentation is not Khostty integration evidence; exact target SDK and supported OS configurations not pinned | INTEGRATE platform primitive, not a new PTY substitute |
| ghostty-org/ghostty parent metadata and inherited tree | Khostty already derives from an existing terminal engine | Exact merge-base, current library API/version, licenses of transitive dependencies and ABI stability not assessed | Prefer minimal upstream reuse; FORK only for demonstrated unmet obligations |

## Best realistic product-absent stacks

For an agent-operated desktop terminal, benchmark WezTerm with a thin explicit-pane adapter and an external durable task/evidence store. On macOS, include cmux as the same-family workflow alternative; kitty is another control/security comparison. The external store is needed only for durable development/evidence, not to replace terminal state. Do not demand that competitors implement this entire research program inside their terminal.

For an embedded terminal library, the comparison is upstream terminal-library integration with minimal host and language bindings, not an unrelated desktop UI. Verify actual upstream exports and native lifetimes before selecting this architecture. These are two competing product interpretations; user authority must choose the required horizon before a weighted comparison.

## Differentiation ledger

- COMMODITY / CONTESTED: basic split/create/focus/send-text/read-state automation, local command protocols, ordinary GPU-terminal experience.
- FALSIFIED AS UNIQUE: merely being an agent-controllable terminal.
- CANDIDATE: a supported owned runtime satisfying specific native Windows and multi-language embedding workflows while preserving upstream terminal semantics; exact outcome and support horizon need authority.
- UNVERIFIED: lower total maintenance, better concurrency/recovery, safer agent access or better human/agent coexistence than the realistic alternatives. No performance or superiority claim is accepted.

## Bootstrap decision ledger

| Subsystem | Alternatives to custom work | Initial choice / decision witness |
|---|---|---|
| Terminal parser / rendering / text stack | Preserve existing upstream engine | REJECT a rewrite absent a demonstrated incompatibility; map upstream obligations and fork delta |
| Desktop automation | Existing CLI/socket adapters versus additive Khostty IPC | Prototype the same real child-effect journey in an existing terminal and Khostty; compare integration and maintenance cost |
| Native Windows session | Official pseudoconsole and existing host patterns | INTEGRATE; run creation/input/output/resize/shutdown/restart on actual Windows before accepting |
| Language ABI / ownership | Upstream exports with thin bindings versus parallel abstractions | ADAPT only necessary boundary; prove allocation, thread and handle lifetimes in a real consumer |
| Durable effort / grader | Existing repo/CI/artifact primitives plus independent policy | COMPOSE externally; terminal is not an agent scheduler or product-truth database |
| Event / pane identity | Existing control APIs versus custom protocol | LEARN FROM; custom epoch/causality behavior only where tested alternatives fail accepted obligations |

Every BUILD CUSTOM/FORK decision needs an accepted obligation, strongest alternative, precise gap, integration-spike result, licensing/health assessment, estimated ownership cost and reversibility plan. None is approved by this first-pass matrix.

## Closure blockers

Still missing: exact source/releases and license texts for alternatives, project-health history, broad standards/terminal conformance survey, accessibility and human UX comparison, benchmark configurations, costs, embedding/native experiments and fresh independent attack. Marketing claims and README test counts do not close these. Avoid committing to full-fork maintenance until a narrow real journey demonstrates a reason for it.

## Pass 6 — stronger thin-host comparator

Ghostling is now pinned as an official-family embedding reference at `ghostty-org/ghostling@63842bf8e5e481160f81d348da9ff6fd27986798` (main observed 2026-09-30). Its root LICENSE is MIT. `main.c` is a small but real libghostty consumer that owns PTY spawn/read/write, feeds child output into `ghostty_terminal_vt_write`, maps input into Ghostty key encoding, and supplies its own window/render loop via raylib.

Decision consequence: K-E03 must compare Khostty wrappers against **direct libghostty consumption plus a minimal host pattern**, not against a hypothetical raw C library. Ghostling is not a production terminal and explicitly warns it is a demo, so it is architecture prior art rather than a ready replacement.

Ghoztty remains the stronger same-family control comparator for K-E02. Together these split the existence test cleanly: Ghostling attacks unnecessary embedding abstraction/fork ownership; Ghoztty attacks unnecessary agent-control breadth. A retained Khostty subsystem needs a concrete gap against the relevant comparator rather than a repository-level uniqueness claim.

External sources inspected this pass: https://github.com/ghostty-org/ghostling at the pinned revision; current public Ghostty source/docs; Ghoztty pinned previously. Runtime bake-offs remain outstanding.
