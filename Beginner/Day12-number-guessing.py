# Guess a number between 1 and 100
# Two levels to play: hard level - 5 attempts; easy level - 10 attempts

# Import packages
import random
import os

# Define constants
HARD_LEVEL = 5
EASY_LEVEL = 10


def number_guessing():
    # Generate a number for guessing
    right_answer = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")
    attempts_remaining = 0
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        attempts_remaining = EASY_LEVEL
    elif level == "hard":
        attempts_remaining = HARD_LEVEL

    while attempts_remaining > 0:
        print(f"You have {attempts_remaining} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == right_answer:
            print("Good Guess! You win!")
            break
        elif guess > right_answer:
            print("Too high.\nGuess again.")
            attempts_remaining -= 1
        else:
            print("Too low. \nGuess again.")
            attempts_remaining -= 1

    if attempts_remaining == 0:
        print("You run out of guesses. Sorry, you lose.")

    if input("Type 'y' to start a new game, or 'n' to quit. ") == 'y':
        os.system("clear")
        number_guessing()


# Greetings
print("Welcome to the Number Guessing Game!")
number_guessing()

