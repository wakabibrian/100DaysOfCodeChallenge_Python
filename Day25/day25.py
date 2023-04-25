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

import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])
