############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The Ace count as 11 or 1.
## THe Ace count as 11 until the hand is over 21.

## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
## Assign the dealer cards until the dealer has at least 17

####################### Rules End ##############################

# import packages
import random
from art import logo
import os

# Basic Settings
# Card pool
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


############################ Functions ############################
# 1. draw a card randomly to a card list.
def card_draw(card_list):
    new_card = random.choice(cards)
    card_list.append(new_card)
    return card_list


# 2. draw two cards to a card list.
def draw_two_cards(card_list):
    card_draw(card_list)
    card_draw(card_list)
    return card_list


# 3. check if the hand goes over.
def go_over_checker(card_list):
    if sum(card_list) <= 21:
        return False
    if 11 in card_list:
        ace_index = card_list.index(11)
        card_list[ace_index] = 1
        # deal with more than one Ace in card_list
        go_over_checker(card_list)
    else:
        return True


# 4. report current score
def report_current_score(player_list, dealer_list):
    # User's cards
    print(f"Your cards: {player_list}, current score: {sum(player_list)}")
    # Dealer's first card
    print(f"Dealer's first card: {dealer_list[0]}")


# 4. report current score
def report_final_score(player_list, dealer_list):
    # User's cards
    print("\n-------- FINAL RESULT --------")
    print(f"    Your final hand: {player_list}, final score: {sum(player_list)}")
    # Dealer's first card
    print(f"    Dealer's final hand: {dealer_list}, final score:{sum(dealer_list)}")


# 5. blackjack game.
def blackjack():
    # Draw two cards for both player and dealer
    player_cards = []
    dealer_cards = []
    draw_two_cards(player_cards)
    draw_two_cards(dealer_cards)

    # Player's turn: player can ask for another card as long as player does not go over.
    another_card = "y"
    while another_card == "y":
        # print current situations
        report_current_score(player_list=player_cards, dealer_list=dealer_cards)

        # If user wants another card
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if another_card == 'y':
            # draw player another card
            card_draw(player_cards)
            # check if player went over
            player_go_over = go_over_checker(player_cards)
            # print results if went over
            if player_go_over:
                report_final_score(player_list=player_cards, dealer_list=dealer_cards)
                return "You went over. You lose. "

    # Dealer's turn: assign dealer a card until dealer's hand > 17.
    #
    while sum(dealer_cards) < 17:
        card_draw(dealer_cards)
        dealer_go_over = go_over_checker(dealer_cards)
        if dealer_go_over:
            report_final_score(player_list=player_cards, dealer_list=dealer_cards)
            return "Dealer went over. You win! "

    # Report the results when both parts did not go over
    report_final_score(player_list=player_cards, dealer_list=dealer_cards)
    if sum(player_cards) > sum(dealer_cards):
        return "You win!"
    elif sum(player_cards) == sum(dealer_cards):
        return "Oops. It's a draw."
    else:
        return "You lose."


############################  Start the game  ############################
play = "y"
os.system('clear')
# To enable replay
while play == "y":
    play = input("\nDo you want to play a game of Blackjack? Type 'y' for yes, 'n' for no: ")
    if play == 'y':
        os.system('clear')
        print(logo)
        # run the game
        print(blackjack())
    else:
        print("See you next time! ;)")