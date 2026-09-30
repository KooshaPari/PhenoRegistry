# Execution receipt 6 — false-green control and differentiation pressure

Date: 2026-09-30. Program remains OPEN.

HeliosLite exact candidate `8451b952...` remains qualified for H-F001..H-F004 by an 8/8 dedicated oracle run plus clean exact-head platform/CVP/security/CI workflows. Canonical state records these findings as resolved for that candidate only.

KCode's prior green native workflow was rejected after log inspection showed its target command executed zero tests. CI now contains an explicit anti-zero-test guard and candidate `5a15dd86...` is rerunning. This demonstrates the program rule that a workflow-level green is not sufficient evidence when the intended criterion did not execute.

Existence-gate pressure increased: Pine/native Windows is not currently a demonstrated KCode fork differentiator; current upstream has substantial Windows/platform handling and frozen KCode did not surface a Pine subsystem. Pine remains an accepted external consumer/integration constraint.

HeliosLite owned `forge_agileplus`, `forge_tracera` and `forge_sharecli` crates are real implementation surfaces absent by name from the pinned upstream control, but their placement in core is unproven. They are now adapter-vs-core architecture experiments rather than automatic retained patches.

No product retirement, rebase, merge or architecture freeze is authorized.