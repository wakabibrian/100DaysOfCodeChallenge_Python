# ---------------Class Inheritance-----------------#
# Inheritance: is another feature of object oriented programming that is really helpful.
# Class Inheritance is the process of inheriting behaviours from an existing class
# A class can inherit appearance; attributes and behaviour; methods
# Fish inheriting from the animal class
# class Fish(Animal):
# def __init__(self):
#     super().__init__() #Initialize everything that super class can do

# class Animal:
#     def __init__(self):
#         self.num_eyes = 2

#     def breathe(self):
#         print("Inhale, exhale.")

# class Fish(Animal):
#     def __init__(self):
#         super().__init__()

#     def breathe(self):
#         super().breathe()
#         print("Doing this under water")

#     def swim(self):
#         print("moving in water.")

# fish = Fish()
# fish.swim()
# fish.breathe()

# --------------How to Slice Lists & Tuples in Python-----------------#
# piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
# print(piano_keys[2:5]) #c,d,e
# print(piano_keys[2:]) #c......
# print(piano_keys[:5]) #......e
# print(piano_keys[2:5:2]) #c,e (skips 2s)
# print(piano_keys[::2]) #a,c,e,g (skips 2s)
# print(piano_keys[::-1]) #g,f,e,--- (reverses)
# # The above slicing method also works for turples 

# --------------Snake Game: Continuation-----------------#
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

scoreboard.game_over()
screen.exitonclick()
