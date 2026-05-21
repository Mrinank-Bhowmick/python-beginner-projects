# === Countdown Timer · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @vk0812.

import time


# Count down from time_sec to zero, printing each second
def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = "{:02d}:{:02d}".format(mins, secs)
        print(timeformat, end="\r")
        time.sleep(1)
        time_sec -= 1

    print("Time Up")


if __name__ == "__main__":
    # Ask user for seconds and start countdown
    try:
        t = input("Enter the time in seconds: ")
        countdown(int(t))
    except:
        print("Invalid input please try again...")
