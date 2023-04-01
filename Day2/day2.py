# -----------------Primitive Data Types--------------------#
# Strings - string of characters ("")
# print("Hello"[0]) #Subscripting
# print("Hello"[4])
# print("Hello"[-1])
# print("123" + "456")

# Interger - Numbers without a decimal point - Whole numbers
# print(123 + 456)
# print(123_456_789) # For visualisation

# Float - Numbers with decimal places (Floating point number)
# print(45.67)

# Boolean
# It has two possible values; True or False

# -----------------Type Errors, Type Checking and Type Conversations--------------------#
# len(234) # Gives a TypeError

# num_char = len(input("What is your name? "))
# print("Your name has " + num_char + " characters") # Gives an error
# print(type(num_char)) # Type Checking

# Type convertion or type casting: changing a piece of data from one data type to another.
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters")

# print(70 + float("170.5"))

# Data Type Exercise
# Write a program that adds the digits in a 2 digit number.
# e.g. if the input was 35, then the output should be 3 + 5 = 8
# num = input("Type a two digit number: ")
# num1 = int(num[0])
# num2 = int(num[1])
# print(num1 + num2)

# -----------------Mathematical Operations--------------------#
# print(1 + 3)
# print(7 - 2)
# print(3 * 2)
# print(6 / 3)
# print(2**2)
# Use PEMDAS: for order of priority: (), **, *, /, +, -

# -----------------BMI Calculator Exercise--------------------#
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person 
    # and a short person both weigh the same amount, the short person is usually more overweight.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m)
# Warning you should convert the result to a whole number.

#Solution
height = float(input("Enter your height: "))
weight = int(input("Enter your weight: "))

bmi = int(weight/height**2) #PEMDAS
print(bmi)