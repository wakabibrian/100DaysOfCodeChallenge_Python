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
# number = int(input("Which number do you want to check? "))

# if number % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

# -----------------Nested if statements and elif statements--------------------#
# Nested if statemet: Once one condition is passed, we can check for another inside the if statement
# Another ifelse is inside the if statement
# if/elif/else: There are more than 1 conditions to check
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >120:
#     print("You can ride the rollcoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry you have to grow before you can ride.")

# Nested If Exercise: BMI2 Exercise
# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# It should tell them the interpretation of their BMI based on the BMI value.
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese

# Solution
# height = float(input("Enter height in m: "))
# weight = int(input("Enter weight in kg: "))
# bmi_float = weight / height ** 2
# bmi = round(bmi_float, 2)

# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#     print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi < 30:
#     print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi < 35:
#     print(f"Your BMI is {bmi}, you are obese.")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obese.")

# Nested If Exercise: Leap Year Exercise
# Write a program that works out whether if a given year is a leap year. 
# A normal year has 365 days, leap years have 366, with an extra day in February.

# This is how you work out whether if a particular year is a leap year.
#     on every year that is evenly divisible by 4 
#     **except** every year that is evenly divisible by 100 
#     **unless** the year is also evenly divisible by 400

# Solution:
# year = int(input("Which year do you want to check? "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap Year")
#         else:
#            print("Not Leap Year") 
#     else:
#         print("Leap Year")
# else:
#     print("Not Leap Year")

# -----------------Multiple if statement in succession--------------------#
# Checking multiple conditions even if the first one was true

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill =0

# if height >120:
#     print("You can ride the rollcoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print(f"Child tickets are for ${bill}.")
#     elif age <= 18:
#         bill = 7
#         print(f"Youth tickets are for ${bill}.")
#     else:
#         bill = 12
#         print(f"Adult tickets are for ${bill}.")

#     wants_photo = input("Do you want photo? Y or N: ")
#     if wants_photo == "Y":
#         bill += 3

#     print(f"Your total bill is ${bill}")
# else:
#     print("Sorry you have to grow before you can ride.")

#######Multiple if statements exercise
# Congratulations, you've got a job at Python Pizza. 
# Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill.
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

print("Welcome to Pyhton Pizza Deliveries!")
size = input("What size of Pizza do you want? S, M or L ")
want_pepperoni = input("Do you want Pepperoni? Y or N ")
want_extra_cheese = input("Do you want Extra Cheese? Y or N ")
final_bill = 0


if size == "S":
    final_bill += 15
elif size == "M":
    final_bill += 20
elif size == "L":
    final_bill += 25

if want_pepperoni == "Y":
    if size == "S":
        final_bill += 2
    else:
        final_bill += 3

if want_extra_cheese == "Y":
    final_bill += 1

print(f"Final bill is: ${final_bill}")









