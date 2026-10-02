# Cross-family normative trace matrix — non-code pass 1

| Intent / invariant | HeliosCLI contract | KCode contract | Shared harness | Oracle/evidence | State |
|---|---|---|---|---|---|
| Client-independent harness semantics | HC-FAM-PROJECTION | K-FAM-PROJECTION | Client rule/Event rule | client interchange conformance | SPECIFIED |
| Worker != effort != product state | HC-FAM-DURABILITY | K-FAM-DURABILITY | Lifetimes | replacement/crash oracle | SPECIFIED; runtime reachability partial |
| External uncertainty before retry | HC-FAM-DURABILITY/TOOLS | K-FAM-DURABILITY/TOOLS | Effect rule | effect + process-death oracles | CONTRACT QUALIFIED; consumers open |
| Exact evidence subject identity | HC-FAM-EVIDENCE | K-FAM-EVIDENCE | Evidence rule | wrong-candidate/stale/missing controls | SPECIFIED |
| Independent grader | HC-FAM-EVIDENCE | K-FAM-EVIDENCE | Grader rule | mutation/false-green controls | SPECIFIED |
| Generic GUI/TUI/CLI/API/SDK embedding | HC-FAM-PROJECTION | K-FAM-PROJECTION | Client rule | cross-client journey | SPECIFIED |
| Active upstream contribution strategy | operations/non-goal | K-FAM-UPSTREAM | bootstrap ledger | delta/maintenance comparison | SPECIFIED / evidence open |
| One CLI unless segmentation survives | architecture alternatives | architecture alternatives | recovered intent | matched role comparison | OPEN DECISION |
| HeliosLite sunset | architecture alternatives | architecture alternatives | lineage matrix | lightweight role benchmark | PRESUMED SUNSET |
| Generic non-coding harness | architecture-dependent | architecture-dependent | Genericity falsification | non-coding conformance workload | OPEN |
| Durable backend replaceable | HC-FAM-DURABILITY | K-FAM-DURABILITY | Durability backend | backend conformance + latency/scale | OPEN SELECTION |
| Runtime/workflow composability | projection/durability | projection/durability | Runtime + workflow composition | actor+workflow integration fixture | SPECIFIED |
| Tenant/trust isolation | HC-FAM-SEC | K-FAM-SEC | Tenancy/trust | cross-tenant denial/adversarial | SPECIFIED; decomposition open |
| Local-first | operations | operations | Local-first conformance | offline conformance | SPECIFIED |
| History compaction preserves authority | durability/evidence | durability/evidence | History compaction/replay | compact/replay equivalence | SPECIFIED |
| Approval freshness | HITL | security/HITL | Approval freshness | stale approval negative | SPECIFIED |
| Evidence privacy/custody | evidence/security | evidence/security | Evidence privacy/custody | redaction/custody controls | SPECIFIED |

Every OPEN decision must remain outside accepted architecture until research/experiment closes it.