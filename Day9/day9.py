# -----------------Python Dictionary-------------------#
# Dictionaries allow us to group together and tag related pieces of information
# Dictionaries have a key and value
# {key: value}

# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
# }

# Retrieving items from a dictionary
# print(programming_dictionary["Bug"])

# You can also use numbers as keys

# Adding items to dictionary
# programming_dictionary["Loop"] = "The action of doing something over and over again"

# # Wipe an existing Diciction
# # programming_dictionary = {}
# # print(programming_dictionary)

# # Editing an item in a dictionary
# programming_dictionary["Bug"] = "An error in code"
# # print(programming_dictionary)

# # Looping through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

# Exercise: Grading program
# Write a program that converts their scores to grades.
# By the end of your program, you should have a new dictionary called student_grades
# that should contain student names for keys and their grades for values.
# The final version of the student_grades dictionary will be checked.

# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"

# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }

# student_grades = {}

# for student in student_scores:

#     score = student_scores[student]

#     if score >= 91:
#         student_grades[student] = "Outstanding"
#     elif score >= 81:
#        student_grades[student] = "Exceeds Expectations"
#     elif score >= 71:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"

# print(student_grades)

# -----------------Nesting Lists and Dictionaries-------------------#
# {
#     key: [list],
#     key2: {dict},
# }

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hmburg", "Stuttgart"],
        "total_visits": 5
    }
]
