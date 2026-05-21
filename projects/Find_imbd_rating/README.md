# Find IMDb Rating

Reads the names of film files from a local directory, searches IMDb for each title, scrapes the rating and genre, and writes the results to `film_ratings.csv`.

## How to run

```
pip install beautifulsoup4 requests pandas
python Find_imbd_rating.py
```

## Dependencies

- beautifulsoup4
- requests
- pandas

## Pyodide-runnable

No — it makes live HTTP requests to IMDb and reads a real directory listing, neither of which is available in a browser sandbox.
