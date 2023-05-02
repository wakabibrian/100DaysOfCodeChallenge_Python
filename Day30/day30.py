# -------------Catching Exceptions: The try catch except finally Pattern-------------#
# FileNotFound aerror
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existence_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

# --- Catching Exceptions
# When something goes wrong, we catch that exception in that moment
# try:
#     # Executing something that might cause an exception (might work and might not)

# except:
#     # Do this if there was an exception (failed)

# else:
#     # Do this if there were no exceptions (didnt fail/succeeded)

# finally:
#     # Do this no matter what happens (failed or succeeded).
#     # Usually used for cleaning things up at the end of code execution

# --- Catching exceptions example
# try:
#     file = open("a_file.txt")
#     dict = {"key": "value"}
#     print(dict["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:  # Not often used
#     file.close()
#     print("File was closed")

# ------------- Raising your own Exceptions-------------#
# You can raise your own exceptions incase your code encounters an expected situations
# raise keyword: helps us to raise our own exceptions
# try:
#     file = open("a_file.txt")
#     dict = {"key": "value"}
#     print(dict["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error I made up")

# --- When to raise errors?
# # Perfect code but going to raise the wrong result
# height = float(input("Height: "))
# weight = int(input("Weight: "))

# if height > 3:
#     # ValueError: whatever value that was entered as argument was wrong
#     raise ValueError("Human height should not be over 3 meters")

# bmi = weight / height**2
# print(bmi)
