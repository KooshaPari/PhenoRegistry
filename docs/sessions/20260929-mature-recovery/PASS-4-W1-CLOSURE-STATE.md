# Pass 4 — W1 archaeology closure state

Date: 2026-09-29. No production source snapshots changed.

## Portage

GitHub directly identifies Portage as a fork of `harbor-framework/harbor`. At observation, upstream main is `0dc28dd8051947ef019b6506357fc8fdb72f0be4`; live graph comparison gives merge base `b83e7686999a18ba90a8603794d7d18d42cab010`, Portage 503 commits from the base and upstream 40 commits from it. Raw commit counts are not feature counts; semantic delta classification is now the remaining fork/existence task.

The dangling `benchmarks/heliosbench` gitlink SHA `c758019115876ed0d99019060adfd08b17a912c5` remains unlocated after current Portage/Registry search. It is an explicit unresolved external-object/history item, but no longer justifies blocking all semantic work.

Portage W1 status: **fork identity/live merge base resolved; packaging + semantic owned delta + gitlink provenance open**.

Repo receipt: `fffac844544bdf66f3e825e5f401c751a376c3f4`.

## PhenoMLX

Accessible PhenoMLX-temp exposes only main, already proved contained in current history. Current PhenoMLX branch enumeration falsifies the stronger “all non-main history is represented” hypothesis:
- `feat/agileplus-snapshot-18b231ee`: 0 ahead / 117 behind — no unique work.
- `fix/metal-fixture-manifest-binding-20260816-v2`: 5 ahead / 115 behind — unique device/artifact evidence-contract work.
- `wip/2026-07-28-d-phenotype-omlx`: 13 ahead / 256 behind — unique cockpit capacity/VRAM/resolver, large benchmark artifacts, Windows scripts and platform-shell/Tauri work.

These unique branches are archaeology evidence, not merge candidates. They require semantic dispositions and current-equivalent checks. Formal PRD/requirements contamination remains excluded from normative derivation.

PhenoMLX W1 status: **main temp lineage resolved; accessible non-main denominator discovered; semantic disposition open**.

Repo receipt: `6a00ca462573a523bb4f14997fb0ee35e2014031`.

## PhenoLab / PhenoLM

A raw July 3 Codex session in the current repository contains direct user messages that materially resolve intent:
- optimize model, harness and model+harness combinations;
- build evalsets from long coding-agent traces and subagent roles;
- measure semantic agent performance plus compute/performance/concurrency;
- compare single and multi-agent/manager/advisor organizations;
- consider multiple serving engines/kernel approaches;
- build a managed self-improving garden loop;
- merge the separated `pheno-specs` back into the harness and use **PhenoLM** as the LLM layer.

The lower-case old specs baseline remains pinned at `13fcdc554c73abc765a34592a244abcf16eddf43`, but the same historical session records that the submodule was uninitialized, local content absent and remote unavailable from that environment. Current connector search also exposes no lower-case repository or exact Registry SHA. Exact content is therefore classified **BOUNDED MISSING SOURCE**, not silently reconstructed.

Later in-repo specs are useful but do not impersonate that missing baseline. Direct user messages plus current canonical docs provide sufficient authority to continue mature ontology/SOTA recovery.

PhenoLab W1 status: **core intent substantially direct-source grounded; old baseline content bounded missing; later reconstruction reconciliation continues**.

Repo receipt: `b52b67f4ed68fad169d17fa7b50a2307b9e25dff`.

## W1 exit decision

Do not declare archaeology globally complete yet.

Move Portage and PhenoLab into W2/W4 in parallel while finishing narrow W1 residuals:
- Portage: semantic fork delta, package authority, gitlink provenance if locatable.
- PhenoLab: later-spec migration/authority mapping; missing baseline stays explicit unless recovered.
- PhenoMLX: semantic disposition of two unique branches before W1 can reasonably close.

No fourth product, merge, production repair, release or destructive operation.
