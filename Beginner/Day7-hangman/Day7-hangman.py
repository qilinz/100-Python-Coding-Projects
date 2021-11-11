# Hangman Game
# import packages
import random

# import 'word_list' from hangman_words.py and choose a word randomly
import hangman_words
chosen_word = random.choice(hangman_words.word_list)
'''
This can also be writen as
from hangman_words import word_list
chosen_word = random.choice(word_list)
'''

# store the word length
word_length = len(chosen_word)

# basic settings
# when starting a new game, end of game is false
end_of_game = False
# total number of lives is 6
lives = 6

# Import the logo from hangman_art.py and print it at the start of the game.
import hangman_art
print(hangman_art.logo)
'''
OR write: 
from hangman_art import logo, stages
print(logo)
'''
# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}.")
    else:
        # Check if user is wrong.
        if guess not in chosen_word:
            # If the guess is wrong, tell users their guess is not in the word.
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            # if lives = 0, user loses.
            if lives == 0:
                end_of_game = True
                print("You lose.")
        else:
            # Check guessed letter
            for position in range(word_length):
                letter = chosen_word[position]
                if letter == guess:
                    display[position] = letter

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win!")

    # Import the stages from hangman_art.py and show users which stage they are at
    stages = hangman_art.stages
    print(stages[lives])
