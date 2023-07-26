name1 = input("Please type Name 1.\n")
name2 = input("Please type Name 2.\n")

total_vowel1 = 0
for i in ["a", "e", "i", "o", "u"]:
    total_vowel1 += name1.count(i)
total_vowel2 = 0
for i in ["a", "e", "i", "o", "u"]:
    total_vowel2 += name2.count(i)

love = 0
if total_vowel1 == total_vowel2:
    import random

    love += random.randint(10, 30)

consonants1 = 0
consonants2 = 0
CONSONANTS = "bcdfghjklmnprstvwxyz"
consonants1 = len([letter for letter in name1 if letter.lower() in CONSONANTS])
consonants2 = len([letter for letter in name2 if letter.lower() in CONSONANTS])

if consonants1 == consonants2:
    import random

    love += random.randint(20, 40)

line1 = name1
line2 = name2
split1 = line1.split()
split2 = line2.split()
fl1 = [word[0] for word in split1]
fl2 = [word[0] for word in split2]

if fl1 == fl2:
    import random

    love += random.randint(10, 30)

if len(name1) == len(name2):
    import random

    love += random.randint(1, 10)

import random

love += random.randint(10, 50)
if love > 100:
    love = 100

print("Calculating...")
import time
import random

time.sleep(random.randint(1, 3))

print("", name1, "and", name2, "have a", love, "% relationship.")
if (love > 90) or (love == 90):
    print("They have an unbreakable relationship that will last forever.")
if ((love < 89) or (love == 89)) and ((love > 70) or (love == 70)):
    print("They have a strong relationship that will most likely lead to a marriage.")
if ((love < 69) or (love == 69)) and ((love > 50) or (love == 50)):
    print("They have a good relationship that can lead to a honeymoon to Paris.")
if (love < 49) or (love == 49):
    print(
        "They have a weak relationship that could have been a 'match made in heaven'."
    )
