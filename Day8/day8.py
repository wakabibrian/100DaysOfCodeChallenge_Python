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


def caesar(user_text, shift_amount, user_direction):

    new_text = ""
    if user_direction == "decode":
        shift_amount *= -1

    for char in user_text:
        # TODO-3: What happens if the user enters a number/symbol/space?
        # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        # e.g. start_text = "meet me at 3"
        # end_text = "•••• •• •• 3"
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            new_text += alphabet[new_position]
        else:
            new_text += char 

    print(f"The {user_direction}d text is {new_text}")
# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
end_program = False

while not end_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    # Try running the program and entering a shift number of 45.
    # Add some code so that the program continues to work even if the user enters a shift number greater than 26.
    # Hint: Think about how you can use the modulus (%).
    
    shift = shift % 26

    caesar(user_text=text, shift_amount=shift, user_direction=direction)

    cont_progam = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()

    if cont_progam == "no":
        end_program = True
        print("Good Bye")