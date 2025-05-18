#PyPassword Generator
import random
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['(', ')', '[', ']' , '{', '}', ',', ':', '.', '*', '=', ';', '"', '#']


print("Welcome to the PyPassword Generator")
number_letters = int(input("How many letters would you like in your password?\n"))
number_symbols = int(input("How many symbols would you like ?\n"))
number_numbers = int(input("How many numbers would you like ?\n"))

password_list = []

for char in range (0, number_letters):
    password_list.append(random.choice(letters))

for char in range (0, number_symbols):
    password_list.append(random.choice(symbols))

for char in range (0, number_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

passwort = ""

for char in password_list:
    passwort += char

print(f"Your new password is:\n{passwort}")
