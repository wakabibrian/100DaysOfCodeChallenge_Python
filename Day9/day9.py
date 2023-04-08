# -----------------Python Dictionary-------------------#
# Dictionaries allow us to group together and tag related pieces of information
# Dictionaries have a key and value
# {key: value}

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieving items from a dictionary
# print(programming_dictionary["Bug"])

# You can also use numbers as keys

# Adding items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"

# Wipe an existing Diciction
# programming_dictionary = {}
# print(programming_dictionary)

# Editing an item in a dictionary
programming_dictionary["Bug"] = "An error in code"
# print(programming_dictionary)

# Looping through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


