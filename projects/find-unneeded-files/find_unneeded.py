import os


def findUnneeded(folderPath, rejectSize):
    """walks through a folder tree and searches for exceptionally large files or folders
    Args:
        folderPath (str): path of folder to walk
        rejectSize (int): file size in bytes to possibly delete
    Returns:
        None
    """
    root = os.path.abspath(folderPath)

    for doc in os.listdir(root):

        docPath = os.path.join(root, doc)

        if os.path.isdir(docPath):
            size = getDirSize(docPath)
        else:
            size = os.path.getsize(docPath)

        if size > rejectSize:
            print(f"{docPath}: {size}")


def getDirSize(start_path):
    """Finds the total size of a folder and it's contents
    Args:
        start_path (str): path to folder
    Returns:
        size (int): folder size in bytes
    """
    size = 0

    for folderName, subFolder, filename in os.walk(start_path):
        for file in filename:
            filePath = os.path.join(folderName, file)
            size += os.path.getsize(filePath)

    return size


if __name__ == "__main__":
    findUnneeded("..", 1000)
