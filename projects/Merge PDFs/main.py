#!/usr/local/bin/python3
import os
import sys
from pikepdf import Pdf


# helper function to list PDF files in a directory
def ls(contents):
    for index, pdf in enumerate(contents):
        print(index, ": ", pdf)


# modify PDF list based on type (exclude/include)
def modify(pdfs, type):
    pdf_selections = input(
        "\nEnter the PDF filenames which should be excluded/included from the list separated by a SPACE:\n> "
    ).split()

    # store user's selections
    final_selections = []

    # check if files exist
    for selection in pdf_selections:
        if selection not in pdfs:
            print(
                f"\n❗️ {selection} does not exist in this directory! Skipping it...\n"
            )
        else:
            print(f"\n❌ Removing '{selection}' from merger...")
            final_selections.append(selection)

    # include/exclude PDFs
    for selection in final_selections:
        if type == "exclude":
            pdfs = list(filter(lambda x: x != selection, pdfs))
        else:
            pdfs = list(filter(lambda x: x == selection, pdfs))

    # return modified list
    return pdfs


if __name__ == "__main__":
    merger = Pdf.new()

    # take directory location from command line argument (if given) else choose current directory as default
    if len(sys.argv[1:]) > 0:
        dir = sys.argv[1]
        contents = os.listdir(dir)
    else:
        dir = os.getcwd()
        contents = os.listdir()

    print("\n\nContents of directory:\n")
    ls(contents)

    # sort PDFs by created time in a given directory
    sorted_contents = sorted(
        list(map(lambda x: os.path.join(dir, x), contents)), key=os.path.getctime
    )
    contents = [s.split(os.path.sep)[-1] for s in sorted_contents]
    pdfs = list(filter(lambda x: x.endswith(".pdf"), contents))

    # start the loop similar to 'do-while' format:
    confirmation = "n"
    while confirmation not in ["y", "Y"]:
        if not pdfs:
            exit("No PDFs to merge... Exiting...")

        print("\nThe final list of PDFs to be merged: \n")
        ls(pdfs)

        # option to modify the list of PDFs
        confirmation = input(
            f"\nTotal: {len(pdfs)}\n\nCONTINUE? ['y'/'Y'] OR MODIFY THIS LIST? ['n'/'N']\n> "
        )

        # start merging final list
        if confirmation in ["y", "Y"]:
            file_name = input(
                "\nEnter the name of the final merged pdf (without the extension - 'pdf'):\n> "
            )

            # prevent user from adding '.pdf' at the end
            while file_name.endswith(".pdf"):
                file_name = input(
                    "\nEnter the name of the final merged pdf (WITHOUT THE EXTENSION - '.pdf'):\n> "
                )

            # if file already exists, prompt user to re-enter file name
            file_name += ".pdf"
            while file_name in os.listdir():
                file_name = input(
                    "\nThe file name already exists in this folder! Please give a unique name!\n> "
                )

            # add PDFs to be merged
            for file in pdfs:
                try:
                    path = os.path.join(dir, file)
                    merger.pages.extend(Pdf.open(path).pages)
                except Exception as e:
                    print(
                        f"❗️ The following PDF: {file} seems to be corrupted... Skipping it... ❗️"
                    )

            # merge the PDFs and save the file in current directory.
            if len(pdfs) > 0:
                merger.save(file_name)
            else:
                exit(f"\nNo PDFs to merge... Exiting...")

            print(
                "\nThe PDFs have been succesfully merged as/in: ",
                os.path.abspath(file_name),
                " ✅",
            )

        # allows user wants to modify list before merging:
        else:
            # get user's numeric input - 1 or 2
            type = input(
                "\n1: Specify filenames to EXCLUDE\n2: Specify filenames to INCLUDE\n\nEnter the choice (number):\n> "
            )
            while type not in ("1", "2"):
                type = input(
                    "\n1: Specify filenames to EXCLUDE\n2: Specify filenames to INCLUDE\n\nEnter the choice (please enter '1' or '2'):\n> "
                )

            # exclude or include user's list
            type = "exclude" if type == "1" else "include"
            pdfs = modify(pdfs, type)
