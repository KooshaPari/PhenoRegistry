# Pass 7 — ontology entry and execution blockers

Date 2026-09-30.

## Oracle execution receipts

### Portage

Commit-associated workflows for the pass-6 oracle head ran. Windows and Ubuntu Python-test jobs again reached checkout/toolchain/container setup and failed at **Install dependencies**. All actual test steps were skipped. This is repeatable setup failure, not native oracle pass/fail evidence.

### PhenoLab

Commit-associated workflows for the pass-6 oracle head also ran. Sampled CI and mutation jobs completed failure with **no recorded steps**, repeating the pre-execution infrastructure pattern. Again, no native oracle result exists.

This is now enough evidence not to block semantic design on blind CI reruns. Infrastructure repair remains a separate prerequisite to native acceptance evidence.

### PhenoMLX

No commit-associated workflow run was returned for the previous research head. Absence remains no evidence.

## PhenoMLX remaining engine SOTA

The first multi-engine cache/profile pass now covers MLX-LM, vLLM, SGLang, TensorRT-LLM and llama.cpp.

SGLang provides RadixAttention and multi-tier HiCache. TensorRT-LLM provides paged/reusable KV, prioritized eviction, host offload, quantized/compressed KV and external cache connectors with explicit compatibility constraints. llama.cpp exposes configurable K/V cache types and draft-cache types.

This further falsifies generic cache ownership. Typed support/qualification profiles remain the strongest PhenoMLX thesis.

Repo receipt: `2a6d1721681bae89fa21a8a0cace39efb0ec6671`.

## W5 ontology v0 created

The three product repos now contain first explicit ontology documents, still DRAFT and ineligible as accepted requirement catalogues.

### Portage
Head `8747dcc174f83c7a5c5343ccd589e59e104c2150`.

Primary identities: EvaluationSubject, TaskContract, Dataset/Suite, EnvironmentProfile, EvaluationJob, Trial, Attempt, Trajectory, Artifact, VerifierPolicy, Assessment, EvidenceEnvelope, Comparison, ConsumerExport.

Critical semantic choice: regrade creates another Assessment over preserved execution; it does not rewrite Trial identity.

### PhenoMLX
Head `75f73adf301d4894ca0b001e7bbb80df39542fde`.

Primary identity is RuntimeProfile = exact model/quantization/engine/hardware/state/cache/speculation/scheduler configuration. Support is profile-scoped rather than inferred from engine feature flags.

### PhenoLab
Head `608c312edc27f68dc1d003f83ccd86aea08d7027`.

Primary identities: SystemSubject graph, Baseline, Intervention, Candidate, Assignment, DatasetPartition, WorkerAttempt, DurableExperiment, Trial, OptimizerFeedback, AcceptancePolicy, Assessment, Comparison, Decision, PromotionRecord, LearningArtifact and pluggable OptimizerEngine.

Critical semantic choice: optimizer feedback and independent product acceptance are separate identities/authority paths.

## Gate movement

W5 has **begun**, not passed. Ontologies require source/implementation/SOTA reconciliation and adversarial review before freeze.

Native execution blockers are now explicit repeated evidence. They do not convert to product failure or green.

Next work:
1. derive first semantic obligation sets from these ontologies without a target count;
2. create shared invariants/evidence identity constraints;
3. map existing implementation onto the highest-risk ontology relations;
4. repair CI only as needed to obtain native oracle receipts, without conflating CI hygiene with product completion.
