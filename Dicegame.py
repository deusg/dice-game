# dice game

import random
import time

def roll_dice(n):
    dice = [] # start with empty list of dice
    # add random numbers between 1 to 6 to the list
    for i in range(n):
        dice.append(random.randint(1,6))
    return dice


def find_winner(cdice_list, udice_list):
    computer_total = sum(cdice_list)
    user_total = sum(udice_list)
    print(f"Computer total {computer_total}")
    print(f"User total {user_total}")
    if user_total > computer_total:
        print("User wins")
    elif user_total < computer_total:
        print("Computer wins")
    else:
        print("It is a tie!")


def roll_again(choices, dice_list):
    print("Rolling again ...")
    time.sleep(3)
    for i in range(len(choices)):
        if choices[i] == "r":
            dice_list[i] = random.randint(1,6)
        time.sleep(3)


def computer_stratetgy1(n):
    # create computer choices : roll everything again
    print("Computer is thinking ...")
    time.sleep(3)
    choices = "" # start with an empty list of choices
    for i in range(n):
        choices = choices + "r"
    return choices


def computer_stratetgy2(n):
    # create computer choices : roll if < 5
    print("Computer is thinking ...")
    time.sleep(3)
    choices = "" # start with an empty list of choices
    for i in range(n):
        if computer_rolls[i] < 5:
            choices = choices + "r"
        else:
            choices = choices + "-"
    return choices


# step1 in main program area - start game
number_dice = input("Enter number of of dice: ")
number_dice = int(number_dice)
ready = input("Ready to start? Hit any key to continue? ")


# step 2 in main program area - roll dice
# User turn to roll
user_rolls = roll_dice(number_dice)
print(f"User first roll: {user_rolls}")

# step 4 - get user choices
user_choices = input("Enter - to hold or r to roll again: ")
# check length of user input
while len(user_choices) != number_dice:
    print(f"You must enter {number_dice} choices")
    user_choices = input("Enter - to hold or r to roll again : ")

# Step 5 - roll again based on user choices
roll_again(user_choices, user_rolls)
print(f"Player new Roll: {user_rolls}")

# computer's turn to roll
print("Computers turn")
computer_rolls = roll_dice(number_dice)
print(f"Computer first roll: {computer_rolls}")

# step 6
# decide on what choice - using one of the strategy functions
computer_choices = computer_stratetgy2(number_dice)
print(f"Compouter Choice: {computer_choices}")
# comouter roll again using the choices it made
roll_again(computer_choices, computer_rolls)
print(f"Computer new Roll: {computer_rolls}")

# final line in code - deciding who wins
find_winner(computer_rolls, user_rolls)