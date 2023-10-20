import turtle as turt
import random

color_list=[(241, 246, 251), (234, 223, 83), (189, 10, 68), (113, 178, 211), (193, 78, 21), (214, 163, 101), (192, 163, 20), (226, 56, 131), (33, 104, 163), (14, 23, 63), (192, 38, 122), (208, 138, 177)]

pen = turt.Turtle()
turt.colormode(255)
pen.penup()
pen.hideturtle()

pen.setheading(225)
pen.forward(300)
pen.setheading(0)
no_of_dots = 100
pen.speed("fastest")

for dot_count in range(1,no_of_dots+1):
    pen.dot(20,random.choice(color_list))
    pen.forward(50)

    if dot_count%10==0:
        pen.setheading(90)
        pen.forward(50)
        pen.setheading(180)
        pen.forward(500)
        pen.setheading(0)

screen = turt.Screen()
screen.exitonclick()
