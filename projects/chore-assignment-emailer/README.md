# Chore Assignment Emailer

Randomly assigns a list of chores among a list of email addresses (distributing them round-robin) and emails each person their assigned chores via Gmail's SMTP server.

## Example

```text
Enter your email: alice@gmail.com
Enter your email password: ••••••••••••
Sending email to example@yahoo.com...
Sending email to example2@yahoo.com...
```

Each recipient receives an email with subject `Your Chores.` listing their randomly assigned chores, e.g.:
`Hi There!, dishes, vacuum are your chores`

## How to run on localhost

```
python chore-emailer.py
```

You will be prompted for your Gmail address and password so the script can log in and send the emails.

## Dependencies

Standard library only (`random`, `smtplib`).
