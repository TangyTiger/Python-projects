"""guess_game_fun
Guess Game with a Function
In this project the guess game is recast using a function"""

import random

computers_number = random.randint(1,100)
PROMPT = 'What is your guess? '

def do_guess_round():
    """Choose a random number, ask the user for a guess
    check wether the guess is true
    and repeat until the user is correct"""
    computers_number = random.randint(1,100)  #Added
    while True:
        players_guess = raw_input(PROMPT)
        if computers_number == int(players_guess):
            print('Correct!')
            break
        elif computers_number > int(players_guess):
            print('Too Low')
        else:
            print('Too high')

while True:
    # Print statements added:
    print("Starting a new Round!")
    print("Let the guessing begin!!!")
    do_guess_round()
    print("") # blank line
