# Execution receipt 19 — separate-process oracle qualified; product compile defects repaired

Date: 2026-09-30. Program remains OPEN.

## Separate-process replacement oracle
Attempt Replacement Oracle is now green on both spec branches: HeliosLite run 36717818675 and KCode run 36717831831. This qualifies the independent process-death model: committed effect reconciles without redispatch; known absence permits one retry; conflict/corrupt receipt fail closed; identity mismatch cannot steal prior evidence. Registry trace rows are promoted to PROCESS_DEATH_ORACLE_QUALIFIED.

This still does not close H-F008/K-F008 because the product-integrated hooks failed compilation.

## HeliosLite #333 failure and repair
Focused Effect Recovery Hook failed with E0433: ToolCallId was propagated in code but not imported into tool_registry.rs. Candidate is repaired at `b455e1fcf2d5a3efd56017e86bc33c225ed87397`. New exact-head CI is required. Prior failing run remains evidence.

## KCode #20 failure and repair
Effect Recovery Hook and daemon-identity regression failed because adding `effect_recovery` directly to Registry broke 12 explicit Registry literals in existing tests/batch tests. This is integration-surface evidence: Registry construction is wider than the first patch assumed. The fixtures now initialize the optional field; current candidate `bac23f8885bb4a5f17bad926ca1451581b1a8b51` requires fresh CI. No prior green is inherited.

## KCode #22
Daemon identity regression, macOS trust policy and linked-issue governance are all green at `a9daae12...`. K-F009 still requires signed-release provenance experiments before closure.

## Persistence coverage
Helios H-S10 and KCode K-S13 were deepened from inventory to semantic partial resolution. KCode transcript recovery is strong but explicitly separate from external-effect authority.

No completion or merge verdict.