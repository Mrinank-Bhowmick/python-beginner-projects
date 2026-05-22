# Code Reviewer

A simple static code-review tool that parses a Python file into an AST and reports possible issues such as missing docstrings, undefined variables, style violations, and poorly formatted comments.

## Example

```text
Code Review Feedback:
- Function 'generate_recipe' should have a docstring or 'pass' statement.
- Variable 'recipe' is used but not defined.
- Improve comment style in line 12: '#TODO fix this'
- Code style issues found. Please check and fix them.
```

If no issues are found the output is:

```text
No coding errors found. Code looks good!
```

## How to run on localhost

```
pip install pycodestyle
python code_reviewer.py
```

By default it analyzes `../Recipe_Generator/recipe_generator.py`; edit the `python_file` variable in the script to review a different file.

## Dependencies

- `pycodestyle`
- `ast` (standard library)
