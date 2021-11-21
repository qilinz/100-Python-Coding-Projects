import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

# create a player
turtle = Player()
# create a car
car_manager = CarManager()
# create a scoreboard
scoreboard = Scoreboard()

# screen listener
screen.listen()
screen.onkey(fun=turtle.up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # randomly generate cars
    if car_manager.cars[-1].xcor() < random.randint(270, 290):
        car_manager.add_car()
    # the speed of the car will depends on the level
    car_manager.move(scoreboard.level)

    # detect collision with cars
    for car in car_manager.cars:
        if turtle.distance(car.pos()) <= 20 and abs(turtle.ycor() - car.ycor()) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect the completion of current level
    if turtle.new_level():
        scoreboard.update()

screen.exitonclick()