# EFFLUX Browser

A minimal desktop web browser built with PyQt5 and QtWebEngine, featuring back/forward/reload buttons and a URL bar.

## Example

1. Run `python main.py`. A maximised desktop window titled "EFFLUX browser" opens, loading `http://www.google.com`.
2. Type a URL (e.g. `https://www.python.org`) in the URL bar at the top and press Enter. The page loads and the URL bar updates to the new address.
3. Click the back button (`⮜`) to return to the previous page, or the forward button (`⮞`) to go forward again.
4. Click the reload button (`⟳`) to refresh the current page.

## How to run on localhost

```
pip install PyQt5 PyQtWebEngine
python main.py
```

## Dependencies

- PyQt5
- PyQtWebEngine
