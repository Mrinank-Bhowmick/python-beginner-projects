# === Password Generator · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @u749929.

import secrets
import string

# Ask user for desired password length
length = int(input("How many characters should the password have? "))
# Clamp length between 4 and 64
length = max(4, min(length, 64))

# Build the pool of allowed characters
alphabet = string.ascii_letters + string.digits + "!@#$%^&*-_"
# Pick random characters to form the password
password = "".join(secrets.choice(alphabet) for _ in range(length))

# Display the generated password
print()
print("Your new password:")
print(password)
print(f"({length} characters — keep it somewhere safe!)")
