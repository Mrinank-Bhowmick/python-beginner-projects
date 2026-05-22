# Currency Converter

A real-time currency converter with a Tkinter GUI. It fetches the latest exchange rates from an online API and lets the user convert an amount between any two currencies via dropdown menus.

## Example

1. The Tkinter window opens (500x200) titled "Currency Converter" and shows the current INR-to-USD rate and today's date.
2. Select the source currency (e.g. INR) from the left dropdown and the target currency (e.g. EUR) from the right dropdown.
3. Type an amount (e.g. `5000`) into the entry field on the left.
4. Click the "Convert" button — the converted amount (e.g. `55.23`) appears in the label on the right.

## How to run on localhost

```
pip install requests
python "currency converter.py"
```

## Dependencies

- `requests`
- `tkinter` (standard library)
