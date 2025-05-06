# Game: Rock Paper Scissors
# Rock 0 win against Scissors 2
# Scissors 2 win against Paper 1
# Paper 1 win against rock 0

import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# 0, 1, 2

computer_choice = random.randint (0, 2)
choice_list = ["Rock", "Paper", "Scissors"]
print(f"Computer chose {choice_list[computer_choice]}")

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number! YOU LOSE!")
elif user_choice == 0 and computer_choice == 2:
    print("YOU WIN!")
elif user_choice == 2 and computer_choice == 0:
    print("YOU LOSE!")
elif user_choice > computer_choice:
    print("YOU WIN!")
elif computer_choice > user_choice:
    print("YOU LOSE!")
elif computer_choice == user_choice:
    print("It's a draw")
