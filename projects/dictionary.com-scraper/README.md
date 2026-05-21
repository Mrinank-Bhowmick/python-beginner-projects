# Dictionary.com Word of the Day Scraper

Scrapes the "Word of the Day" from dictionary.com, can fetch all its meanings, generate a text-to-speech pronunciation, and open the word's page in a browser.

## How to run

```
pip install beautifulsoup4 gtts
python wordOfTheDay.py
```

## Dependencies

- `beautifulsoup4` (`bs4`)
- `gtts`

## Pyodide-runnable

No — it fetches pages from dictionary.com over the network, uses the online `gtts` service, and launches an external browser/media player.
