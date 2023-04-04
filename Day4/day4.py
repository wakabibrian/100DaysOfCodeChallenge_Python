# -----------------Random Module-------------------#
# import random
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
# random_number = random.randint(0,1)

# if random_number == 0:
#     print("Heads")
# else:
#     print("Tails")

# -----------------Lists-------------------#
# A list is Data structure, its just a way of storing and organising data in Python,
# grouped pieces of data with a connection - Orderly; Order matters

# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine",
#                      "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# print(states_of_america[0])
# print(states_of_america[-1]) # Starts counting from the end of the list

# states_of_america[1] = "Pencilvania"
# states_of_america.append("Agelland") # Appending an item to the end of the list
# states_of_america.extend(["Wakaland", "Kayland", "Loylan"]) # Adding a list to a list
# print(states_of_america)

# Exercise
# You are going to write a program that will select a random name from a list of names.
# The person selected will have to pay for everybody's food bill.
# import random

# name_string = input("Give everybody's names sepparated by a comma: ")
# names = name_string.split(", ")

# rand_name_number = random.randint(0, len(names)-1)
# print(rand_name_number)

# random_person = names[rand_name_number]
# print(f"{random_person} is going to buy the meal today!")

# -----------------IndexErrors and Working with Nested Lists-------------------#
# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine",
#                     "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# number_of_states = len(states_of_america)
# print(states_of_america[number_of_states]) # Gives an index error, list index out of range

# Nested list, having list inside a list
# fruits = ["mango", "pineaple", "Ovacado", "Pear"]
# vegetables = ["Cabbages", "Spinachi", "Dodo"]

# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen[1][1]) #Prints Spinachi

####################### Exercise:Treasure Map
row1 = ['⬜', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
position_x = int(position[0]) - 1
position_y = int(position[1]) - 1
map[position_y][position_x] = "x"
print(f"{row1}\n{row2}\n{row3}")