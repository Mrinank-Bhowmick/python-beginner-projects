# Amazon Product Availability Checker

A console script that fetches an Amazon product page, parses it with
BeautifulSoup, and reports whether the product is in stock.

Before running, edit `amazon.py`:

- Set `product_url` to the Amazon product page you want to track.
- Set a valid `User-Agent` string in `headers` (Amazon blocks the default one).

## Example

After setting `product_url` and `User-Agent` in `amazon.py` and running the
script, the console prints one of:

```text
Wireless Bluetooth Headphones is available on Amazon.
```

or

```text
Wireless Bluetooth Headphones is currently out of stock on Amazon.
```

## How to run on localhost

```bash
pip install requests beautifulsoup4
python amazon.py
```

## Dependencies

- `requests` — fetches the product page
- `beautifulsoup4` — parses the HTML
