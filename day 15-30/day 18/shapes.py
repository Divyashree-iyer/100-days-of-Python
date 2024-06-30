from turtle import Turtle,Screen
import random
timmy=Turtle()

def change_color():
    timmy.color(random.random(),random.random(),random.random())
    

sides=3
shapes=10
for shape in range(3,shapes+1):
    change_color()
    for side in range(sides):
        timmy.forward(40)
        timmy.right(360/sides)
    sides+=1
    
screen=Screen()
screen.exitonclick()