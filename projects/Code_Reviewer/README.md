# Code Reviewer

A simple static code-review tool that parses a Python file into an AST and reports possible issues such as missing docstrings, undefined variables, style violations, and poorly formatted comments.

## How to run

```
pip install pycodestyle
python code_reviewer.py
```

By default it analyzes `../Recipe_Generator/recipe_generator.py`; edit the `python_file` variable in the script to review a different file.

## Dependencies

- `pycodestyle`
- `ast` (standard library)

## Pyodide-runnable

No — it reads a Python source file from the real filesystem by relative path, and `pycodestyle` is not available in Pyodide.
