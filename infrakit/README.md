# Phenotype InfraKit

Shared infrastructure crates extracted from the Phenotype ecosystem.

This workspace contains generic infrastructure components that are shared across Phenotype services.

**Absorbed into:** [`phenotype-registry`](https://github.com/KooshaPari/phenotype-registry) (PR #554)

## Crates

- `phenotype-analytics`: Analytics and reporting infrastructure
- `phenotype-bdd`: Behavior-driven development support
- `phenotype-compliance-scanner`: Compliance rule scanning
- `phenotype-config-core`: Unified configuration loading and management
- `phenotype-contract-tests`: Contract testing infrastructure
- `phenotype-contracts`: Shared traits and types
- `phenotype-crypto`: Cryptographic utilities
- `phenotype-fs`: High-performance file operations (shutil replacement)
- `phenotype-git-core`: Git operations core
- `phenotype-health`: Health check abstraction
- `phenotype-http-client`: HTTP client with error classification
- `phenotype-jsonl`: Streaming JSONL parser with integrity verification
- `phenotype-mock`: Mock trait generators and test doubles
- `phenotype-observability`: Telemetry and observability
- `phenotype-path`: Path resolution utilities
- `phenotype-project-registry`: Project registry operations
- `phenotype-rate-limiter`: Token-bucket rate limiter
- `phenotype-resources`: Resource management
- `phenotype-security-aggregator`: Security alert aggregation and scoring
- `phenotype-sentry-config`: Sentry error tracking configuration
- `phenotype-testing`: Test fixture trait and utilities
- `phenotype-utils`: General-purpose utilities
- `phenotype-validation`: Data validation infrastructure
- `agileplus-dashboard`: AgilePlus dashboard components
- `agileplus-dashboard-server`: AgilePlus dashboard server

## Usage

Add to your Cargo.toml:

```toml
[dependencies]
phenotype-jsonl = { path = "../phenotype-registry/infrakit/crates/phenotype-jsonl" }
phenotype-fs = { path = "../phenotype-registry/infrakit/crates/phenotype-fs" }
# ... other phenotype crates
```

## License

MIT
