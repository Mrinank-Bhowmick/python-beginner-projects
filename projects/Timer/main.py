from time import sleep

duration = int(input("Enter the duration in seconds: "))
count = 0

while True:
    if count == duration:
        print("Your time is up!")
        break
    else:
        print(count, end="\r")
        sleep(1)
        count += 1
