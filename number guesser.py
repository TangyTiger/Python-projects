import random

number = random.randint(1,100)
print("Welcome to Number Guesser!")
print("You get 30 tries to guess my number between 1 and 100")
print(" ")
i = 0
while i < 15:
    guess = int(input("Guess a number?"))
    if guess<number: 
        print("The number guessed is too low")
    elif guess>number:
        print("The number guessed is too high")
    else:
        print("The number guessed is correct!!!")
        break
    i = i+1

                
