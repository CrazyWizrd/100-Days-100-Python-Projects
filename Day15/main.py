from art import *
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
print(logo)
def money(drink,output_money):
    if drink == "report":
        return output_money
    money_required = MENU[drink]["cost"]
    print("Please insert coins.")
    money_given = (int(input("How many quarters?: "))) * 0.25
    money_given += (int(input("How many dimes?: "))) * 0.10
    money_given += (int(input("How many nickles?: "))) * 0.05
    money_given += (int(input("How many pennies?: "))) * 0.01
    if money_given >= money_required:
        change = round(money_given - money_required , 2)
        global final_money
        final_money += money_required
        return f"Here is ${change} in change.\nHere is your {drink} ☕️. Enjoy!"
    else:
        for _ in resources:
            resources[_] += MENU[drink]["ingredients"][_]
        return "Sorry that's not enough money. Money refunded."

def machine(total_money):
    beverage = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if beverage == "espresso" or beverage == "latte" or beverage == "cappuccino":
        for _ in resources:
            if resources[_] >= MENU[beverage]["ingredients"][_]:
                resources[_] -= MENU[beverage]["ingredients"][_]
            else:
                print(f"Sorry insufficient {_}. Please try again later.")
                machine(final_money)
        print(money(beverage,total_money))
        machine(final_money)
    elif beverage == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${total_money}")
        machine(final_money)
    elif beverage == "stop":
        return
    else:
        print("Please enter the correct option.")
        machine(final_money)

final_money = 0
machine(final_money)
