from tkinter import *

FONT = ("Arial", 10, "normal")


def save_data():
    website = website_input.get()
    email = email_username_input.get()
    password = password_input.get()

    with open("data.txt", "a") as passwords_file:
        passwords_file.write(f"{website} | {email} | {password}\n")

    website_input.delete(0, END)
    email_username_input.delete(0, END)
    password_input.delete(0, END)

    website_input.focus()


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
website_input.grid(column=1, row=1, columnspan=2, sticky="EW")
website_input.focus()
email_username_input = Entry(font=FONT)
email_username_input.grid(column=1, row=2, columnspan=2, sticky="EW")
email_username_input.insert(0, "wakabibrian95@gmail.com")
email_username_input.config()
password_input = Entry(font=FONT)
password_input.grid(column=1, row=3, sticky="EW")

# Buttons
generate_password_button = Button(text="Generate Password", font=FONT)
generate_password_button.grid(column=2, row=3, sticky="EW")
add_btn = Button(text="Add", width=35, font=FONT, command=save_data)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
