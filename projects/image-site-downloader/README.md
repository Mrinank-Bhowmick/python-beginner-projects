# Image Site Downloader

Searches Imgur for a query term, scrapes the resulting image thumbnails, and downloads up to a chosen number of them into a local `results/` folder.

## How to run

```
pip install requests bs4
python imgur-downloader.py
```

## Dependencies

- requests
- bs4

## Pyodide-runnable

No — it makes live HTTP requests and writes downloaded files to disk, neither of which is available in a browser sandbox.
