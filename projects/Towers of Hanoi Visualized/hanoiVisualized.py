import time
from tkinter import Tk, Canvas, Frame, BOTH, Widget
import math
import tkinter
import argparse
from typing import Text

# Window and drawing properties
WINDOW_WIDTH = 1920 // 2
WINDOW_HEIGHT = 1080 // 2

GROUND_HEIGHT = WINDOW_WIDTH // 20

PILLAR_WIDTH = WINDOW_WIDTH // 75
PILLAR_HEIGHT = WINDOW_HEIGHT / 2.25

MAX_DISKS = 10

DISK_HEIGHT = PILLAR_HEIGHT / MAX_DISKS / 1.5
DISK_WIDTH = PILLAR_WIDTH * 10

# All colors used for disk (max 10)
DISK_COLOR = ["#e6194B", "#3cb44b", "#ffe119", "#4363d8",
              "#f58231", "#911eb4", "#42d4f4", "#f032e6", "#bfef45", "#fabed4"]


# X coordinates of the pillars
pillarLocations = []

# Amount of disks used
diskCount = 4

# Disks for each pilar
state = {
    "A": [],
    "B": [],
    "C": []
}

# Drawing class


class Window(Frame):

    # Canvas used in this class
    canvas = None

    def __init__(self):
        # Initialize tkinter
        super().__init__()

        # Assign canvas
        self.canvas = Canvas(self)
        # Draw the pillars/ towers
        self.initTowers()

    # Draw the towers to the canvas
    def initTowers(self):
        # Get canvas
        canvas = self.canvas

        # Set title and show display
        self.master.title("Towers of Hanoi")
        self.pack(fill=BOTH, expand=1)

        # Create floor rect
        canvas.create_rectangle(
            0, WINDOW_HEIGHT - GROUND_HEIGHT, WINDOW_WIDTH, WINDOW_WIDTH, outline="#000", width=3, fill="#a9a9a9")

        # Setup pillar list
        pillars = []

        # Create the pillars
        for i in range(1, 4):

            # Calculate pillar x coordinates using window width
            x0 = (WINDOW_WIDTH / 4) * i - PILLAR_WIDTH
            x1 = x0 + (2 * PILLAR_WIDTH)

            # Append middle point x coordinate of pillars to list
            pillars.append(x0 + PILLAR_WIDTH)

            # Calculate pillar y coordinates using window height
            y0 = WINDOW_HEIGHT - GROUND_HEIGHT
            y1 = y0 - PILLAR_HEIGHT

            # Create the pillar, assign color
            canvas.create_rectangle(
                x0, y0, x1, y1, outline="#000", width=3, fill="#000")

        # Copy pillars to the pillarLocations list
        pillarLocations[:] = list(pillars)

        # Add this canvas
        canvas.pack(fill=BOTH, expand=1)

    # Function for drawing all of the disks
    def drawDisks(self, pillarStates):
        # Get canvas
        canvas = self.canvas

        # Remove all sprites from the canvas
        canvas.delete("all")

        # Initialize the towers again
        self.initTowers()

        # Calculate maxwidth of disks, distance between pillars is used to get max disk size
        maxDiskWidth = (pillarLocations[1] - pillarLocations[0]) - 10

        # Loop through disk list
        for i in pillarStates:

            # For getting correct x position and setting color of disks
            pillar = 0

            # 'A' is at index 0 of list, 'C' at index 2
            if i == "A":
                pillar = 0
            elif i == "B":
                pillar = 1
            else:
                pillar = 2

            # For correctly setting the y position of the disks
            height = 0

            diskCount = len(
                pillarStates['A']) + len(pillarStates['B']) + len(pillarStates['C'])
            # Loop through all disks on a pillar
            for j in pillarStates[i]:
                # Skip empty pillars
                if j != None:
                    # Calculate disk width dynamically using max size and amount of disks
                    diskWidth = maxDiskWidth - \
                        ((DISK_WIDTH / diskCount) * (diskCount - j))

                    # Calculate x coordinates using the correct pillar coordinates and the width of the disks
                    x0 = pillarLocations[pillar] - (diskWidth/2)
                    x1 = x0 + diskWidth

                    # Calculate y coordinates using the window height and ground height
                    y0 = WINDOW_HEIGHT - GROUND_HEIGHT - (height * DISK_HEIGHT)
                    y1 = y0 - DISK_HEIGHT

                    # Next disk has to be higher
                    height += 1

                    # Draw the disk
                    canvas.create_rectangle(
                        x0, y0, x1, y1, outline="#000", width=3, fill=DISK_COLOR[j-1])

                    # Draw a number corresponding to the disk inside of the disk (1 -> diskCount)
                    canvas.create_text(x0 + diskWidth / 2,
                                       (y0 - DISK_HEIGHT / 2) + 1, font=('Purisa', int(DISK_HEIGHT)-2), text=j, fill="#fff")


def main():
    # Add argument parser
    parser = argparse.ArgumentParser()
    # -a flag can be used when running to specifiy desired disk amount
    parser.add_argument('-a', type=int, required=False)
    args = parser.parse_args()

    # Check for limits of the argument 0 disks won't work, 10 is max
    if args.a != None and 0 < args.a <= MAX_DISKS:
        diskCount = args.a
    else:
        # Default disk count is 4
        diskCount = 4

    # Fill the state list with diskCount elements
    for i in range(diskCount, 0, -1):
        state['A'].append(i)

    # Set up Tkinter window
    root = Tk()

    # Init window class
    window = Window()

    # Set window size
    root.geometry("%sx%s" % (WINDOW_WIDTH, WINDOW_HEIGHT))
    # show the window
    root.update()

    # Draw the disks in their initial states
    window.drawDisks(state)

    # Update window
    root.update()

    # Start Hanoi func 500ms after mainloop
    root.after(500, hanoi(len(state["A"]), "A", "B", "C", root, window))
    root.mainloop()


# Function for chaning the state list and recalling the drawing class
def change_state(source, destination, root, window):
    # Remove upper disk
    removed = state[source].pop()
    # Transfer upper disk to different pillar
    state[destination].append(removed)

    # 500ms delay before redrwaing disks
    root.after(500, window.drawDisks(state), window)
    # Update the window
    root.update()


# Hanoi main function
def hanoi(n, source, auxiliary, destination, root, window):
    if n == 1:
        # Move disk from source to destination
        change_state(source, destination, root, window)
    else:
        # Recursive hanoi part
        hanoi(n-1, source, destination, auxiliary, root, window)
        change_state(source, destination, root, window)
        hanoi(n-1, auxiliary, source, destination, root, window)


# Call main function
if __name__ == "__main__":
    main()
