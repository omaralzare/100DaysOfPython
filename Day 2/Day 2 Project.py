# https://appbrewery.github.io/python-day2-demo/

print("Welcome to the tip calculator!")
bill = int(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
realTip = tip / 100
numOfPeople = int(input("How many people to split the bill? "))
print(f"Each person should pay: ${(bill + (realTip * bill)) / numOfPeople}")
