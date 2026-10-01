# Quality overlay

Quality properties attach to applicable subjects rather than cloning functional requirements.

| Quality | Required contract |
|---|---|
| Correctness | accepted behavior and negative controls; no false greens |
| Reliability | crash/restart/reconnect/retry/recovery semantics; no lost accepted state |
| Performance | latency/throughput/concurrency/resource budgets per journey and configuration |
| Scalability | bounded queues/backpressure/fairness; distributed worker behavior where enabled |
| Security | least authority, sandbox/policy, secrets/IAM, approval provenance, untrusted tool/output handling |
| Privacy | explicit data destinations/retention/redaction; client and telemetry boundaries |
| Accessibility | interactive clients meet defined keyboard/screen-reader/contrast/output semantics |
| Usability | discoverable state, approvals, errors, recovery, progress and intervention |
| Interoperability | versioned APIs/events; capability negotiation; MCP/A2A/provider adapters where adopted |
| Maintainability | upstream delta minimized; extension points and generated protocols preferred to forks |
| Observability | trace/event/evidence correlation across lifetimes |
| Reproducibility | candidate/config/environment/verifier identity sufficient to repeat applicable evaluations |
| Upgradeability | schema/protocol/config migration, coexistence and rollback |
| Portability | supported OS/arch/client/backend matrix explicit |
| Cost/QoS | token/compute/tool budgets, priority/fairness and degradation policy |
