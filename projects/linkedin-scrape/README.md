# LinkedIn Profile Scraper

Logs into LinkedIn with Selenium (Firefox) and scrapes contact information (email, phone, website) from a connection's profile.

## Example

```text
Enter email address or number with country code: you@example.com
Enter your password:
Andriy Burkov
Email Address: andriy@example.com
Phone Number: +1-555-0100
```

## How to run on localhost

```
pip install -r requirements.txt
python linkedin_profile.py
```

Requires Firefox and the bundled geckodriver.

## Dependencies

selenium, beautifulsoup4, requests, lxml.
