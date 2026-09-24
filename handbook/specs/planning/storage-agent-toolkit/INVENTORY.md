# Storage-agent tooling inventory

**Review date:** 2026-09-07. **Scope:** the user's four-drive Windows desktop, with optional management of a MacBook's volume from Windows or the reverse.

This is a researched tooling inventory and original agent-workflow proposal, not a live storage audit. Actual disks, filesystem types, letters, controller topology, mount paths, installed tools and remote permissions have not been measured. The included policy and plans are contracts for an implementer; they do not enforce access by themselves.

## Recommendation

Use native collectors on each host, a shared metadata catalog, and a small set of task-specific skills. Add MCP only when the agent runtime needs that interface. Avoid giving every agent a new whole-disk crawler or unrestricted elevated shell.

Windows default: native storage discovery, WizTree, Everything/ES, Czkawka, smartctl, Robocopy and restic. Mac default: diskutil/tmutil, ncdu, Czkawka, supported smartctl telemetry and restic. Cross-host: ordinary OpenSSH and rclone SFTP; optionally Tailscale networking. TreeSize Professional is a paid reporting alternative; dua is an optional portable scanner.

## Baseline assessment

The attached baseline correctly distinguishes multi-volume analysis from one-codebase trees. It identifies an existing disk-usage MCP project and proposes compiled backends plus bounded agent output. Those are useful starting points.

Do not deploy the pasted multi-volume Python scanner unchanged. In the supplied file, `entry.is_link()` is not the correct DirEntry method; the exposed `max_depth` does not govern scanning; a hard-coded depth cutoff undercounts totals; and exceptions disappear rather than describing incomplete coverage. The first snippet can even convert a scan failure into a zero-size result. These are observations about the pasted code, not a source audit of the named third-party repository.

Source basis: user upload `Pasted markdown(4).md`, surfaced lines 97–108, 228–249 and 341–381. The original upload is not redistributed inside this bundle.

## Inventory

Evidence IDs refer to `sources.json`. Selection tiers are recommendations, not benchmark rankings.

