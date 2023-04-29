# ------------------How to Create Lists using List Comprehension---------------------#
# This is unique to the Python language (only)
# List Comprehension: Is a case where you create a new list from the previous list

# Before
# numbers = [1, 2, 4, 6]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)

#
# new_list = [new_item for item in list]
# numbers = [1, 2, 4, 6]
# new_list = [n+1 for n in numbers]
# print(numbers)
# print(new_list)

# name = "Wakabi"
# letters_list = [letter for letter in name]
# print(letters_list)

# double_item = [number*2 for number in range(1, 5)]
# print(double_item)

# --- Conditional List Comprehension
# names = ["Alex", "Beth", "Wakabi", "Britney", "Dave", "Rose", "Maria"]
# short_names = [name for name in names if len(name) <= 4]
# print(short_names)

# long_names = [name.upper() for name in names if len(name) >= 5]
# print(long_names)

# ------------------Exercise 1: Squaring Numbers---------------------#
# You are going to write a List Comprehension to create a new list called squared_numbers.
# This new list should contain every number in the list numbers but each number should be squared.
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# squared_numbers = [number ** 2 for number in numbers]

# print(squared_numbers)

# ------------------Exercise 2: Filtering Even Numbers---------------------#
# You are going to write a List Comprehension to create a new list called result.
# This new list should only contain the even numbers from the list numbers.
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [number for number in numbers if number % 2 == 0]

print(result)
