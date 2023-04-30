# ---------------------History of GUI and Introduction to Tkinter-------------------#
# Tkinter inter can be used in creating Graphical User Interfaces
# GUI are different from using consoles

# ---------------------Creating Windows and Labels with Tkinter-------------------#
# import tkinter

# # Creating a window
# window = tkinter.Tk()
# window.title("My first GUI program")
# window.minsize(width=500, height=300)

# # Creating a Label
# my_label = tkinter.Label(text="I am a label", font=("Arial", 18, "bold"))
# my_label.pack(expand=True)


# # Keeping the window running
# window.mainloop()

# ---------------------Setting Default Values for Optional Arguments inside a Function Header-------------------#
# Using Advanced Python Arguments inorder to specify a wider range of inputs
# Arguments with default values
# def my_function(a=1, b=2, c=3):
#     pass


# my_function()  # No need to provide the inputs in the function calls
# # changing one of the default value, the rest take on the default values
# my_function(b=5)

# ---------------------*args: Many Positional Arguments-------------------#
# * working with Unlimited positional arguments
# args by convension - arguments
# def add(*args):
#     for n in args:
#         print(n)


# add(2, 4, 6, 7)

# --- Challenge
# def add(*args):  # * puts any number of positional arguments in a tuple
#     # You can either loop through them or use index
#     sum = 0
#     for n in args:
#         sum += n
#     return sum


# print(add(1, 2, 3, 4, 5, 6, 7))

# ---------------------**kwargs: Many Keyword Arguments-------------------#
# ** helps in working with arbitrary number of keyword arguments
# def calculate(n, **kwargs):
#     print(kwargs)  # ** puts any number of keyword arguments in a dictionary
#     # Accessing
#     # for key, value in kwargs.items():
#     #     print(f"{key}: {value}")

#     # Alternatively
#     # print(kwargs["add"])

#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)


# calculate(2, add=3, multiply=5)

# ---------------------Back to tkinter module-------------------#
# Reason why there are no options when we call the methods is because they used unlimited
# keyword argurments (kwargs)

# How to create classes with unlimited arguments
# class Car:
#     def __init__(self, **kw):
#         self.make = kw.get("make")
#         self.model = kw.get("model")
#         self.color = kw.get("color")
#         self.size = kw.get("size")


# my_car = Car(model="Haria")
# print(my_car.make)  # Returns none
# print(my_car.model)

# ---------------------Buttons, Entry, and Setting Component Options-------------------#
# from tkinter import *

# # Creating a window
# window = Tk()
# window.title("My first GUI program")
# window.minsize(width=500, height=300)

# # Creating a Label Component
# my_label = Label(text="I am a label", font=("Arial", 18, "bold"))
# my_label.pack()

# # Updating properties
# my_label["text"] = "New Text"
# # my_label.config(text="New Text")


# # Creating a Button Component


# def button_clicked():
#     new_text = input.get()
#     my_label.config(text=new_text)


# button = Button(text="Click me", command=button_clicked)
# button.pack()

# # Creating Entry component (input)
# input = Entry(width=20)
# input.pack()

# # Keeping the window running
# window.mainloop()
