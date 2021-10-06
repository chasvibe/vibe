import random

def roll_dice():
    dice = random.randint(1,6)
    #roll = print(f'The number on the dice is ---> {dice}')
    return dice


def compare(guess, roll):



roll = roll_dice()
guess = eval(input("Please guess a number between 1 and 6: "))
while guess != roll:
    guess = eval(input("Please try again: "))
    if guess == roll:
        print("Nice! You guessed right!")
        break
    elif guess < roll:
        print("Sorry, too low...")
    elif guess > roll:
        print("Sorry, too high...")