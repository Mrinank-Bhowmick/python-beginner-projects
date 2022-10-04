from turtle import *  # importing libraries
import turtle as t
import random
import time

tim = t.Turtle()

t.colormode(255)


def random_colour():  # random colour generator
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b  # red,blue,green


def turtle_movement():
    tim.pensize(10)  # sets the size
    rgb = random_colour()
    direction = random.randint(1, 4)
    tim.pencolor(rgb[0], rgb[1], rgb[2])
    # defining the movement
    if direction == 1:
        tim.left(90)
        tim.forward(30)
        time.sleep(0.5)
    elif direction == 2:
        tim.right(90)
        tim.forward(30)
        time.sleep(0.5)
    elif direction == 3:
        tim.forward(30)
        time.sleep(0.5)
    elif direction == 4:
        tim.backward(30)
        time.sleep(0.5)


colours = [
    "GreenYellow",
    "Chartreuse",
    "Tan",
    "LightSkyBlue",
    "DeepPink",
    "MediumSlateBlue",
]

t.pensize(10)
for _ in range(0, 200):
    turtle_movement()

screen = Screen()
screen.exitonclick()
