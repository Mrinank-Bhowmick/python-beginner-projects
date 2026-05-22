# Reddit Scraper

Fetches the top posts from the r/python subreddit via Reddit's JSON API and stores them in a local SQLite database (`reddit_news.db`).

## Example

```text
$ python -c "import grabnews; grabnews.reddit_get()"
Inserted
Inserted
Inserted
Inserted
Inserted
Inserted
Inserted
Inserted
Inserted
Inserted
```

Each `Inserted` line means one top post from r/python was written to `reddit_news.db`. Re-running the script prints `Updated` for posts already in the database.

## How to run on localhost

```sh
pip install requests
python -c "import grabnews; grabnews.reddit_get()"
```

## Dependencies

- requests
- sqlite3 (standard library)
