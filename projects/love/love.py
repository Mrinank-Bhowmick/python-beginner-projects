import turtle as t

t.bgcolor("black")
t.speed(0)
t.width(12)


def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)


def heart():
    t.color("red", "red")
    t.begin_fill()
    t.left(140)
    t.forward(113)
    curve()
    t.left(120)
    curve()
    t.forward(112)
    t.end_fill()


heart()
t.pencolor("red")
t.penup()
t.goto(0, 125)
t.pendown()

t.done()