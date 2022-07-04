from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

espresso = MenuItem("espresso", 50, 0, 18, 1.5)

latte  =MenuItem("latte", 200, 150, 24, 2.5)

capuccino=MenuItem("capuccino", 250, 100, 24, 3.0)

drinks_menu=Menu()

coffe_deliver = CoffeeMaker()

money_machine=MoneyMachine()

on=True
while on:
    choice = input("What would you like?"+" "+ drinks_menu.get_items()+":")
    if choice=="report":
        coffe_deliver.report()
    elif choice=="off":
        on=False
    elif choice==(drinks_menu.find_drink(choice)).name:
        seleccion=(drinks_menu.find_drink(choice))
        if coffe_deliver.is_resource_sufficient(seleccion):
            if money_machine.make_payment(seleccion.cost):
                coffe_deliver.make_coffee(seleccion)







