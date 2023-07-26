# Import the random module to enable random selection from lists
import random

# List of different time frames
when = ["A few years ago", "Yesterday", "Last night", "A long time ago", "On 20th Jan"]

# List of different characters/animals
who = ["a rabbit", "an elephant", "a mouse", "a turtle", "a cat"]

# List of different names
name = ["Ali", "Miriam", "daniel", "Hoouk", "Starwalker"]

# List of different places of residence
residence = ["Barcelona", "India", "Germany", "Venice", "England"]

# List of different places where the characters went
went = ["cinema", "university", "seminar", "school", "laundry"]

# List of different events that happened
happened = [
    "made a lot of friends",
    "Eats a burger",
    "found a secret key",
    "solved a mistery",
    "wrote a book",
]

# Randomly select one item from each list and concatenate them into a sentence
print(
    random.choice(when)
    + ", "
    + random.choice(who)
    + " that lived in "
    + random.choice(residence)
    + ", went to the "
    + random.choice(went)
    + " and "
    + random.choice(happened)
)
