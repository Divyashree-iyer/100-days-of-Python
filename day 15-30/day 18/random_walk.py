from turtle import Turtle,Screen
import random
timmy=Turtle()

def change_color():
    timmy.color(random.random(),random.random(),random.random())
    
timmy.speed("fastest")

for i in range(360):
    change_color()
    timmy.circle(100,None, 100)
    timmy.right(1)

    
screen=Screen()
screen.exitonclick()