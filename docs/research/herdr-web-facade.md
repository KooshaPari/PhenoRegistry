> Authored by Instinct

# HERDR web access design (Oct 8, 2026)
Design only; nothing installed or changed. Researched from upstream source and docs; no live desktop state was inspected.

## His rulings that apply
- Read-only only. No QR pairing. No session state through PhenoRegistry. Clipboard excluded.
- Write/control is a separate later grant.
- Network direction (stated by him): tailnet = machine-to-machine fabric (desktop, laptop, agents, HERDR internals). CF Access/Tunnel = identity edge for browser-reached clients (Instinct cloud browser, cockpit, future facades). cloudflared runs inside the tailnet so the CF edge terminates into tailnet-local services. Tailnet stays the source of truth for machine identity; CF Access mirrors it for people and clients. Sequence: desktop first, laptop second.
- The cloud browser is not on his tailnet, so the CF edge is the only path for Instinct; Tailscale alone does not work for it.
- The desktop-side install (facade service + cloudflared, HERDR 0.9.2+ check) is local work for him or his local agents. Web code and CF prep can be done remotely on his OK.

## Recommendation
A small read-only HERDR web facade on the 24/7 desktop, reached through Cloudflare Tunnel + Cloudflare Access.
Browser -> Access -> Tunnel -> loopback HTTP facade -> local HERDR socket.
Reuse HERDR's runtime, status aggregation and pane-reading. Do not replace it, publish state through PhenoRegistry, or require QR pairing. Reuse the cockpit's Access pattern, not its Pages deployment: Pages alone cannot read the desktop socket.

## 1. What HERDR is
- Upstream: https://github.com/GroepOnline/herdr. No standalone KooshaPari/herdr repo among the 66 accessible repos. His plugins: herdr-jcode, herdr-forgecode, herdr-helioslite; substantive copies in PhenoShared/absorption.
- A native terminal workspace runtime: persistent PTYs, workspaces/tabs/panes, background session server, detection/reporters, plugins, CLI and a newline-JSON local socket API (Unix socket; named pipe on Windows).
- Upstream already has herdr-gateway: a read-only HTTP/SSE adapter on 127.0.0.1:7777 (HERDR_GATEWAY_PORT, HERDR_SOCKET_PATH). Routes: GET /health, /v1/session, /v1/workspaces, /v1/agents, /v1/ops/context, /v1/events, /v1/clipboard. No auth, no dashboard, no pane-output route. Source uses UnixStream, so it is not Windows-portable. Source: https://github.com/GroepOnline/herdr/blob/b1a44f719fed5b29f06824ffc79636d678a74279/src/bin/herdr-gateway.rs . Docs: https://herdr.dev/docs/fleet-ops/ . The clipboard route exists in source though undocumented. Exclude it.

## 2. What it aggregates
- Snapshot/list/get gives pane/workspace/tab identities, layout, labels/cwd/process, detected agent state, reported native session refs. pane.read gives visible or bounded recent terminal text. Lifecycle events are status/resource changes, not full conversations. Protocol: https://herdr.dev/docs/socket-api/ (installed CLI: `herdr api schema --json`).
- Codex: official integration reports native session identity for restore; lifecycle is screen-manifest detection.
- KCode (crates/kcode-herdr): native working/idle/blocked lifecycle and session/resume reporting. Source warns kcode/forge are not in HERDR's official source table, so native agent_session may not populate. Restore uses resume_argv and needs HERDR 0.9.2+. Show missing native identity honestly.
- herdr-jcode wrapper mode just execs jcode, with no per-turn interception.
- Limit: HERDR sees managed panes plus attached reporters, not every headless child behind a shared KCode daemon or terminals launched outside HERDR. KCode has a separate harness API bridge at ~/.kcode/kcode-api.sock (sessions, discovery, streaming, get_history). Add it as a separate read-only adapter only if full headless-swarm inventory or transcripts are needed.

## 3. Minimal build
- Facade on loopback only (proposed 127.0.0.1:7780), reusing the gateway privately or calling the socket directly. Do not fork HERDR.
- Dashboard: host/session/workspace/tab/pane tree, agent state + source, explicit native ID when available, selected-pane terminal text with capture timestamp and truncation. Escape terminal contents as text, handle ANSI safely, no clickable control links.
- Bounded typed reads only (proposed): GET /api/hosts, /api/sessions, /api/session/{key}/snapshot, /api/session/{key}/agents, /api/session/{key}/pane/{id}/output?source=recent-unwrapped&lines=200, selected status SSE.
- Discover and allowlist named HERDR session sockets. Key identity by host+session+workspace/tab/pane and revalidate the occupant before reading. Snapshot on connect, resnapshot to reconcile; event history is not durable.
- Server-side method allowlist. No generic RPC proxy, shell param, stdin, plugin invocation, pane create/close/focus/resize, input, clipboard, filesystem read or API-key provisioning.
- Access-gate the whole hostname including API and events, using the verified cockpit identity allowlist. Validate Cf-Access-Jwt-Assertion (signature, issuer, audience, expiry) at the facade, or enforce Access at cloudflared plus a strict loopback origin. No caching of sensitive output, cap lines/bytes, redact likely secrets, audit logs free of terminal bodies and tokens.
- Route via CF Tunnel to the facade loopback port, no inbound router ports. https://developers.cloudflare.com/tunnel/routing/ , https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/

## 4. Checklist
- A. Establish desktop OS/runtime, herdr version, gateway availability, named sockets, `herdr api schema --json`. The Sept 27 eval recorded HERDR 0.9.1; verify today: https://github.com/KooshaPari/HarnessDesk/blob/4cda9fc62d8fece1f28946ca89e2332a531104d2/docs/sessions/20261004-moshi-evaluation/herdr-foundation.md
- B. Facade plus contract tests against his exact schema. On native Windows use a CLI/named-pipe adapter.
- C. Run under the desktop user that owns the HERDR sockets. User service + cloudflared service with restart and log rotation. No admin.
- D. Access policy BEFORE the public tunnel route. Verify denial without login, blocked write/clipboard paths. Tunnel creds secured on the desktop.
- E. Acceptance: existing Codex + KCode/JCode/Forge panes readable without starting agents; identity across detach/reattach; named sessions distinguished; crafted requests cannot write; no clipboard; HERDR restart recovers; disconnect shows stale/offline; authenticated cloud-browser read end to end. Headless workers verified separately.
- Laptop coverage is separate: its own facade + tunnel, must show offline when sleeping. Desktop first.

## Write/control later
HERDR supports pane.send_text/send_keys/send_input and agent.prompt locally. Browser controls would be small to build but are materially different authority, so keep them disabled. A future control service needs an explicit separate permission mode, occupant checks, POST + CSRF/Origin protection, per-action audit/confirmation and replay prevention. Structured approve/deny/cancel needs native harness APIs, not simulated keystrokes.

## Caveats
- No live desktop state inspected.
- Public Cargo.toml says 0.8.8, private notes saw 0.9.1, KCode reporter references 0.9.2+. Version and schema compatibility is the first local gate.
- Upstream LICENSE is AGPL/commercial. Avoid copying or forking HERDR code in the baseline; reconcile the exact-version license before any fork.
- GitHub code-search misses are not evidence of absence.
