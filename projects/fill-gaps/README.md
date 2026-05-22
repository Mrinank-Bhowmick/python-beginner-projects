# Fill Gaps

A utility for renaming numbered files in a folder. `fillGaps` closes gaps in a numbered sequence (e.g. `spam001`, `spam003` becomes `spam001`, `spam002`), and `insertGaps` opens a gap at a chosen index.

## Example

Given files `spam001.txt` and `spam003.txt` in the current directory, running `fillGaps` closes the gap:

```text
Before: spam001.txt, spam003.txt
After:  spam001.txt, spam002.txt
```

Calling `insertGaps('.', 'spam', 2)` on `spam001.txt`, `spam002.txt` would shift files up to open a slot at index 2:

```text
Before: spam001.txt, spam002.txt
After:  spam001.txt, spam003.txt
```

## How to run on localhost

```
python fill_gaps.py
```

## Dependencies

Standard library only (`os`, `re`, `shutil`).
