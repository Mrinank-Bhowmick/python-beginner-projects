# Importing the necessary modules
import tkinter
from time import strftime

# Creating the main application window
top = tkinter.Tk()
top.title("Clock")  # Setting the title of the window
top.resizable(0, 0)  # Making the window non-resizable


# Function to update the time display
def time():
    # Get the current time in the format HH:MM:SS AM/PM
    string = strftime("%H:%M:%S %p")

    # Update the text of the clockTime Label with the current time
    clockTime.config(text=string)

    # Schedule the time function to be called again after 1000 milliseconds (1 second)
    clockTime.after(1000, time)


# Creating a Label widget to display the time
clockTime = tkinter.Label(
    top,
    font=("courier new", 40),
    background="black",
    foreground="white",
)

# Position the Label widget in the center of the window
clockTime.pack(anchor="center")

# Call the time function to start updating the time display
time()

# Start the Tkinter main event loop
top.mainloop()
