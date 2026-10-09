# Pass 10 — active experimental branches and controller blockers

Observed 2026-09-30. Exactly two products.

## Melosviz M-E02

Developer-agent implementation PR #302 exists. A prior exact head passed its dedicated deterministic video_export vertical workflow, but recovery-controller review found generative cache evidence did not bind renderer/model/workflow/tool identity.

Controller patch current head: `65f6a5b551f9e5ca12846393c8ef44726754a9b5`.
- real-render reuse for generative/pro-tool scenes now requires explicit backend identity;
- deterministic video_export declares `video_export:ffmpeg:v1`;
- unqualified real-render evidence is not stored/reused;
- held-out tests cover no-identity no-reuse, qualified reuse, identity-change invalidation.

New exact-head workflows are queued. Earlier greens do not transfer. External pass-5 oracle against candidate-produced output remains open.

## Khostty K-E03

Developer-agent PR #9 exists. Dedicated PR run 24 on `aeede977...` failed during Python syntax validation before native build/comparison. Controller repaired only the literal escaped-newline syntax. Current head `1e51ffcb222201d03eed2c28eb910d63d1d2903b`; new exact-head workflows queued.

No wrapper acceptance until candidate + upstream native artifacts both execute the same wrapper/direct-C harness and preserve authenticated build identities.

## Khostty K-E02

Controller opened separate draft PR #10 from the frozen baseline. Candidate `a007160c333566a45b5a1572b7099ed57529203d` adds an opt-in `KHOSTTY_AGENT_IPC=1` GTK lifecycle owner for AppHost/Broker/Manager/Auth/Server and a dedicated compile/module-test workflow.

Independent source review immediately found a blocking lifetime defect in the pre-existing server design: detached connection threads may remain after Server.deinit's 5-second drain timeout while still referencing Server/Manager/Broker/Auth/AppHost. A real GTK teardown could then free native/dependency state still reachable by those threads. Existing lifecycle tests close clients before draining and do not exercise an idle client across teardown.

K-E02 therefore remains BLOCKED even if the compile workflow passes. Required repair is bounded force-disconnect + worker completion/join before dependency/App teardown, with idle/half-frame/subscribed/concurrent-client shutdown controls. Do not substitute process-exit leaking or an indefinite hang.

## Handoff

Experimental implementation is active and independently graded. No experiment is merge-authorized. General developer handoff remains blocked for both products.
