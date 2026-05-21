# === Timer · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @cj-praveen.

# Import sleep to pause execution for one second
from time import sleep

# Ask the user how many seconds to count
duration = int(input("Enter the duration in seconds: "))

# Start count at zero
count = 0

# Loop, printing each second until duration is reached
while count < duration:
    print(count, end="\r")
    sleep(1)
    count += 1

# Notify the user that the timer has finished
print("Your time is up!")
