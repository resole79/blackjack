import random
from art import *

# Declare Variable
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# Function to give random cards
def deal_card(deck_of_cards):
    """
    Function to give random cards
    accept:
    deck_of_cards -> list
    return:
    random_card -> int
    """
    random_card = random.choice(deck_of_cards)

    return random_card


# Function to calculate score
def calculate_score(list_of_cards):
    """
    # Function to calculate score
    accept:
    list_of_cards -> list
    return:
    score -> int
    """
    score = sum(list_of_cards)
    # "if" condition to check blackjack
    if len(list_of_cards) == 2 and 11 in list_of_cards and 10 in list_of_cards:
        score = 0

    # "if" condition to check ace
    elif 11 in list_of_cards and sum(list_of_cards) > 21:
        index_card = list_of_cards.index(11)
        list_of_cards[index_card] = 1
        score = sum(list_of_cards)
    return score


# Function to compare scores and declare who win
def compare(user_score, computer_score):
    """
    Function to compare scores and declare who win
    accept:
    user_score, computer_score -> int
    """
    if user_score == 0:
        print("\nBlack Jack")
        print("You Win\n")
    elif user_score > 21:
        print("\nYou Bust!")
        print("Dealer Win\n")
    elif computer_score == 0:
        print("\nBlack Jack")
        print("Dealer Win\n")
    elif computer_score > 21:
        print("\nDealer Bust!")
        print("You Win\n")
    elif user_score > computer_score:
        print("\nYou Win\n")
    elif user_score < computer_score:
        print("\nDealer Win\n")
    elif user_score == computer_score:
        print("\nYou Draw")
        print("Push!\n")


# Function Game
def play_game():
    # Declare variable
    stand_over = False
    user_cards = []
    computer_cards = []
    dealer_score = -1
    player_score = -1

    print(logo)

    # deal the cards one each a time
    for card_number in range(4):
        if card_number % 2 == 0:
            user_cards.append(deal_card(cards))
        else:
            computer_cards.append(deal_card(cards))

    print(f"\n{star1} Card & Score {star2}")
    print(f"Dealer first card: {computer_cards[0]}")
    print(f"Player card: {user_cards[0]} {user_cards[1]} Score: {sum(user_cards)}")
    print(f"{star}")

    # Cycle while condition to exit player stand or game is over
    while not stand_over:
        player_score = calculate_score(user_cards)
        dealer_score = calculate_score(computer_cards)

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            stand_over = True
        else:
            hit_or_stand = input("\nTape 'Hit' if you want another card or tape 'Stand' if you want to pass: ").lower()
            if hit_or_stand == "hit":
                # append another cart to list and calculate a new score
                user_cards.append(deal_card(cards))
                player_score = calculate_score(user_cards)

                player_message = f"Player card: "
                for card in user_cards:
                    player_message += f" {card} "
                player_message += f"Score: {player_score}"
                print(player_message)

            elif hit_or_stand == "stand":
                stand_over = True
            else:
                print("Sorry you choice is uncorrected")

    while dealer_score < 17 and dealer_score != 0:
        computer_cards.append(deal_card(cards))
        dealer_score = calculate_score(computer_cards)

    compare(player_score, dealer_score)

    # Print out the final score message
    print(f"\n{star1} Final Score {star2}")

    dealer_message = f"Dealer card: "
    for card in computer_cards:
        dealer_message += f" {card} "
    if calculate_score(computer_cards) == 0:
        dealer_message += f"Score: Black Jack"
    else:
        dealer_message += f"Score: {dealer_score}"
    print(dealer_message)

    player_message = f"Player card: "
    for card in user_cards:
        player_message += f" {card} "
    if calculate_score(user_cards) == 0:
        player_message += f"Score: Black Jack"
    else:
        player_message += f"Score: {player_score}"
    print(player_message)

    print(star)


play_again = "y"
while play_again == "y":
    while True:
        play_again = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if play_again == 'y':
            play_game()
        elif play_again == 'n':
            print("\nGoodbye!")
            break
        else:
            print("Sorry you choice is uncorrected")
