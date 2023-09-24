# adixoo https://github.com/adixoo
import turtle as t
import os

# Initialize player scores
player_a_score = 0
player_b_score = 0

# Create a window
window = t.Screen()
window.title("The Pong Game")
window.bgcolor("green")
window.setup(width=800, height=600)
window.tracer(0)  # Turn off automatic screen updates

# Creating the left paddle
leftpaddle = t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=5, stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350, 0)

# Creating the right paddle
rightpaddle = t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5, stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350, 0)  # Corrected the initial position

# Code for creating the ball
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball_dx = 0.2  # Changed variable name to match usage
ball_dy = 0.2  # Changed variable name to match usage

# Code for creating a pen to display the score
pen = t.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(
    "Player A: 0                    Player B: 0",
    align="center",
    font=("Arial", 24, "normal"),
)


# Functions to move the left paddle
def leftpaddleup():
    y = leftpaddle.ycor()
    y += 20  # Adjusted the paddle movement
    leftpaddle.sety(y)


def leftpaddledown():
    y = leftpaddle.ycor()
    y -= 20  # Adjusted the paddle movement
    leftpaddle.sety(y)


# Functions to move the right paddle
def rightpaddleup():
    y = rightpaddle.ycor()
    y += 20  # Adjusted the paddle movement
    rightpaddle.sety(y)


def rightpaddledown():
    y = rightpaddle.ycor()
    y -= 20  # Adjusted the paddle movement
    rightpaddle.sety(y)


# Assign keys to play
window.listen()
window.onkeypress(leftpaddleup, "w")
window.onkeypress(leftpaddledown, "s")
window.onkeypress(rightpaddleup, "Up")
window.onkeypress(rightpaddledown, "Down")

# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)

    # Border setup for ball
    if ball.ycor() > 290:
        ball.sety(290)
        ball_dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball_dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball_dx *= -1
        player_a_score += 1
        pen.clear()
        pen.write(
            "Player A: {}                    Player B: {} ".format(
                player_a_score, player_b_score
            ),
            align="center",
            font=("Arial", 24, "normal"),
        )
        # os.system("afplay wallhit.wav&")

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball_dx *= -1
        player_b_score += 1
        pen.clear()
        pen.write(
            "Player A: {}                    Player B: {} ".format(
                player_a_score, player_b_score
            ),
            align="center",
            font=("Arial", 24, "normal"),
        )
        # os.system("afplay wallhit.wav&")

    # Handling collisions with paddles
    if (
        (ball.xcor() > 340)
        and (ball.xcor() < 350)
        and (
            ball.ycor() < rightpaddle.ycor() + 50
            and ball.ycor() > rightpaddle.ycor() - 50
        )
    ):
        ball.setx(340)
        ball_dx *= -1
        # os.system("afplay paddle.wav&")

    if (
        (ball.xcor() < -340)
        and (ball.xcor() > -350)
        and (
            ball.ycor() < leftpaddle.ycor() + 50
            and ball.ycor() > leftpaddle.ycor() - 50
        )
    ):
        ball.setx(-340)
        ball_dx *= -1
        # os.system("afplay paddle.wav&")
