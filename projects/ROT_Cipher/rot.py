#!/usr/bin/python3
class Rot:
    """" A brute forcing script on
    rot cipher
    """
    def __init__(self, Nstep = [int]):
        self.Nstep = Nstep
        
    @staticmethod
    def encrypt(plaintext, key):
      
        """
        This function encrypts the plaintext given
        using a key
        """
         cipher_text = ''
         for str in self.ciphertext:
             if str.isalpha():
                 if ord(str) >= 97:
                    val = (ord(str) + inc + 26) % 122
                    rot = val if val > 97 else val + 96
                    str = chr(rot)
                else:
                    val = (ord(str) + inc + 26) % 90
                    rot = val if val > 65 else val + 64
                    str = chr(rot)
            cipher_text += str
        return cipher_text
      @staticmethod
     def decrypt(ciphertext, key):
        """
        This function uses the given 
        key to decrypt the cipher text
        """
        plain_text = ''
        for str in ciphertext:
            if str.isalpha():
                if ord(str) >= 97:
                    val = (ord(str) - inc + 26) % 122
                    rot = val if val > 97 else val + 96
                    str = chr(rot)
                else:
                    val = (ord(str) - inc + 26) % 90
                    rot = val if val > 65 else val + 64
                    str = chr(rot)
            plain_text += str
            
        return plain_text

crack = Rot(30)
print(crack.encrypt('rotcipher', 30))
