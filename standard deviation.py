import numpy as np
import math

numbers = []
array = {}
quantity = int(input("How many numbers will you enter? (answer in digit format. Example: 9: "))
for i in range(quantity):
    numbers_input = int(input("Enter one of your numbers.(Answer in digit format; example: 9: "))
    numbers.append(numbers_input)
    array.insert(numbers_input)
addition = sum(numbers)
average = addition/quantity
array = np.array([numbers])
array_two = array - average
array_squared = array_two**2
variance = sum(array_squared)
standard_deviation = math.sqrt(variance)
print("Standard deviation is:", standard_deviation)
