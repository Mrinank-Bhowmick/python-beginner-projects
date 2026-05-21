# Send Email

A script that connects to Gmail's SMTP server and sends a plain-text email. The sender's username and password are read from environment variables.

## How to run

```sh
export username=your@gmail.com
export password=yourpassword
python main.py
```

## Dependencies

Standard library only (uses `smtplib` and `os`).

## Pyodide-runnable

No - it opens an SMTP network connection to Gmail's mail server, which is blocked in the browser sandbox.
