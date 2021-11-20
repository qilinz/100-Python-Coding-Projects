from turtle import Turtle
import random


def random_position():
    x_random = 20 * random.randint(-11, 11)
    y_random = 20 * random.randint(-11, 11)
    # The food will be in the middle of the path of the snake in this way.
    return x_random, y_random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.goto(random_position())

    def move(self):
        self.goto(random_position())