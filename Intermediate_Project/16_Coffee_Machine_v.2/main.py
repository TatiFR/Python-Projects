from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create an object by calling the blueprints(classes) the "Coffee Maker", "Menu" and "Money Machine"
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

# Like in previous activity, while the coffee machine is turned on we will have a while loop running with tasks
is_on = True

while is_on:
    option = menu.get_items()
    choice = input(f"What would you like? ({option}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        # Give the new variable the ability to call the report
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        # Check the resources are sufficient (this is dependent on different drink types we will run a while loop)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
