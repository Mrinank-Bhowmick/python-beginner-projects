# AES 256 Encryption and Decryption

A beginner-friendly console project demonstrating AES-256 encryption and
decryption in Python. It uses AES in GCM mode (authenticated encryption) with a
key derived from your password via `scrypt`.

Choose `1` to encrypt a message (prints the cipher text, salt, nonce and tag) or
`2` to decrypt by entering those values back.

## Example

```text
                AES 256 Encryption and Decryption Algorithm
                -------------------------------------------

Enter 1 to encrypt and 2 to decrypt: 1
Enter the Password: hunter2

Enter the Secret Message: meet me at noon

Encrypted:
---------------

cipher_text: 9pX2k7Qe1A==
salt: Hh0r2Hk9pQqVz8m1Yw3aBQ==
nonce: Lm4nKp7Rt2sVx8yZ
tag: Tz1qWe4rUi7oPa2sDf5gHj==
```

To recover the message, run the program again, choose `2`, and enter the four
values above along with the same password.

## How to run on localhost

```bash
pip install pycryptodomex
python AES256.py
```

## Dependencies

- `pycryptodomex` — the `Cryptodome` AES implementation
