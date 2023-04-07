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

# Exercise: Paint Area Calculator
# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall.
# Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
# number of cans = (wall height x wall width) ÷ coverage per can.
# import math

# def paint_calc(height, width, cover):
#     numer_of_cans = math.ceil((height * width) / cover)
#     print(f"You'll need {numer_of_cans} cans of paint.")

# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5

# paint_calc(width=test_w, height=test_h, cover=coverage)

# Exercise: Prime  Number Checker
# A prime number is a number that is only divisible by 1 and its self
# You need to write a function that checks whether if the number passed into it is a prime number or not.

# def prime_checker(number):

#     is_prime = True

#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False

#     if is_prime:
#         print("It's a prime number")
#     else:
#         print("It's a not prime number")


# n = int(input("Check this number: "))
# prime_checker(number=n)

# -----------------Day 8 Project: Caesar Cipher (Encoding Text)-------------------#
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().


def caesar(user_text, shift_amount, user_direction):

    new_text = ""

    if user_direction == "decode":
        shift_amount = -shift_amount

    for letter in user_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_text += alphabet[new_position]

    if user_direction == "encode":
        print(f"The encoded text is {new_text}")
    elif user_direction == "decode":
        print(f"The decoded text is {new_text}")

# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(user_text=text, shift_amount=shift, user_direction=direction)