# Bigram Autocomplete

A simple word-autocomplete tool. It builds bigram (word-pair) frequencies from a training corpus you type in, then predicts the next words following a starting word.

## Example

```text
Insert the training corpus here (can be multiline)the cat sat on the mat. the cat ate the rat.
insert a word: the
the cat sat on the mat
```

## How to run on localhost

```
python bigram_autocomplete.py
```

## Dependencies

Standard library only (uses `re`).
