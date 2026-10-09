> Authored by Instinct

# KCode divergence from JCode (Oct 8, 2026)
Research only. Correction: KCode is PUBLIC (https://github.com/KooshaPari/KCode), not private as earlier notes said.

## Repo
MIT, fork of 1jehuang/jcode, created Sep 11 2026, default branch master. Recent push Oct 9: "refactor(decollision): rename jcode to kcode (#33)". Latest fork release v0.85.0-k1.0.0 (Sep 15).
Compare (1jehuang/jcode master...KooshaPari:KCode master): 137 commits ahead, 2,531 behind. Upstream is around v0.89.x; the fork's last sync was around v0.85 (a 43-commit merge). PR #23 "Merge upstream v0.88.0 into KCode" (490 files) is still open.
Verdict: meaningfully diverged as an additive layer on a stale base, not a rewrite, and falling behind (about 2.5k commits). Upstream has 7,293 contributions; KooshaPari has 3 on the contributor graph (work is mostly agent-authored).

## His 137 commits, key areas
1. Swarm TUI: gallery/strip/dock rework (active/idle, per-role border colors, DAG plan view, agent search/filter, rename, multi-select batch ops, detail card with tokens/cost/queue depth, protocol fields on SwarmMemberRuntime), status bar and dispatch stats.
2. New crates in app-core: auto-dream (memory consolidation LLM call, 24h gate), micro-compact, cache-vectors, permission-bubble (session forking with depth guard), tool-search index, session-memory, command-risk.
3. Agent modes and commands: manager and researcher modes with tool gating, /goal, /loop recurring task command (ambient recurrence fields), elicitation channel (native and MCP tool).
4. Providers: ForgeCode runtime provider, OpenCode Go Responses-API routing, orcarouter, default_model fallback, OpenRouter panic fix.
5. Terminal and runtime: HERDR reporter (status/install CLI, plugins herdr-jcode, herdr-forgecode), terminal detection (14 terminals), shell integration (6 shells), DECSET 2026 synchronized updates, macOS taskgated and signing fixes.
6. Build, release, security: Bun installer, GitHub Packages (ghcr), screen-capture env gates with audit logging, jcode-dev isolated dev wrapper, non-incremental/sccache builds, aws-lc bump, CI/clippy cleanup, Dependabot, docs/specs/CHANGELOG, kcode.sh installer.

## Open PRs (Sep 27 - Oct 9)
ACP session discovery and remote interaction broker (#10), daemon identity in ping handshake (#14), ForgeCode fail-closed (#16), macOS trust fixes (#18, #22), durable effect recovery hook (#20), upstream v0.88 merge (#23), /poke context recovery (#25), isolated dev runtime state (#27), decollide phases (#34), mature-first recovery spec (#12).

## Effect on the JCode assessment
- Worker role: inherited and strengthened (swarm dock, manager/researcher modes, herdr lifecycle, ACP broker PR; README cites headless swarm worker RAM numbers).
- Ambient Mode: inherited and extended (recurrence fields for /loop).
- Chat gateway: still none. No Telegram/Discord/gateway work in commits or PRs; code search found 0 hits for telegram/gateway/discord. Caveat: forks are often unindexed, so this rests mainly on commit and PR lists. Closest are the ACP remote-interaction broker PR and HERDR terminal reporting; neither is a chat gateway.

## Caveats
No file-by-file diff was read. GitHub's compare view caps at 300 files, and about 120 of the 137 commit titles were seen.
