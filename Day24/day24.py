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

# -----------Write and remembering the highest score of the snake game--------------#


# from turtle import Screen
# from snake import Snake
# from food import Food
# from scoreboard import Scoreboard
# import time

# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# screen.title("My Snake Game")
# screen.tracer(0)

# snake = Snake()
# food = Food()
# scoreboard = Scoreboard()

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

#     # Detect collision with food
#     if snake.head.distance(food) < 15:
#         food.refresh()
#         snake.extend()
#         scoreboard.increase_score()

#     # Detect collision with wall
#     if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
#         # game_is_on = False
#         scoreboard.reset()
#         snake.reset()

#     # Detect collision with tail
#     for segment in snake.segments[1:]:
#         if snake.head.distance(segment) < 10:
#             scoreboard.reset()
#             snake.reset()

# # scoreboard.game_over()
# screen.exitonclick()

# ----------Understand Relative and Absolute File Paths---------------#
# On computers, files live within folders
# On windows, c is usually the root folder
# --- Absolute File Path might be
# c:
# c:/Work
# c:/Work/report.doc
# c:/Work/Project
# c:/Work/Project/talk.ppt #Navigated to file talk.ppt
# Absolute path always start off relative to the root

# --- Relative File Path might be
# Relative always start off from the Working Directory:
# Directory/Folder that we are currentltly working from
# If we are working from Project folder and talk.ppt is in the project folder
# The relative file path is: ./talk.ppt
# If we are in the Work folder, to get to talk.ppt: ./Project/talk.ppt
# But the absolute path doesnot change

# --- Going upwards in the folder tree
# To access report.doc if we are working in the project folder..
# ../report.doc
# for relative path, if the file is in the same folder; ./report.doc or report.doc
# Difference between Absolute and Relative: For absolute, it is relative to the root folder
# For Relative, it is relative to the current working directory
