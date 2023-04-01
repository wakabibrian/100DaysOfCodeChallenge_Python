# -----------------Control Flow with if/else and conditional operators--------------------#
# Conditional if/else: Doing A or B depending on a condition
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >120:
#     print("You can ride the rollcoaster!")
# else:
#     print("Sorry you have to grow before you can ride.")

# Comparison Operators
# >, <, >=, <=, ==, !=

# Control Flow & Conditionals Exercise
# Write a program that works out whether if a given number is an odd or even number.
# Even numbers can be divided by 2 with no remainder.
number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")