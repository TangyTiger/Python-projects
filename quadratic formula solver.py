import math

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))


#vertex
print("X of Vertex is \n" + str(-(b)/(2*a)))

denominator = 2 * a
determinant = b**2 - 4*a*c
total_sqrt = math.sqrt(determinant)



# x intercepts
try: 
    x1 = (-(b)+ total_sqrt)/denominator
    print("x1: ")
    print(x1)

    try:
        x2 = (-(b)- total_sqrt)/denominator
        print("x2: ")
        print(x2)
    except:
        print("no - answer")


except:

    try: 
        print("no + answer")
        x2 = (-(b)- total_sqrt)/denominator
        print(x2)
    except:
        print("No soloutions")


