import random
LIVES = 6

def ChooseWord():
  words = {"Apple":"Fruit", "Truck":"Vehicle", "Purple":"Color"}
  word = random.choice(list(words.keys()))
  return word.lower(), words[word]

def CreateWordGuessed(word):
  wordList = []
  for i in range(len(word)):
    wordList.append('-')
  return wordList

def GetLetterFromUser():
  letter = input("Pick Letter: ").lower()
  while len(letter) != 1:
    print("Invalid input, please try again...")
    letter = input("Pick Letter: ").lower()
  return letter

def FitLetterInWordGuessed(word, letter, wordGuessed):
  match = False
  for i in range(len(word)):
    if word[i] == letter:
      wordGuessed[i] = letter
      match = True
  return wordGuessed

def main():
  word, wordHint = ChooseWord()
  print(word)
  wordGuessed = CreateWordGuessed(word)
  counter = 0
  while True:
    print("".join(wordGuessed)+" (hint:"+wordHint+")")
    letter = GetLetterFromUser()
    wordGuessed, match = FitLetterInWordGuessed(word, letter, wordGuessed)
    if match == False:
      counter += 1
      if counter == LIVES:
        print("Game Over!")
        break

main()