# Internal dependency snapshot supplement

Date: 2026-09-29.

Both ShareCLI and BytePort pin shared Phenotype Rust dependencies to PhenoInfra revision prefix `dd040ed1`. Cargo.lock resolves the BytePort source to exact commit:

`KooshaPari/PhenoInfra@dd040ed1bb293e3c843245448a9a173f5dff3470`

The commit exists and is dated 2026-09-16. This exact revision is now the frozen directly depended-on internal source for the current recovery pass.

### ShareCLI
Root Cargo.toml declares phenotype-crypto, phenotype-health, phenotype-observability and phenotype-state-machine from this revision. Consumer mapping remains to be completed per crate; declaring a dependency does not prove a mature product obligation.

### BytePort
Root Cargo.toml declares phenotype-crypto, phenotype-observability and phenotype-health from this revision. Current code search finds these re-exported through `crates/integration`; the June agent-generated transport/CLI lineage remains separately classified. Consumer reach beyond re-export must be proven before these shared crates influence product mapping.

The dependency commit itself is not a product acceptance source. Its relevant package trees/APIs must be inspected only where actual callers materially depend on them.
