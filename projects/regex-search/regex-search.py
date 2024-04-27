import os
import re


def regexSearch(regexStr, folderPath):
    """Searches all txt files in a folder for any line that matches a user-supplied regular expression
    Args:
        folderPath (str): path of folder to parse
    Returns:
        None
    """
    if not os.path.isdir(folderPath):
        return "Input a directory path"

    userRegex = re.compile(regex)

    for filename in os.listdir(folderPath):

        if filename.endswith(".txt"):

            with open(filename) as file:

                for line in file:
                    mo = userRegex.search(line)

                    if mo:
                        print(line, end="")


if __name__ == "__main__":

    regex = input("enter regex: ")
    regexSearch(regex, ".")
