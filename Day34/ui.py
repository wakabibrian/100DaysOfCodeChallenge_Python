from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # labels
        self.score_label = Label(
            text="Score: 0", bg=THEME_COLOR, fg="White", font=("Arial", 12, "normal"))
        self.score_label.grid(column=1, row=0)

        # canvas
        self.canvas = Canvas(width=300, height=250,
                             bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150, 125, width=280, text="Quiz Question here", fill=THEME_COLOR, font=("Arial", 16, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # buttons
        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        self.true_button = Button(
            image=true_image, highlightthickness=0, borderwidth=0)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(
            image=false_image, highlightthickness=0, borderwidth=0)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
