import random
letters = ["A", "B", "C", "D", "E", "F"]
length = 4

def main():
  list_code = create_code(4)
  secret_code = "".join(list_code)

  guess_counter = 0
  guess = ""
  list_guess = ""
  while guess_counter < 10 and guess != secret_code:
    list_guess = get_code()
    guess = "".join(list_guess)
    result = check_code(secret_code, guess)
    guess_counter+= 1
  

  if guess == secret_code:
    print("You win!")
  else:
    print("Sorry, you lost. The corect code was", secret_code)


def create_code(length):
  letters_copy = letters.copy()
  code_word = ""
  for i in range(length):
    letter = random.choice(letters_copy)
    letters_copy.remove(letter)
    code_word = code_word + letter
  code = list(code_word)
  return code

def get_code():
  guess_code = input("Guess the 4 digit code (abcd): ").upper()
  user_code = list(guess_code)
  if len(user_code) != length:
    print("Must enter 4 letters")
    get_code()
  for i in range(len(guess_code)):
    if user_code[i] in letters: 
      continue
    else:
      print("invalid answer, choose between letters a, b, c, d, e, f")
      get_code()
      break
  return guess_code


def check_code(secret_code, guess):
  white_counter = 0
  red_counter = 0
  win = False
  for i in range(len(guess)):
    if guess[i] == secret_code[i]:
      red_counter += 1
      continue
    elif guess[i] in secret_code:
      white_counter += 1
      continue
    else:
      continue
  print("R"*red_counter, "W"*white_counter)
  return white_counter, red_counter


main()
