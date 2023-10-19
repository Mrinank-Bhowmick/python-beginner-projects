import hashlib
import requests

# Request the user password in stdin
password = input("Enter password: ")

# Hash the password using SHA1. SHA1 is the required hash function for querying the HIBP API
m = getattr(hashlib, "sha1")()
m.update(password.encode())
hash_val = m.hexdigest()

# Connect to the HIBP API
url = "https://api.pwnedpasswords.com/range/" + hash_val[0:5]
r = requests.get(url)

# Split the string into a list, with each element of the list representing a single line
list = r.text.split("\n")
output = {}

# Convert each line in the list into a dictionary, with the hash as the key and the frequency as the value
for line in list:
    suffix, count = line.split(":")
    output[hash_val[0:5] + suffix.lower()] = int(count)

# If the hash value of the entered password is a key in the dictionary, print its frequency
if hash_val in output.keys():
    print(
        "Your password hash has appeared",
        "{:,}".format(output[hash_val]),
        "times in known data breaches.",
    )
else:
    print("your password hash has not appeared in a known data breach.")
