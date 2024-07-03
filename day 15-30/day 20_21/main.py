from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time



screen=Screen()
screen.bgcolor("black")
screen.setworldcoordinates(-300, -300, 300, 300)
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()
screen.update()

screen.listen()
screen.onkey(fun=snake.up,key="Up")
screen.onkey(fun=snake.down,key="Down")
screen.onkey(fun=snake.left,key="Left")
screen.onkey(fun=snake.right,key="Right")

food=Food()
scoreboard=Scoreboard()
game_is_on=True

while game_is_on:
   
    screen.update()
    time.sleep(0.15)
    snake.move()
    #detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        snake.extend()
        food.refresh()
    if snake.head.xcor()>=300 or snake.head.xcor()<=-300:
            snake.head.goto(-snake.head.xcor(),snake.head.ycor())
    elif snake.head.ycor()>=300 or snake.head.ycor()<=-300:
            snake.head.goto(snake.head.xcor(),-snake.head.ycor())
    
    #detect collision with tail
    for turtle in snake.turtles[1:]:
        if snake.head.distance(turtle)<10:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()