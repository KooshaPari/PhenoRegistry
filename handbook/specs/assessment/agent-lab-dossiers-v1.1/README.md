# Agent Lab Assessment Dossiers — v1.1

**Start with [OPEN-ME.html](OPEN-ME.html)** for eight filled, readable examples. Everything needed to inspect them is inside this package. No server, external fonts, network, GitHub connection, Docker, AgilePlus, or Tracera instance is required.

## Naming

| Layer | Name | Purpose |
|---|---|---|
| Whole operating system | Agent Lab Evaluation System | The existing protocol, catalog, operating procedures, and reference kernel. |
| Reusable master | **Master Assessment Kit** | Schemas, authoring templates, profiles, rubric definitions, procedures, and renderers. It is a file set, not a single document. |
| A bounded specification of work | Assignment capsule | The exact subject, intent, criteria, profile, gates, evidence requirements, and epoch. |
| A completed assessment snapshot | **Assessment Dossier** | The assignment, inventory/context, results, evidence, findings, decisions, and continuity records for one scope and baseline. |
| Main readable projection | Assessment report | `ASSESSMENT.md` and `ASSESSMENT.html`, generated from canonical JSON. |
| Numerical/status projection | Scorecard | One part of the dossier. It never replaces the evidence or the wider decision record. |

A rubric is the definition of the questions and acceptance conditions. A result fills in one scoped instance of a criterion. A scorecard aggregates results. A dossier preserves all of them with context and provenance.

## Included examples

| Directory | Case | Evidence class | Scoped rows |
|---|---|---|---:|
| `examples/01-restoration-before/` | Success text but no restoration | Executed bundled synthetic fixture | 2 |
| `examples/02-restoration-after/` | Correct restoration and corruption rejection | Executed bundled synthetic fixture | 2 |
| `examples/03-agent-born-library/` | Local library slice, missing broader value/compatibility evidence | Fictional scenario | 14 |
| `examples/04-polished-dashboard/` | Coherent visual design, broken durable outcome | Fictional scenario; 18 domains | 36 |
| `examples/05-service-blocked-deployment/` | Local slice versus blocked hosted release | Fictional scenario | 14 |
| `examples/06-polyrepo-integration/` | Passing components, broken consumer composition | Fictional scenario | 12 |
| `examples/07-grader-before/` | Correct product rejected by incidental filename rule | Fictional scenario | 11 |
| `examples/08-grader-after/` | Same subject under corrected evaluator baseline | Fictional scenario | 11 |

There are **102 scoped rows** across the eight snapshots. Repeated criteria across snapshots are instances, not extra catalog criteria. The 1,080-entry candidate catalog remains in the retained core. The examples do not pretend to evaluate it all.

## Two different kinds of truth

The restoration pair contains freshly executed observations from the included Python fixture. No user repository was involved, and two passing toy predicates do not establish a production-safe backup system.

The six other cases are deliberately fictional. Their stated PASS/FAIL values teach how a filled assessment would read. Every such result is `PROPOSED`, there are no claimed instrument qualifications, and the core evidence reducer gives them no operational credit. The reports show both **scenario premise** and **admissible evidence**. This separation prevents an example from becoming a spurious product acceptance when imported by an agent.

## Commands

Use an installed Python 3.10+ interpreter. The actual tested interpreter is recorded in [qualification](qualification/VALIDATION-REPORT.md). No third-party runtime dependency is required.

```sh
python tools/dossier.py check-package
python tools/dossier.py verify-all
python tools/dossier.py verify examples/04-polished-dashboard
python core-v1.0/tools/pep.py self-test
python -m unittest discover -s qualification -p 'test_*.py' -v
```

To regenerate the disposable human/machine views after a deliberate source edit:

```sh
python tools/dossier.py render examples/04-polished-dashboard
python tools/dossier.py render-all
```

`render` deliberately replaces only the declared generated outputs. It does not overwrite canonical JSON. An edited distribution no longer matches its old release manifest; create a new release manifest through your authorized release process rather than suppress the failed integrity check. Regenerating a view is not accepting a product, approving an action, or signing evidence.

## Use with a real repository

Give an operating agent [START-HERE.md](START-HERE.md) and use [master/README.md](master/README.md). Map these logical paths into the current owner-held audit directory. Do not create a repository merely for this file set.

New assessment records should live outside this immutable distribution, for example in an authorized subject's audit folder or under an ignored `.local-runs/` scratch folder. Use the retained core initializer and the dossier template; activate actual intent, scope, measurements, and evidence rather than copying the fictional premises.

## Version and compatibility

`core-v1.0/` is the prior v1.0 kit retained byte-for-byte, including its own manifest. The additive dossier layer is v1.1. Core schemas remain `1.0.0`; only the additional dossier-context schema is `1.1.0`. This is not a silent rewrite of the core grader or its catalog.

[Master contract](MASTER-ASSESSMENT-KIT.md) · [Format and integrity](docs/FORMAT-AND-INTEGRITY.md) · [Validation report](qualification/VALIDATION-REPORT.md) · [Sources](docs/SOURCES.md)
