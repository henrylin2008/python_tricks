from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO:
# 1. print report
# 2. Check resources sufficient?
# 3. Process coins
# 4. Check transaction successful?
# 5. Make Coffee.

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

# money_machine.report()
# coffee_maker.report()

while is_on:
    options = menu.get_items()      # list of available items (latte/espresso/cappuccino/)
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False               # shut off
    elif choice == "report":        # get report
        coffee_maker.report()       # report of all resources
        money_machine.report()      # report of current profit
    else:
        drink = menu.find_drink(choice)   # user's input of drink
        # check if resource is sufficient (True/False) and if payment is successful (True/False)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)         # make coffee

