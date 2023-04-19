from turtle import Turtle 
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):
    
    def __init__(self):
        self.score = 0
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)

    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

