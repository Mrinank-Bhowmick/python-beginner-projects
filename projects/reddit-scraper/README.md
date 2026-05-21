# Reddit Scraper

Fetches the top posts from the r/python subreddit via Reddit's JSON API and stores them in a local SQLite database (`reddit_news.db`).

## How to run

```sh
pip install requests
python -c "import grabnews; grabnews.reddit_get()"
```

## Dependencies

- requests
- sqlite3 (standard library)

## Pyodide-runnable

No - it uses `requests` to fetch live data from Reddit over the network, which is blocked in the browser sandbox.
