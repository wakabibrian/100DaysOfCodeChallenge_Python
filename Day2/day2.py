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

# Solution
# height = float(input("Enter your height: "))
# weight = int(input("Enter your weight: "))

# bmi = int(weight/height**2) #PEMDAS
# print(bmi)

# -----------------Number Manipulation and F Strings--------------------#
# Rounding Numbers
# print(round(3/2))
# print(round(8/3, 2))
# print(8//3) # Chops digits after a decimal point (Whole number)

#Number manipulation
# score = 0
# score += 1 # Same as score = score + 1; Also use s
# print(score)

# F strings
# print(f"Your score is {score}")

# -----------------Your life in Weeks Exercise--------------------#
# Create a program using maths and f-Strings that tells us how many days, 
    # weeks, months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x days, y weeks, and z months left.
# Where x, y and z are replaced with the actual calculated numbers.

# age = int(input("What is your current age? "))
# years_left = 90 - age
# months_left = years_left*12
# weeks_left = years_left*52
# days_left = years_left * 365

# message = f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left"
# print(message)

# -----------------Day 2 Project: Tip Calculator--------------------#
#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Solution
print("Welcome to the Tip Calculator")
total_bill = float(input("What's the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, 15? "))
total_people = int(input("How many people to split the bill? "))

total_bill_with_perc = total_bill + (total_bill*(percentage_tip/100))
tip_calc = (total_bill_with_perc / total_people)
tip_calc_rounded = round(tip_calc, 2)
message = f"Each person should pay: ${tip_calc_rounded}"
print(message)