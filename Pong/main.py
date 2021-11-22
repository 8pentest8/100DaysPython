from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score

START_POSITION = [(580.0, 0.0), (-580.0, 0.0), (100.0, 100.0)]

r_paddle = Paddle(START_POSITION[0])
l_paddle = Paddle(START_POSITION[1])
#top_paddle = Paddle(START_POSITION[2])
ball = Ball()

score = Score()
screen = Screen()

screen.setup(width=1200, height=800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

screen.listen()
screen.onkey(r_paddle.go_left, "Left")
screen.onkey(r_paddle.go_right, "Right")
screen.onkey(l_paddle.go_left, "a")
screen.onkey(l_paddle.go_right, "d")
game_over = False


while not game_over:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 380 or ball.ycor() < -375:
        ball.bounce_y()
    if ball.distance(r_paddle) < 60 and ball.xcor() > 540 or ball.distance(l_paddle) < 60 and ball.xcor() < -540:
        ball.bounce_x()
    if ball.xcor() > 560:
        ball.reset_position()
        score.l_point()
    if ball.xcor() < -560:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
