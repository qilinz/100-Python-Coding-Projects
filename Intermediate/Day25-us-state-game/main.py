import turtle
import pandas as pd

# Set up the screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# import data
data = pd.read_csv("50_states.csv")


def show_state_name(name):
    state_name = turtle.Turtle()
    state_name.hideturtle()
    state_name.penup()
    state = data[data['state'] == name]
    x = float(state.x)
    y = float(state.y)
    print(x, y)
    state_name.goto(x, y)
    state_name.write(f"{name}")


# generate a list of states
state_list = data.state.to_list()

while len(state_list) > 0:
    answer_state = screen.textinput(title=f"{50 - len(state_list)}/50 States Correct ",
                                    prompt="What's another state's name?\n(Type 'q' to quit)")
    answer_state = answer_state.title()
    if answer_state == "Q":
        break
    elif answer_state in state_list:
        show_state_name(answer_state)
        state_list.remove(answer_state)

# generate csv for states not guessed
missed_state = pd.DataFrame(state_list, columns=['state'])
missed_state.to_csv("missed_state.csv")