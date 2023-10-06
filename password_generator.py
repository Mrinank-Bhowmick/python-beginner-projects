import secrets
import string

letter = string.ascii_letters
digits = string.digits
special_char = string.punctuation
pwd = letter + digits + special_char

password_len = 10
password = ""
for i in range(password_len):
    password += secrets.choice(pwd)
    
    if (any(char in special_char for char in password) and 
        sum(char in digits for char in password) >=2):
        break
    
print(password)