#---------------Class Inheritance-----------------#
# Inheritance: is another feature of object oriented programming that is really helpful.
# Class Inheritance is the process of inheriting behaviours from an existing class 
# A class can inherit appearance; attributes and behaviour; methods
# Fish inheriting from the animal class
# class Fish(Animal):
    # def __init__(self):
    #     super().__init__() #Initialize everything that super class can do

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()
    
    def breathe(self):
        super().breathe()
        print("Doing this under water")

    def swim(self):
        print("moving in water.")

fish = Fish()
fish.swim()
fish.breathe()


# from turtle import Screen
# from snake import Snake
# import time

# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# screen.title("My Snake Game")
# screen.tracer(0)

# snake = Snake()

# screen.listen()
# screen.onkey(snake.up, "Up")
# screen.onkey(snake.down, "Down")
# screen.onkey(snake.left, "Left")
# screen.onkey(snake.right, "Right")

# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)

#     snake.move()


# screen.exitonclick()
