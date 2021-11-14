
# import data
from coffee_data import MENU, resources


# Functions
def resource_unit(any_resource):
    """
    Find the unit for the resource
    :param any_resource: name of the resource
    :return: the unit of the resource
    """
    unit_dict = {
        "water": "ml",
        "milk": "ml",
        "coffee": "g"
    }
    return unit_dict[any_resource]


def report():
    """
    Report the current resources of the coffee machine.
    """
    for _ in current_resources:
        print(f"{_.capitalize()}: {current_resources[_]}{resource_unit(_)}")
    if earnings != 0:
        print(f"Money: ${earnings}")


def resource_checker(coffee_name):
    """
    Check if the machine has enough resources to make the coffee.
    :return: True for enough. False for not enough.
    """
    coffee_ingredients = MENU[coffee_name]["ingredients"]
    for ingredient in coffee_ingredients:
        if coffee_ingredients[ingredient] > current_resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True


def coin_checker(coffee_name):
    """
    Require inputs of four kinds of coins
    :return: True if enough. False if not enough
    """
    print(f"The price is $ {MENU[coffee_name]['cost']}. Please insert coins.")
    quarters = int(input("How many quarters? ($0.25): "))
    dimes = int(input("How many dimes? ($0.10): "))
    nickles = int(input("How many quarters? ($0.05): "))
    pennies = int(input("How many quarters? ($0.01): "))
    coins_sum = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    changes = coins_sum - MENU[coffee_name]["cost"]
    if changes < 0:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        global earnings
        earnings += MENU[coffee_name]["cost"]
        print(f"Here's $ {round(changes, 2)} in change.")
        return True


def make_coffee(coffee_name):
    """
    Make coffee and reduce the resources used.
    """
    # reduce the resources used
    for resource in MENU[coffee_name]["ingredients"]:
        current_resources[resource] -= MENU[coffee_name]["ingredients"][resource]
    # Tell users the coffee is ready
    print(f"Here's your {coffee_name}. Enjoy! :) ")


def coffee_machine():
    # Prompt user by asking "What would you like? "
    order = input("What would you like? (espresso/latte/cappuccino): ")
    # Turn off the machine by entering "off" to the prompt
    if order == "off":
        quit()
    elif order == "report":
        report()
    # check if resources and coins are enough
    else:
        if resource_checker(order) and coin_checker(order):
            make_coffee(order)
    coffee_machine()


# set the resources for the coffee machine
current_resources = resources
# set the initial earnings for the coffee machine
earnings = 0
# run the machine
coffee_machine()