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

# monday = data[data.day == "Monday"]
# # print(monday.condition)
# temp_cel = int(monday.temp[0])
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
# # data.to("new_data.csv")

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
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(
    title="Guess the state", prompt="What's another state's name?")

print(answer_state)

# ----- Getting the coordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
