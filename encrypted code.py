

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ","."]
print(alphabet[0])
user_input = "this is a test."
user_sentance = list(user_input)

print(user_sentance)

#user_sentance = user_input.split()
#print(user_sentance)
counter = 0

#def remove_space():
 #   return string.replace(" ", "")

#def remove_period():
#    user_sentance.replace(".", "")

counter_1 = 0

def counter_2():
    counter_2 = 0   


def counter_1():
    counter_1 = 0   

def main():
    for i in user_sentance:
        counter_1 = 0
        counter_2 = 0
        for x in alphabet:
            
            if user_sentance[counter_1] == alphabet[counter_2]:
                print(counter_2)
                counter_2 = 0
                main()  
            else:
                main()
                counter_2 += 1
        counter_1 += 1
        
        #if "." in user.sentance[counter]:
         #   user_sentance[counter].replace(".","")
          #  print(user_sentance)
           # main()
        #else:
        #    break


x = 0
#while x > 1:
main()

