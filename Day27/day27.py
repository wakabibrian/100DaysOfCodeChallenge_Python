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

# ------------Setting Default Values for Optional Arguments inside a Function Header----------#
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

# ----------Other Tkinter Widgets: Radiobuttons, Scales, Checkbuttons and more (All)----------#

# from tkinter import *

# # Creating a new window and configurations
# window = Tk()
# window.title("Widget Examples")
# window.minsize(width=500, height=500)

# # Labels
# label = Label(text="This is old text")
# label.config(text="This is new text")
# label.pack()

# # Buttons


# def action():
#     print("Do something")


# # calls action() when pressed
# button = Button(text="Click Me", command=action)
# button.pack()

# # Entries
# entry = Entry(width=30)
# # Add some text to begin with
# entry.insert(END, string="Some text to begin with.")
# # Gets text in entry
# print(entry.get())
# entry.pack()

# # Text
# text = Text(height=5, width=30)
# # Puts cursor in textbox.
# text.focus()
# # Adds some text to begin with.
# text.insert(END, "Example of multi-line text entry.")
# # Get's current value in textbox at line 1, character 0
# print(text.get("1.0", END))
# text.pack()

# # Spinbox


# def spinbox_used():
#     # gets the current value in spinbox.
#     print(spinbox.get())


# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()

# # Scale
# # Called with current scale value.


# def scale_used(value):
#     print(value)


# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()

# # Checkbutton


# def checkbutton_used():
#     # Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())


# # variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(
#     text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()

# # Radiobutton


# def radio_used():
#     print(radio_state.get())


# # Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1,
#                            variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2,
#                            variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()


# # Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))


# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
# window.mainloop()

# ---------------------Tkinter Layout Managers: pack(), place() and grid()-------------------#
# Pack - Packs each of the widgets next to each otherm (Starts from top) unless you change the side parameter
# Place - Precise positioning by providing x and y value (so specific, hard to work with)
# Grid - Uses columns and rows (Imagines  the entire program is divided in rows and columns) - Easy and flexible

# from tkinter import *


# def button_clicked():
#     new_text = input.get()
#     my_label.config(text=new_text)


# # Creating a window
# window = Tk()
# window.title("My first GUI program")
# window.minsize(width=500, height=300)
# window.config(padx=20, pady=20)

# # Label widget
# my_label = Label(text="I am a label", font=("Arial", 18, "bold"))
# my_label.config(text="New Text")
# # my_label.pack(side="left")
# # my_label.place(x=0, y=0)
# my_label.grid(column=0, row=0)
# my_label.config(padx=50, pady=50)

# # Button widget
# button = Button(text="Click me", command=button_clicked)
# # button.pack(side="left")
# button.grid(column=1, row=1)

# # New Button
# new_button = Button(text="New Button")
# # button.pack(side="left")
# new_button.grid(column=2, row=0)

# # Entry widget
# input = Entry(width=20)
# # input.pack(side="left")
# input.grid(column=3, row=2)

# # Keeping the window running
# window.mainloop()

# ---------------------Day 27 Project: Mile to Kilometers Converter-------------------#
from tkinter import *

FONT = ("Arial", 16, "normal")


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.60934, 2)
    km_results_label.config(text=km)


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=100, pady=100)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

equals_to_label = Label(text="is equal to", font=FONT)
equals_to_label.grid(column=0, row=1)

km_results_label = Label(text=f"{0}", font=FONT)
km_results_label.grid(column=1, row=1)

calculate_button = Button(text="Calculate", font=FONT, command=miles_to_km)
calculate_button.grid(column=1, row=2)

miles_input = Entry(width=10, font=FONT)
miles_input.grid(column=1, row=0)


window.mainloop()
