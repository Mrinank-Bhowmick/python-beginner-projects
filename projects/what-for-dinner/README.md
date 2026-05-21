# What For Dinner

A console app that suggests a random meal for dinner. It fetches a random recipe from TheMealDB API and prints the meal name, origin, category, cooking instructions, and a YouTube link in a colorized format.

## How to run

```bash
pip install requests
python main.py
```

## Dependencies

- requests

## Pyodide-runnable

No — it uses `requests` to call the live TheMealDB API, which is not available in Pyodide.
