# IP Blacklist Checker

A CLI script that checks whether given IP addresses are blacklisted by querying the blacklistchecker.com API.

## Example

```text
$ python blacklist_checker.py 192.168.1.1 8.8.8.8
Blacklist check result is:
IP blacklists check returned next results:
8.8.8.8 is detected in ['SORBS-SPAM', 'UCEPROTECT-LEVEL1'] blacklists
```

When run without arguments, the script prompts interactively:
```text
Type in ip to check
1.2.3.4
IPs not blacklisted!
IP blacklists check returned next results:
```

## How to run on localhost

```
pip install requests
python blacklist_checker.py [ip ...]
```

Requires a free API key from blacklistchecker.com.

## Dependencies

requests.
