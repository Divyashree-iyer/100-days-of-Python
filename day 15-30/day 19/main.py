from turtle import Screen, Turtle
from random import randint

race_on=False
screen=Screen()
screen.screensize(500,400)
user_guess=screen.textinput(title="Make your bet", prompt="Choose who wins. VIBGYOR")

colors=["violet","indigo","blue","green","yellow","orange","red"]
timmy=[]
pos=200/7
for i in range(0,7):
    timmy.append(Turtle(shape="turtle"))
    timmy[i].penup()
    timmy[i].color(colors[i])
    timmy[i].goto(x=-220,y=-100+33*i)
   
  
if user_guess:
    race_on=True
    
while race_on:
    for tim in timmy:
        if tim.xcor()>250:
            race_on=False
            wins=tim.pencolor()
            print(f"{wins} wins")
            break
        tim.forward(randint(10,20))

if wins==user_guess:
    print("you win")
else:
    print("you lose")
screen.exitonclick()

