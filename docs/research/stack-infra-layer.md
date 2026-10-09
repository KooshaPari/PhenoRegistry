> Authored by Instinct

# Stack infra layer and network direction (Oct 8, 2026)
His rulings from Oct 8 (relayed via the Instinct agent). Decision lines, not research.

## Infra layer
- One Postgres is the anchor (Temporal, Hatchet and Kestra all want it).
- NATS = agent event bus (single binary, low ops cost). JetStream when persistence is needed. For agent-to-agent traffic and Hermes events.
- MinIO = artifact/blob store (agent outputs, exports, files), so orchestrator payloads stay small. Disk + R2 is the fallback if he does not want it.
- Neo4j: rejected for now. Hermes FTS5, JCode's embedding graph and Postgres cover relationship queries. Add it only when a workload needs traversal.
- Rule: every further exotic service is an ops tax on one desktop and needs a workload that demands it.

## Network
- Tailnet = machine-to-machine fabric (desktop, laptop, agents, HERDR internals).
- Cloudflare Access/Tunnel = identity edge for browser-reached clients (Instinct's cloud browser, the cockpit, future facades). The cloud browser is not on the tailnet, so CF is its only path.
- cloudflared runs inside the tailnet so the CF edge terminates into tailnet-local services.
- Tailnet stays the source of truth for machine identity; CF Access mirrors it for people and clients, not the other way around, so CF does not become a control point for the whole fabric.
- Sequence: desktop first, laptop second.

## Containerization
- Containerize agents and workloads on BOTH devices. Bare metal stays his end-user environment, used solely to try finished works.
- Session access (resolved by him): HERDR panes live on bare metal and their shells are `docker exec` into the agent containers. He sees sessions as a single pane on bare metal with exact current state, WSL-like. HERDR stays the session layer; agents stay contained. The HERDR web facade (see herdr-web-facade.md) then sees container sessions through the same panes.
- Related constraint from the orchestrator report: never mount the host Docker socket into coding workers; isolated workspaces per agent.

## Isolation model
- One shared, versioned base image. Per-task container instances spawned by the orchestrator, each with only that task's workspace and scoped credentials, destroyed on completion.
- NOT one shared running environment for all agents: that breaks bounded workers and prompt-injection containment.
- gVisor or Kata only for truly untrusted code.

## Host drive access
- Grant-style shares, like IAM: scoped path (for example his downloads folder or a project dir), read or read-write, per agent/task, default deny, logged.
- The orchestrator bind-mounts only the granted paths at container spawn.
- Mount granularity: TOOL-scoped by default (ephemeral, exists for the single action). Only an explicit user "approve for this session" elevates a mount to session level, and only when relevant to the task. Nothing ambient or permanent by default.
- Grants go through the same independent approval broker as other privileged actions. A drive share is just another resource type.

## Resource model
- Hosts: 16 GB M1 Pro laptop and 64 GB 5800X desktop, both expected to run tens to hundreds of agents.
- Agent identity lives in state (PhenoRegistry/git). Containers are ephemeral execution slots from the shared image, not agents.
- Bounded warm-container pool per host: on the order of 10-20 concurrent on the laptop, more on the desktop (starting figures to be measured, not tested yet).
- The orchestrator enforces per-host concurrency limits and queues the rest. Idle agents are checkpointed and their slots recycled.
