# Scrape Y Combinator

Scrapes article titles and links from the Hacker News (Y Combinator) front page and writes them to `ycombinatornews.csv`.

## Example

```text
$ python main.py
Done
```

After running, a file `ycombinatornews.csv` is created in the same directory containing two columns — `ARTICLE TITLE` and `ARTICLE LINKS` — with one row per story scraped from the Hacker News front page.

## How to run on localhost

```sh
pip install requests beautifulsoup4 lxml
python main.py
```

## Dependencies

- requests
- beautifulsoup4
- lxml
- csv (standard library)
