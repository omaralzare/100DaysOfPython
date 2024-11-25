# https://appbrewery.github.io/python-day4-demo/
import random

computerChoice = random.randint(0, 2)
yourChoice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
)
if yourChoice == 0:
    print(
        """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
    )
elif yourChoice == 1:
    print(
        """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
    )
elif yourChoice == 2:
    print(
        """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
    )
else:
    print("You typed an invalid number, you lose!")
    exit()
if computerChoice == 0:
    print("Computer chose: ")
    print(
        """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
    )
elif computerChoice == 1:
    print("Computer chose: ")
    print(
        """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
    )
elif computerChoice == 2:
    print("Computer chose: ")
    print(
        """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
    )
if yourChoice == computerChoice:
    print("It's a draw")
elif yourChoice == 0 and computerChoice == 1:
    print("You lose")
elif yourChoice == 0 and computerChoice == 2:
    print("You win!")
elif yourChoice == 1 and computerChoice == 0:
    print("You win!")
elif yourChoice == 1 and computerChoice == 2:
    print("You lose")
elif yourChoice == 2 and computerChoice == 0:
    print("You lose")
elif yourChoice == 2 and computerChoice == 1:
    print("You win!")
