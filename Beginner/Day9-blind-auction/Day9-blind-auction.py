# Blind auction
# Import packages
# package for clearing the screen
import os
# package for ASCII art
from art import logo

# Greetings
print(logo)

# create a empty dict
bids = {}
end_of_bid = False

while not end_of_bid:
    name = input("What's your name? ")
    bid = int(input("What's your bid? $"))
    bids[name] = bid
    # ask if there's anyone else
    add_new_player = input('Anyone else wants to join? type "yes" to add new people, "no" to see the result\n')
    if add_new_player == "yes":
        # clear the screen to prevent new user from seeing the previous bids
        os.system('clear')
    else:
        end_of_bid = True

# find the person with highest bid
winner = ""
winner_bid = 0
for player in bids:
    bid = bids[player]
    if bid > winner_bid:
        winner = player
        winner_bid = bid

# give the result
print(f"The winner is {winner} with a bid of ${winner_bid}.")
