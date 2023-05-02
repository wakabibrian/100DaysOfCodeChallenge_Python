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

# ------------- Coding Exercise: IndexError Handling-------------#
# fruits = ["Apple", "Pear", "Orange"]

# # TODO: Catch the exception and make sure the code runs without crashing.


# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")


# make_pie(4)

# ------------- Coding Exercise: KeyError Handling-------------#
# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]

# total_likes = 0


# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError:
#         total_likes = total_likes + 0 # or pass

# print(total_likes)

# -------- Code Exercise: Exception Handling in the NATO Phonetic Alphabet Project---------#
# import pandas

# data = pandas.read_csv("nato_phonetic_alphabet.csv")
# phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

# error_exist = True

# while error_exist:
#     word = input("Enter a word: ").upper()

#     try:
#         output_list = [phonetic_dict[letter] for letter in word]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#     else:
#         error_exist = False

# print(output_list)

# --- Or
# def generate_phonetic():
#     word = input("Enter a word: ").upper()
#     try:
#         output_list = [phonetic_dict[letter] for letter in word]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#         generate_phonetic()
#     else:
#         print(output_list)


# generate_phonetic()

# -------------Day 30 Project: Improving Password Manager-------------#
# Write, read and update JSON data in the Password Manager
# JSON - JavaScript Object Notation.
# Most common form of transfering data over the internet
# Its composed of a bunch of nested lists and dictionaries
# It has the key-value pair data structure

# --- working with json in Python
# use inbuilt json library
# Write - json.dump()
# Read - json.load()
# Update - json.update()

from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip
import json

FONT = ("Arial", 10, "normal")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_input.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)

    # Pypthon pyperclip package, copies text to clipboard
    pyperclip.copy(password)
# ---------------------------- SEARCH ------------------------------- #


def find_password():
    website = website_input.get()

    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(
            title="Error", message="No Data File Found")
    else:
        if website in data:
            password = data[website]["password"]
            email = data[website]["email"]
            messagebox.showinfo(title=website_input.get(),
                                message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(
                title="Error", message=f"No Details for the {website} exists")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = website_input.get()
    email = email_username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        # Dialog Box: Mainly used for giving the user some feedback
        # messagebox is another module of code
        messagebox.showinfo(
            title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as passwords_file:
                # Reading old data
                data = json.load(passwords_file)
        except FileNotFoundError:
            with open("data.json", "w") as passwords_file:
                # saving the updated data
                json.dump(new_data, passwords_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as passwords_file:
                # saving the updated data
                json.dump(data, passwords_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
            website_input.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", font=FONT)
website_label.grid(column=0, row=1)
email_username_label = Label(text="Email/Username:", font=FONT)
email_username_label.grid(column=0, row=2)
password_label = Label(text="Password:", font=FONT)
password_label.grid(column=0, row=3)


# Entries
# Only one single absolute value for width is needed for the longest widget,
# (ie the Add button) and the other widgets will snap neatly in their positions.
# using sticky="EW"; EW part is the compass directions (E)ast and (W)est and
# the sticky basically "sticks" the widget to the edges of the column.
website_input = Entry(font=FONT)
website_input.grid(column=1, row=1, sticky="EW")
website_input.focus()
email_username_input = Entry(font=FONT)
email_username_input.grid(column=1, row=2, columnspan=2, sticky="EW")
email_username_input.insert(0, "wakabibrian95@gmail.com")
email_username_input.config()
password_input = Entry(font=FONT)
password_input.grid(column=1, row=3, sticky="EW")

# Buttons
generate_password_button = Button(
    text="Generate Password", font=FONT, command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="EW")
add_btn = Button(text="Add", width=35, font=FONT, command=save_data)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")
search_button = Button(text="Search", font=FONT, command=find_password)
search_button.grid(column=2, row=1, sticky="EW")

window.mainloop()
