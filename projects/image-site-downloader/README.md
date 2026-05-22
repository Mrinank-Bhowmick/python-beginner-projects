# Image Site Downloader

Searches Imgur for a query term, scrapes the resulting image thumbnails, and downloads up to a chosen number of them into a local `results/` folder.

## Example

1. The script is hardcoded to search Imgur for `"messi"` and download up to 10 thumbnail images.
2. Run `python imgur-downloader.py`.
3. Matching images are saved by their original filename into the `results/` directory (created automatically).

## How to run on localhost

```
pip install requests bs4
python imgur-downloader.py
```

## Dependencies

- requests
- bs4
