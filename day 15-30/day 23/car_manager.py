import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        #super().__init__()
        self.all_cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE
        
    def generate_car(self):
        x=random.randint(0,10)
        if x%10==0:
            car=Turtle("square")
            car.shapesize(1,2,1)
            rand=random.choice(COLORS)
            car.color(rand)
            rand_x=280
            rand_y=random.randint(-250,250)
            car.penup()
            car.setpos(rand_x,rand_y)
            car.speed(3)
            self.all_cars.append(car)
    
    def speed_inc(self):
        self.car_speed+=MOVE_INCREMENT
            
    def move(self):
        for car in self.all_cars:
            car.goto(car.xcor()-self.car_speed,car.ycor())