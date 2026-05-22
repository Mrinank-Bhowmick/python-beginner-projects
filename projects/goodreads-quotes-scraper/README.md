# Goodreads Quotes Scraper

Scrapes quotes from Goodreads — top popular, recently added, by tag, or by page number — and saves the results to `temp.json`.

## Example

```text
Enter choice..
1. Top Popular Quotes..
2. Top Recent Quotes..
3. Top Quotes by Tag..
4. Top Quotes by Pagination..
..3
To view complete list of tags press '' or visit goodreads.com
Tag please..love
Tag found.
Getting top quotes for the tag: love
"The best thing to hold onto in life is each other." -- Audrey Hepburn
"I am not afraid of storms, for I am learning how to sail my ship." -- Louisa May Alcott
```

Results are saved to `temp.json`.

## How to run on localhost

```
pip install bs4 selenium
python goodreadsScrape.py
```

## Dependencies

- bs4
- selenium
