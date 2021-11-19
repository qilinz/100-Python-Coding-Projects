from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race?\n(red, orange, yellow, green, blue, purple)\nEnter a color:"
)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

# set start point
x_start = -220
y_start = -150

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=x_start, y=y_start)
    turtles.append(new_turtle)
    y_start += 60

game_is_on = False
if user_bet:
    game_is_on = True

while game_is_on:
    for turtle in turtles:
        # check if turtle reach rhe goal
        # Why 230 instead of 250: the winner turtle will be out of screen completely
        if turtle.xcor() >= 230:
            winner = turtle.pencolor()
            game_is_on = False
            # check if the bet is correct
            if user_bet == winner:
                print("Congrats! You win! The {winner} turtle is the winner.")
            else:
                print(f"Oops, you lose. The {winner} turtle is the winner.")

        # move a random distance
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()