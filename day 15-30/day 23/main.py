import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Game")
screen.tracer(0)

player=Player()

screen.listen()
screen.onkey(player.move, "Up")

car_manager=CarManager()

scoreboard=Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.generate_car()
    car_manager.move()
    
    if player.finish():
        scoreboard.score_inc()
        car_manager.speed_inc()
        player.start()
      
    for car in car_manager.all_cars:
        if car.distance(player)<20:
            scoreboard.game_over()
            game_is_on=False

screen.exitonclick()