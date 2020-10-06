def main():
    list_a = []
    list_b = []
    list_a_digits = int(input("There are two lists you must fill out. For the first list, enter how many numbers you are adding to the list: "))
    list_a_digits += 1
    w = 1
    y = 1

    #While loop keeps adding user input to a list
    while w < list_a_digits:
        add_number_a = int(input("Add number to the list: "))
        list_a.append(add_number_a)
        w+=1

    list_b_digits = int(input("This is now the second list. How many digits you are adding to this second list: "))

    while y < list_b_digits:
        add_number_b = int(input("Add number to the list: "))
        list_b.append(add_number_b)
        y+=1



    for i in list_a:
        for x in list_b:
            if i == x:
                print(x)

    #For every number in list a, compare with number in list b. check if it matches with a number in list_b.
                
while True:
    main()

