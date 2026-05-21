# Goodreads Quotes Scraper

Scrapes quotes from Goodreads — top popular, recently added, by tag, or by page number — and saves the results to `temp.json`.

## How to run

```
pip install bs4 selenium
python goodreadsScrape.py
```

## Dependencies

- bs4
- selenium

## Pyodide-runnable

No — it fetches live web pages over the network (and imports Selenium), which is not available in a browser sandbox.
