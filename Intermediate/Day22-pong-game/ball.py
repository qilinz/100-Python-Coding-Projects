from turtle import Turtle
import random

MOVE_DISTANCE = 20


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.hideturtle()
        self.move_speed = 0.1

    def initiate(self, winner_x):
        self.move_speed = 0.1
        angle = random.randint(40, 80)
        if winner_x < 0:
            angle += 180
        self.home()
        self.setheading(angle)
        self.settiltangle(-angle)
        self.showturtle()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def horizontal_bounce(self):
        angle = self.heading()
        if angle <= 180:
            bounce_angle = 180 - angle
        else:
            bounce_angle = 540 - angle
        self.setheading(bounce_angle)
        self.settiltangle(-bounce_angle)

    def vertical_bounce(self):
        angle = self.heading()
        bounce_angle = 360 - angle
        self.setheading(bounce_angle)
        self.settiltangle(-bounce_angle)
        # the move speed will increase
        self.move_speed *= 0.9
