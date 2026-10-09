# Independent-style adversarial specification review — pass 2

Assume pass-1 repairs are still wrong.

## Alternative interpretation probes

1. **Server-owned session vs harness-owned session.** Codex/jcode may own native session semantics that cannot be fully normalized. Contract permits adapter-native opaque session state plus canonical references/capability snapshots; it does not require destructive translation. Explained.

2. **Durable engine replay semantics differ.** Temporal replay, Durable Task orchestration and local event logs have different determinism constraints. DurableExecutionPort must expose capability profile; workloads requiring timers/external events/distributed resume reject insufficient backends. Explained, but adapter conformance remains execution blocker.

3. **Ephemeral chat should not pay durable overhead.** J-HC-02 allows local ephemeral execution; durability becomes required by declared workflow/effect policy. Explained.

4. **GUI may need richer state than CLI.** Client-local presentation state is allowed; authoritative effort/session/effect/artifact state remains shared. Explained.

5. **Real-time computer use has continuous state not discrete tool calls.** Model as Workspace/Capability session producing Commands/Effects/Artifacts and high-rate projection; may need stream-specific lease/latency contracts. Add quality profile, ontology still explains it.

6. **Multi-agent shared-memory blackboard.** Represent as an Artifact/StateStore capability associated with DurableEffort; access/version policy explicit. No new lifetime required.

7. **Speculative execution.** Multiple WorkerAttempts may branch from one effort/checkpoint; only accepted effects/artifacts promote. Scheduler/Grader/Evidence model explains it.

8. **Nested durable workflows.** DurableEffort may parent/sub-effort with independent attempts/effects and acceptance. Add parent relation; no new identity class.

9. **Offline-first local mode.** Local stores satisfy ports with local trust/retention profile; later sync requires conflict/version semantics. Explained.

10. **External SaaS owns task truth.** Adapter may reference imported assertion/remote task state, but local acceptance authority and evidence provenance remain explicit. Explained.

## Remaining non-code gaps after pass 2
- full historical prompt corpus still not individually resolved;
- Agentora source/API obligation audit incomplete;
- SOTA breadth needs security/IAM, memory/context, evaluation/grading and computer-use passes;
- KCode full delta classification incomplete;
- complete Helios root command/test/release/security mapping incomplete;
- capability lineage rows are pass-1 hypotheses, not final dispositions;
- durable/client adapter conformance requires execution later.

## Verdict
Ontology/contract is now broad enough to explain the tested alternative interpretations, but **program non-code finality is still blocked by evidence coverage**, not a known missing core identity class.
