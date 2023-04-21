from turtle import Turtle, Screen

class Paddle(Turtle):

    def __init__(self, x_position, y_position):

        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.y_pos = y_position
        self.x_pos = x_position
        self.penup()
        self.goto(x=self.x_pos, y=self.y_pos)

    def move(self):
        screen = Screen()
        screen.listen()
        screen.onkey(fun=self.up, key="up")
        screen.onkey(fun=self.down, key="down")

    def up(self):
        self.forward(20)

    def down(self):
        self.forward(20)
