#!/usr/local/bin/python3
import os
import sys
from pikepdf import Pdf


def ls(contents):
    for index, pdf in enumerate(contents):
        print(index, ': ', pdf)


if __name__ == '__main__':

    merger = Pdf.new()

    if len(sys.argv[1:]) > 0:
        dir = sys.argv[1]
        contents = os.listdir(dir)
    else:
        dir = os.getcwd()
        contents = os.listdir()

    print("\n\nContents of directory:\n")
    ls(contents)

    sorted_contents = sorted(
        list(map(lambda x: os.path.join(dir, x), contents)), key=os.path.getctime)
    contents = [s.split(os.path.sep)[-1] for s in sorted_contents]
    pdfs = list(filter(lambda x: x.endswith('.pdf'), contents))

    confirmation = 'n'

    while confirmation not in ['y', 'Y']:
        print("\nThe final list of PDFs to be merged: \n")
        ls(pdfs)

        confirmation = input(
            f"\nTotal: {len(pdfs)}\n\nCONTINUE? ['y'/'Y'] OR ADD ANY MORE EXCEPTIONS TO THE LIST? ['n'/'N']\n> ")

        if confirmation in ['y', 'Y']:
            file_name = input(
                "\nEnter the name of the final merged pdf (without the extension - 'pdf'):\n> ")

            while '.pdf' in file_name:
                file_name = input(
                    "\nEnter the name of the final merged pdf (WITHOUT THE EXTENSION - '.pdf'):\n> ")

            file_name += '.pdf'

            while file_name in os.listdir():
                file_name = input(
                    "\nThe file name already exists in this folder! Please give a unique name!\n> ")

            for file in pdfs:
                try:
                    path = os.path.join(dir, file)
                    merger.pages.extend(Pdf.open(path).pages)
                except Exception as e:
                    print(
                        f"❗️ The following PDF: {file} seems to be corrupted... Skipping it... ❗️")

            if len(pdfs) > 0:
                merger.save(file_name)
            else:
                exit(f"\nNo PDFs to merge... Exiting...")

            print("\nThe PDFs have been succesfully merged as/in: ",
                  os.path.abspath(file_name), " ✅")

        else:
            pdf_exceptions = input(
                "\nEnter the PDF file names which should be excluded from the list separated by comma:\n> ").split(',')

            final_exceptions = []

            for exception in pdf_exceptions:
                if exception not in pdfs:
                    print(
                        f"\n❗️ {exception} does not exist in this directory! Skipping it...\n")
                else:
                    print(f"\n❌ Removing '{exception}' from merger...")
                    final_exceptions.append(exception)

            for exception in final_exceptions:
                pdfs = list(filter(lambda x: x != exception, pdfs))
