import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create the snake body
snake = Snake()
# Create the food
food = Food()
# Create the scoreboard
scoreboard = Scoreboard()

# Control the snake
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

## Move the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    # parts except the head: move to the position of the part before it
    snake.move()

    # Detect the collision of food
    if snake.head.distance(food.pos()) <= 5:
        # snake + 1
        scoreboard.add_score()
        food.move()
        snake.grow()
        # food change position.

    # Detect the collision of wall
    if snake.head.xcor() <= -290 or snake.head.xcor() >= 290 or snake.head.ycor() <= -290 or snake.head.ycor() >= 290:
        game_is_on = False
        scoreboard.game_over()

    # Detect the collision of tail
    for part in snake.parts[1:]:
        if snake.head.distance(part) <= 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
