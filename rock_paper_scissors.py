import random
n = 1
while 1 > 0:
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
    print(f"GAME NUMBER {n}")
    try:
        user_choice = int(input("\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
        if user_choice > 2 or user_choice < 0:
            print("\nYou typed an invalid number, you lose!")
        else:
            game = [rock, paper, scissors]
            print("\nYou choose: " + "\n" + game[user_choice])
            pc_choice = random.randint(0, 2)
            print("Computer chose: " + "\n" + game[pc_choice])
            row_1 = ('Draw', 'You are win', 'You are lose')
            row_2 = ('You are lose', 'Draw', 'You are win')
            row_3 = ('You are win', 'You are lose', 'Draw')
            options = (row_1, row_2, row_3)
            print(options[pc_choice][user_choice])
    except ValueError:
        print("\nYou typed an invalid number, you lose!")
    continue_game = input("\nDo you want to continue? Input yes or no. ")
    continue_game = continue_game.lower()
    if continue_game == 'yes':
        n += 1
        continue
    elif continue_game == 'no':
        print("\nGame is over.")
        break
    else:
        print("\nGame is over. You typed an invalid value.")
        break