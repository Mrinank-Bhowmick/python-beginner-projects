# English Thesaurus

A console thesaurus/dictionary that looks up word meanings from a local `data.json` file, suggesting close matches when a word is misspelled.

## How to run

```
python App.py
```

Run from the repository root so the `projects\English Thesaurus\data.json` path resolves correctly.

## Dependencies

Standard library only (`json`, `difflib`).

## Pyodide-runnable

No — it loads `data.json` using a hard-coded Windows relative path; it could only run in Pyodide if that data file were loaded into the virtual filesystem first.
