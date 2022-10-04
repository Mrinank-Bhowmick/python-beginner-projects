# create a timer

# from time module import sleep
from time import sleep

# get the duration from user
duration = int(input("Enter the duration in seconds: "))

# The current duration
count = 0

# This loop run until the test condition is false
while count < duration:
    # prints the current duration
    print(count, end="\r")
    # sleep for 1 second
    sleep(1)
    # update the current duration
    count += 1

# prints if the time is up
print("Your time is up!")
