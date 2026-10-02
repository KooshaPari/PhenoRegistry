# Execution receipt 7 — both first high-risk primitives qualified

Date: 2026-09-30. Program remains OPEN.

## KCode #14 exact qualification
Candidate `effe7dcb1491e7a9933475c1c57a81e2c40e08d2` completed Harness Recovery Daemon Identity run 36686592906 successfully. `cargo check -p jcode-protocol -p jcode-app-core` passed. The guarded targeted command executed exactly one intended test: `server::startup_tests::main_accept_loop_reports_exact_runtime_identity`; result 1 passed, 0 failed, 1256 filtered out, 8.07s. The test uses the actual main accept/readiness socket and asserts server version, git hash, PID and SHA-256 of current executable bytes.

Earlier zero-test green, debug-socket mismatch and hidden-output failure remain preserved as negative-control history. They are not overwritten by the final pass.

## HeliosLite
Candidate `8451b952...` remains exact-head qualified for H-F001..H-F004 by 8/8 dedicated adversarial oracle tests and all 12 observed successful workflows.

## Next high-risk vertical slice
Both products still lack demonstrated worker-replacement safety around uncertain external side effects. Registry now defines explicit external-effect receipt states and a crash-boundary experiment. Search did not surface an obvious first-class named idempotency/effect-receipt abstraction in frozen primary sources; this is not proof of behavioral absence, so implementation mapping remains open.

Architecture rule: durable effect reconciliation belongs with durable development effort/orchestration. The runtimes need adapter hooks, not automatically duplicate canonical effort engines.

No architecture freeze, merge, retirement, rebase or mature-product completion follows from these two primitive qualifications.