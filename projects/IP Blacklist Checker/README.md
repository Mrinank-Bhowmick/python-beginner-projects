# IP Blacklist Checker

A CLI script that checks whether given IP addresses are blacklisted by querying the blacklistchecker.com API.

## How to run

```
pip install requests
python blacklist_checker.py [ip ...]
```

Requires a free API key from blacklistchecker.com.

## Dependencies

requests.

## Pyodide-runnable
No — it makes live HTTP API requests to an external blacklist service.
