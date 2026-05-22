# Regex Search

A console tool that prompts for a regular expression and prints every line in the `.txt` files of a folder that matches it.

## Example

```text
enter regex: \bpython\b
This is a python tutorial.
Learn python programming today.
```

The tool searches all `.txt` files in the current directory and prints every line that matches the supplied regular expression.

## How to run on localhost

```sh
python regex-search.py
```

## Dependencies

Standard library only (uses `os` and `re`).
