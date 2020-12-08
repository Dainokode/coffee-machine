from art import logo
from database import *


def coffee_machine():
    # Menu, ingredients and costs
    # Espresso:
    espresso_water = MENU["espresso"]["ingredients"]["water"]
    espresso_coffee = MENU["espresso"]["ingredients"]["coffee"]
    espresso_cost = MENU["espresso"]["cost"]
    # Latte:
    latte_water = MENU["latte"]["ingredients"]["water"]
    latte_milk = MENU["latte"]["ingredients"]["milk"]
    latte_coffee = MENU["latte"]["ingredients"]["coffee"]
    latte_cost = MENU["latte"]["cost"]
    # Cappuccino:
    cappuccino_water = MENU["cappuccino"]["ingredients"]["water"]
    cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]
    cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
    cappuccino_cost = MENU["cappuccino"]["cost"]

    # Coffee machine's money
    MONEY = 0

    # Coffee machine's resources
    WATER = resources["water"]
    MILK = resources["milk"]
    COFFEE = resources["coffee"]

    # Automatic message after choosing drink
    MESSAGE = "Please insert coins."

    time_break = True

    # user choice
    while time_break and WATER > 0 or MILK > 0 or COFFEE > 0:
        choice = input(
            "What would you like? (espresso/latte/cappuccino) ").lower()
        if choice == "report":
            print(
                f"The machine has:\n Water: {WATER}ml\n Milk: {MILK}ml\n Coffee: {COFFEE}gr\n Money: ${MONEY}")
        elif choice == "espresso":
            # tell user drink's cost
            print(f"The espresso is {espresso_cost}\n")
            # current money inserted for drink
            money_inserted = 0
            # ask to enter coins
            print(MESSAGE)
            quarters = int(input("How many quarters? "))
            for quarter in range(quarters):
                money_inserted += 0.25
            dimes = int(input("How many dimes? "))
            for dime in range(dimes):
                money_inserted += 0.10
            nickels = int(input("How many nickels? "))
            for nickel in range(nickels):
                money_inserted += 0.05
            pennies = int(input("How many pennies? "))
            for penny in range(pennies):
                money_inserted += 0.01
            # logic
            if money_inserted < espresso_cost:
                print(
                    f"Sorry, you did not enter the correct amount here's your money {money_inserted}\n")
            elif WATER <= 0 or COFFEE <= 0:
                print(
                    f"Sorry, the machine is out of resources. Here's your money {money_inserted}\n")
                return
            elif money_inserted == espresso_cost and WATER >= 0 or COFFEE >= 0:
                MONEY += money_inserted
                WATER -= espresso_water
                COFFEE -= espresso_coffee
                print("Enjoy your espresso! ☕\n")
                if money_inserted > espresso_cost:
                    change = money_inserted % espresso_cost
                    MONEY -= change
                    print(f"Here's your change, {change}\n")

        elif choice == "latte":
            # tell user drink's cost
            print(f"The latte is {latte_cost}\n")
            # current money inserted for drink
            money_inserted = 0
            # ask to enter coins
            print(MESSAGE)
            quarters = int(input("How many quarters? "))
            for quarter in range(quarters):
                money_inserted += 0.25
            dimes = int(input("How many dimes? "))
            for dime in range(dimes):
                money_inserted += 0.10
            nickels = int(input("How many nickels? "))
            for nickel in range(nickels):
                money_inserted += 0.05
            pennies = int(input("How many pennies? "))
            for penny in range(pennies):
                money_inserted += 0.01
            # logic
            if money_inserted < latte_cost:
                print(
                    f"Sorry, you did not enter the correct amount here's your money {money_inserted}\n")
            elif WATER <= 0 or MILK <= 0 or COFFEE <= 0:
                print(
                    f"Sorry, the machine is out of resources. Here's your money {money_inserted}\n")
                return
            elif money_inserted == latte_cost and WATER >= 0 or MILK >= 0 or COFFEE >= 0:
                MONEY += money_inserted
                WATER -= latte_water
                MILK -= latte_milk
                COFFEE -= latte_coffee
                print("Enjoy your latte! 🥛\n")
                if money_inserted > latte_cost:
                    change = money_inserted % latte_cost
                    MONEY -= change
                    print(f"Here's your change, {change}\n")

        elif choice == "cappuccino":
            # tell user drink's cost
            print(f"The cappuccino is {cappuccino_cost}\n")
            # current money inserted for drink
            money_inserted = 0
            # ask to enter coins
            print(MESSAGE)
            quarters = int(input("How many quarters? "))
            for quarter in range(quarters):
                money_inserted += 0.25
            dimes = int(input("How many dimes? "))
            for dime in range(dimes):
                money_inserted += 0.10
            nickels = int(input("How many nickels? "))
            for nickel in range(nickels):
                money_inserted += 0.05
            pennies = int(input("How many pennies? "))
            for penny in range(pennies):
                money_inserted += 0.01
            # logic
            if money_inserted < cappuccino_cost:
                print(
                    f"Sorry, you did not enter the correct amount here's your money {money_inserted}\n")
            elif WATER <= 0 or MILK <= 0 or COFFEE <= 0:
                print(
                    f"Sorry, the machine is out of resources. Here's your money {money_inserted}\n")
                return
            elif money_inserted == cappuccino_cost and WATER >= 0 or MILK >= 0 or COFFEE >= 0:
                MONEY += money_inserted
                WATER -= cappuccino_water
                MILK -= cappuccino_milk
                COFFEE -= cappuccino_coffee
                print("Enjoy your cappuccino! ☕\n")
                if money_inserted > cappuccino_cost:
                    change = money_inserted % cappuccino_cost
                    MONEY -= change
                    print(f"Here's your change, {change}\n")

        answer = input("Do you want another drink? Choose 'y' or 'n': ")
        if answer == "n":
            time_break = False


print(logo)


coffee_machine()
