# -----------------Python Higher Order Functions & Event Listeners-------------------#
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forwards)
# Passing a function as an input we only pass in the name without adding the parenthesis
# The above is known as Higher order funcctions
# Higher Order Functions used mostly in event listeners
screen.exitonclick()

# -----------------Challenge: Make an Etch-A-Sketch App-------------------#


