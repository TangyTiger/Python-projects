kg = int(input("What is your weight in kg?"))
meters = float(input("What is your height in meters?"))
bmi = (kg/(meters*meters))

a = round(bmi,2)

if(a < 18.5):
    print(a, ", is you bmi. You are underweight, eat more")
elif(bmi >= 18.5 and bmi <= 25):
    print(bmi, "is your bmi. You are normal. Good Job!")
elif(bmi > 25 and  bmi <= 30):
    print(a, "is your bmi. You are overweight, be more active")
else:
    print(a, "is your bmi. You are obese, eat less, and be more active")
    

