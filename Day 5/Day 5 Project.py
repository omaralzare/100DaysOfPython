import random

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
letters = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
symbols = ["!", "@", "#", "$", "%", "&", "*", "(", ")"]
print("Welcome to the PyPassword Generator!")
lettersInput = int(input("How many letters would you like in your password?\n"))
symbolsInput = int(input("How many symbols would you like\n"))
numbersInput = int(input("How many numbers would you like\n"))
password = []
result = ""
for i in range(lettersInput):
    password.append(random.choice(letters))
for i in range(symbolsInput):
    password.append(random.choice(symbols))
for i in range(numbersInput):
    password.append(random.choice(numbers))
print(password)
random.shuffle(password)
print(password)
print(f"Your password is: {result.join(password)}")
