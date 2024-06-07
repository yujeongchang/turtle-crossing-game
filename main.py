import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key= "Up", fun= player.move)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # creating cars should be controlled by throwing a dice. (Make the chance lower to 1/6)
    car_manager.create_car()
    # created cars need to be moved constantly.
    car_manager.move_cars()

    if player.is_at_finish_line():
        ## previous level should be deleted.
        player.go_to_start()
        scoreboard.increase_level()
        car_manager.increase_speed()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.gameover()


screen.exitonclick()