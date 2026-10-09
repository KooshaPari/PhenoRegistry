# Independent-style adversarial ontology review — pass 1

Date: 2026-09-30.  
Scope: ShareCLI and BytePort ontology v1 candidates.  
Method: assume each ontology is wrong and search for valid product behaviors/configurations it cannot explain. This is an internal adversarial pass, **not the required fresh independent reviewer**.

## ShareCLI counterexample attack

### A1 — one invocation belongs to multiple overlapping policy scopes
Example: a cargo process belongs to a user Project, a repository Workspace, and a global host admission policy.

Current ontology has Project/Workspace but does not explicitly model policy precedence/composition.

**Required refinement:** add `PolicyScope` / `PolicyDecision` or explicitly define that Project/Workspace/Host supply inputs to an Admission/Equivalence policy resolver. Do not encode precedence in UI/config accident.

### A2 — process outlives the worker/controller that registered it
ProcessGeneration survives one worker attempt and may need adoption by another ShareCLI control process.

Current ontology distinguishes process lifetime from PID but not durable ownership claim vs ephemeral controller.

**Required refinement:** ownership is a durable `ControlRegistration/OwnershipClaim` with generation and authority; worker/controller process is not the owner entity.

### A3 — one invocation fans out to multiple executions/speculations
Speculation/racing may create several ExecutionAttempts for one Invocation, with one selected result and others cancelled.

Current ontology supports ExecutionAttempt but not selection/cancellation relationship.

**Required refinement:** ResultSelection/AttemptDisposition belongs to execution lifecycle; durable reuse can only bind accepted selected result.

### A4 — one equivalence class is valid for in-flight sharing but not durable reuse
Already recognized semantically, but current EquivalenceDecision enum can make this explicit. Good.

### A5 — native cache supplies result but ShareCLI did not execute it
Tool-native cache hit is an observed ResultArtifact from an external mechanism, not necessarily ShareCLI ExecutionAttempt.

**Required refinement:** ResultArtifact provenance must support external/native producer and an Observation/ImportedResult relation rather than inventing a local attempt.

### A6 — remote/distributed work
Current product thesis is owned-workstation/local coordination; mesh history exists. If a future accepted journey coordinates remote workers, Host becomes a set and Lease/provider identity must be distributed.

**Disposition:** do not add distributed ontology now. Record as explicit out-of-scope/growth extension so mesh implementation cannot silently force it in.

### A7 — filesystem session applies to only part of an invocation
Subprocesses may escape/interact with paths outside the mount.

**Required refinement:** FilesystemSession has scope/coverage; `filesystem_ready=true` is not proof all relevant I/O was intercepted.

## BytePort counterexample attack

### B1 — one deployment contains multiple services/resources
Already anticipated by `ProviderResource[]`, but BuildArtifact is singular in the identity chain.

**Required refinement:** DeploymentIntent must support a service/component graph with zero/one/multiple BuildArtifacts and provider resources, while preserving per-component identity.

### B2 — service uses prebuilt artifact while another service builds from source
BuildOperation cannot be globally mandatory.

**Required refinement:** component-level ArtifactResolution supports `prebuilt verified` or `built`; DeploymentIntent references resolved artifacts.

### B3 — database/managed resource has no runnable BuildArtifact
A mature manifest may provision a database alongside an app.

**Required refinement:** ProviderResource may realize non-artifact desired components; RealizedDeployment is not only BuildArtifact→runtime.

### B4 — blue/green or rolling update temporarily has multiple realized generations
Project→one RealizedDeployment is insufficient.

**Required refinement:** DeploymentGeneration / rollout relationship; several ProviderResources/generations may coexist with desired/current/retiring roles.

### B5 — artifact is multi-platform index
One OCI digest may identify an index whose selected platform manifest differs.

**Required refinement:** BuildArtifact records media kind/platform set; RuntimeAdapter receipt records exact selected platform artifact where relevant.

### B6 — provider mutation succeeds but provider lookup cannot immediately find it
UNKNOWN cannot be collapsed to absent.

Already supported by UNKNOWN/RECONCILING; add bounded retry/evidence age requirements.

### B7 — publication occurs before deployment or is a draft preview
PortfolioProjection should not require RealizedDeployment for every mode.

**Required refinement:** Projection mode can be draft/planned/realized; verified live facts only exist when evidence supports them. Mature publication policy decides which modes may be public.

### B8 — rollback targets an earlier artifact/source generation
Current identity chain can represent it but lifecycle relation is missing.

**Required refinement:** DeploymentIntent/Generation carries predecessor/supersedes/rollback-of relation.

### B9 — external engine owns operation state
Already allowed by invariant 6/12. Need `ExternalOperationRef` as explicit identity, not prose exception.

### B10 — source is not Git
Current SourceReference definition allows generic selectors, but recovered product intent is Git-centric.

**Disposition:** keep source ontology generic enough for archive/local/prebuilt extension, but do not claim support absent an accepted adapter.

## Required ontology changes before candidate freeze

### ShareCLI
Add:
- PolicyScope/PolicyDecision;
- durable OwnershipClaim/ControlRegistration;
- AttemptDisposition/ResultSelection;
- external/native result provenance;
- FilesystemSession coverage/scope;
- explicit local-only current product boundary with distributed growth extension.

### BytePort
Add:
- Component/Service desired graph;
- ArtifactResolution per component;
- non-artifact resources;
- DeploymentGeneration/rollout relationships;
- ExternalOperationRef;
- artifact media/platform identity;
- projection mode/draft semantics;
- predecessor/supersedes/rollback relations.

## Verdict

Both ontology candidates survive the broad product identity attack but are **not freeze-ready**. The missing entities above are semantic gaps, not reasons to return to implementation-shaped models.

No completion percentage changes.
