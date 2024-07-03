from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong Game")

scoreboard=Scoreboard()

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))

ball=Ball()
  

screen.listen()

screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_on=True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    #detect collision with wall
    if ball.ycor()>=280 or ball.ycor()<=-280:
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()
    
    #detect paddle miss
    if ball.xcor()>380:
        scoreboard.l_inc()
        ball.reset_pos()
    elif ball.xcor()<-380:
        scoreboard.r_inc() 
        ball.reset_pos()
    
print("left score="+l_score)
print("right score="+r_score)
screen.exitonclick()