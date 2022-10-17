# Convert an integer number to BINARY || OCTAL || HEXADECIMAL.

n = int(input('Firstly, pick any integer number: '))
print(f'The number you picked is {n}.')
print('-----------------------------------------')
print('''Now what do you want to convert it to?
[ 1 ] - BINARY
[ 2 ] - OCTAL
[ 3 ] - HEXADECIMAL''')
converter = int(input('OPTION --> '))
if converter == 1:
    print(f'The number {n} in BINARY is: {bin(n)[2:]}')
elif converter == 2:
    print(f'The number {n} in OCTAL is: {oct(n)[2:]}')
elif converter == 3:
    print(f'The number {n} in HEXADECIMAL is: {hex(n)[2:]}')
else:
    print('You have to choose an option between 1 to 3. Try again later.')