import random

n = int(input("Enter number of points (larger gives closer estimate): "))

def estimate_pi(n):
    num_in_circle = 0
    total_num = 0
    for i in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        distance = x**2 + y**2
        if distance <= 1:
            num_in_circle +=1
        total_num +=1
    print((4*num_in_circle)/total_num)
        

estimate_pi(n)
