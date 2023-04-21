from turtle import Turtle, Screen

screen = Screen()
screen.title("Wakabi Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_len=1, stretch_wid=5)
paddle.penup()
paddle.goto(350, 0)


def go_up():
    y_position = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), y_position)


def go_down():
    y_position = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), y_position)


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()
