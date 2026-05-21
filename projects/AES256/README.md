# AES 256 Encryption and Decryption

A beginner-friendly console project demonstrating AES-256 encryption and
decryption in Python. It uses AES in GCM mode (authenticated encryption) with a
key derived from your password via `scrypt`.

Choose `1` to encrypt a message (prints the cipher text, salt, nonce and tag) or
`2` to decrypt by entering those values back.

## How to run

```bash
pip install pycryptodomex
python AES256.py
```

## Dependencies

- `pycryptodomex` — the `Cryptodome` AES implementation

## Pyodide-runnable

Yes. `pycryptodome` is available in the Pyodide playground, and the program is a
pure `input()`/`print()` console app. The screen-clearing `os.system` call was
removed so it runs cleanly in-browser.
