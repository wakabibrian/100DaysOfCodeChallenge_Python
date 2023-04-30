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
def my_function(a=1, b=2, c=3):
    pass


my_function()  # No need to provide the inputs in the function calls
# changing one of the default value, the rest take on the default values
my_function(b=5)
