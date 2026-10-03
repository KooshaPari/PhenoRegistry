# Pass 15 — prototype discrimination

Date 2026-09-30. Exactly Dino + Civis.

## Dino run 36686256615

Candidate `5727cae4367b805ca813d534324d80a2f9751e48`; artifact `11084390021`, sha256 `e9b5c5955442db203cd6df3a1ec61914c89246800ef9fccb6d93ebc35e019a8d`.

Six tests executed: 2 passed, 4 failed.

All three unchanged production-path controls remained red:
- removed content stale;
- identical reload conflict accumulation;
- removed patch stale at150 instead of current disk200.

Of the three test-only generation prototype cases, two passed:
- fresh generation removes historical registration and converges;
- failed candidate does not replace prior published generation.

Prototype patch case failed before semantic assertion because `TryPublish` classified an additional patch progress string (`Applying ...`) as a hard error. This is harness classification, not evidence against fresh-generation patch isolation. Prototype classifier corrected in `ac56ea3da4bec50ae26a2eb1d3393b5013970c30` to ignore the same patch progress categories already observed in ContentLoadResult.

Interpretation: fresh isolated generation construction already discriminates positively on removal convergence and failure atomicity while current path remains red. Patch isolation requires rerun.

## Civis run 36686311329

Candidate `0d6fd4c809b030654553880847a041425503fc67`; artifact `11084975866`, sha256 `e8daba089bf0414a162999f7b1e835d0212e3335187c122fbb9f3599cbf77959`.

Compile failed before tests because the prototype imported `ResearchCache` from crate root; the type is `crate::engine::ResearchCache`. This is prototype harness debt, not persistence behavior. Fixed in `ed8d8bbbffc4883ecbb7fa382c28aeb43ab60b14`.

No Civis prototype semantic result from this run.

## Next evidence threshold

Dino architecture becomes strongly supported for the isolated SDK problem if the corrected patch prototype passes while all three production controls remain red. Civis architecture gets its first discrimination only after the corrected prototype compiles and runs beside unchanged red controls.
