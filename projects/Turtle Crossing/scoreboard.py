from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-215, 250)
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def increase_score(self):
        self.level += 1

    def game_over_msg(self):
        self.clear()
        self.setx(0)
        self.write(f" You reached Level: {self.level}", align="center", font=FONT)
        self.home()
        self.write(f"Game Over!", align="center", font=FONT)

