temp = int(input("What is the temperature?"))
wind = int(input("What is the windspeed?"))
if temp > 90 and wind < 5:
    print("It is Dry")
elif temp > 90 and wind > 5:
    print("It is hot")
elif temp < 90 and wind >5:
    print("It is breezy")
else:
    print("It is warm")
