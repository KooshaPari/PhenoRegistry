# Pass 6 — finite tracked denominators, semantic spines, and expanded experimental handoff

Observed 2026-09-29. Exactly two product programs remain in scope.

## Handoff state

- **Khostty: READY FOR EXPERIMENTAL IMPLEMENTATION** — K-E01, K-E02 and K-E03 may now run in separate worktrees. General development remains blocked.
- **Melosviz: READY FOR EXPERIMENTAL IMPLEMENTATION** — M-E01 and independent M-ESEC may run now. M-E02/M-E03 remain dependency-gated. General development remains blocked.

## Tracked source denominators

Melosviz product-relevant tracked inventory: **688 unique blobs** across the inventoried product trees, zero duplicate paths between inventory parts. This is a tracked-source denominator only, not a requirements count or progress percentage.

Khostty product-relevant tracked inventory: **2,055 unique blobs** after deduplicating 62 overlapping paths between inventory parts; zero object-ID conflicts. The inherited `test/` bulk is separately quantified at **4,020 blobs / 4,030 entries** and vendor at **9 blobs / 16 entries**. Those sources remain verification/dependency evidence but are excluded from product-obligation counting so inherited fixtures cannot inflate product coverage.

## Semantic spine closure

Melosviz: the conductor/API/CLI high-risk spine has been resolved far enough to stabilize these architecture facts: scene type is routing rather than identity; execution done/outcome/artifact validity/acceptance are distinct states; the in-process event bus is not durable product state; provenance sidecars are supporting evidence rather than the acceptance authority; CLI/API/UI must consume typed scene/assembly state.

Khostty: Windows App, renderer, surface creation and named-pipe operations are explicitly unimplemented in frozen source. The new agent protocol's AppHost/server/broker/manager symbols were searched fork-aware and have no application-startup caller outside IPC implementation/protocol/docs. Combined with protocol §7, this closes the current mount archaeology to a reasonable falsification standard.

## New Melosviz security blocker

`bridge/security.py::loopback_check` promises loopback-only default behavior but only rejects wildcard `0.0.0.0`, `::`, and `*`. Source-equivalent execution shows `192.168.1.10`, `10.0.0.7`, and `example.com` all return `(True, "loopback")` without `MELOSVIZ_BRIDGE_ALLOW_PUBLIC=1`. `server.py` uses this result immediately before `uvicorn.run`, so the behavior is mounted. Bearer auth is conditional and legacy auth-off/manual mode exists, making this a real boundary issue rather than logging drift.

Product-local `pass6/test_bridge_bind_contract.py` and `SECURITY-RECEIPT.json` define the bounded M-ESEC repair. Full checkout pytest remains to execute.

## Khostty alternative gate tightened

Pinned Ghoztty `fd3838acfa834c29e99616cdc8500c0208a13a09` source was inspected beyond README. It implements named-pane PTY child input (`+send-keys`), plain-text terminal/scrollback read (`+read`), app/pane identity seeded into child env, stale weak-reference pruning, `0600` AF_UNIX IPC, list/rearrange/lifecycle actions, and a separate session-persistence architecture with agent-owned PTYs.

Therefore Khostty's custom IPC cannot claim differentiation merely from child input, readback, targeting, controller replacement or persistence. Remaining candidates (structured state/search/events, explicit token auth, intended cross-platform transport) must prove an accepted unmet need. K-E02 now uses Ghoztty as the primary same-family baseline.

## Latest product evidence heads

- Khostty: `1ba1aaf067834849ded0ddcc5a249dd474861bf1`
- Melosviz: `834bf02112bdb9434f895d77094564b971c72c80`

Both canonical product branches remain draft specification/experiment branches. No product implementation candidate, merge, release, scalar completion score, or independent final review is claimed.
