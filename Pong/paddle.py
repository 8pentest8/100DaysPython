import turtle
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=8, stretch_len=2)
        self.color("white")
        self.goto(position)

    def go_left(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)

    def go_right(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)


