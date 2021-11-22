import random
from blackjack_art import logo
import os

def deal_card():
    """
    cards - list of values, card - return random value from list cards
    :return: a random card from the deck
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """
    :return: sum of cards or result which tell us that somebody (user or pc) get 21 points
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    """
    :return: status game
    """
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, computer has Blackjack!"
    elif user_score == 0:
        return "Win with a Blackjack!"
    elif user_score > 21:
        return "Lose, you went over!"
    elif computer_score > 21:
        return "Win, computer went over!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    """

    :return: all logic game
    """
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for some in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Your cards: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hands {user_cards}, final score {user_score}")
    print(f"    Computer final hands {computer_cards}, final score {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system('clear')
    os.system('CLS')
    play_game()
