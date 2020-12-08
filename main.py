from art import logo
from database import *

money = 0


def machine_resources():
    resources_info = f" Water: {resources['water']}ml\n Milk: {resources['milk']}ml\n Coffee: {resources['coffee']}gr\n Money: ${money}"
    return resources_info


def is_resource_sufficient(drink):
    if MENU[drink]["ingredients"]["water"] > resources["water"] or MENU[drink]["ingredients"]["milk"] > resources["milk"] or MENU[drink]["ingredients"]["coffee"] > resources["coffee"]:
        print(
            f"Sorry, there are not enough resources in the machine. Please contact the admin to refill it.")
        return False
    else:
        print(f"The {drink} is ${MENU[drink]['cost']}")
        return True


def subtract_resources(drink):
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    return resources


def insert_money():
    print("Please insert coins: ")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.15
    total += int(input("How many nickels? ")) * 0.5
    total += int(input("How many pennies? ")) * 0.1
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
        print("Machine is turning off...")
        is_on = False
    elif choice == "report":
        print(machine_resources())
    elif choice == "refill":
        refill_machine()
        print("Machine's resources have been refilled. Choose 'report' to check status.")
    elif choice == "espresso" and is_resource_sufficient("espresso"):
        insert = insert_money()
        if insert == MENU['espresso']['cost']:
            subtract_resources("espresso")
            money += insert
            print("Enjoy your espresso! ☕")
        elif insert < MENU['espresso']['cost']:
            print(
                f"Sorry, you have not entered the right amount. here's your money {insert}")
        elif insert > MENU['espresso']['cost']:
            subtract_resources("espresso")
            change = insert - MENU['espresso']['cost']
            money += MENU['espresso']['cost']
            print(f"Here's your change {change}.")
            print("Enjoy your espresso! ☕")
    elif choice == "latte" and is_resource_sufficient("latte"):
        insert = insert_money()
        if insert == MENU['latte']['cost']:
            subtract_resources("latte")
            money += insert
            print("Enjoy your latte! 🥛")
        elif insert < MENU['latte']['cost']:
            print(
                f"Sorry, you have not entered the right amount. here's your money {insert}")
        elif insert > MENU['latte']['cost']:
            subtract_resources("latte")
            change = insert - MENU['latte']['cost']
            money += MENU['latte']['cost']
            print(f"Here's your change {change}.")
            print("Enjoy your latte! 🥛")
    elif choice == "cappuccino" and is_resource_sufficient("cappuccino"):
        insert = insert_money()
        if insert == MENU['cappuccino']['cost']:
            subtract_resources("cappuccino")
            money += insert
            print("Enjoy your cappuccino! ☕")
        elif insert < MENU['cappuccino']['cost']:
            print(
                f"Sorry, you have not entered the right amount. here's your money {insert}")
        elif insert > MENU['cappuccino']['cost']:
            subtract_resources("cappuccino")
            change = insert - MENU['cappuccino']['cost']
            money += MENU['cappuccino']['cost']
            print(f"Here's your change {change}.")
            print("Enjoy your cappuccino! ☕")
