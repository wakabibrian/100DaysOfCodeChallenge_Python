# -----------------Python Higher Order Functions & Event Listeners-------------------#
# from turtle import Turtle, Screen

# tim = Turtle()
# screen = Screen()

# def move_forwards():
#     tim.forward(10)


# screen.listen()
# screen.onkey(key="space", fun=move_forwards)
# # Passing a function as an input we only pass in the name without adding the parenthesis
# # The above is known as Higher order funcctions
# # Higher Order Functions used mostly in event listeners
# screen.exitonclick()

# -----------------Challenge: Make an Etch-A-Sketch App-------------------#
# W - Forward
# S - Backward
# A - Counter-clockwise
# D - Clockwise
# C - Clear drawing
# from turtle import Turtle, Screen

# tim = Turtle()
# screen = Screen()
# keys = ("w", "s", "d", "a", "c")
# call_function = ""

# def move_forwards():
#     tim.forward(10)

# def move_backwards():
#     tim.backward(10)

# def move_clockwise():
#     tim.right(10)

# def move_counter_clockwise():
#     tim.left(10)

# def clear_drawing():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()


# screen.listen()

# for key_pressed in keys:
#     if key_pressed == keys[0]:
#         call_function = move_forwards
#     elif key_pressed == keys[1]:
#         call_function = move_backwards
#     elif key_pressed == keys[2]:
#         call_function = move_clockwise
#     elif key_pressed == keys[3]:
#         call_function = move_counter_clockwise
#     elif key_pressed == keys[4]:
#         call_function = clear_drawing


#     screen.onkey(key=key_pressed, fun=call_function)


# screen.exitonclick()

# -----------------Object State and Instances-------------------#
# You can create instances of classes (different objects from the same class)
# timmy = Turtle()
# tommy = Turtle()

# Their attributes and methods are known as state
# They have different states

# -----------------Day 19 Project: Turtle Race-------------------#
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a Bet", prompt="Which Turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -30, 10, 50, 90, 130]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")

        radom_distance = random.randint(0, 10)
        turtle.forward(radom_distance)

screen.exitonclick()

