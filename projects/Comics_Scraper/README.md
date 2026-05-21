# XKCD Comics Scraper

Downloads comic images from xkcd.com — either every comic in bulk, or a single comic by number — saving them to a local `xkcd` folder.

## How to run

```
pip install requests beautifulsoup4 lxml
python comicXCD_scraper.py
```

## Dependencies

- `requests`
- `beautifulsoup4` (`bs4`)
- `lxml`

## Pyodide-runnable

No — it scrapes the live xkcd.com website over the network and writes image files to disk.
