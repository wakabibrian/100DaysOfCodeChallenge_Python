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
# 1. Basic import: import turtle (keyword Modulename)
# tim = turtle.Turtle()

# 2. from...import...: from turtle import Turtle (keyword Modulename keyword Thing in the Module):
#   This ais useful when we are using the class Turtle alot
# tim = Turtle()
# tom = Turtle()

# 3. from...import...*: from turtle import * (keyword Modulename keyword Thing everything(*)))
#  Its had in readability. Avoid it

# Aliasing Module: useful in long name modules
# import turtle as t
# tim = t.Turtle()

# Installing Modules
# There are some modules that you cant just import
# Modules which are packaged with the Python standard library like turtle, you can just use import without install
# These are small Library to get you started.
# For bigger library from the internet we have to use/install from the Python Library
# We only install libraries that we want to use

# -----------------Turtle Challenge 2 - Draw a Dashed Line-------------------#
# from turtle import Turtle, Screen

# tim = Turtle()
# for _ in range(20):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# -----------------Turtle Challenge 3 - Drawing Different Shapes-------------------#
# from turtle import Turtle, Screen
# import random

# class Shape:
#     def __init__(self):
#         self.number_of_sides = 3
#         self.tim = Turtle()

#     def draw_shape(self):

#         number_sides = self.number_of_sides
#         for _ in range(number_sides):
#             self.tim.forward(100)
#             self.tim.right(360/self.number_of_sides)
#         self.number_of_sides += 1

#     def change_pen_color(self):
#         colours = ["cyan", "purple", "red", "blue", "brown", "black", "magenta", "forest green"]
#         self.tim.pencolor(random.choice(colours))

# shape = Shape()

# for _ in range(8):
#     shape.change_pen_color()
#     shape.draw_shape()

# -----------------Turtle Challenge 4 - Generate a Random Walk-------------------#
# from turtle import Turtle, Screen
# import random

# tim = Turtle()

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# direction = [0, 90, 180, 270]
# tim.pensize(10)
# tim.speed("fastest")


# for _ in range(200):
#     tim.color(random.choice(colours))
#     tim.forward(30)
#     tim.setheading(random.choice(direction))


# -----------------Python Tuples and How to Generate Random RGB Colours-------------------#
# A Tuple is a datatype in python: eg (1, 3, 8)
# Tuple (1, 3, 8) - Ordered
# List [1, 3, 8]

# my_tuple = (1, 3, 8)
# print(my_tuple[0])

# Difference with lists: A tuple you cant change the values, cant remove items (Immutable)
# my_tuple[2] = 7 # Error
# Why use Tuples: If you want to create things that are constant e.g color scheme for a website
# if you want to change: you have to first convert it into a list list(my_tuple)


# import turtle as t
# import random

# tim = t.Turtle()
# t.colormode(255)

# def random_color():
#     random_red = random.randint(0, 255)
#     random_green = random.randint(0, 255)
#     random_blue = random.randint(0, 255)
#     random_color = (random_red, random_green, random_blue)
#     return random_color


# # colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# direction = [0, 90, 180, 270]
# tim.pensize(10)
# tim.speed("fastest")


# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(direction))

# -----------------Turtle Challenge 5 - Draw a Spirograph-------------------#
# import turtle as t
# import random

# tim = t.Turtle()
# t.colormode(255)
# tim.speed("fastest")


# def random_color():
#     random_red = random.randint(0, 255)
#     random_green = random.randint(0, 255)
#     random_blue = random.randint(0, 255)
#     color = (random_red, random_green, random_blue)
#     return color

# def draw_spiral(circle_gap):
#     for _ in range(int(360/circle_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.right(circle_gap)

# draw_spiral(5)


# screen = t.Screen()
# screen.exitonclick()

# -----------------Day 18 Project: Hirst Painting Project-------------------#
# import turtle as t
# import random
# t.colormode(255)

# import colorgram

# rgb_colors = []

# image = "C:/Users/b.wakabi/Desktop/100DaysOfCodeChallenge_Python/Day18/art.jpg"
# colors = colorgram.extract(image, 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))

# print(rgb_colors)

# color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165),
#               (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
# tim = t.Turtle()


# def starting_position(x_position, y_position):
#     tim.penup()
#     tim.setx(x_position)
#     tim.sety(y_position)
#     tim.pendown()


# def draw_row_dots(color):
#     tim.penup()
#     tim.forward(50)
#     tim.dot(20, color)
#     tim.pendown()

# x = -200
# y = -200

# for _ in range(10):
#     starting_position(x, y)

#     for _ in range(10):
#         new_color = random.choice(color_list)
#         draw_row_dots(new_color)

#     y += 50

# tim.penup()
# # tim.hideturtle()
 
# for y in range(-250, 250, 50):
#     for x in range(-250, 250, 50):
#         tim.goto(x,y)
#         tim.dot(20, random.choice(color_list))
 

import turtle as t
import random
t.colormode(255)

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165),
              (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
tim = t.Turtle()


tim.speed("fastest")
tim.hideturtle()
tim.penup()

x_col, x_row = -200, -200
y = -200

for _ in range(10):
    tim.sety(y)

    for _ in range(10):
        new_color = random.choice(color_list)
        
        tim.setx(x_row)
        tim.dot(20, new_color)
        x_row += 50

    y += 50
    x_col += 50
    x_row = -200    



screen = t.Screen()
screen.exitonclick()
