from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
EASY_LEVEL = 6
#  Higher it is easier the game becomes since frequency of cars is 1/ EASY LEVEL ex. for 6, probability becomes 1/6 app.
#  so only 1/6 cars app. will appear for every 0.1 sec


class CarManager:

    def __init__(self):
        self.current_speed = STARTING_MOVE_DISTANCE

        self.cars = []

    def create_car(self):
        chance = random.randint(1, EASY_LEVEL)
        if chance == 1:
            car = Turtle("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.goto(300, random.randint(-240, 240))
            self.cars.append(car)

    def move_car(self):
        for car in self.cars:
            car.back(self.current_speed)

    def increment_speed(self):
        self.current_speed += MOVE_INCREMENT
