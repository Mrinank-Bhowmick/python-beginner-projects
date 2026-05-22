# BitTorrent Downloader

Checks an email inbox for torrent links sent from a verified account, launches a torrent client to download them, and sends an SMS notification when each download finishes.

## Example

```text
Enter your email: myemail@gmail.com
Enter your email password: ••••••••••••
```

The script connects to the Gmail IMAP server, searches the inbox for messages
from the verified sender, extracts any torrent links found, launches the
torrent client for each link, and sends an SMS notification via Twilio when
each download finishes.

## How to run on localhost

```
pip install -r requirements.txt
python download_torrent.py
```

## Dependencies

- imapclient
- pyzmail
- twilio
