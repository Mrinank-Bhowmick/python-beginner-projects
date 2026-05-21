# BitTorrent Downloader

Checks an email inbox for torrent links sent from a verified account, launches a torrent client to download them, and sends an SMS notification when each download finishes.

## How to run

```
pip install -r requirements.txt
python download_torrent.py
```

## Dependencies

- imapclient
- pyzmail
- twilio

## Pyodide-runnable

No - it connects to an IMAP email server, launches an external torrent client via subprocess, and sends SMS through the Twilio API.
