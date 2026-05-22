# English Thesaurus

A console thesaurus/dictionary that looks up word meanings from a local `data.json` file, suggesting close matches when a word is misspelled.

## Example

```text
Ctrl-C to exit

Enter the word to find meaning: happy
Meaning 1: feeling or showing pleasure or contentment

Enter the word to find meaning: happpy
Did u mean the word happy ?

Press Yes-Y,No-N,Exit-E: Y
Meaning 1: feeling or showing pleasure or contentment

Enter the word to find meaning: xyzabc
```

(No close match found — the program prints nothing and prompts again.)

## How to run on localhost

```
python App.py
```

Run from the repository root so the `projects\English Thesaurus\data.json` path resolves correctly.

## Dependencies

Standard library only (`json`, `difflib`).
