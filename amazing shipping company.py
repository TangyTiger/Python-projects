price = {
    "sofa":739.35, 
    "computer":598.29,
    "TV" :999.98,
    "desk":668.42,
    "smart phone":702.19,
    "rug":448.36,
    "football": 24.32,
    "water bottle":13.62,
    }

price2 = {
    "    sofa    ":739.35, 
    "  computer  ":598.29,
    "     TV     " :999.98,
    "    desk    ":668.42,
    " smart phone":702.19,
    "     rug    ":448.36,
    "  football  ": 24.32,
    "water bottle":13.62,
    }

space = {
    "sofa":"    sofa    ", 
    "computer":"  computer  ",
    "TV" :"     TV     ",
    "desk":"    desk    ",
    "smart phone":" smart phone",
    "rug":"     rug    ",
    "football":"  football  ",
    "water bottle":"water bottle",
    }

tax = {
    "WA":1.10,
    "OR":0.00,
    "CA":1.12,
    "AZ":1.08,
    "NV":1.09,
    }

shipping = {
    "WA":00.00,
    "OR":25.00,
    "AZ":45.00,
    "NV":50.00,
    }


print(75*"-")
print(20*" ", "THE SHIPPING COMPANY | Item Purchase Menu")
print(75*"-")
print(5*" ", "Sl. No.", 17*" ", "ITEM", 16*" ", "UNIT PRICE ($)")
print(6*" ",1, 22*" ", "Sofa", 19*" ", 739.35)
print(6*" ",2, 20*" ","computer", 17*" ", 598.29)
print(6*" ",3, 23*" ", "TV", 20*" ", 999.98)
print(6*" ",4, 22*" ", "Desk", 19*" ", 668.42)
print(6*" ",5, 20*" ", "Smart Phone",14*" ", 702.19)
print(6*" ",6, 23*" ", "Rug",19*" ", 448.36)
print(6*" ",7, 20*" ", "Football", 17*" ", 24.32)
print(6*" ",8, 20*" ", "Water Bottle",13*" ", 13.62)
print(75*"-")

print("Hello Customer! You will now be entering how much of each item you want to purchase from our company. Please enter each quantity as an integer. If you don't want to purchase an item, please enter 0.")
quantity = {
    }
for key in price:
    question = "How many " + key + "s" + " do you want to buy?"
    quantity[key]=int(input(question))
print(80*"-")
print("WA:10% tax, 0$ shipping")
print("OR:0% tax, 25$ shipping")
print("CA:12% tax, 35$ shipping")
print("AZ:8% tax, 45$ shipping")
print("NV:9% tax, 50$ shipping")
state = input("What state do you want your items shipped to?")
print(75*"-")
print(29*" ", "The Shipping Company")
print(75*"-")
print("Website: www.theshippingcompany.com | Ph: 425-555-8932 | Location: Redmond, WA")
print(75*"-")
print(5*" ", "Sl. No", 12*" ", "ITEM", 12*" ", "QUANTITY", 12*" ", "UNIT PRICE", 12*" ", "PRICE")
slot_number = 1
subtotal = 0
for key in price:
    if quantity[key] != 0:
        cost = round((price[key]*quantity[key]),2)
        subtotal = round((cost + subtotal),2)
        if key == "football" or "water bottle":
            print(7*" ", slot_number, 12*" ", space[key], 12*" ", quantity[key], 14*" ", price[key], 16*" ", cost)
        else:  
            print(7*" ",slot_number, 12*" ", space[key], 12*" ", quantity[key], 14*" ", price[key], 16*" ", cost)
        slot_number = slot_number + 1
print(75*"-")
tax_total = round((tax[state]*subtotal),2)
if subtotal > 100 and subtotal < 500:
    discount = 0.96
elif subtotal > 500 and subtotal < 1000:
    discount = 0.90
elif subtotal > 1000:
    discount = 0.75
total = round((discount*subtotal),2)
print(60*" ", "subtotal: ", subtotal)
print(60*" ", "total w/ tax: ", tax_total)
print(60*" ", "total w/ tax and discount: ",total)


            
