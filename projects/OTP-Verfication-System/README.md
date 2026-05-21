# OTP Verification System

Generates a random 6-digit OTP, emails it to a user via Gmail's SMTP server, and then verifies the code the user types back in.

## How to run

```
python main.py
```

Edit `main.py` with valid Gmail credentials (an app password) before running.

## Dependencies

Standard library only (`os`, `math`, `random`, `smtplib`).

## Pyodide-runnable

No — it connects to Gmail's SMTP server over the network to send email, which is not possible in a browser sandbox.
