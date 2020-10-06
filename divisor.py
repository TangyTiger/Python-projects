def main():
    #user input

    user_number = float(input("Enter a number: "))

    #Divides by two so computer has less to caluclate
    num = user_number//2
    #print(num)

    #rounds number so doesn't stay in float format
    round(num,0)
    #print(type(num))

    #Converts number into integer again
    int_num = int(num)
    #print(type(int_num))
    #print(int_num)

    #Divisor is what computer uses to divide user input by
    divisor = 1

    #To create the perameters for loop
    int_num = int_num + 1

    
    for divisor in range(divisor,int_num):
        if user_number%divisor == 0:
            print(divisor)

while True:
    
    main() 
