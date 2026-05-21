# === OTP Generator · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @iamdestinychild.

import random

# Define character pools for building OTPs
s_char = "abcdefghijklmnopqrstuvwxyz"
b_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
d_char = "123456789"


class Otp:
    # Store the desired OTP length
    def __init__(self, len):
        self.len = len

    # Generate a digits-only OTP
    @property
    def digits(self):
        num = 0
        result = []
        while num < self.len:
            rand_choice = "".join(random.choices(d_char, k=self.len)[0:1])
            result.append(rand_choice)
            num += 1
        value = "".join(result)
        return value

    # Generate an OTP mixing uppercase letters and digits
    @property
    def bd_digits(self):
        num = 0
        result = []
        while num < self.len:
            b_choice = "".join(random.choices(b_char, k=self.len)[0:1])
            d_choice = "".join(random.choices(d_char, k=self.len)[0:1])
            result.append(b_choice)
            result.append(d_choice)
            num += 1
        value = "".join(result[0 : self.len])
        return value

    # Generate an OTP mixing lowercase letters and digits
    @property
    def sd_digits(self):
        num = 0
        result = []
        while num < self.len:
            s_choice = "".join(random.choices(s_char, k=self.len)[0:1])
            d_choice = "".join(random.choices(d_char, k=self.len)[0:1])
            result.append(s_choice)
            result.append(d_choice)
            num += 1
        value = "".join(result[0 : self.len])
        return value

    # Generate an OTP using all three character types
    @property
    def sbd_digits(self):
        num = 0
        result = []
        while num < self.len:
            s_choice = "".join(random.choices(s_char, k=self.len)[0:1])
            b_choice = "".join(random.choices(b_char, k=self.len)[0:1])
            d_choice = "".join(random.choices(d_char, k=self.len)[0:1])
            result.append(s_choice)
            result.append(b_choice)
            result.append(d_choice)
            num += 1
        value = "".join(result[0 : self.len])
        return value


# Create a 10-digit OTP and print it
print("OTP:" + Otp(10).digits)
