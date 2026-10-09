# SOTA research — security, memory and computer-use pass

Date: 2026-10-01.

## Security
OWASP 2026 agentic guidance highlights prompt injection, tool/privilege abuse, data exfiltration, memory poisoning, excessive autonomy, high-impact action abuse, approval manipulation, cascading multi-agent failures, unbounded cost and supply-chain risk.

Contract consequences:
- Principal/tenant identity and least-authority Capability grants;
- external/retrieved/model-generated content remains untrusted data;
- memory writes pass policy/provenance/integrity controls;
- approval binds immutable CommandIntent;
- high-impact effects require independent policy/verification where configured;
- multi-agent delegation never implicitly transfers all parent authority;
- cost/resource budgets are enforceable policy, not prompt advice;
- MCP/tool supply chain carries server/tool/version/provenance identity.

## Memory/context
Persistent memory is a security boundary. A one-time malicious repository/tool result can poison future sessions if promoted into trusted memory. Memory entries therefore need source authority, scope/tenant, creation method, trust class, expiry/retention and retrieval policy. Memory is not system instruction by default.

Context compaction/summarization must preserve protected constraints or surface uncertainty; summary success is tested adversarially against dropped restrictions.

## Computer use
OSWorld 2.0 reports 108 long-horizon workflows with median human completion around 1.6 hours and hundreds of agent tool calls; frontier systems still show low full completion and failures around constraint tracking, dynamic state and skipped verification.

Contract consequences:
- CommandIntent/effect identity must scale to long action sequences;
- workspace observations are versioned/stale-able;
- hidden/dynamic state triggers clarification/re-observation policies;
- verification is explicit before terminal acceptance;
- latency/step efficiency are first-class quality measures;
- continuous GUI streams require leases/projections but irreversible actions still pass command/effect authority.

## Required security oracle families
Indirect prompt injection; memory poisoning; cross-tenant memory leak; tool schema spoof; privilege escalation; approval replay; command mutation after approval; secret-in-trace; compromised MCP server; malicious artifact; child-agent authority escalation; denial-of-wallet; poisoned checkpoint; stale capability snapshot; supply-chain/runtime identity mismatch.
