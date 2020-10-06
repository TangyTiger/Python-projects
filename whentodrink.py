bday = int(input("What year were you born?"))
year = 2018
while bday > 2018:
    bday = int(input("Please enter a year before 2018:"))
    age = year-bday
if age > 21:
    print("You are allwed to drink")
else:
    drinkin = 21-age
    print("You can drink in", drinkin,"years.")
