from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526,
                highlightthickness=0, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=front_img)
canvas.create_text(400, 156, text="French", font=("Arial", 30, "italic"))
canvas.create_text(400, 263, text="trouve", font=("Arial", 50, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# buttons
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

right_button = Button(image=right_img, highlightthickness=0)
right_button.grid(column=1, row=1)
wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(column=0, row=1)

window.mainloop()
