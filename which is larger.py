n1 = int(input("Please enter an integer here:"))
n2 = int(input("Please enter a second integer here:"))
n3 = int(input("Please enter a third integer here:"))
if n1 > n2 and n1 > n3:
    print(n1, "is the largest integer")
elif n2 > n1 and n2 > n3:
    print(n2, "is the largest integer")
else:
    print(n3, "is the largest integer")
