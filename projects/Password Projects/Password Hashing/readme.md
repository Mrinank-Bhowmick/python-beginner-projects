# Password Hashing
The password hashing program will take a password string from the user and generate a corresponding hash for that password. Four hash functions are available to be used in this program:
* MD5
* SHA-1
* SHA-256
* SHA-512

## Executing the program
> python hashing_passwords.py INPUT [-t {sha1, sha256,sha512,md5}]

Where "INPUT" is the password that will be hashed. The
default hash-type is sha256, which will be automaticcaly applied if no hash function is specified.

## Usage example
1. The provided password is "Github" and the hash function is specified to be SHA-1
```
$ python hashing_passwords.py Github -t sha1
< hash-type : sha1 >
c53ced31f785a1888b348de05057011fedd3be48
```

2. The provided password is "Github" and no hash function has been specified. Therefore the default SHA-256 function is used.
```
$ python hashing_passwords.py Github
< hash-type : sha256 >
1720d8eaff790da6af4406905ba663d0cc6a6cea2b3e54e7384ac334a037f59d
```