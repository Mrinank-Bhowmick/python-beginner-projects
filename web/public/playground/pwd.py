# Password Generator
# Builds a strong random password using the `secrets` module.

import secrets
import string

length = int(input("How many characters should the password have? "))
length = max(4, min(length, 64))

alphabet = string.ascii_letters + string.digits + "!@#$%^&*-_"
password = "".join(secrets.choice(alphabet) for _ in range(length))

print()
print("Your new password:")
print(password)
print(f"({length} characters — keep it somewhere safe!)")
