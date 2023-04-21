from turtle import Turtle, Screen

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)

    def go_up(self):
        y_position = self.ycor() + 20
        self.goto(self.xcor(), y_position)


    def go_down(self):
        y_position = self.ycor() - 20
        self.goto(self.xcor(), y_position)
