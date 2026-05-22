# Link Verification

Fetches a web page, extracts all of its links, and reports which ones are good or broken.

## Example

```text
Good: https://automatetheboringstuff.com/
Good: https://nostarch.com/automatestuff2
Broken: https://example.com/missing-page
Good: https://python.org
3 Good. 1 Broken
```

## How to run on localhost

```
pip install -r requirements.txt
python verify_links.py
```

## Dependencies

requests, beautifulsoup4.
