import random

while True:
    input("Press enter to roll the dice: ")
    roll = random.randint(1, 6)
    print("Dice rolled", roll)
    choice = input("Roll again? (y/n): ").lower()
    if choice=="n":
        break
    elif choice!="y":
        print("Invalid choice, rolling again...")