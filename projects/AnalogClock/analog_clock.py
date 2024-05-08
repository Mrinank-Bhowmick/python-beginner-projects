import tkinter as tk
from math import sin, cos, pi


def update_clock():
    current_time = time_var.get()
    seconds = current_time % 60
    minutes = (current_time // 60) % 60
    hours = (current_time // 3600) % 12

    # Calculation of the angles for the clock hands (in degrees)
    seconds_angle = 90 - seconds * 6
    minutes_angle = 90 - minutes * 6 - seconds * 0.1
    hours_angle = 90 - (hours * 30 + minutes * 0.5)

    canvas.delete("all")  # Deletes all previous drawings

    canvas.create_oval(50, 50, 250, 250)  # To draw clock face

    for i in range(1, 13):  # Drawing clock numbers
        angle = 90 - i * 30  # Calculation of the angle for each number
        x = 150 + 85 * cos(angle * (pi / 180))
        y = 150 - 85 * sin(angle * (pi / 180))
        canvas.create_text(x, y, text=str(i), font=("Arial", 12, "bold"))

    draw_hand(150, 150, seconds_angle, 80, 1)
    draw_hand(150, 150, minutes_angle, 70, 2)
    draw_hand(150, 150, hours_angle, 50, 4)

    time_var.set(current_time + 1)  # Updating the time

    root.after(1000, update_clock)  # Updating the clock every 1000ms (1 second)


def draw_hand(x, y, angle, length, width):
    radian_angle = angle * (pi / 180)
    end_x = x + length * cos(radian_angle)
    end_y = y - length * sin(radian_angle)
    canvas.create_line(x, y, end_x, end_y, width=width)


root = tk.Tk()  # Creating the main window
root.title("Analog Clock")

canvas = tk.Canvas(root, width=350, height=350)
canvas.pack()

time_var = tk.IntVar()
time_var.set(10 * 3600)

update_clock()  # Starting the clock update function
root.mainloop()  # Running the Tkinter main loop
