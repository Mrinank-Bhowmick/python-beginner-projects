# Strong Password Detector

Checks whether a password is "strong" using regular expressions: it must be at least eight characters long and contain uppercase letters, lowercase letters and at least one digit.

## Example

```text
$ python strong-password.py
True
```

Running the script tests the hardcoded sample password `"A&dsas9$_"` against the strength rules (≥8 characters, uppercase, lowercase, digit) and prints `True` because it passes all four checks. Change the `password` variable in the script to test other passwords.

## How to run on localhost

```
python strong-password.py
```

## Dependencies

Standard library only (`re`).
