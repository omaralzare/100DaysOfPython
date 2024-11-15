# https://appbrewery.github.io/python-day2-demo/

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? ")) / 100
numOfPeople = float(input("How many people to split the bill? "))
result = round((bill + (tip * bill)) / numOfPeople, 2)
print(f"Each person should pay: ${result}")
