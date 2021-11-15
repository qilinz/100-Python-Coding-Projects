from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True

# Work starts
while is_on:
    order = input(f"What would you like? ({menu.get_items()}): ")
    # Find the drink
    if order == "report":
        coffee_machine.report()
        money_machine.report()
    elif order == "off":
        is_on = False
    else:
        drink_name = menu.find_drink(order)
        if drink_name is not None:
            # check if resources and money are enough
            if coffee_machine.is_resource_sufficient(drink_name) and money_machine.make_payment(drink_name.cost):
                #  make coffee
                coffee_machine.make_coffee(drink_name)
