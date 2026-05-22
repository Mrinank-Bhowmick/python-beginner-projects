# XKCD Comics Scraper

Downloads comic images from xkcd.com — either every comic in bulk, or a single comic by number — saving them to a local `xkcd` folder.

## Example

```text
Choose your option:
1.Download all images	2.Download Specific image
2
Enter any comic number between 1-2990: 42
Download image http://imgs.xkcd.com/comics/geeks_and_nerds.png
Finished
```

To download every comic, choose option `1`. The script traverses pages backwards from the latest, printing each URL as it downloads into the `xkcd/` folder.

## How to run on localhost

```
pip install requests beautifulsoup4 lxml
python comicXCD_scraper.py
```

## Dependencies

- `requests`
- `beautifulsoup4` (`bs4`)
- `lxml`