| Tool | Role and priority | Agent interface | Decision / limitation |
|---|---|---|---|
| Native Windows Storage cmdlets + CIM | Core; Windows | Structured PowerShell objects / JSON adapter | Map devices, partitions, volumes and mount paths before cleanup; reconcile provider coverage rather than trusting a drive letter. [S06] |
| diskutil + tmutil | Core on Mac; macOS | Native command output; prefer supported machine-readable variants | Understand APFS container sharing and snapshots; keep capacity-pool accounting separate from per-volume logical size. [S07, S31] |
| WizTree | Preferred Windows scan; Windows | CLI CSV export | Fast local NTFS MFT scan. Elevate only the approved collector when necessary. Filename/size duplicate matches are candidates, not verified byte identity. Personal-only free licensing; commercial use needs suitable license. [S01, S02, S03] |
| Everything + ES | Preferred Windows search; Windows | Query CLI; structured exports | Use as the persistent name/metadata index; do not interpret an absent result as proof a file is absent outside index coverage. [S04] |
| TreeSize Professional | Paid alternative; Windows | CLI / saved reports / scheduled scans | Choose instead of the default space-reporting frontend when scheduled reporting and an established operator GUI matter. Scheduling is Professional-only. [S05] |
| ncdu | Preferred Mac structured scan; macOS / Unix | JSON export | Export the tree to a file and query offline. One-filesystem scans and output depth must not be confused with total-size accuracy. Interactive deletion is not an analysis permission. [S08] |
| dua-cli | Optional portable analyzer; Windows / macOS / Linux | CLI aggregates / interactive UI | Useful compiled scanner. APFS clone deduplication is opt-in and not a complete reclaimable-block oracle. [S09] |
| czkawka_cli | Preferred cross-platform duplicate review; Windows / macOS / Linux | CLI reports | Select exact-content hash mode for duplicate review. Similar-media detection and same-name groups must remain separate. No automatic removal. [S10] |
| fclones | Optional structured alternative; Linux-first; validate Windows / macOS | JSON / CSV groups and separate action commands | Attractive separation of detection from action, but upstream platform caveats prevent making it the default across both target hosts. [S11] |
| smartmontools smartctl | Core where hardware supports it; Cross-platform; device/controller-dependent | JSON telemetry | Collect drive identity, health, wear and errors where exposed. Missing telemetry means unsupported/unknown, not healthy. No repair or destructive tests. [S12, S13] |
| rclone | Core when moving data between hosts; Windows / macOS / Linux | CLI; SFTP backend | Use controlled copies plus check/readback. SFTP hash capability depends on the remote backend/shell; it does not promise native metadata fidelity. [S14, S15] |
| Robocopy | Core Windows-native movement; Windows | CLI / logs / exit codes | Useful when Windows metadata matters. Preview first. Do not make mirror/purge the default; those operations can delete destination data. [S16] |
| restic | Core data backup; Windows / macOS / Linux | CLI / repository checks | Independent versioned backup. Windows VSS is supported with the documented option; application consistency still needs owner-aware handling. Verify repository data and actual restores. [S17, S18] |
| Syncthing | Optional selected-folder sync; Host availability depends on build/distribution | REST API | Not full-drive management or a backup substitute. Versioning primarily archives incoming remote changes, not every local edit. [S19, S20] |
| OpenSSH | Core cross-host control; Windows / macOS / Linux | SSH / SFTP | Each host executes native collectors. Restrict identities and supported commands; use independent approved credentials for both directions. [S21, S22] |
| Tailscale network layer | Optional reachability; Windows / macOS / Linux | Private network under normal OpenSSH | Use ordinary OpenSSH over the network for symmetry. Tailscale SSH server is not supported on Windows; its macOS server requires CLI tailscaled. [S23] |
| SQLite or DuckDB storage catalog | Recommended integration component; Per chosen implementation | Bounded read queries / snapshot files | This is a proposed design, not a supplied service: share cached scans across agents, retain errors, scope and timestamps, and avoid flooding contexts with file trees. [Original design] |
| Application-owned cleanup commands; uv as verified example | Core cleanup policy; Per application | Native owner CLI | Use supported cleanup operations rather than deleting internal cache structure. uv placement across filesystems can lose hardlink benefits. [S30] |
| mamertofabian/mcp-everything-search | Optional adapter; Windows / macOS / Linux | MCP | Windows Everything, macOS mdfind and Linux locate/plocate are distinct backends with different coverage. Search only; not a disk-accounting system. [S26] |
| MCP filesystem reference server | Optional narrow file access; Host runtime-dependent | MCP | Explicit roots plus OS permissions. This is a reference server, not proof of an audited read-only security boundary. [S25] |
| dknell/mcp-system-info | Optional convenience; Host/runtime-dependent | MCP get_disk_info | Convenient usage and mount overview; does not replace disk topology, folder accounting or SMART telemetry. [S27] |
| sandraschi/disk-usage-mcp | Evaluation only; Validate on target hosts | MCP / reports / dashboard per README | Closest existing match to the baseline: wraps dua and czkawka. Its README is not evidence of production readiness; no runtime/source audit was completed. Validate install procedure instead of trusting the pasted uvx claim. [S24] |
| Desktop Commander | Optional supervised bridge; Windows / macOS | MCP terminal and file tools | Useful if the agent lacks local shell access. Broad execution remains broad execution; do not treat settings alone as a security boundary. [S28] |
| Smart Tree / Deep Directory Tree MCP | Optional navigation only; Per project | MCP / compact directory context | Useful for selected paths, not the central authority for full-machine storage accounting. [S32, S33] |

## Proposed agent skills

The nine directories in `skills/` are original workflow templates, not third-party packages represented as audited or already installed. Each uses a SKILL.md with required name/description metadata. Agent-runtime discovery locations and permission controls vary. [S29]

| Skill | Deliverable |
|---|---|
| storage-survey | Physical-device, partition, volume and capacity-pool map; coverage and privilege gaps. |
| storage-space-audit | Largest consumers, growth since prior scan and distinct logical/allocated/reclaimable accounting. |
| storage-duplicate-review | Exact-content candidate groups, intentional-copy exclusions, potential reclaim uncertainty. |
| storage-rebalance-plan | Owner-aware placement/migration proposal with filesystem and application compatibility checks. |
| storage-apply-approved-plan | Only explicitly approved, still-valid changes, through an enforcing adapter; no implementation included. |
| storage-backup-verify | Independent recovery evidence, data verification and selected restore tests. |
| storage-cross-host | Host-local execution through verified SSH identities and capability-aware SFTP transfers. |
| storage-owner-cleanup | Application-supported cache, build-artifact and obsolete-download cleanup proposals. |
| storage-health | Device telemetry and failure-risk escalation without firmware, repair or destructive tests. |

## Shared catalog and scheduler: implementation proposal

Keep the bulk data outside the language model. Catalog by host ID, physical device ID, filesystem volume ID, capacity-pool ID, mount path, scan time, collection source and tool version. Drive letters alone are not identities. Represent shared APFS container capacity once. Preserve logical size, allocated size and estimated reclaimable size separately; an unknown metric must be null, not zero.

