
from random import randint

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

choices = [rock, paper, scissors]

# print winner user, winner computer, or draw
def who_wins(computer, user):
    computer_response = computer
    user_response = user

    # return array of computer and user picks
    def picks():
        user_computer = [computer_response, user_response]
        return user_computer

    # results
    if user_response == scissors and computer_response == paper:
        user_wins(picks()[1], picks()[0])
    elif user_response == paper and computer_response == rock:
        user_wins(picks()[1], picks()[0])
    elif user_response == rock and computer_response == scissors:
        user_wins(picks()[1], picks()[0])
    elif user_response == computer_response:
        draw(picks()[1], picks()[0])
    else:
        computer_wins(picks()[1], picks()[0])

# amount of stars per outcome
def stars(num):
    i = 4
    star = '*'
    while i <= len(num):
        star += '*'
        i += 1
    return star

# display user and computer picks
def picks(user_pick, computer_pick):
    print ('User: ', user_pick, '\nComputer:', computer_pick)

# display user wins
def user_wins(user_pick, computer_pick):
    user_wins = '\n* user wins! *\n'
    print (stars(user_wins) + user_wins + stars(user_wins))
    picks(user_pick, computer_pick)

# display draw
def draw(user_pick, computer_pick):
    draw = '\n* draw *\n'
    print (stars(draw) + draw + stars(draw))
    picks(user_pick, computer_pick)

# display computer wins
def computer_wins(user_pick, computer_pick):
    computer_wins = '\n* copmuter wins *\n'
    print (stars(computer_wins) + computer_wins + stars(computer_wins))
    picks(user_pick, computer_pick)

# random choice 1 - 3 for computer
def rand_choice():
    computer_choice = randint(1, 3)
    return computer_choice

# user choice
def choice():
    user_choice = 0

    while user_choice != 1 and user_choice != 2 and user_choice != 3:
        user_choice = input('Please choose a number:\n1. Rock\n2. Paper\n3. Scissors\nNumber: ')
        try:
            user_choice = int(user_choice)
        except:
            print('\n-----\nInvalid Choice, try again\n-----\n')
            continue
    return user_choice

# return rock, paper, or scissors string
def menu_selection(choice):
    pick = choices[choice-1]
    return pick

# computer
computer = menu_selection(rand_choice())

# user
user = menu_selection(choice())

# compare user to computer
who_wins(computer,user)
