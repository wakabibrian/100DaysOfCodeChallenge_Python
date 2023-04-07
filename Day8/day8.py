# -----------------Functions With inputs-------------------#
# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
# def greet():
#     print("Hello,")
#     print("My name is Wakabi Brian.")
#     print("How are you?")

# greet()

# Variable names inside () gives funtions inputs
# def greet_with_name(name):
#     print(f"Hello {name}") 
#     print(f"How do you do {name}?") 

# greet_with_name("Brian")

# Parament - name of variable
# Argument - the value passed to the variable when being called

# -----------------Funtions with more than 1 input, Positional vs Keyword arguments-------------------#
# def greet_with_name(name, location):
#     print(f"Hello, my name is {name}")
#     print(f"I am from {location}")

# greet_with_name("Wakabi", "Maganjo")

# The above are called positional arguments because they arguments are based on position of parameters
# Keyword arguments we assign values to variable names when calling the function, we dont mind about the position.

# greet_with_name(location="Kampala", name="Wakabi")

##### Exercise: Paint Area Calculator
# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. 
# Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
# number of cans = (wall height x wall width) ÷ coverage per can.
import math

def paint_calc(height, width, cover):
    numer_of_cans = math.ceil((height * width) / cover)
    print(f"You'll need {numer_of_cans} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

paint_calc(width=test_w, height=test_h, cover=coverage)