from turtle import Turtle


ALIGNMENT = "center"
FONT = ('Courier', 56, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left = 0
        self.right = 0
        self.show_score()

    def show_score(self):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 230)
        self.write(arg=f"{self.left}     {self.right}", align='center', font=FONT)

    def add_score(self, winner_x):
        if winner_x > 0:
            self.right += 1
        else:
            self.left += 1
        self.clear()
        self.show_score()

