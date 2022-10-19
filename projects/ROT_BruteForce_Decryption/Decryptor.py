#!/usr/bin/python3
class Rot:
    """" A brute forcing script on
    rot cipher
    """
    def __init__(self, Nstep = [int], cipher = [str]):
        self.Nstep = Nstep
        self.ciphertext = cipher

    def rotring(self):
        """
        loops through the cipher text and
        increment according to rot rules
        till it finds the flag string
        """
        for inc in range(self.Nstep):
            plaintext = ''
            for str in self.ciphertext:
                if str.isalpha():
                    if ord(str) >= 97:
                        val = (ord(str) - inc + 26) % 122
                        rot = val if val > 97 else val + 96
                        str = chr(rot)
                    else:
                        val = (ord(str) - inc + 26) % 90
                        rot = val if val > 65 else val + 64
                        str = chr(rot)
                plaintext += str
            if 'abcctf' in plaintext:
                print('Flag found!!!!!!!!!!\n')
                print(plaintext)
                break
            plaintext = ''

ciphertext = "Aol ullk av ohcl hmmpupaf pz doha thrlz aol mshn av il hijjam{hMMpupaf_OHz_bz}"

crack = Rot(30, ciphertext)
crack.rotring()
