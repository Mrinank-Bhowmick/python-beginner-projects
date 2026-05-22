# Dictionary.com Word of the Day Scraper

Scrapes the "Word of the Day" from dictionary.com, can fetch all its meanings, generate a text-to-speech pronunciation, and open the word's page in a browser.

## Example

```text
Word of the day is: ephemeral
Do you want to know the meanings of the word ? Press 1.. else Press 0
1
Fetching all meanings of the word: ephemeral
1. lasting for a very short time

Do you want to know how the word is pronounced ? Press 1.. else Press 0
1
Generating text-to-speech for ephemeral
Check current directory where script resides.

Do you want to know more about the word ? Press 1.. else Press 0
1
Opening url with word details..
```

## How to run on localhost

```
pip install beautifulsoup4 gtts
python wordOfTheDay.py
```

## Dependencies

- `beautifulsoup4` (`bs4`)
- `gtts`
