from higher_lower_art import logo, vs
from higher_lower_data import data
from random import choice
from random import shuffle

def data_(account):
    return account['name'], account['follower_count'], account['description'], account['country']

def check_answer (decision, a_followers, b_followers):
    if a_followers > b_followers:
        return decision == "a"
    else:
        return decision == "b"

account_a = choice(data)
account_b = choice(data)

print(logo)
score = 0
game_finished = False
while not game_finished:
    account_a = account_b
    account_b = choice(data)
    if account_a == account_b:
        account_b = choice(data)

    print(f"Compare A: {data_(account_a)[0]}, {data_(account_a)[2]}, from {data_(account_a)[3]}.")
    print(vs)
    print(f"Compare B: {data_(account_b)[0]}, {data_(account_b)[2]}, from {data_(account_b)[3]}.")
    decision = input("Who has more followers? Type 'A' or 'B': ").lower()
    is_correct = check_answer(decision, data_(account_a)[1], data_(account_b)[1])
###################################
    print(logo)
    if is_correct:
        score += 1
        print(f"You`re right! Currect score: {score}.\n")
    else:
        print(f"Sorry, that`s wrong! Final score: {score}\n")
        game_finished = True



