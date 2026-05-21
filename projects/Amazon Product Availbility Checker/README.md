# Amazon Product Availability Checker

A console script that fetches an Amazon product page, parses it with
BeautifulSoup, and reports whether the product is in stock.

Before running, edit `amazon.py`:
- Set `product_url` to the Amazon product page you want to track.
- Set a valid `User-Agent` string in `headers` (Amazon blocks the default one).

## How to run

```bash
pip install requests beautifulsoup4
python amazon.py
```

## Dependencies

- `requests` — fetches the product page
- `beautifulsoup4` — parses the HTML

## Pyodide-runnable

No. It makes a live HTTP request to Amazon, and browsers block cross-origin
scraping requests, so it cannot run in the in-browser Pyodide playground.
