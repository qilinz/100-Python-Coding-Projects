from turtle import Turtle
MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)

    def up(self):
        if self.ycor() <= 230:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() >= -230:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_y)
