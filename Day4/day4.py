# -----------------Random Module-------------------#
import random
# import my_module

# Module helps in splitting the code.
# Radom module holds functions for random numbers 

# random_integer = random.randint(1,10)
# print(random_integer)

# random_float = random.random()
# print(random_float*5)

# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")

# print(my_module.pi)

# Exercise
# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
random_number = random.randint(0,1)

if random_number == 0:
    print("Heads")
else:
    print("Tails")