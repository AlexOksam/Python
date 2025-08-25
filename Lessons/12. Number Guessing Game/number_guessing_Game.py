import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check users guess against actual answer

def check_answer(user_guess, actual_answer, turn):
    """Checks answer against guess, retuern the number of turns remaining"""
    if user_guess > actual_answer:
        print("Too high.")
        return turn - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turn - 1
    else:
        print(f"You got it! The answer was {actual_answer}")


# Function to set difficulty

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS # 5
    else: 
        return HARD_LEVEL_TURNS # 10


def game ():
    """Choosing a random number between 1 and 100"""
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()

    guess = 0 # empty variable for save guessing
    
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        # The user guess a number
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have run out of guesses, you lose")
            return
        elif guess != answer:
            print("Guess again.")

game()
