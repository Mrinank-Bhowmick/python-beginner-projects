import argparse
import hashlib

# Outline the arguments that the user must input when they call the program
parser = argparse.ArgumentParser(description="hashing given password")
parser.add_argument("password", help="input password you want to hash")
parser.add_argument(
    "-t", "--type", default="sha256", choices=["sha256", "sha512", "md5", "sha1"]
)
args = parser.parse_args()

# Store the user-entered arguments into variables
password = args.password
hashtype = args.type

# Hash the password, using the hash function that the user provided
m = getattr(hashlib, hashtype)()
m.update(password.encode())
print("< hash-type : " + hashtype + " >")
print(m.hexdigest())
