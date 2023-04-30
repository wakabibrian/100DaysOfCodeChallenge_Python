# ------------------How to Create Lists using List Comprehension---------------------#
# This is unique to the Python language (only)
# List Comprehension: Is a case where you create a new list from the previous list

# Before
# numbers = [1, 2, 4, 6]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)

#
# new_list = [new_item for item in list]
# numbers = [1, 2, 4, 6]
# new_list = [n+1 for n in numbers]
# print(numbers)
# print(new_list)

# name = "Wakabi"
# letters_list = [letter for letter in name]
# print(letters_list)

# double_item = [number*2 for number in range(1, 5)]
# print(double_item)

# --- Conditional List Comprehension
# names = ["Alex", "Beth", "Wakabi", "Britney", "Dave", "Rose", "Maria"]
# short_names = [name for name in names if len(name) <= 4]
# print(short_names)

# long_names = [name.upper() for name in names if len(name) >= 5]
# print(long_names)

# ------------------Exercise 1: Squaring Numbers---------------------#
# You are going to write a List Comprehension to create a new list called squared_numbers.
# This new list should contain every number in the list numbers but each number should be squared.
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# squared_numbers = [number ** 2 for number in numbers]

# print(squared_numbers)

# ------------------Exercise 2: Filtering Even Numbers---------------------#
# You are going to write a List Comprehension to create a new list called result.
# This new list should only contain the even numbers from the list numbers.
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [number for number in numbers if number % 2 == 0]

# print(result)

# ------------------Exercise 3: Data Overlap---------------------#
# Take a look inside file1.txt and file2.txt.
# They each contain a bunch of numbers, each number on a new line.

# You are going to create a list called result which contains the numbers
# that are common in both files.

# with open("file1.txt") as file1:
#     file_data1 = file1.readlines()

# with open("file2.txt") as file2:
#     file_data2 = file2.readlines()

# result = [int(num) for num in file_data1 if num in file_data2]
# print(result)

# ------------------How to use Dictionary Comprehension---------------------#
# new_dict = {new_key: new_value for item in list}
# new_dict = {new_key: new_value for (key, value) in dict.items()}
# new_dict = {new_key: new_value for (key, value) in dict.items() if test}
# import random
# names = ["Brian", "Alex", "Britney", "Loyce", "Beth", "Joel"]
# new_dict = {name: random.randint(1, 100) for name in names}

# passed_students = {name: mark for (
#     name, mark) in new_dict.items() if mark >= 60}

# print(passed_students)

# ------------------Dictionary Comprehension Exercise 1---------------------#
# You are going to use Dictionary Comprehension to create a dictionary called result
# that takes each word in the given sentence and calculates the number of letters in each word.
# Try Googling to find out how to convert a sentence into a list of words

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆

# # Write your code below:
# result = {word: len(word) for word in sentence.split()}

# print(result)

# ------------------Dictionary Comprehension Exercise 2---------------------#
# You are going to use Dictionary Comprehension to create a dictionary called weather_f
# that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆


# # Write your code 👇 below:
# weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}

# print(weather_f)

# ------------------How to Iterate over a Pandas DataFrame---------------------#

# import pandas
# student_dict = {
#     "student": ["Wakabi", "Britney", "Keylah"],
#     "score": [90, 65, 78]
# }

# # Before
# for (key, value) in student_dict.items():
#     print(f"{key}: {value}")


# student_data_frame = pandas.DataFrame(student_dict)
# # print(student_data_frame)

# # Loop through the rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # print(row.student)
#     # print(row.score)
#     if row.student == "Britney":
#         print(row.score)
