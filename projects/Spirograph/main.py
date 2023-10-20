import turtle as turt
import random

pen = turt.Turtle()

turt.colormode(255)

pen.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        pen.color(random_color())
        pen.circle(100)
        pen.setheading(pen.heading() + size_of_gap)

draw_spirograph(5)

screen = turt.Screen()
screen.exitonclick()