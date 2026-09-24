# Executed example and its limits

[executed-toy-loop/demo-summary.json](executed-toy-loop/demo-summary.json) records a real local run of the bundled deterministic toy. It is not a run against the user's repository or an autonomous agent session.

The before variant returns successful-looking text without restoring records. The qualified observations reject that no-op. The after variant restores checked data and detects corrupt backup content. Both result sets pin actual toy/evaluator source and fixture observations; evidence JSON is retained under each bundle's raw directory.

```sh
python tools/pep.py summarize examples/executed-toy-loop/before
python tools/pep.py summarize examples/executed-toy-loop/after
python tools/demo_loop.py --out .local-runs/new-toy-run
```

These examples qualify only the two toy predicates and exercise record reduction. They do not validate the catalog, a real backup system, a model's reliability, cryptographic identity, all adversarial possibilities or full fresh-session lab operation. See [worked scenarios](../docs/18-WORKED-SCENARIOS.md) for broader proposed applications; those scenarios are not measured results.
