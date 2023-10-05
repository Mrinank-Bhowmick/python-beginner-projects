import turtle
import winsound

win = turtle.Screen()
win.setup(height=600, width=800)
win.title("PINGPONG")
win.bgcolor("#9933FF")
win.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.speed(0)
paddle_a.color("#33ff33")
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.speed(0)
paddle_b.color("#33ff33")
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

# BALL
ball = turtle.Turtle()
ball.shape("circle")
ball.speed(0)
ball.color("#ffff33")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.12
ball.dy = -0.12

# PEN
pen = turtle.Turtle()
pen.speed(0)
pen.color("#000000")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.clear()
pen.write(f"Player A: {score_a} Player B: {score_b}",
          align="center", font=("Courier", 24, "normal"))


# Functions


def paddle_a_up():
    paddle_a.sety(paddle_a.ycor() + 20)


def paddle_a_down():
    paddle_a.sety(paddle_a.ycor() - 20)


def paddle_b_up():
    paddle_b.sety(paddle_b.ycor() + 20)


def paddle_b_down():
    paddle_b.sety(paddle_b.ycor() - 20)


# Keyboard binding
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")


while True:
    win.update()

    # moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}",
                  align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("error.wav", winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}",
                  align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("error.wav", winsound.SND_ASYNC)

    # Paddle and ball condition
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor()+40 and ball.ycor() > paddle_b.ycor()-40:
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor()-40:
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if paddle_b.ycor() > 250:
        paddle_b.sety(250)
    if paddle_b.ycor() < -250:
        paddle_b.sety(-250)
    if paddle_a.ycor() > 250:
        paddle_a.sety(250)
    if paddle_a.ycor() < -250:
        paddle_a.sety(-250)
