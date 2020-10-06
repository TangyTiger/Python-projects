def main():
    animal = input("What is your favorite animal? ").capitalize()
    nick_name = input("What is you nickname? (If no nickname, enter first three letters of name): ").lower()
    number = input("What is your favorite number? (Answer in digit form. Example-9): ").lower()
    sports_team = input("What is your favorite sport's team? ").capitalize()
    hobby = input("What is your hobby? ").lower()
    print("Your password is:    ",animal+nick_name+number+sports_team+hobby+"!=)")

main()
