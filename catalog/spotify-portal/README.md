# Spotify Portal repository catalog

Snapshot: 2026-10-09 UTC. 31 public repositories whose names do not begin with zz (case-insensitive); 4 archived reference repositories.

Register this directory's catalog-info.yaml as a static Portal Location using its verified commit URL after review. Each .yaml file contains one JSON document (valid YAML), avoiding the pilot's multi-document hook problem. The Location resolves the owner and all repository records.

Repository Resources represent actual Git repositories; product Components retain independent metadata. Existing Tracera and AgilePlus Component entities and ownership are untouched. The phenotype-platform group represents catalog accountability, not capability reassignment. No dependencies, lifecycle readiness, or completion claims are inferred from names.

Private entries must be configured inside private Portal; do not publish private source contents here. Archived records remain searchable references; their presence does not authorize unarchiving or scheduling implementation. GitHub installation must use selected repositories, never All repositories. Refresh the inventory before access changes: concurrent work can add, rename or archive repositories.

Validation: JSON parsing, unique entity references, local owner resolution, existing relative Location targets, trailing-slash source URLs, public visibility and zz exclusion checked. Portal ingestion, workspace attachment and GitHub access expansion remain unverified pending browser authentication. Xirp connection is user-reported; no local session was launched or tested.

Pilot PRs: Tracera #1101 and AgilePlus #1100 remain open. Commit status endpoints report Vercel build-rate-limit failure; CodeRabbit and Snyk pass. This is not a complete check-runs audit.

Merge gate: review metadata and CI, register the verified commit-pinned location, verify the owner and 31 repository Resources in Portal, then reconcile immutable GitHub repository IDs with a fresh inventory. Catalog coverage is separate from implementation or usable-product progress.

This is bounded additive catalog metadata; no product behavior or capability absorption is changed. No AgilePlus CLI specification was generated in this environment.
