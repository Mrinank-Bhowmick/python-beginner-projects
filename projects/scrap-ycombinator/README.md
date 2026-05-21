# Scrape Y Combinator

Scrapes article titles and links from the Hacker News (Y Combinator) front page and writes them to `ycombinatornews.csv`.

## How to run

```sh
pip install requests beautifulsoup4 lxml
python main.py
```

## Dependencies

- requests
- beautifulsoup4
- lxml
- csv (standard library)

## Pyodide-runnable

No - it uses `requests` to fetch a live website over the network, which is blocked in the browser sandbox.
