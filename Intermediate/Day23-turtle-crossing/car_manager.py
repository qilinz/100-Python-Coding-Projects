import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.add_car()

    def add_car(self):
        new_car = Turtle()
        new_car.color(random.choice(COLORS))
        new_car.shape("square")
        new_car.penup()
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.goto(320, random.randint(-250, 260))
        self.cars.append(new_car)

    def move(self, level):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE + (level-1) * MOVE_INCREMENT)

