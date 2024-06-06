import re


def strip(text):
    """python's str.strip() method implemented using regex
    Args:
        text (str): text to strip of white space
    Returns:
        textStripped (str): text stripped of white space
    """
    stripStartRegex = re.compile(r"(^\s*)")
    stripEndRegex = re.compile(r"(\s*$)")

    textStartStripped = stripStartRegex.sub("", text)
    textStripped = stripEndRegex.sub("", textStartStripped)

    return textStripped


if __name__ == "__main__":
    text = " test ffs   "
    print(strip(text))
