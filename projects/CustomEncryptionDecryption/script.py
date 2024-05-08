import string
import random
import jwt
import base64
import os
from dotenv import load_dotenv
load_dotenv()


class CustomEncrDecr:
    def __init__(self) -> None:
        self.__SECRET_KEY = str(os.getenv('SECRET_KEY'))
        self.__ENDE_KEY_LEN = int(os.getenv('ENDE_KEY_LEN'))
        self.__keyStore = privateKeyStore(self.__ENDE_KEY_LEN)
    
    def _encryptText(self, text) -> str:
        encryptedText = ''
        for char in text:
            val = self.__keyStore._getCipherEStore().get(char)
            encryptedText += char if val is None else val
        encryptedText = base64.b64encode(encryptedText.encode('utf-8')).decode('utf-8')
        return encryptedText
    
    def _decryptText(self, encryptedText) -> str:
        decryptedText = ''
        encryptedText = base64.b64decode(encryptedText.encode('utf-8')).decode('utf-8')
        for idx in range(0, len(encryptedText), self.__ENDE_KEY_LEN):
            st = encryptedText[idx: idx + self.__ENDE_KEY_LEN]
            val = self.__keyStore._getCipherDStore().get(st)
            decryptedText += st if val is None else val
        return decryptedText

    def _generateCipherText(self) -> str:
        self.__keyStore._generateCipherEStore()
        self.__keyStore._generateCipherDStore()
        dataString = jwt.encode(self.__keyStore._getCipherEStore(), self.__SECRET_KEY, algorithm='HS256')
        cipherText = base64.b64encode(dataString.encode('utf-8')).decode('utf-8')
        with open('cipher_text.txt', 'w') as file:
            file.write(str(cipherText).strip())
    
    def _verifyCipherText(self, cipherText='') -> None:
        dataString = base64.b64decode(cipherText.encode('utf-8')).decode('utf-8')
        cipherEstore = jwt.decode(dataString, self.__SECRET_KEY, algorithms=['HS256'])
        self.__keyStore._setCipherEStote(cipherEstore)
        self.__keyStore._generateCipherDStore()


class privateKeyStore:
    def __init__(self, CIPHER_KEY) -> None:
        self.__CIPHER_ESTORE = {}
        self.__CIPHER_DSTORE = {}
        self.__ENDE_KEY_LEN = CIPHER_KEY

    def _getCipherEStore(self) -> dict:
        return self.__CIPHER_ESTORE

    def _getCipherDStore(self) -> dict:
        return self.__CIPHER_DSTORE
    
    def _setCipherEStote(self, cipherEstore) -> None:
        self.__CIPHER_ESTORE = cipherEstore
    
    def _generateCipherDStore(self) -> dict:
        for k, v in self.__CIPHER_ESTORE.items():
            self.__CIPHER_DSTORE[v] = k

    def _generateCipherEStore(self) -> dict:
        for char in string.ascii_letters + string.digits + string.punctuation + string.whitespace:
            self.__CIPHER_ESTORE[char] = self.__generateSecureText()

    def __generateSecureText(self) -> str:
        return ''.join(random.choices(string.ascii_letters + string.digits + string.hexdigits + string.octdigits, k=self.__ENDE_KEY_LEN))


if __name__ == '__main__':
    print('\nWelcome to Custom Encryption & Decryption Program!')
    customEncrDecr = CustomEncrDecr()
    exitFlag = False
    while(not exitFlag):
        userOption = input('\n\nDo you already have a CIPHER TEXT ? \n\ta. Press \'c\' to continue with the default CIPHER TEXT \n\tb. Press \'y\' if you already have a CIPHER TEXT \n\tc. Press \'g\' to generate a CIPHER TEXT  \n\td. Press \'r\' to report a BUG \n\nYou have chosen: ')
        match userOption:
            case 'y':
                print('\nPlease add the CIPHER TEXT into the \'cipher_text.txt\' file! then start the program!\n')
                exit()
            case 'g':
                customEncrDecr._generateCipherText()
                print('\nYour CIPHER TEXT has been generated successfully! and added into the \'cipher_text.txt\' file!')
                exitFlag = True
            case 'c':
                try:
                    with open('cipher_text.txt', 'r') as file:
                        cipherText = str(file.read()).strip()
                        customEncrDecr._verifyCipherText(cipherText)
                        exitFlag = True
                except Exception as exc:
                    print("\n\n", exc)
                    exitFlag = False
                    print('\nCIPHER TEXT is INVALID! Make sure you have added a valid CIPHER TEXT inside the \'cipher_text.txt\' file!')
            case 'r':
                print('\nPlease send me a detail email at \'amitmanna0287@gmail.com\'. Keep the subject as \'BUG: Custom Encryption & Decryption Program\'. \n\nTo follow me use below social accounts: \n\ta. LinkedIn: https://www.linkedin.com/in/amitm0287/ \n\tb. GitHub: https://github.com/AmitM0287 \n\nThank you for time! Have a good day :)\n')
                exit()
            case _:
                print('\nPlease choose a valid option next time!')
    exitFlag = False
    while(not exitFlag):
        userOption = input('\n\nPlease choose one option from below: \n\ta. Press \'e\' to ENCRYPT a TEXT \n\tb. Press \'d\' to DECRYPT a ENCRYPTED TEXT \n\tc. Press \'q\' to QUIT the program ? \n\nYou have chosen: ')
        match userOption:
            case 'e':
                text = input('\nPlease enter your text : ')
                print('\nYour ENCRYPTED TEXT text is: ', customEncrDecr._encryptText(text), '\n')
            case 'd':
                try:
                    _encryptedText = input('\nPlease enter your ENCRYPTED TEXT : ')
                    print('\nYour DECRYPTED TEXT is: ', customEncrDecr._decryptText(_encryptedText))
                except Exception as exc:
                    print('\nENCRYPTED TEXT is INVALID! Make sure you are using the same CIPHER TEXT which you used at the time of ENCRYPTION!')
            case 'q':
                print('\nThanks for using custom encryption & decryption program! Have great day :)\n')
                exit()
            case _:
                print('\nPlease choose a valid option next time!')
        exitFlag = False if input('\nDo you want to continue to the program ? \n\ta. Press \'c\' to continue! \n\tb. Press \'any other key\' to quit the program!  \n\nYou have chosen: ') == 'c' else True
