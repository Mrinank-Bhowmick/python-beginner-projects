import string

# Constants
acentos = "óá"
exceptions = "_ "
sequenceNumbers = "0123456789"
sequenceAlphabet = string.ascii_lowercase
controller = False


# METHODS VERIFY IF PASS IS STRONG
def numberOfCharacters(password):
    bonus = len(password) * 4
    return bonus


def upperCaseLetters(password):
    charsUpper = 0
    if not password.isupper():
        for i in password:
            if i.isupper():
                charsUpper += 1

        if charsUpper != 0:
            charsUpper = (len(password) - charsUpper) * 2
    return charsUpper


def lowerCaseLetters(password):
    charsLower = 0
    if password.islower():
        for i in password:
            if i.islower() and i not in acentos:
                charsLower += 1

        if charsLower != 0:
            charsLower = (len(password) - charsLower) * 2
    return charsLower


def numbers(password):
    charsNumber = 0
    if not password.isdigit():
        for i in password:
            if i.isdigit():
                charsNumber += 1
    return charsNumber * 4


def symbols(password):
    charsSymbol = 0
    for i in password:
        if (
            i.lower() not in sequenceAlphabet
            and i not in exceptions
            and i not in sequenceNumbers
        ):
            charsSymbol += 1
    return charsSymbol * 6


def middleNumberOrSymbol(password):
    CharsMiddle = 0
    for i in range(1, len(password)):
        if (
            password[i].isdigit()
            or (
                password[i].lower() not in sequenceAlphabet
                and password[i] not in exceptions
            )
        ) and i != len(password) - 1:
            CharsMiddle += 1
    return CharsMiddle * 2


def requirements(password):
    requirementsCount = 0

    if len(password) >= 8:
        requirementsCount += 1

        if upperCaseLetters(password) > 0:
            requirementsCount += 1

        if lowerCaseLetters(password) > 0:
            requirementsCount += 1

        if numbers(password) > 0:
            requirementsCount += 1

        if symbols(password) > 0:
            requirementsCount += 1

        if requirementsCount == 4:
            requirementsCount = requirementsCount * 2
        else:
            requirementsCount = 0

    return requirementsCount


def lettersOnly(password):
    countDigit = 0

    for i in password:
        if i.isdigit():
            countDigit += 1

    if countDigit == 0:
        countDigit = len(password) * -1
    else:
        countDigit = 0

    return countDigit


def numbersOnly(password):
    countLetters = 0

    for i in password:
        if i.isalpha():
            countLetters += 1

    if countLetters == 0:
        return len(password) * -1
    else:
        countLetters = 0

    return countLetters


def consecutiveLowerCase(password):
    countLowerCase = 0
    password = password + "1"

    for i in range(len(password)):
        if (
            password[i].islower()
            and password[i + 1].islower()
            and password[i + 1] not in acentos
            and password[i] not in acentos
        ):
            countLowerCase += 1

    return (countLowerCase * 2) * -1


def consecutiveUpperCase(password):
    countUpperCase = 0
    password = password + "1"

    for i in range(len(password)):
        if password[i].isupper() and password[i + 1].isupper():
            countUpperCase += 1

    return (countUpperCase * 2) * -1


def consecutiveNumbers(password):
    countNumbers = 0
    password = password + "a"

    for i in range(len(password)):
        if password[i].isdigit() and password[i + 1].isdigit():
            countNumbers += 1

    return (countNumbers * 2) * -1


def sequentialNumbers(password):
    numbers = ""
    countNumbers = 0

    for i in range(len(password)):
        numbers += password[i : i + 3]

        if numbers in sequenceNumbers and len(numbers) == 3:
            countNumbers += 1

        numbers = ""

    return (countNumbers * 3) * -1


def sequentialLetters(password):
    letters = ""
    countLetters = 0

    for i in range(len(password)):
        letters += password[i : i + 3]

        if letters in sequenceAlphabet and len(letters) == 3:
            countLetters += 1

        letters = ""

    return (countLetters * 3) * -1
