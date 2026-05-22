# Reuters Scraper

Scrapes technology news headlines, summaries, times, and links from the Reuters website and writes them to `reuters_scrape.csv`.

## Example

```text
$ python scrape.py
```

The script scrapes the Reuters technology page and writes results to `reuters_scrape.csv`. While running it prints each article's headline, summary snippet, timestamp, and link to the console:

```text
Tech giants face new antitrust scrutiny in Europe
Regulators are ramping up investigations into major technology companies...
2 hours ago
https://www.reuters.com/technology/tech-giants-face-antitrust-2024-01-15/
```

The CSV file contains columns: `Headline`, `Summary`, `Time`, `Article Link`.

## How to run on localhost

```sh
pip install beautifulsoup4 lxml
python scrape.py
```

## Dependencies

- beautifulsoup4
- lxml
- urllib, csv (standard library)
