# Data Entry Automation

**In this project, We have Scrapped data(for educational Purpose only) from a rental properties website and upload it to as response of Google Form and then convert it to the .csv file**

**Library Used**
_-> Selenium_
_-> bs4_
_-> time_

If you find any Difficulty in understanding things, then check for the docs of these library.

## Example

1. Set `chrome_path`, `FORM`, and `HEADERS["User-Agent"]` in `main.py` with your ChromeDriver path, Google Form URL, and browser user-agent string.
2. Run `python main.py`. The script sends an HTTP request to Zillow and scrapes rental property addresses, prices, and links into three lists.
3. A Chrome browser window opens automatically. For each scraped listing, Selenium navigates to the Google Form, fills in the address, price, and link fields, and clicks Submit.
4. After all entries are submitted, download the form responses as a CSV from Google Forms to get the collected data in spreadsheet format.
