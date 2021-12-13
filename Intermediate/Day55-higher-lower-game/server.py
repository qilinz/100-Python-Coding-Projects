from flask import Flask
from random import randint
app = Flask(__name__)

ans = randint(0, 9)


@app.route('/')
def introduction():
    return f"<h1>Guess a number between 0 and 9" \
           f"<h3> Write your answer after the address of the website.</h3>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'></img>"


@app.route('/<int:guess>')
def check(guess):
    if guess == ans:
        return "<h1 style='color: green'>You found me! </h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'></img>"
    if guess < ans:
        return "<h1 style='color: red'>Too low, try again! </h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'></img>"
    else:
        return "<h1 style='color: purple'>Too high, try again! </h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'></img>"


if __name__ == "__main__":
    app.run(debug=True)