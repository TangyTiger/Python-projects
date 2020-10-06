while True: 
    dimension1 = int(input("What is the length (in units) of the board game? "))
    dimension2 = int(input("What is the width (in units) of the board game? "))

    for i in range(dimension1):
        print("_ " * dimension2)
        
