# ADR-DEP-004 — Runtime lane and PaaS qualification

**Status:** proposed

## Decision

Propose rootless Podman plus native WSL systemd/Quadlet for the first persistent-service slice; evaluate WSLC separately. PaaS candidates are conditional adapters, not prerequisites.

## Alternatives tested conceptually

- Make Coolify a required Podman layer now: no qualified path shown.
- Use a Podman-aware UI as a second writer: violates the single-actuator boundary.

## Revisit / closure

Installed-version discovery and lifecycle tests; no engine installation follows from this ADR alone.

Sources: S013, S014, S015, S016, S017, S018, S019, S020, S021.

This record does not authorize mutation. ADR-DEP-001 and ADR-DEP-014 record stated user constraints.