Every scan must carry scope, explicit exclusions, unreadable paths, interrupted/unmounted state and completeness. Limit result rows and response bytes; use drilldown handles for deeper inspection. Reuse a fresh scan rather than launching one per agent. As an initial conservative scheduling policy, permit one heavy hashing/traversal job per physical disk and one mutation executor per host; tune only after measuring foreground workload impact. Multiple volumes may share one physical device.

MCP methods such as inventory, usage_top, search, duplicate_candidates, health, plan, apply, verify and undo would be a good integration boundary. These are proposed interfaces, not provided methods in every listed product. Runtime access must be enforced outside the model using OS identities, read-only views where appropriate, constrained argument parsing and approved roots. Never implement a security boundary as a regex around an unrestricted shell string.

## Windows–Mac in either direction

Run each scanner where its filesystem lives. An agent on Windows can call a constrained Mac adapter over SSH; a Mac agent can call the Windows adapter in the same way. The remote shell, path syntax, executable discovery, privilege model and supported commands remain host-specific. [S21, S22]

Use ordinary OpenSSH over the LAN or a private Tailscale network. Do not assume Tailscale SSH server works on Windows. Verify host keys, use dedicated identities, avoid agent forwarding and public unauthenticated MCP listeners, and never copy a private key between hosts just to make both directions convenient. macOS Remote Login access and Full Disk Access must be deliberately scoped; neither bypasses the need for least privilege. [S21, S22, S23]

Return metadata and manifests rather than crawling a mounted SFTP tree. Transfers are separate from inventory. rclone SFTP checksum capability varies by remote shell/backend; perform documented content readback where needed. File-content checks alone do not establish preservation of ACLs, extended attributes, resource forks, alternate streams, sparse layout or application semantics. Do not silently flatten unsupported metadata. [S14, S15]

## Change protocol: implementation proposal

1. Survey and scan within authorized scope. Reconcile missing or stale information before proposing removal.
2. Produce an immutable plan with volume identities, paths, file identity/fingerprints, intended changes, destination headroom, dependency owners, expected reclaim range and rollback/recovery evidence.
3. Obtain approval for that exact plan. Acquire locks and recheck identities, mount state and file changes before executing.
4. For migration, stage a copy; verify content and required metadata; cut over using an owner-supported mechanism; retain the source until independently recoverable. Cross-volume movement is not one atomic rename.
5. Purge only after retention and separately authorized checks. Quarantine on the same volume is reversible but does not itself free the requested space. Shared blocks, hardlinks and retained snapshots can reduce actual reclamation.

No formatting, repartitioning, pool changes, filesystem repair, firmware work, destructive tests, permanent purge or snapshot-retention changes are authorized by this bundle. Never use copy-sync mirroring as an implicit deletion policy. Intentional backups, Git worktrees, linked caches and active VM/database artifacts require owner-specific rules, not name/age heuristics.

## Special cases for this workload

Model files, source trees, environment caches, VM images, creative projects and reproducible build outputs must have different policies. Do not move all caches to a separate drive merely because it has space: uv recommends keeping its cache on the environment's filesystem to preserve linking efficiency, and supports owner-mediated pruning rather than arbitrary internal deletion. [S30]

On APFS, capacity belongs to the shared container and snapshots may explain discrepancies between file-tree sums and free space. Time Machine also distinguishes available/reclaimable snapshot space. A large tree is not necessarily equivalent to the bytes deletion will reclaim. [S07, S31]

Exact-content duplicates are still not necessarily redundant: a backup exists for failure isolation; hardlinked names may already share allocation; application paths can be intentional. Never use WizTree's name/size/date duplicate groups as a substitute for exact-content confirmation. [S02; original deletion policy]

## Rollout order

Start with an authorized read-only topology survey, then one native space scanner and shared search/index layer. Add independent recovery and a restore test before any cleanup. Add exact duplicate review, owner-aware cleanup and migration plans. Enable SSH in one direction, validate permissions and metadata behavior, then enable the other. Keep broad filesystem and terminal MCP adapters optional, not prerequisites.

## Validation checklist for the implementer

Test drive-letter changes, disconnected drives, permission-denied paths, partial scans, APFS shared pools, junction/symlink escapes, sparse files, hardlinks, active writers, cloud placeholders, case/Unicode name collisions, transfer interruption, malicious filenames, concurrent plans, insufficient destination space, stale hashes, unsupported SMART and restoration from backup. No test has been run against the user's computers by this bundle's author.
