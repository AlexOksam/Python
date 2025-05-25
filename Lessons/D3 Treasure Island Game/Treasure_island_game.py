print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
choise1: str = input("        Type 'Left' or 'Right' ").lower()

if choise1 == "left":
    choise2: str = input('You\'ve come to a like, there is an island in the middle of the lake. '
    'Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()
    
    if choise2 == "wait":
        choise3: str = input("You arrive at the island unharmed. There is house with 3 doors."
        "One red, one yellow and one blue. Which color do you choose? ").lower()

        if choise3 == "yellow":
            print("You found the treasure. YOU WIN!")
        else:
            rint("Game Over!")
    else:
        print("Game Over!")
else:
    print("You fell in to a hole. Game Over!")
