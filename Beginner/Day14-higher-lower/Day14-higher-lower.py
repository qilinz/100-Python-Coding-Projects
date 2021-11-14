# Import packages, data and ASCII arts
import random
import os
from art import logo, vs
from gamedata import data


# Functions
def random_select():
    """
    Select a person from the list and then remove it
    :return: the person info dict
    """
    selected = random.choice(data_list)
    data_list.remove(selected)
    return selected


def present_info(person):
    """
    Present info of the "person"
    :param person: any dict from the list
    :return: a string describing the person
    """
    return f"{person['name']}, a {person['description']}, from {person['country']}."


def pose_question(person_A, person_B):
    """
    Pose the question
    :param person_A: the first person to compare
    :param person_B: the second person to compare
    """
    print(f"Compare A: {present_info(person_A)}")
    print(vs)
    print(f"Against B: {present_info(person_B)}")


def right_answer(person_A, person_B):
    """
    Compare the followers of two people and return the right answer
    :param person_A: the first person to compare
    :param person_B: the second person to compare
    :return: string "A" or "B" representing the first person or the second one
    """
    if person_A['follower_count'] > person_B['follower_count']:
        return 'A'
    else:
        return 'B'


# Greetings
print("Welcome to the Higher or Lower Game!")
print(logo)
# Basic settings
# Save the data as a copy
data_list = data
# Set the initial score
score = 0
end_of_game = False
# Select comparison_A randomly from the list
comparison_A = random_select()

while not end_of_game:
    # Select comparison_B randomly from the remaining list
    comparison_B = random_select()
    # pose the question
    pose_question(comparison_A, comparison_B)
    # Save the correct answer
    answer = right_answer(comparison_A, comparison_B)
    # Gather user's answer
    guess = input("Who has more followers? Type 'A' or 'B': ")
    # Let user retry if user's answer is invalid
    while guess != "A" and guess != "B":
        guess = input("Please give a valid answer. Who has more followers? Type 'A' or 'B': ")

    # Give the results
    os.system("clear")
    print(logo)
    # Wrong answer
    if guess != answer:
        print(f"Sorry, that's wrong. Final score: {score}")
        end_of_game = True
    # Right answer
    else:
        score += 1
        # if answer all the questions right
        if len(data_list) == 0:
            print(f"OMG! You guess all the answers right! Final score: {score}")
            end_of_game = True
        else:
            print(f"You're right!. Current score: {score}")
            comparison_A = comparison_B