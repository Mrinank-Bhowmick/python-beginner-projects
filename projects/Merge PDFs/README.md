# Merge PDFs

A CLI tool that lists PDF files in a directory, lets you include/exclude files interactively, and merges the selected PDFs into a single file.

## Example

```text
Contents of directory:

0 :  chapter1.pdf
1 :  chapter2.pdf
2 :  notes.pdf

The final list of PDFs to be merged:

0 :  chapter1.pdf
1 :  chapter2.pdf
2 :  notes.pdf

Total: 3

CONTINUE? ['y'/'Y'] OR MODIFY THIS LIST? ['n'/'N']
> y

Enter the name of the final merged pdf (without the extension - 'pdf'):
> combined

The PDFs have been succesfully merged as/in:  /home/user/docs/combined.pdf  ✅
```

## How to run on localhost

```
pip install -r requirements.txt
python main.py [directory]
```

## Dependencies

pikepdf.
