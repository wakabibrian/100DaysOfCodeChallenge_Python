# -----------------Functions with Outputs-------------------#
# They allow you to have an output once a function is completed
# def my_function():
#     return 3*2

# output = my_function()
# print(output)

# def format_name(f_name, l_name):
#     first_name = f_name.title()
#     last_name = l_name.title()

#     return f"{first_name} {last_name}"

# formated_name = format_name("WaKABi", "brian")
# print(formated_name)

# -----------------Multiple return values-------------------#
# Return statement tells that its the end of the program hence exit
# Statements after the return statement will not be exexuted
# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "You didn't provide valid inputs"

#     first_name = f_name.title()
#     last_name = l_name.title()
#     return f"{first_name} {last_name}"

# formated_name = format_name(input("Enter first name: "), input("Enter first name: "))
# print(formated_name)

# Exercise: Days in a month
# In the starting code, you'll find the solution from the Leap Year challenge.
# First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year."
# it should return True if it is a leap year and return False if it is not a leap year.

# You are then going to create a function called days_in_month() which will take a year and a month as inputs, e.g.
# days_in_month(year=2022, month=2)

# And it will use this information to work out the number of days in the month, then return that as the output, e.g.:
# 28

# The List month_days contains the number of days in a month from January to December for a non-leap year.
# A leap year has 29 days in February.

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                return False
#         else:
#             return True
#     else:
#         return False

# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     leap_year = is_leap(year)

#     if month > 12 or month < 1:
#         return "Invalid month"
#     elif leap_year and month == 2:
#         return 29
#     else:
#         return month_days[month-1]

# #🚨 Do NOT change any of the code below
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

# -----------------Docstrings-------------------#
# Docstrings help us to create documentation as we are coding along in our functions or in other blocks of code
# Forexample it helps to tell what the function is going to do (When you call the function)
# Docstrings has to go as the first line after the declaration
# You use 3 quotation marks

# def format_name(f_name, l_name):
#     """ Takes a first and last name and fomart it to return the title case version of the name"""

#     if f_name == "" or l_name == "":
#         return "You didn't provide valid inputs"

#     first_name = f_name.title()
#     last_name = l_name.title()
#     return f"{first_name} {last_name}"

# formated_name = format_name(input("Enter first name: "), input("Enter first name: "))
# print(formated_name)

# -----------------Day 10 Project: Calculator-------------------#
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = int(input("What's the first number?: "))

for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number?: "))

calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")
