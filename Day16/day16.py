# -----------------Why do we need OOP - Object Oriented Programming?-------------------#
# Day 15 downwards we did procedural programming - we set procedures/ functions that do particular things.
# The code can be long, complex and confusing: Works from top to bottom and jumps to a function

# Object Oriented pradigm solves procedural programming issues
# Splits complex tasks into smaller pieces
# Different people can work on different modules simultaneously
# Each pieces become reusable if we need the same functionality in the future

# -----------------How to use OOP: Objects and Classes-------------------#
# In OOP, we are trying to model real life objects
# When modeling objects, we think of what it has and what it does
# What it has - attributes (variables).
# What it does - methods (functions).
# It's called a  method because it is a function that a particular modelled object can do
#### We can have multiple objects generated from the same type: from the same blue print.
# In OOP, a blue of an object is called a class
# Objects are generated from a blue print called class

# -----------------How to create objeects and classes-------------------#
# Classes are always written with first letter of each word capitalised (Pascal Case), 
# differentiating it from all variables and function names
# car = CarBluePrint(), 
# car - object created from a CarBluePrint() class

# from turtle import Turtle, Screen

# # creating an object
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)

# my_screen = Screen()

# # object attributes, what the my_screen object has
# print(my_screen.canvheight) # Accessing the attribute

# # object methods, what the my_screen object does
# my_screen.exitonclick()

# -----------------How to Add Python Packages and use PyPi-------------------#
# Packages: Using code that other developers have written
# Package differs from module because it is a whole bunch of code that other developers have written 
# PyPi - Python Package Index
# Inorder to use packages found from the Python Package Index, you have to install them
# import prettytable

# -----------------Building the Coffee Machine in OOP-------------------#
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
