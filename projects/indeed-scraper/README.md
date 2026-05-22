# Indeed Job Scraper

Scrapes job listings from Indeed for several cities and job titles, then saves the results to a CSV file.

## Example

1. Run `python indeed-scraper.py`.
2. The script iterates over 8 job titles (e.g., `full+stack+developer`, `data+scientist`) across 4 cities (Mumbai, Bangalore, Hyderabad, Pune), printing each URL as it fetches results:
   ```
   http://www.indeed.co.in/jobs?q=full+stack+developer&l=mumbai&start=0
   full+stack+developer mumbai 0
   ...
   ```
3. When finished, all scraped listings (job title, company, summary, location, salary, date) are saved to `job_listing.csv`.

## How to run on localhost

```
pip install -r requirements.txt
python indeed-scraper.py
```

## Dependencies

requests, beautifulsoup4, lxml, pandas.
