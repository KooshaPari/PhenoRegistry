# Threat model and assurance depth

## Assets and failures

Protect source and user data, secrets, build/release authority, accepted requirements, grader fixtures, raw observations, resource budgets, work ownership, registry custody and sponsor trust. Failures include accidental stale evidence, path mixups, duplicate state, score gaming, prompt injection, poisoned dependencies, hidden skipped tests, stale-worker effects and self-consistent but useless products.

Repository files, research pages, logs and tool output are untrusted evidence, not instructions to expand authority. Do not execute arbitrary discovered scripts on a privileged workstation. Use existing authorized native sandboxes or VMs; Docker is not a prerequisite. A prompt-only sandbox is not an enforcement boundary.

## Boundaries

Separate builder write permissions from protected acceptance inputs when consequence warrants it. Use actual OS/repository permissions, narrow credentials, producer identities and independent observation paths. Multiple agents sharing the same mutable oracle are not automatically independent. Keep protected holdouts out of readable logs.

Scope executable tests to disposable fixtures and explicit resource/effect limits. Do not use actual customer data, victim systems, production destructive actions or unauthorized DRM/authentication bypasses. For game/mod testing, use permitted local builds, explicit accounts and valid licensing; unavailable parallel sessions become a tooling or authority finding.

## Assurance tiers

These are proposed operational tiers, not certifications. Low-consequence reversible exploration may use a short protocol and local observations. Shared or persisted behavior needs real integration, negative controls, rollback and traceability. Sensitive or irreversible effects need stronger independence, custody and authority verification. Preserve any already accepted higher floors. Do not use risk-proportionality as a silent reason to weaken a mandatory contract.

## Reference kernel boundary

The kernel parses records and checks paths, local digests, selected references, qualification flags and arithmetic. It does not verify actual host policy, remote identities, signatures, grader truth, consumer value, every semantic requirement or race-free filesystem access. Run it on quiescent trusted copies; local path checks are not a hostile-filesystem sandbox. It has no network side effects and does not execute product commands.

A malicious actor controlling both raw evidence and metadata can fabricate a coherent bundle. The cure is independently controlled evidence/authority paths and authenticated receipts, not more local hash checks. The toy demonstrates behavioral negative controls for one bounded example, not adversarial certification of the whole lab.
