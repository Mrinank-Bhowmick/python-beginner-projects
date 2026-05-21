# pdf-paranoia

Bulk-encrypts and decrypts PDF files. It walks a directory tree, encrypts every unencrypted PDF with a user-supplied password (writing the result into an `untitled folder`), and can decrypt the `_encrypted` PDFs back again.

## How to run

```
pip install PyPDF2
python pdfParanoia.py
```

## Dependencies

- PyPDF2

## Pyodide-runnable

No — it walks the real filesystem with `os.walk` and reads/writes PDF files on disk, which is unavailable in the browser.
