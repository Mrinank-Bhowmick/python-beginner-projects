# pdf-paranoia

Bulk-encrypts and decrypts PDF files. It walks a directory tree, encrypts every unencrypted PDF with a user-supplied password (writing the result into an `untitled folder`), and can decrypt the `_encrypted` PDFs back again.

## Example

```text
Enter encryption password: mysecretpass
```

The script walks the current directory, encrypts every unencrypted `.pdf` it finds with `mysecretpass`, and writes the result to `untitled folder/` with `_encrypted` inserted before the extension (e.g. `report.pdf` becomes `untitled folder/report_encrypted.pdf`). It then decrypts any `_encrypted.pdf` files found using the same password, writing the plain copies alongside them.

## How to run on localhost

```
pip install PyPDF2
python pdfParanoia.py
```

## Dependencies

- PyPDF2
