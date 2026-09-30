# Architecture validation matrix — pass 1

Date: 2026-09-30. Status: OPEN. Each row needs an experiment or source-backed disposition before architecture freeze.

| Risk / hypothesis | HeliosLite | KCode | Falsifying experiment / evidence |
|---|---|---|---|
| Independent acceptance cannot false-green | Candidate #322 qualified 8/8 adversarial oracle tests; exact candidate only | Evidence harness itself caught zero-test false green; product identity test still pending | Remove/alter guard; witness must fail. Bind exact run/candidate |
| Runtime identity binds actual serving process | CLI executable identity still needs explicit installed/runtime witness where daemonized surfaces apply | #14 candidate version/git/PID/exe SHA on main Ping; native test pending | New client -> old daemon; wrong socket; copied version label; executable digest mismatch |
| Timeout/cancel kills descendants | #322 adds process-tree termination; Linux oracle covers timeout terminal state, descendant survival still needs direct fixture and Windows validation | Existing upstream/fork lifecycle substantial; exact process-tree semantics not yet mapped | Spawn grandchild that ignores TERM; cancel; prove no surviving effect/process |
| Persistence survives restart without conflating effort | Dual SQLite/DBD surfaces unresolved | Session/server persistence substantial; durable effort remains external | Crash at write/effect boundaries; resume with new worker; verify no lost/duplicate accepted state |
| Custom storage daemon is justified | forge_dbd custom single-writer daemon | N/A/other server ownership | Compare WAL/direct ownership under concurrent writers, crash recovery and complexity |
| Custom daemon hot path is justified | Zig forge_daemon performance experiment | shared server is core upstream architecture | Matched startup/dispatch latency/RSS/correctness with/without daemon, cold/warm |
| Sandbox actually enforces policy | Linux Landlock feature-gated; Windows documented placeholder | Current tool permission/destructive gate differs | Adversarial file/network/process escape on each supported profile; disabled backend must report unsupported |
| LLM guardian cannot authorize itself | forge_guardian risk layer exists | permission systems upstreamed | Deterministic authority must dominate LLM score; mutate LLM verdict and prove forbidden op stays denied |
| External integrations do not clone authority | local forge_agileplus/forge_tracera raise duplication concern | no named integrations found | Thin adapter prototype versus embedded clone; external rejection must remain non-green |
| POSIX-oriented Windows path is viable | pheno_shell/winterminal utilities exist, not Pine | upstream Windows support exists | Matched command/path/env/PTY/signal suite on clean Windows with native/Pine adapter; no WSL assumption |
| Provider subprocess preserves semantics | Helios provider model inherited; KCode can invoke ForgeCode | ForgeCode/Claude CLI runtimes | Golden transcript/tool/cancel/resume cases versus direct provider; quantify transformations/loss |
| Deep fork beats maintained upstream + overlay | 742-commit delta needs semantic reduction | 136 divergent commits vs 2320-behind current upstream control | Retained-patch ledger + matched user journeys + maintenance burden |

Passing a unit test for a primitive does not close a row whose claim is end-to-end or platform-specific.