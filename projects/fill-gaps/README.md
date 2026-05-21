# Fill Gaps

A utility for renaming numbered files in a folder. `fillGaps` closes gaps in a numbered sequence (e.g. `spam001`, `spam003` becomes `spam001`, `spam002`), and `insertGaps` opens a gap at a chosen index.

## How to run

```
python fill_gaps.py
```

## Dependencies

Standard library only (`os`, `re`, `shutil`).

## Pyodide-runnable

No — it lists, renames, and moves files on the real filesystem, which is not available in a browser sandbox.
