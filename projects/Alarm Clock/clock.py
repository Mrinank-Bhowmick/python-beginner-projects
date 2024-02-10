import tkinter
from time import strftime

# Creating the main application window
top = tkinter.Tk()
top.title("Dynamic Clock")  # Updated title
top.resizable(0, 0)  # Making the window non-resizable


# Function to determine the time of day
def get_time_of_day(hour):
    if 5 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 18:
        return "Afternoon"
    else:
        return "Evening"


# Function to update the time display
def update_time():
    current_time = strftime("%H:%M:%S %p")
    hour = int(strftime("%H"))
    time_of_day = get_time_of_day(hour)

    # Update the text of the clockTime Label with the current time and time of day
    clock_time.config(text=current_time + f"\nGood {time_of_day}!")

    # Dynamically change the background color based on time of day
    color = (
        "lightblue"
        if time_of_day == "Morning"
        else "lightyellow" if time_of_day == "Afternoon" else "lightcoral"
    )
    top.configure(background=color)

    # Schedule the update_time function to be called again after 1000 milliseconds (1 second)
    clock_time.after(1000, update_time)


# Creating a Label widget to display the time
clock_time = tkinter.Label(
    top,
    font=("courier new", 40),
    background="black",
    foreground="white",
)

# Position the Label widget in the center of the window
clock_time.pack(anchor="center")

# Call the update_time function to start updating the time display
update_time()

# Start the Tkinter main event loop
top.mainloop()
