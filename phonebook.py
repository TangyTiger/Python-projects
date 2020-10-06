def main():
    phonebook = {}
    while True:
        user_selection = int(input("Select your choice: \n1-add\n2-remove\n3-search\n4-exit\n"))
        while user_selection < 1 or user_selection > 4:
            print("Choose correct value")
            user_selection = int(input("Select your choice: \n1-add\n2-remove\n3-search\n4-exit\n"))
        if user_selection == 1:
            add(phonebook)
        elif user_selection == 2:
            remove(phonebook)
        elif user_selection == 3:
            search(phonebook)
        else:
            return False

def input_number(message):
    while True:
        try:
            user_selection = int(input(message))
        except ValueError:
            continue
        else:
            return user_selection

def add(phonebook):
    name = input("Name: ").lower()
    number= input("phone number: ")
    phonebook[name] = number
    print(phonebook)
    

def remove(phonebook):
    name = input("Who would you like to remove: ").lower()
    if name in phonebook:
        phonebook.pop(name)
    else:
        print("this name is not in your phonebook")

def search(phonebook):
    user_input = input("Who would you like to search for: ").lower()
    if user_input in phonebook:
        print(phonebook[user_input])
    else:
        print("this person is not in your phone book")


main()

