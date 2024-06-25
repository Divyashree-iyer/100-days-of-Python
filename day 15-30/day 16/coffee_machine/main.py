from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

off=False

menu=Menu()

coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()

while not off:
    drink=input(f"What would you like from {menu.get_items()}: ") 
    
    if drink=="report":
        coffee_maker.report()
        money_machine.report()
    elif drink=="off":
        print("it was lovely serving you")
        off=True
    elif menu.find_drink(drink):
        Drink=menu.find_drink(drink)
        if coffee_maker.is_resource_sufficient(Drink):
            if money_machine.make_payment(Drink.cost):
                coffee_maker.make_coffee(Drink)
    
    
    
        