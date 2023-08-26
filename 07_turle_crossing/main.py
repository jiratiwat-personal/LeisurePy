import time
from turtle import Screen
from player import Player
from car_manager import CarManager
import car_manager
from scoreboard import Scoreboard
import random

current_speed = car_manager.STARTING_MOVE_DISTANCE
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
cars = []


player = Player()

screen.listen()
screen.onkey(player.move, "Up")


def set_cars_speed():
    for car in cars:
        car.set_speed(current_speed)

def cars_move():
    for car in cars:
        car.move()


def check_finish_line():
    # global declaration is needed when modifying the parameter outside the scope
    global current_speed
    if player.ycor() == 280:
        player.setpos(0, -280)
        scoreboard.levelup()
        current_speed += car_manager.MOVE_INCREMENT
        set_cars_speed()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    cars_move()
    check_finish_line()
    # generate new car every 6th count
    if random.randint(1, 6) == 6:
        cars.append(CarManager(current_speed))
    # check crash
    for car in cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.gameover()
    screen.update()


screen.exitonclick()
