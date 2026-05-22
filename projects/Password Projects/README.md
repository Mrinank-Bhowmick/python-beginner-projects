# Password Projects

The Password Projects directory contains several mini-projects related to passwords and their security.

## Example

The sub-projects are independent console programs. For example, running the Password Generator:

```text
$ python "Password Generator/main.py"
_____________________________________
| Welcome to this Password Generator |
-------------------------------------

how long do you want your password to be (minimum of 8 number)12

Enter the length of password: 12

Your password is: aB3$kL!mQr9p
__________________________________________
| Thanks for using the Password Generator |
------------------------------------------
```

See each sub-project's own README for its specific usage and output.

The projects are:

1. [Password Breach Frequency](https://github.com/u749929/python-beginner-projects/tree/main/projects/Password%20Projects/Password%20Breach%20Frequency)
    * Uses the HaveIBeenPwned API to check the security of a user's password, by checking if the password has appeared in a known data breach, and how frequently the password has been seen in breaches.

2. [Password Generator](https://github.com/u749929/python-beginner-projects/tree/main/projects/Password%20Projects/Password%20Generator)
    * Generates a random password for the user, based on parameters. The user can select to exclude certain charcaters and choose the lenght of their password.

3. [Password Hashing](https://github.com/u749929/python-beginner-projects/tree/main/projects/Password%20Projects/Password%20Hashing)
    * Generates a cryptographic hash for an input password from the user. the user can specify from 4 of the most well known hash functions in order to generate the hash.

4. [Password Meter](https://github.com/u749929/python-beginner-projects/tree/main/projects/Password%20Projects/Password%20Meter)
    * Uses a defined set of rules in order to provide users with a score (meter) for their password security. This score is based on parameters such as the length of the password, the types of characters used and the order of characters.

5. [Password Manager](https://github.com/u749929/python-beginner-projects/tree/main/projects/Password%20Projects/Password_manager)
    * A password manager where users can store their emails and corresponding passwords for a variety of services.

6. [WiFi Password Generator](https://github.com/u749929/python-beginner-projects/tree/main/projects/Password%20Projects/WiFi%20Password%20Generator)
    * This program will attempt to get the password for the conected wifi network and retunr this password to the user. If no password is found, the program will return nothing.
