# Password Breach Frequency

The password breach frequency program uses the HaveIBeenPwned (HIBP) API to query whether a password hash has appeared in known data breaches. If the password has appeared in the data breaches, the program will return the number of times that that password has been seen accross all the known data breaches. 

This program is useful, as it can inform people on whether their passwords are secure. The program can provide users with valuable insights for their password choices, to ensure that they continue to maintain strong cybersecurity practices.

## Usage
From the Password Breach Frequency directory, enter the command:
> python main.py

This will launch the interactive program, which will request the password from the user.

## Example
```
Enter password: 12345678
Your password hash has appeared 5,172,909 times in known data breaches.
```