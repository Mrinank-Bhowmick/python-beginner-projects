# Password Manager

A desktop password manager built with Tkinter. Users can store a website, email and password, generate random passwords, save the entries to a `data.json` file, and search for stored credentials.

## Example

1. The "Password Managger" window opens with fields for Website, Email, and Password, plus a logo image.
2. Type a website name (e.g. `github.com`) in the Website field and your email in the Email field.
3. Click "genetrate" to fill the Password field with a randomly generated password.
4. Click "ADD" — a confirmation dialog shows the entered password and email; click OK to save to `data.json`.
5. To retrieve saved credentials, type a website name and click "Search"; a dialog shows the stored email and password for that site.

## How to run on localhost

```
pip install scipy
python main.py
```

## Dependencies

- scipy (imported by `passgen.py`)
- Tkinter (bundled with Python)
