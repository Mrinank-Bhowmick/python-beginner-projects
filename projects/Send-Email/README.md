# Send Email

A script that connects to Gmail's SMTP server and sends a plain-text email. The sender's username and password are read from environment variables.

## Example

```text
$ export username=sender@gmail.com
$ export password=yourpassword
$ python main.py
Successfully the mail is sent
```

The script reads `username` and `password` from environment variables, connects to Gmail's SMTP server, and sends the hardcoded plain-text message to `reciver789@gmail.com`.

## How to run on localhost

```sh
export username=your@gmail.com
export password=yourpassword
python main.py
```

## Dependencies

Standard library only (uses `smtplib` and `os`).
