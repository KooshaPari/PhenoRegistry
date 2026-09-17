# Executable reference kernel

## Requirements and scope

`tools/pep.py` uses Python's standard library and targets Python 3.10 or later. The packaged qualification report identifies the actual tested interpreter/OS; other supported-looking versions and platforms are not claimed tested. No database, API key, network connection, Docker, AgilePlus or Tracera installation is required. Use `python`, `python3` or Windows `py -3` as appropriate for the installed interpreter.

Commands run from the extracted package root unless an absolute script path is used.

```sh
python tools/pep.py check-package
python tools/pep.py self-test
python tools/pep.py catalog
python tools/pep.py catalog --domain D08
python tools/pep.py validate templates/intent.template.json
python tools/pep.py summarize examples/executed-toy-loop/before
python tools/pep.py summarize examples/executed-toy-loop/after
python tools/demo_loop.py --out /absolute/new/toy-run
python tools/pep.py init-assessment --out /absolute/new/assessment --profile cli --subject-label my-project
python tools/pep.py inspect /absolute/authorized/repository --max-files 5000
```

The output paths above must be new paths. The demo and initializer refuse overwrite. The inspector returns names/sizes only, skips generated directories and symlinks, does not read file contents or execute commands, and does not produce a complete source snapshot or quality score. Its output can contain private filenames; handle it accordingly.

## Implemented

Strict JSON parsing rejects duplicate object keys and non-finite numeric constants. A bounded local schema validator checks the exact schema vocabulary shipped by this release; unknown keywords fail closed. It is not a general JSON Schema implementation. Relative schema references resolve only inside the bundled schema directory. No remote schema fetch occurs.

Bundle checks enforce selected assignment/result/subject/catalog bindings, file-byte digests, current timestamps relative to assessment, listed-record completeness, measurement binding identity, qualification scope and evaluator identity, and valid supersession relations. Results reduce deterministically into independent rates, unresolved applicability and non-compensating gates. Multiple effective results remain UNKNOWN rather than selecting a lucky winner.

## Not implemented

This is not a universal repository grader, scheduler, semantic model judge, registry, identity service, cryptographic signer, remote adapter, lease enforcement daemon or policy engine. It does not execute the 1,080 catalog procedures. It does not independently validate external authority references, actual grader observations, expert qualifications or product usefulness. Generic records outside the assessment bundle receive shape validation, not universal cross-record graph validation.

Qualification flags are accepted input records; local evidence bytes are verified, not authenticated. The toy supplies real execution evidence for its own two predicates. Extending this to actual product checks needs a qualified adapter and stronger trust paths where appropriate.

## Bundle layout

`assignment.json`, `assessment.json`, `results/<id>.json`, `evidence/<id>.json`, `qualifications/<id>.json`, optional `measurement-bindings/<id>.json`, and raw evidence files. The three indexed record directories must match the assessment manifest. Evidence paths must be existing regular non-symlink files below the bundle. Registry references remain external and unverified by this kernel.

## Exit behavior

Core commands return 0 when their requested operation is structurally successful, 2 for invalid input/integrity problems, and self-test returns the unittest process status. `summarize` may return exit 0 with a FAIL or BLOCKED product gate: successful analysis is not successful product acceptance. Inspect the JSON gate state. A future CI adapter must map these deliberately, not assume zero means product success.

## Package integrity

`MANIFEST.json` hashes all distributed files except itself. The ZIP has a companion SHA-256 file. These detect accidental alteration relative to the supplied records, not authenticity against an attacker replacing both. Run tests on the extracted package. Runtime bytecode and `.local-runs/` are excluded from file-set comparison and are not trusted input to acceptance.

## Cross-run boundary

The kernel validates one assessment bundle, not a trusted global history. Two bundles with the same epoch label can only be compared after checking their acceptance definitions. It does not enforce that all agents used the same meaning for that label. Source changes create new immutable candidate bindings; material acceptance changes require an epoch amendment. The demo uses two candidate snapshots under one unchanged toy acceptance meaning.
