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
# Unlimited arguments
# args by convension - arguments
# def add(*args):
#     for n in args:
#         print(n)


# add(2, 4, 6, 7)

# --- Challenge
def add(*args):  # * puts any number of arguments in a tuple
    # You can either loop through them or use index
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(1, 2, 3, 4, 5, 6, 7))
