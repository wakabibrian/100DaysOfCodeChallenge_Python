# ----------------Reading CSV Data in Python----------------#
# CSV - Comma Separated Values
# Each row is a single piece of data
# Each piece of data is separated by a comma without space

# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)

#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# ----------------Pandas Library----------------#
# It is Python's Data Analysis Library
# For performing analysis on tabular data

# ----------------DataFrames & Series: Working with Rows & Columns----------------#
# import turtle
# import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
# print(type(data)) - Data frame (Whole sheet)
# print(type(data["temp"])) - Series (single column)
# panda_dict = data.to_dict()
# temps = data["temp"].to_list()
# sum = 0
# print(panda_dict)
# print(list)

# for temp in temps:
#     sum += temp

# average_temp = sum/len(temps)
# print(average_temp)

# average = data["temp"].mean()
# print(average)

# maximum = data["temp"].max()
# print(maximum)

# print(data.condition)

# ---Data in rows
# print(data[data["day"] == "Monday"])

# maximum = data["temp"].max()
# print(data[data["temp"] == maximum])

# monday = data[data.day == "Wednesday"]
# print(monday)
# print(monday.condition)
# temp_cel = monday.temp[0]
# # (0°C × 9/5) + 32
# temp_fer = (temp_cel * (9/5)) + 32
# print(temp_fer)

# --- Creating a DataFrame from scratch
# data_dict = {
#     "students": ["Amy", "Brian", "Britney"],
#     "scores": [70, 95, 62]
# }

# data = pandas.DataFrame(data_dict)
# print(data)
# # data.to_csv("new_data.csv")

# ----------------The Great Squirrel Census Data Analysis (with Pandas!)----------------#
# import pandas

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# # Option 1
# # squirrel_colors_list = data["Primary Fur Color"].to_list()
# # black = squirrel_colors_list.count("Black")
# # gray = squirrel_colors_list.count("Gray")
# # cinnamon = squirrel_colors_list.count("Cinnamon")

# # Option 2
# black = len(data[data["Primary Fur Color"] == "Black"])
# cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
# gray = len(data[data["Primary Fur Color"] == "Gray"])

# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [gray, cinnamon, black]
# }

# squirrel_color_data = pandas.DataFrame(data_dict)

# squirrel_color_data.to_csv("squirrel_color.csv")

# ----------------Day 25 Project: U.S. States Game----------------#
import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
correct_guesses = []

t = turtle.Turtle()

while len(correct_guesses) <= 50:
    answer_state = screen.textinput(
        title=f"{len(correct_guesses)}/50 Guess the state", prompt="What's another state's name?").title()

    data = pandas.read_csv("50_states.csv")
    state_list = data.state.to_list()

    if answer_state == "Exit":

        not_guessed = [
            state for state in state_list if state not in correct_guesses]

        new_data = pandas.DataFrame(not_guessed)
        new_data.to_csv("states_to_learn.csv")

        for state in not_guessed:
            not_guessed_state = data[data.state == state]
            x_coor = not_guessed_state.x[state_list.index(state)]
            y_coor = not_guessed_state.y[state_list.index(state)]

            t.hideturtle()
            t.color("red")
            t.penup()
            t.goto(x_coor, y_coor)
            t.write(state)

        break

    if answer_state in state_list and answer_state not in correct_guesses:
        correct_guesses.append(answer_state)

        guessed_state = data[data.state == answer_state]
        x_coor = guessed_state.x[state_list.index(answer_state)]
        y_coor = guessed_state.y[state_list.index(answer_state)]

        t.hideturtle()
        t.penup()
        t.goto(x_coor, y_coor)
        t.write(answer_state)

screen.exitonclick()

# ----- Getting the coordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
