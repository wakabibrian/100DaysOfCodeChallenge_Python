# ---------------------History of GUI and Introduction to Tkinter-------------------#
# Tkinter inter can be used in creating Graphical User Interfaces
# GUI are different from using consoles

# ---------------------Creating Windows and Labels with Tkinter-------------------#
import tkinter

# Creating a window
window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# Creating a Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 18, "bold"))
my_label.pack(expand=True)


# Keeping the window running
window.mainloop()
