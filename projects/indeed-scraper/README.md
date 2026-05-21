# Indeed Job Scraper

Scrapes job listings from Indeed for several cities and job titles, then saves the results to a CSV file.

## How to run

```
pip install -r requirements.txt
python indeed-scraper.py
```

## Dependencies

requests, beautifulsoup4, lxml, pandas.

## Pyodide-runnable
No — it makes live HTTP requests to Indeed to scrape web pages, which Pyodide cannot do.
