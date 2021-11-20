import random
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# set start position of paddles
LEFT_POSITION = (-480, 0)
RIGHT_POSITION = (480, 0)
# set the keys to move the paddles
LEFT_PADDLE_UP = "w"
LEFT_PADDLE_DOWN = "s"
RIGHT_PADDLE_UP = "Up"
RIGHT_PADDLE_DOWN = "Down"

# set the screen
screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.mode("logo")

# set a line in the middle of the screen
middle_line = Turtle()
middle_line.color("white")
middle_line.pensize(3)
middle_line.hideturtle()

line_y = 280
while line_y >= -260:
    middle_line.penup()
    middle_line.goto(0, line_y)
    middle_line.pendown()
    line_y -= 10
    middle_line.goto(0, line_y)
    line_y -= 10
screen.update()

# create paddles and place them on the right positions
left_paddle = Paddle(LEFT_POSITION)
right_paddle = Paddle(RIGHT_POSITION)
screen.update()

# move the paddles
screen.listen()
screen.onkey(fun=left_paddle.up, key=LEFT_PADDLE_UP)
screen.onkey(fun=left_paddle.down, key=LEFT_PADDLE_DOWN)
screen.onkey(fun=right_paddle.up, key=RIGHT_PADDLE_UP)
screen.onkey(fun=right_paddle.down, key=RIGHT_PADDLE_DOWN)

# create a ball
ball = Ball()
ball.initiate(random.choice([1, -1]))


# create a scoreboard
scoreboard = Scoreboard()


# def collision with paddles
def hit_paddle(paddle):
    if abs(paddle.xcor() - ball.xcor()) <= 20:
        if paddle.ycor() - 50 <= ball.ycor() <= paddle.ycor() + 50:
            return True


game_is_on = True
while game_is_on:
    ball.move()
    screen.update()
    time.sleep(ball.move_speed)
    # detect the collision of the wall
    if abs(ball.ycor()) + 20 >= 300:
        ball.horizontal_bounce()
    # detect collision with paddles
    if 480 - abs(ball.xcor()) <= 30:
        if hit_paddle(left_paddle) or hit_paddle(right_paddle):
            ball.vertical_bounce()
        else:
            winner_x = -ball.xcor()
            scoreboard.add_score(winner_x)
            ball.initiate(winner_x)
            time.sleep(0.5)


screen.exitonclick()
