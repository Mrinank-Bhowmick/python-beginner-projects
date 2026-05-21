# Web Crawler (Movie Extract)

A web-scraping script intended to crawl Rotten Tomatoes' top-movies list, extract movie URLs, names, and synopses, and save them into an `.xls` spreadsheet.

## How to run

```bash
pip install requests lxml beautifulsoup4 xlwt
python main.py
```

Note: the source file currently contains syntax errors and would need fixing before it runs.

## Dependencies

- requests
- lxml
- beautifulsoup4
- xlwt

## Pyodide-runnable

No — it uses `requests` to scrape live websites, which is not available in Pyodide.
