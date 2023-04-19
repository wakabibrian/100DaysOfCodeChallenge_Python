from turtle import Turtle, Screen
# Step1: Create a snake body

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

starting_positions = [(0,0), (-20,0), (-40,0)]


# x_cord = 0

for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.goto(position)
    # new_segment.goto(x=x_cord, y=0)
    # x_cord -= 20


screen.exitonclick()
