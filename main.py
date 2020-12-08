from art import logo
from database import *

money = 0


def machine_resources():
    resources_info = f" Water: {resources['water']}ml\n Milk: {resources['milk']}ml\n Coffee: {resources['coffee']}gr\n Money: ${money}"
    return resources_info


def is_resource_sufficient(drink):
    for item in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][item] > resources[item]:
            print(
                f"Sorry, there is not enough {item} in the machine. Please contact the admin to refill the {item}.\n")
            return False
    else:
        print(f"The {drink} is ${MENU[drink]['cost']}\n")
        return True


def subtract_resources(drink):
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    return resources


def insert_money():
    print("Please insert coins: \n")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.15
    total += int(input("How many nickels? ")) * 0.5
    total += int(input("How many pennies? \n")) * 0.1
    return total


def refill_machine():
    for resource in resources:
        resources[resource] += 100
    return resources


print(logo)

is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino) ").lower()
    if choice == "off":
        print("Machine is turning off...\n")
        is_on = False
    elif choice == "report":
        print(machine_resources())
    elif choice == "refill":
        refill_machine()
        print("Machine's resources have been refilled. Choose 'report' to check status.\n")
    elif choice == "espresso" and is_resource_sufficient("espresso"):
        insert = insert_money()
        if insert == MENU['espresso']['cost']:
            subtract_resources("espresso")
            money += insert
            print("Enjoy your espresso! ☕\n")
        elif insert < MENU['espresso']['cost']:
            print(
                f"Sorry, you have not entered the right amount. here's your money {insert}\n")
        elif insert > MENU['espresso']['cost']:
            subtract_resources("espresso")
            change = insert - MENU['espresso']['cost']
            money += MENU['espresso']['cost']
            print(f"Here's your change {change}.")
            print("Enjoy your espresso! ☕\n")
    elif choice == "latte" and is_resource_sufficient("latte"):
        insert = insert_money()
        if insert == MENU['latte']['cost']:
            subtract_resources("latte")
            money += insert
            print("Enjoy your latte! 🥛\n")
        elif insert < MENU['latte']['cost']:
            print(
                f"Sorry, you have not entered the right amount. here's your money {insert}\n")
        elif insert > MENU['latte']['cost']:
            subtract_resources("latte")
            change = insert - MENU['latte']['cost']
            money += MENU['latte']['cost']
            print(f"Here's your change {change}.")
            print("Enjoy your latte! 🥛\n")
    elif choice == "cappuccino" and is_resource_sufficient("cappuccino"):
        insert = insert_money()
        if insert == MENU['cappuccino']['cost']:
            subtract_resources("cappuccino")
            money += insert
            print("Enjoy your cappuccino! ☕\n")
        elif insert < MENU['cappuccino']['cost']:
            print(
                f"Sorry, you have not entered the right amount. here's your money {insert}\n")
        elif insert > MENU['cappuccino']['cost']:
            subtract_resources("cappuccino")
            change = insert - MENU['cappuccino']['cost']
            money += MENU['cappuccino']['cost']
            print(f"Here's your change {change}.")
            print("Enjoy your cappuccino! ☕\n")
