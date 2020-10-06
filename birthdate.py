birth_year = (input("What year were you born? Enter the year in this format YYYY >>"))
if birth_year == "2006":
    print("Hello, Aditya!")
elif birth_year == "2010":
    print("Hello, Aayush")
elif birth_year == "1976":
    birth_month = input("Enter your birth month (e.g. January, March, December, etc.? ")
    birth_month = birth_month.lower()
    if birth_month == "october":
        print("Hello, Mummy")
    elif birth_month == "december":
        print("Hello, Papa")
    else:
        print("I don't know you")
else:
    print("I don't know you")
