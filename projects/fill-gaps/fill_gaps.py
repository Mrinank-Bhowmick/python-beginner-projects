import os
import re
import shutil


def getFilesWithPrefix(folderPath, prefix):
    """get all files with a certain prefix
    Args:
        folderPath (str): path to folder to search
    Returns:

    """
    fileRegex = re.compile(prefix + "(\d{1,})(.\w+)")
    fileList = sorted(
        [file for file in os.listdir(folderPath) if fileRegex.match(file)]
    )
    return fileList


def fillGaps(folderPath, prefix):
    """fill gaps in numbering of files in folder
    Args:
        folderPath (str): path to folder to search
        prefix (str): prefix of files to fill gap
    Returns:
        None
    """
    fileList = getFilesWithPrefix(folderPath, prefix)  # files sorted ascending order
    fileRegex = re.compile(prefix + "(\d{1,})(.\w+)")

    start = int(
        fileRegex.search(fileList[0]).group(1)
    )  # start with the minimum number in list
    count = start  # count to be incremented during checks for gaps
    max_length = len(
        fileRegex.search(fileList[-1]).group(1)
    )  # max length of largest number, for padding zeros

    for file in fileList:

        mo = fileRegex.search(file)
        fileNum = int(mo.group(1))

        if fileNum != count:
            newFileName = (
                prefix
                + "0" * (max_length - len(str(fileNum)))
                + str(count)
                + mo.group(2)
            )
            shutil.move(os.path.abspath(file), os.path.abspath(newFileName))

        count += 1


def insertGaps(folderPath, prefix, index):
    """insert gaps in numbering of files in folder
    Args:
        folderPath (str): path to folder to search
        prefix (str): prefix of files to insert gap
        index (int): where to insert the gap
    Returns:
        None
    """

    fileList = getFilesWithPrefix(folderPath, prefix)  # files sorted ascending order
    fileRegex = re.compile(prefix + "(\d{1,})(.\w+)")

    max_length = len(
        fileRegex.search(fileList[-1]).group(1)
    )  # max length of largest number, for padding zeros

    firstIndex = int(fileRegex.search(fileList[0]).group(1))  # smallest number
    lastIndex = int(fileRegex.search(fileList[-1]).group(1))  # largest number

    if index >= firstIndex and index <= lastIndex:  # if gap index falls in range

        i = 0
        currIndex = firstIndex
        while currIndex < index:
            # loop till the file number is >= gap index
            i += 1
            currIndex = int(fileRegex.search(fileList[i]).group(1))

        if currIndex == index:  # if gap index is taken, make a gap else already free

            for file in fileList[i:][::-1]:
                # loop through reversed file list, to prevent overwriting results and increment file number

                mo = fileRegex.search(file)
                newFileNum = int(mo.group(1)) + 1
                newFileName = (
                    prefix
                    + "0" * (max_length - len(str(newFileNum)))
                    + str(newFileNum)
                    + mo.group(2)
                )
                shutil.move(os.path.abspath(file), os.path.abspath(newFileName))


if __name__ == "__main__":

    with open("spam001.txt", "w") as s1, open("spam003.txt", "w") as s3:
        s1.write("spam001")
        s3.write("spam003")

    fillGaps(".", "spam")
    # insertGaps('.', 'spam', 2)
