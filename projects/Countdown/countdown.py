import time


def countdown_timer(time_span__seconds): #"countdown is not specifc enough."
    '''
    Argument:
    time_span__seconds(int):Time duration in seconds.
    '''
    while time_span__seconds:
        mins, secs = divmod(time_span__seconds, 60) #mins = duration_seconds // 60, secs = duration_seconds % 60
        time_format = "{:02d}:{:02d}".format(mins, secs)
        print(time_format, end="\r")
        time.sleep(1)
        time_span__seconds -= 1

    print("Time Up")


if __name__ == "__main__":
    try:
        user_input = input("Enter the time in seconds: ") # t has no meaning.
        countdown_timer(int(user_input))
    except:
        print("Invalid input please enter a valid number...")
