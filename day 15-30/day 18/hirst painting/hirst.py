# import colorgram
# colors=colorgram.extract('hirst.jpg',20)
# rgb_c=[]
# for color in colors:
    # r=color.rgb.r
    # g=color.rgb.g
    # b=color.rgb.b
    # new_color=(r,g,b)
    # rgb_c.append(new_color)
# print(rgb_c)

from turtle import Turtle,Screen
import turtle as t
import random
timmy=Turtle()
timmy.hideturtle()
timmy.speed("fastest")

t.colormode(255)
colors=[(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71)]

for col in range(10):
    for row in range(10):
        color=random.randint(0,15)
        timmy.pendown()
        timmy.dot(20,colors[color])
        timmy.penup()
        timmy.forward(40)
        timmy.pendown()
        timmy.dot(20,colors[color])
        timmy.penup()
        
    if col%2==0:
        timmy.left(90)
        timmy.forward(40)
        timmy.left(90)
    else:
        timmy.right(90)
        timmy.forward(40)
        timmy.right(90)
        
        
    
screen=Screen()
screen.exitonclick()