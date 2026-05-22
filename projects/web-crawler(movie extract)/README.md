# Web Crawler (Movie Extract)

A web-scraping script intended to crawl Rotten Tomatoes' top-movies list, extract movie URLs, names, and synopses, and save them into an `.xls` spreadsheet.

## Example

When the script runs successfully, it fetches the Rotten Tomatoes top-movies list and prints each entry to the console, then saves results to `movies_top100.xls`:

```text
1 https://www.rottentomatoes.com/m/some_movie
 Movie: Some Great Film
Movie info: A gripping story about...
2 https://www.rottentomatoes.com/m/another_movie
 Movie: Another Classic
Movie info: An epic tale of...
```

## How to run on localhost

```bash
pip install requests lxml beautifulsoup4 xlwt
python main.py
```

Note: the source file currently contains syntax errors and would need fixing before it runs.

## Dependencies

- requests
- lxml
- beautifulsoup4
- xlwt
