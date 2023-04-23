# ----------How to Open, Read, and Write to Files using the "with" Keyword---------------#
# Reading the file
# with open("./my_file.txt") as file:  # with keyword helps in opening and closing the file
#     contents = file.read()
#     print(contents)

# Writing to the existing file
# with open("my_file.txt", mode="a") as file:
#     # By default mode - r (read only)
#     # w - write (erases and writes new text)
#     # a - append (adds text to the existing)
#     file.write("\nMy text.")

# Writing to the non existing file - creates the file, mode has to always be w
# with open("new_file.txt", mode="w") as file:
#     file.write("\nMy text.")

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
        # game_is_on = False
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

# scoreboard.game_over()
screen.exitonclick()
