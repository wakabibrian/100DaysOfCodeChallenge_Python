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
should_continue = True

# 3. Print report.
##       a. When the user enters “report” to the prompt, a report should be generated that shows
##       the current resource values. e.g.
##       Water: 100ml
##       Milk: 50ml
##       Coffee: 76g
##       Money: $2.5
def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

# 4. Check resources sufficient?
##      a. When the user chooses a drink, the program should check if there are enough
##          resources to make that drink.
##      b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
##          not continue to make the drink but print: “ Sorry there is not enough water. ”
##      c. The same should happen if another resource is depleted, e.g. milk or coffee.
def check_resources(user_input, resources):
    """Takes user_requests and returns True if resources are enough"""
    espresso_water = MENU["espresso"]["ingredients"]["water"]
    espresso_coffee = MENU["espresso"]["ingredients"]["coffee"]

    latte_water = MENU["latte"]["ingredients"]["water"]
    latte_milk = MENU["latte"]["ingredients"]["milk"]
    latte_coffee = MENU["latte"]["ingredients"]["coffee"]

    cappuccino_water = MENU["cappuccino"]["ingredients"]["water"]
    cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]
    cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]

    if user_input == "espresso":
        return resources["water"] >= espresso_water and resources["coffee"] >= espresso_coffee
         
    elif user_input == "latte":
        return resources["water"] >= latte_water and resources["milk"] >= latte_milk and resources["coffee"] >= latte_coffee
    
    elif user_input == "cappuccino":
        return resources["water"] >= cappuccino_water and resources["milk"] >= cappuccino_milk and resources["coffee"] >= cappuccino_coffee

# Process coins.
##      a. If there are sufficient resources to make the drink selected, then the program should
##          prompt the user to insert coins.
##      b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
##      c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
##          pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

while should_continue:
    # 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
    ##       a. Check the user’s input to decide what to do next.
    ##       b. The prompt should show every time action has completed, e.g. once the drink is
    ##          dispensed. The prompt should show again to serve the next customer.
    user_request = input("  What would you like? (espresso/latte/cappuccino): ").lower()

    if user_request == "report":
        report()
    elif user_request == "espresso" or user_request == "latte" or user_request == "cappuccino":
        print(check_resources(user_request, resources))
    # 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
    ##       a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
    ##       the machine. Your code should end execution when this happens.
    elif user_request == "off":
        should_continue = False



# Check transaction successful?
##      a. Check that the user has inserted enough money to purchase the drink they selected.
##      E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
##          program should say “ Sorry that's not enough money. Money refunded. ”.
##      b. But if the user has inserted enough money, then the cost of the drink gets added to the
##          machine as the profit and this will be reflected the next time “report” is triggered. E.g.
##          Water: 100ml
##          Milk: 50ml
##          Coffee: 76g
##          Money: $2.5
##      c. If the user has inserted too much money, the machine should offer change.
##          E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
##          places.

# Make Coffee.
##       a. If the transaction is successful and there are enough resources to make the drink the
##           user selected, then the ingredients to make the drink should be deducted from the
##           coffee machine resources.
##           E.g. report before purchasing latte:
##               Water: 300ml
##               Milk: 200ml
##               Coffee: 100g
##               Money: $0
##               Report after purchasing latte:
##               Water: 100ml
##               Milk: 50ml
##               Coffee: 76g
##               Money: $2.5
##         b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
##               latte was their choice of drink.
