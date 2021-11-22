import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=800, height=700)
user_bet = screen.textinput(title="Make you bet", prompt="Which turtle will win the race? (red, black, green, "
                                                         "blue, gray, yellow, orange) Enter a color: ").lower()
color_list = ["red", "black", "green", "blue", "gray", "yellow", "orange"]
y_pos = [-300, -200, -100, 0, 100, 200, 300]
all_turtels = []

is_race_on = False


for turtle_index in range(0, 7):
    _turtle = Turtle(shape="turtle")
    _turtle.color(color_list[turtle_index])
    _turtle.penup()
    _turtle.goto(x=-350, y=y_pos[turtle_index])
    all_turtels.append(_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtels:
        random_disance = random.randint(0, 10)
        turtle.forward(random_disance)
        if turtle.xcor() > 350:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                is_race_on = False
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
                is_race_on = False




screen.exitonclick()