menu = {
    "e" : { # espresso
        "ingredients": {
            "water" : 50,
            "coffee" : 18,
        },
        "cost" : 1.5,
        "name" : "espresso"
    },
    "l" : { # latte
        "ingredients": {
            "water" : 200,
            "milk" : 150,
            "coffee" : 24,
        },
        "cost" : 2.5,
        "name" : "latte"
    },
    "c" : { # cappuccino
        "ingredients": {
            "water" : 250,
            "milk" : 100,
            "coffee" : 24,
        },
        "cost" : 3.0,
        "name" : "cappuccino"
    }
}

profit = 0

resources = {
    "water" : 300,
    "milk" : 200,
    "coffee" : 100,
}

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient"""
    for i in order_ingredients:
        if order_ingredients[i] >= resources[i]:
            print(f"Sorry there is not enough {i}.")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many nickles?: ")) * 0.1
    total += int(input("How many dimes?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Returns True when payment is accepted, or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for i in order_ingredients:
        resources[i] -= order_ingredients[i]
    print(f"Here is your {drink_name}")

is_on = True

while is_on:
    choise = input("What would you like? (espresso 'e' /latte 'l' /cappuccino 'c'): ").lower()
    if choise == 'off':
        is_on = False
    elif choise == 'report':
        print(f"RESOURCES \nWATER: {resources['water']} ml \nMILK: {resources['milk']} ml \nCOFFEE: {resources['coffee']} g \nMONEY: {round(profit,2)} $")
    else:
        drink = menu[choise]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(drink["name"], drink["ingredients"])

