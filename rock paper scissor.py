import random

while 1>0:
    UserChoice = input("Choose one: rock, paper, scissors: ").lower()
    ComputerChoices = ["rock", "paper", "scissors"]

    ComputerChoice = random.choice(ComputerChoices)
    print("My choice is", ComputerChoice)

    if ComputerChoice == "rock" and UserChoice == "paper":
        print("You win!")
    elif ComputerChoice == "rock" and UserChoice == "scissors":
        print("You lose!")
    elif ComputerChoice == "rock" and UserChoice == "rock":
        print("We tied!")
    elif ComputerChoice == "paper" and UserChoice == "rock":
        print("You lose!")
    elif ComputerChoice == "paper" and UserChoice == "scissors":
        print("You win!!")
    elif ComputerChoice == "paper" and UserChoice == "paper":
        print("We tied!")
    elif ComputerChoice == "scissors" and UserChoice == "rock":
        print("You win!")
    elif ComputerChoice == "scissors" and UserChoice == "paper":
        print("You lose!")
    elif ComputerChoice == "scissors" and UserChoice == "scissors":
        print("We tied!")
    else:
        print("Your input was invalid.")
