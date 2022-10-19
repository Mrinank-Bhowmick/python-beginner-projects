import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)

screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()
    score.show_score()
    for car_i in car.cars:
        if player.distance(car_i) < 20:
            game_is_on = False
            score.game_over_msg()
    if player.ycor() > 280:
        player.reset_turtle()
        car.increment_speed()
        score.increase_score()


screen.exitonclick()


