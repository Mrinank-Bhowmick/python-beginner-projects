# Reuters Scraper

Scrapes technology news headlines, summaries, times, and links from the Reuters website and writes them to `reuters_scrape.csv`.

## How to run

```sh
pip install beautifulsoup4 lxml
python scrape.py
```

## Dependencies

- beautifulsoup4
- lxml
- urllib, csv (standard library)

## Pyodide-runnable

No - it uses `urllib` to fetch a live website over the network, which is blocked in the browser sandbox.
