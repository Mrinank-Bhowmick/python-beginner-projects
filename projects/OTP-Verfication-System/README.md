# OTP Verification System

Generates a random 6-digit OTP, emails it to a user via Gmail's SMTP server, and then verifies the code the user types back in.

## Example

```text
Enter your email: user@example.com
Enter Your OTP >>: 482951
Verified
```

If the wrong code is entered:

```text
Enter Your OTP >>: 000000
Please Check your OTP again
```

## How to run on localhost

```
python main.py
```

Edit `main.py` with valid Gmail credentials (an app password) before running.

## Dependencies

Standard library only (`os`, `math`, `random`, `smtplib`).
