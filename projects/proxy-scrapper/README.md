# Proxy Scrapper

Install BeautifulSoup
```sh
pip3 install beautifulsoup4
```

Run script
```sh
python3 proxy_scrapper.py
```

## Dependencies

- requests
- beautifulsoup4

## Pyodide-runnable

No - it uses `requests` to fetch a live website over the network, which is blocked in the browser sandbox.