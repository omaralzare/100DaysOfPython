# https://appbrewery.github.io/python-day1-demo/

print("Welcome to the Band Name Generator.")
cityName = str(input("What's the name of the city you grew up in?\n"))
petName = str(input("What's your pet's name?\n"))
print("Your band name could be", cityName, petName)

# Exercise 1 : Printing Practice
# Write a program that uses print statements to print the following recipe into the Output console.
# The text to print is already there, you just need to make it into code.
# Your code should print all five lines exactly the same as the example output below.
# Make sure that you don't change any of these existing text as everything, punctuation and casing all need to match!
# 1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.
# 2. Knead the dough for 10 minutes.
# 3. Add 3g of Salt.
# 4. Leave to rise for 2 hours.
# 5. Bake at 200 degrees C for 30 minutes.
print(
    "1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.\n2. Knead the dough for 10 minutes.\n3. Add 3g of Salt.\n4. Leave to rise for 2 hours.\n5. Bake at 200 degrees C for 30 minutes."
)

# Exercise 3 : Variables
# We have 2 variables glass1 and glass2.
# glass1 contains milk and glass2 contains juice.
# Write 3 lines of code to switch the contents of the variables.
# You are not allowed to type the words "milk" or "juice".
# You are only allowed to use variables to solve this exercise.
glass1 = "milk"
glass2 = "juice"
tempGlass = glass1
glass1 = glass2
glass2 = tempGlass
# Extra line of code
print(glass1 + " " + glass2)
