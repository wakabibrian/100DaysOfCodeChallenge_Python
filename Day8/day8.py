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


def encrypt(user_text, user_shift):
    cipher_text = ""

    for letter in user_text:
        position = alphabet.index(letter)
        new_position = position + user_shift
        cipher_text += alphabet[new_position]

    print(f"The encoded text is {cipher_text}")

# TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(encr_text, shift_amount):
    plain_text = ""

    for letter in encr_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]

    print(f"The decoded text is {plain_text}")

  # TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by 
  # the shift amount and print the decrypted text.
  # e.g.
  # cipher_text = "mjqqt"
  # shift = 5
  # plain_text = "hello"
  # print output: "The decoded text is hello"


# TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. 
# Then call the correct function based on that 'drection' variable. 
# You should be able to test the code to encrypt *AND* decrypt a message.

if direction == "encode":
    encrypt(user_text=text, user_shift=shift)
elif direction == "decode":
    decrypt(encr_text=text, shift_amount=shift)
