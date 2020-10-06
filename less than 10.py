#List to hold user input
user_list = []
number_of_elements = int(input("How many numbers are you adding to this list: "))
number_of_elements += 1
x = 1

#While loop keeps adding user input to a list
while x < number_of_elements:
    add_number = int(input("Add number to the list: "))
    user_list.append(add_number)
    x+=1


#FOr loop goes through list and prints digits less than ten    
for i in user_list:
    if i<10:
        print(i)

#First, takes how many numbers that will be added by user to repeat the question of adding numbers to list
#While Loop will "Add number to the list:" as many times as stated above. Each input wil be added to a list
#For loop will go through every number in list and check if number is less than ten. If is, then it will print it. 
