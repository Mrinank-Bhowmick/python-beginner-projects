# World Cup Player Comparison

Scrapes 2022 World Cup team statistics from fbref.com, lets you pick two players from two countries, and saves a bar chart comparing their combined goals and assists.

## How to run

```bash
pip install pandas requests beautifulsoup4 numpy matplotlib
python main.py
```

## Dependencies

- pandas
- requests
- beautifulsoup4
- numpy
- matplotlib

## Pyodide-runnable

No — it uses `requests` to scrape a live website, which is not available in Pyodide.
