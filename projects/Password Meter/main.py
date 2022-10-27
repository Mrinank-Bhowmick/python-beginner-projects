from meter_pass import *

# ENTER WITH PASSWORD
password = input("Type your password: \n")

# ALL VALIDATIONS PRINT TO VERIFY %
bonus = numberOfCharacters(password)
print(numberOfCharacters(password), "% Number of Characters")

bonus += upperCaseLetters(password)
print(upperCaseLetters(password), "% Uppercase Letters")

bonus += lowerCaseLetters(password)
print(lowerCaseLetters(password), "% Lowercase Letters")

bonus += numbers(password)
print(numbers(password), "% Numbers")

bonus += symbols(password)
print(symbols(password), "% Symbols")

bonus += middleNumberOrSymbol(password)
print(middleNumberOrSymbol(password), "% Middle Numbers or Symbols")

bonus += requirements(password)
print(requirements(password), "% Requirements")

# ALL DEDECTIONS
print("============Deductions=============")

bonus += lettersOnly(password)
print(lettersOnly(password), "% Letters Only")

bonus += numbersOnly(password)
print(numbersOnly(password), "% Numbers Only")

bonus += consecutiveUpperCase(password)
print(consecutiveUpperCase(password), "% Consecutive Uppercase Letters")

bonus += consecutiveLowerCase(password)
print(consecutiveLowerCase(password), "% Consecutive Lowercase Letters  ")

bonus += consecutiveNumbers(password)
print(consecutiveNumbers(password), "% Consecutive Numbers")

bonus += sequentialLetters(password)
print(sequentialLetters(password), "% Sequential Letters ")

bonus += sequentialNumbers(password)
print(sequentialNumbers(password), "% Sequential Numbers")
