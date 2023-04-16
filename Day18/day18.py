# -----------------Understanding Turtle Graphics and How to use the Documentation-------------------#
# Turtle Module helps us to draw graphics on the screen
# from turtle import Turtle, Screen

# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)

# GUI - Graphical User Interfaces can show images, can help you to click, drag etc.
# Turtle module relies on Tkinter to create graphics on the screen

# -----------------Turtle Challenge 1 - Draw a Square-------------------#
# tim = Turtle()

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# -----------------Importing Modules, Installing Packages, and Working with Aliases-------------------#
# Ways of importing modules
#1. Basic import: import turtle (keyword Modulename)
# tim = turtle.Turtle()

#2. from...import...: from turtle import Turtle (keyword Modulename keyword Thing in the Module): 
    #   This ais useful when we are using the class Turtle alot
# tim = Turtle()
# tom = Turtle()

#3. from...import...*: from turtle import * (keyword Modulename keyword Thing everything(*)))
    #  Its had in readability. Avoid it

##### Aliasing Module: useful in long name modules
# import turtle as t
# tim = t.Turtle()

##### Installing Modules
# There are some modules that you cant just import
# Modules which are packaged with the Python standard library like turtle, you can just use import without install
# These are small Library to get you started.
# For bigger library from the internet we have to use/install from the Python Library
# We only install libraries that we want to use








# screen = Screen()
# screen.exitonclick()
