import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

score = Scoreboard()
car_man = CarManager()
player = Player()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_man.create_cars()
    car_man.move_car()

    for car in car_man.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    if player.is_finish():
        player.go_to_start()
        car_man.level_up()
        score.increase_level()
screen.exitonclick()
