import re


def testPasswordStrength(password):
    """check for at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit
    Args:
        password (str): password as string
    Returns:
        strong (bool): True if password is strong else
    """

    eightCharsLongRegex = re.compile(r"[\w\d\s\W\D\S]{8,}")
    upperCaseRegex = re.compile(r"[A-Z]+")
    lowerCaseRegex = re.compile(r"[a-z]+")
    oneOrMoreDigitRegex = re.compile(r"\d+")

    if not eightCharsLongRegex.search(password):
        return False
    elif not upperCaseRegex.search(password):
        return False
    elif not lowerCaseRegex.search(password):
        return False
    elif not oneOrMoreDigitRegex.search(password):
        return False

    return True


if __name__ == "__main__":
    password = "A&dsas9$_"
    print(testPasswordStrength(password))
