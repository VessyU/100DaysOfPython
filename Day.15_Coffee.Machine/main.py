#import sys

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money_made = 0

#def choice():
#    choice = input("What would you like? (espresso/latte/cappucino)").lower
#    return choice

def successful_payment(input_money, drink_cost):
    if input_money >= drink_cost:
        change = round(input_money - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global money_made
        money_made += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Take your money back. ")
        return False

def enough_resources(ingredients):
    for x in ingredients:
        if ingredients[x] > resources[x]:
            print(f"Sorry there is not enough {x}.")
            return False
        return True

def payment():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total_money = 0.25*quarters + 0.1*dimes + 0.05*nickles + 0.01*pennies
    return total_money

def drink(drink_name, ingredients):
    for i in ingredients:
        resources[i] -= ingredients[i]
    print(f"Here is your name {drink_name} ☕. Enjoy!")

#def programm():
#    choice()
#    if choice() == "off":
#        sys.exit()
#    money = payment()
#    resources["money"] = money
machine_on = True

while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        machine_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money_made}")
    else:
        drink_choice = MENU[choice]
        if enough_resources(drink_choice["ingredients"]):
            payment = payment()
            if successful_payment(payment, drink_choice["cost"]):
                drink(choice, drink_choice["ingredients"])
