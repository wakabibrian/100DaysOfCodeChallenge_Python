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

money = 0
turned_on = True


# 4. Check resources sufficient
def resources_sufficient(menu):
    """Returns True if resources are enough"""

    is_sufficient = False

    for resource in menu:
        is_sufficient = resources[resource] >= menu[resource]
        if is_sufficient == False:
            print(f"Sorry there is not enough {resource}.")
            return False

    return is_sufficient


# 5. Process coins.
def total_coins():
    """Calculates total coins inserted"""

    print("Please insert coins.")
    quarter = int(input("how many quarters?: "))
    dime = int(input("how many dimes?: "))
    nickle = int(input("how many nickles?: "))
    pennie = int(input("how many pennies?: "))
    return (quarter*0.25) + (dime*0.10) + (nickle*0.05) + (pennie*0.01)


# 6. Check transaction successful?
def transaction_success(amount_inserted, drink):
    """Returns successful if the money inserted is enough"""

    global money
    drink_cost = MENU[drink]["cost"]
    change = 0

    if amount_inserted == drink_cost:
        money += amount_inserted
        return True
    elif amount_inserted > drink_cost:
        change = round(amount_inserted - drink_cost, 2)
        money += drink_cost
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# 7. Make Coffee.
def make_coffee(drink):
    """Takes drink, reduces ingredients as per the drink"""

    for ingredient in MENU[drink]["ingredients"]:
        resources[ingredient] -= MENU[drink]["ingredients"][ingredient]

    print(f"Here is your {drink}. Enjoy!")


while turned_on:
    # 1. Prompt user.
    user_request = input("  What would you like? (espresso/latte/cappuccino): ").lower()

    # 3. Print report.
    if user_request == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")

    elif user_request == "espresso" or user_request == "latte" or user_request == "cappuccino":
        is_resources_sufficient = resources_sufficient(MENU[user_request]["ingredients"])
        if is_resources_sufficient:
            total_coins_inserted = total_coins()
            is_transaction_successful = transaction_success(total_coins_inserted, user_request)
            if is_transaction_successful:
                make_coffee(user_request)

    # 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
    elif user_request == "off":
        turned_on = False
