print(
'''
Welcome To Costco
42653 NE 55th St
'''
)
bread = float(input("How many loaves of bread did you purchase?"))

candy = float(input("How many bags of candy did you purchase?"))

milk = float(input("How many cartons of milk did you purchase?"))

apple = float(input("How many apples did you purchase?"))
print(75*"-")
print(34*" ", "Costco")
print(75*"-")
print("Website: www.costco.com | Phone: 425-555-8932 | Location: Redmond, Washington")
print(75*"-")
print("sl. No.", 5*" ", "ITEM", 8*" ", "QTY", 6*" ", "UNIT PRICE", 8*" ", "PRICE")
print(75*"-")

brep = round((bread*4.50),2)
canp = round((candy*3.99),2)
milp = round((milk*5.25),2)
aplp = round((apple*1.80),2)
print(2* " ", "1", 8*" ", "Bread", 7*" ", bread, 8*" ", "4.50", 12*" ", brep)
print(2* " ", "2", 8*" ", "candy", 7*" ", candy, 8*" ", "3.99", 12*" ", canp)
print(2* " ", "3", 8*" ", "milk", 8*" ", milk, 8*" ", "5.25", 12*" ",milp)
print(2* " ", "4", 8*" ", "apples", 6*" ", apple, 8*" ", "1.80",12*" ",aplp)
print(75*"-")
sut = round((brep + canp + milp + aplp),2)
print(55*" ", "SUBTOTAL", sut)
tot = round(((brep + canp + milp + aplp)*1.1),2)
print(53*" ", "TOTAL W/ TAX: ", tot)
print(75*"-")
print("Hello Customer! Thank you for shopping at Costco! We accept payments in 5 and 10 dollar bills.")
fd = int(input("How many five dollar bills will be used to pay for your purchase?"))
td = int(input("How many ten dollar bills will be used to pay for your purchase?"))
print(75*"-")   
fid = fd*5
ted = td*10
money = fid + ted
if money > tot:
    change = round((money - tot),2)
    print("You get ", change, "dollars back")

while money < tot:
    debt = round((tot - money),2)
    print("You still have to pay", debt, "dollars more")
    fd = int(input("How many five dollar bills will be used to pay for your purchase?"))
    td = int(input("How many ten dollar bills will be used to pay for your purchase?"))
    fid = fd*5
    ted = td*10
    money = fid + teds
    tot=debt
    if money > debt:
        change = round((money - tot),2)
        print("You get ", change, "dollars back")
        break

print(75*"-")
print("Thank you for shopping at Costco, I hoped you enjoyed your visit. Have a good day, we hope to see you again!")


