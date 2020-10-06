import numpy
import math

while True:
    numbers = []
    quantity = int(input("How many numbers will you enter? (answer in digit format. Example: 9: "))
    for i in range(quantity):
        numbers_input = float(input("Enter one of your numbers.(Answer in digit format; example: 9: "))
        numbers.append(numbers_input)

    numbers.sort()
    

    print("The sortered numbers are", numbers)
    # Adding all numbers to compute average
    addition = sum(numbers)
    average = addition/quantity
    print("average =", average)

    # x-mean
    array = numpy.array([numbers])
    array_two = array - average
    print("Print x-mean", array_two)

    #(x-mean)^2
    array_squared = array_two**2
    print("(x-mean^2", array_squared)



    variance = array_squared.sum()/quantity
    print("The variance is", variance)

    standard_deviation = math.sqrt(variance)
    print("Standard deviation is:", standard_deviation)
