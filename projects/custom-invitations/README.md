# Custom Invitations

Generates a Word document (`invitations.docx`) containing a personalized party invitation page for each name listed in `guests.txt`.

## Example

Given a `guests.txt` containing:
```
Alice
Bob
Carol
```

Running the script produces `invitations.docx` with three pages. Each page reads:

> *It would be a pleasure to have the company of*
> **Alice**
> *at 11101 Memory lane on the evening of*
> April 31st
> *at 24 O'Clock*

A new page break separates each guest's invitation.

## How to run on localhost

```
pip install python-docx
python customInvitations.py
```

## Dependencies

- `python-docx`
