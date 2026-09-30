# Khostty local-IPC security bootstrap — pass 6

Research date: 2026-09-30. Frozen product source: `a29aa9c6553d9f42aa68e2919116c0f6d53f329d`.
Status: security architecture research, not a protocol freeze.

## Threat-boundary correction

Khostty's shared bearer token is useful request authentication and fails closed when absent. It is **not by itself a mutually-untrusted-process boundary inside one OS account**: the default token file is intentionally readable by that user session, and a same-UID process may possess the same ambient filesystem authority.

The architecture therefore needs to state which adversary it is defending against:
1. other OS users / accidental clients;
2. stale or wrong Khostty instance;
3. mutually untrusted agents/processes under the same user account;
4. sandboxed/remote automation principals.

Do not collapse these into a generic “authenticated” checkbox.

## Existing OS primitives

### Linux / AF_UNIX

Linux exposes kernel-authenticated peer credentials for connected AF_UNIX sockets through `SO_PEERCRED`; `SCM_CREDENTIALS` with `SO_PASSCRED` can also carry PID/real UID/GID. Pathname-socket access also depends on directory/socket permissions on Linux, but POSIX does not guarantee portable socket-file permission semantics.

Disposition:
- USE peer UID/PID as an **additional observed identity**, not a replacement for policy.
- Keep a private runtime directory and explicitly qualify its mode and socket mode.
- If per-agent authorization is required, map peer process/sandbox identity to a capability grant rather than share one omnipotent token.

### macOS / BSD-style local sockets

macOS provides `getpeereid()` for the effective UID/GID of the peer on a connected local socket. Apple/BSD documentation treats this as a kernel-provided peer identity mechanism.

Disposition:
- USE peer UID/GID to enforce same-user boundary and provide evidence about the connecting principal.
- If same-user agents need distinct rights, UID alone is insufficient; use an approved broker/sandbox identity or delegated capability.

### Windows named pipes

Windows named pipes support explicit security descriptors/DACLs. Microsoft documents that if no descriptor is supplied, the default descriptor grants full control to LocalSystem, administrators and the creator owner and read access to Everyone and anonymous accounts. The server can also impersonate a connected named-pipe client to use/query the client's security context.

Disposition:
- BUILD the Windows transport with an explicit DACL rather than relying on default security.
- Bind the pipe to the intended interactive user/session or approved service identity.
- Use client security context/identity where a policy decision requires it.
- Treat bearer tokens, if retained, as defense-in-depth/capability material rather than the only Windows boundary.

## Capability model

If K-E02 proves the mature use case needs mutually untrusted same-user agents, prefer a small capability model over one global token:

```
principal
  → capability lease
      {instance, pane/workspace scope, allowed operations, expiry, nonce/generation}
```

Potential operation classes:
- observe: list/state/read/events;
- interact: child input/focus;
- topology: create/split/resize/close;
- administrative: token/capability rotation or broad instance operations.

A capability must bind to the target instance epoch. Recreated panes/windows cannot inherit authority merely by reusing a numeric/name identifier.

This is a candidate model. Do not implement it unless the accepted threat model actually requires same-account agent separation.

## K-E02 security witnesses

For each supported platform/configuration:
- actual runtime-dir and endpoint ACL/mode;
- peer identity observable at accepted connection;
- wrong-user denial where safely testable;
- same-user behavior documented as allowed or policy-limited;
- stale/wrong-instance connection;
- capability/token rotation and revocation;
- child environment inspection for secret leakage;
- unauthorized read/input/topology actions produce no side effects;
- restart changes epoch and invalidates stale target/capability identity;
- collector failure is BLOCKED, never secure-by-assumption.

## Comparator consequence

Ghoztty's owner-only 0600 Unix socket and Khostty's owner-session token solve substantially the same coarse OS-user trust problem on macOS. Khostty only earns a security differentiation claim if it demonstrates a stronger accepted property: cross-platform explicit ACL/peer identity, scoped/delegated capabilities, safer instance identity, auditable policy, or another concrete outcome.

## External sources

- Linux `unix(7)`: AF_UNIX pathname permissions, `SO_PEERCRED`, `SCM_CREDENTIALS`.
- Apple `getpeereid(3)`: peer effective UID/GID for local socket connections.
- Microsoft Named Pipe Security and Access Rights: explicit security descriptors and default DACL behavior.
- Microsoft `ImpersonateNamedPipeClient`: server-side use of client security context.

These establish available OS mechanisms, not Khostty implementation evidence.
