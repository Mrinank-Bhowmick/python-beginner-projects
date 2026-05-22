# Encryptor and Decryptor

A Tkinter GUI application that encrypts and decrypts text using Base64 encoding, gated behind a secret key.

## Example

1. The Tkinter window opens (375x398) titled "Encrypt Decrypt".
2. Type `Hello World` into the "Enter text" area.
3. Enter `1234` in the "Enter secret key" field (the correct key).
4. Click **ENCRYPT** — a new red window opens titled "Encryption" showing the Base64-encoded result, e.g. `SGVsbG8gV29ybGQK`.
5. Paste that encoded string back into the main text area, enter `1234` again, and click **DECRYPT** — a green window opens showing `Hello World`.
6. Click **RESET** to clear both the text area and the key field.

## How to run on localhost

```
python encrypt.py
```

## Dependencies

Standard library only (`tkinter`, `base64`).
