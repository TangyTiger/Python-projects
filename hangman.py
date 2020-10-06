import random

words = ["monkey", "banana", "scale", "team", "rabid", "scary", "charge", "lamp", "man", "lip", "scribble", "acid", "experience"]
chosen_word = (random.choice(words))
print(chosen_word)
string_number =  len(chosen_word)
print("There are", string_number, "letters in this word")
number_guesses = int(input("How many times would you like to guess?"))
guessed_letter = input("Guess a letter?")
i = 1
for i in number_guesses:
    if guessed_letter in chosen_word:
        print("you guessed a letter")
    else:
        print("That letter is not in the random word")
    i = i+1

#print "you get 10 tries to geuss the word"
#random word from list. Ask to guess letter
