# Absorbed Crate: Apisync (KooshaPari/Apisync)

## Direct Source Absorption (2026-09-12)

The Apisync source code has been directly absorbed into this registry entry.
This supersedes the prior pointer-only entry.

### Absorption summary

| Field | Value |
| --- | --- |
| Source repo | `KooshaPari/Apisync` |
| Source state | Archived (read-only) on GitHub — 2026-06-19 |
| Version | v0.2.10 |
| Commit count | 503 commits |
| Releases | 12 |
| What it is | REST / GraphQL / WebSocket API toolkit (Rust) |
| Lines of code | 4,745 (Rust source + config) |
| Rust source lines | 4,441 |
| Config lines (TOML) | 304 |
| Files absorbed | 45 |
| Git bundle | `/tmp/apisync-recovered-full.bundle` (preserved for full history) |
| Recovery date | 2026-09-12 |

### Files absorbed

```
registry/absorbed-crates/apisync/
├── ABSORPTION.md                           # this file
├── README.md                               # tombstone pointer for archived remote
├── UPSTREAM.md                             # supersession chain + repoint guidance
├── Cargo.toml                              # crate manifest (package: apisync v0.2.10)
├── LICENSE                                 # MIT license
├── lib.rs                                  # library root
├── api.rs                                  # API layer
├── endpoints.rs                            # endpoint definitions
├── error.rs                                # error types
├── adapters/
│   ├── mod.rs
│   ├── graphql/
│   │   ├── mod.rs
│   │   ├── schema.rs                       # GraphQL schema (288 lines)
│   │   └── server.rs                       # GraphQL server (174 lines)
│   ├── rest/
│   │   ├── mod.rs
│   │   └── hyper_server.rs                 # REST/Hyper server (710 lines)
│   └── websocket/
│       ├── mod.rs
│       └── server.rs                       # WebSocket server (635 lines)
├── application/
│   ├── mod.rs
│   ├── handler.rs                          # request handlers
│   └── router.rs                           # request routing
├── clients/
│   ├── mod.rs
│   ├── graphql.rs                          # GraphQL client (256 lines)
│   ├── rest.rs                             # REST client (228 lines)
│   └── websocket.rs                        # WebSocket client (259 lines)
├── domain/
│   ├── mod.rs                              # domain types (338 lines)
│   ├── middleware.rs
│   └── middleware/
│       └── request_id.rs                   # request ID middleware
├── infrastructure/
│   ├── mod.rs
│   └── logging.rs                          # logging infrastructure
├── fuzz_targets/
│   └── router_dispatch.rs                  # fuzz testing for router
├── property_tests.rs                       # property-based tests (312 lines)
├── rest_integration_tests.rs               # REST integration tests
├── graphql_benchmark.rs                    # GraphQL benchmark
├── perf.rs                                 # performance utilities
├── _typos.toml                             # typo checker config
├── cliff.toml                              # git-cliff changelog config
├── clippy.toml                             # Clippy lint config
├── deny.toml                               # cargo-deny config
├── gitleaks.toml                           # secrets scanning config
├── mise.toml                               # mise (task runner) config
├── mutants.toml                            # cargo-mutants config
├── nextest.toml                            # nextest runner config
├── rust-toolchain.toml                     # pinned Rust toolchain
├── rustfmt.toml                            # formatter config
└── trace-gate.toml                         # tracing config
```

### Directory structure

The absorbed source follows Apisync's original layout:

- **`adapters/`** — Protocol adapters: REST (Hyper), GraphQL (async-graphql), WebSocket (tokio-tungstenite)
- **`application/`** — Request handling and routing
- **`clients/`** — Client implementations for each protocol
- **`domain/`** — Domain types, middleware, request ID generation
- **`infrastructure/`** — Cross-cutting concerns (logging)

### Prior migration trail

```
KooshaPari/Apisync           2026-06-19   archived
        │                                  content extracted into
        ▼                                  KooshaPari/apikit (v0.1.0 source of truth)
KooshaPari/apikit            2026-06-21   archived
        │                                  full content absorbed
        ▼                                  (governance + src + CI + tooling + docs)
KooshaPari/phenotype-tooling/
  └─ docs/absorbed-from-apikit/           active canonical home — 107 tracked files
```

| Date | Source → Target | Notes |
| ---- | --------------- | ----- |
| 2026-06-19 | `KooshaPari/Apisync` → archived | Original repo archived |
| 2026-06-20 | `Apisync` → `KooshaPari/apikit` | Governance, docs, CI, tooling absorbed |
| 2026-06-21 | `KooshaPari/apikit` → archived; absorbed into `phenotype-tooling` | Full absorption |
| 2026-09-01 | Pointer README placed in registry | Pointer-only entry for GitHub archival |
| **2026-09-12** | **`KooshaPari/Apisync` source → `phenotype-registry/registry/absorbed-crates/apisync/`** | **Direct source absorption (this commit)** |

## Repoint instructions

See `UPSTREAM.md` for Cargo dependency repointing, submodule cleanup, and ADR
provenance instructions.

## Verification

- All 45 files from the recovered Apisync source are present
- Rust source: 4,441 lines across all `.rs` files
- Config: 304 lines across all `.toml` files
- Total: 4,745 lines of code + configuration
- Git bundle preserved at `/tmp/apisync-recovered-full.bundle` for full history access
