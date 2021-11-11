# Store the ASCII Art of rock, paper and scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# import packages
import random

# Record user choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
# Input validation check
if (user_choice > 2) or (user_choice < 0):
    print("Please enter a valid number.")
    quit()

# Generate computer choice randomly
computer_choice = random.randint(0, 2)

# Make a list of three options using the same order
choices = [rock, paper, scissors]

# Compare two choices and store the result
result = ""
# win condition
if (user_choice - computer_choice == 1) or (user_choice - computer_choice == -2):
    result = "Congrats! You win!"
# tie condition
elif user_choice == computer_choice:
    result = "Oops, you tie."
else:
    result = "Sorry, you lose."

# Give choices and the game result
# User choice
print("Your choice is\n" + choices[user_choice])
# Computer choice
print("Computer's choice is\n" + choices[computer_choice])
# Game result
print(result)
