from tkinter import *

# --- Column Span Explanation
# window = Tk()

# r = Label(bg="red", width=20, height=5)
# r.grid(row=0, column=0)

# g = Label(bg="green", width=20, height=5)
# g.grid(row=1, column=1)

# b = Label(bg="blue", width=40, height=5)
# b.grid(row=2, column=0, columnspan=2)


# window.mainloop()

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)


# Entries
# Only one single absolute value for width is needed for the longest widget,
# (ie the Add button) and the other widgets will snap neatly in their positions.
# using sticky="EW"; EW part is the compass directions (E)ast and (W)est and
# the sticky basically "sticks" the widget to the edges of the column.
website_input = Entry()
website_input.grid(column=1, row=1, columnspan=2, sticky="EW")
email_username_input = Entry()
email_username_input.grid(column=1, row=2, columnspan=2, sticky="EW")
password_input = Entry()
password_input.grid(column=1, row=3, sticky="EW")

# Buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3, sticky="EW")
add_btn = Button(text="Add", width=35)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
