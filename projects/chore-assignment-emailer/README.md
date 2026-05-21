# Chore Assignment Emailer

Randomly assigns a list of chores among a list of email addresses (distributing them round-robin) and emails each person their assigned chores via Gmail's SMTP server.

## How to run

```
python chore-emailer.py
```

You will be prompted for your Gmail address and password so the script can log in and send the emails.

## Dependencies

Standard library only (`random`, `smtplib`).

## Pyodide-runnable

No — it uses `smtplib` to make an outbound SMTP connection to Gmail, which is not possible in the browser sandbox.
