# -----------------Printing - print() function--------------------#
# print("Hello World!") #Use the print() function to print to console

# Printing Exercise
# Write a Python code which prints the lines as below
###########
# Day 1 - Python Print Function
# The function is declared like this:
# print('what to print')
############
# print("Day 1 - Python Print Function")
# print("The function is declared like this:")
# print("print('what to print')")

# -----------------Separating string lines using \n--------------------#
# print("This is the first line.\nThis is the second line.")

# -----------------String concatenation with +--------------------#
# print("Hello" + " Wakabi")

# -----------------Input Function--------------------#
# Used for getting inputs from the user
# print("Hello " + input("What is your name? "))

# Input Exercise
# Write a program that prints the number of characters in a user's name.
# You might need to Google for a function that calculates the length of a string.

# print(len(input("What is your name? ")))

# -----------------Variables--------------------#
# Variables are responsible for storing  pieces of data
# It can be changed
# Varible names should have a meaning
# Dont use keywords
# Dont start with a number
# No space within  multiword variables (Use underscore)

# name = input("What is your name? ")
# print(name)

# Variables Exercise
# Write a program that switches the values stored in the variables a and b.

# a = input("a: ")
# b = input("b: ")

# temp = a
# a = b
# b = temp

# print("a: " + a)
# print("b: " + b)

# -----------------Day 1--------------------#
# Day 1 Project: Band Name Generator
# 1. Create a greeting for your program.
# 2. Ask the user for the city that they grew up in.
# 3. Ask the user for the name of a pet.
# 4. Combine the name of their city and pet and show them their band name.
# 5. Make sure the input cursor shows on a new line:

# Solution
print("Welcome to the Band Name Generator")
city = input("What is the name of the city you grew up in?\n")
pet = input("What is your pet's name?\n")
print("Your Brand Name could be " + city + " " + pet)
