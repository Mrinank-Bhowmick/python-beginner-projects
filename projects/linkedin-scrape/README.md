# LinkedIn Profile Scraper

Logs into LinkedIn with Selenium (Firefox) and scrapes contact information (email, phone, website) from a connection's profile.

## How to run

```
pip install -r requirements.txt
python linkedin_profile.py
```

Requires Firefox and the bundled geckodriver.

## Dependencies

selenium, beautifulsoup4, requests, lxml.

## Pyodide-runnable
No — it drives a real browser with Selenium to scrape a live website.
