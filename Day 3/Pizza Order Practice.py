print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
pepperoni = input("Do you want pepperoni on your pizz? Y or N: ")
extraCheese = input("Do you want extra cheese? Y or N: ")
bill = 0
if size == "S" or size == "s":
    bill = 15
    if pepperoni == "Y" or pepperoni == "y":
        bill += 2
elif size == "M" or size == "m":
    bill = 20
    if pepperoni == "Y" or pepperoni == "y":
        bill += 3
elif size == "L" or size == "l":
    bill = 25
    if pepperoni == "Y" or pepperoni == "y":
        bill += 3
else:
    print("invalid input")
if extraCheese == "Y" or extraCheese == "y":
    bill += 1
print(f"Your final bill is ${bill}")
