symbol = input("Would you like to add, divide, multiply, or subtract? eg. multiply: ")

symbol = symbol.lower()

number1 = float(input("Pick the first number to "+ symbol + " with. Only use numbers: "))

number2 = float(input("Pick the second number to "+ symbol + " with. Only use numbers: "))

if symbol == "multiply":
    answer = number1*number2
    print("The answer is", answer)
    
elif symbol == "add":
    answer = number1+number2
    print("The answer is", answer)
    
elif symbol == "subtract":
    answer = number1-number2
    print("The answer is", answer)

elif symbol == "divide":
    answer = number1/number2
    print("The answer is", answer)

else:
    print("I can not work with these numbers or operation... sorry.")
