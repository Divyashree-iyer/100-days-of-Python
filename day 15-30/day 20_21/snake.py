from turtle import Turtle

MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
STARTINGPOSITION=[(0,0),(-20,0),(-40,0)]

class Snake:
    def __init__(self):
        self.turtles=[]
        self.create_snake()
        self.head=self.turtles[0]
        
    def create_snake(self):
        for position in STARTINGPOSITION:
            self.add_body(position)
    
    def add_body(self,position):
        turtle=(Turtle(shape="square"))
        turtle.color("white")
        turtle.penup()
        turtle.setposition(position)
        self.turtles.append(turtle)
     
    def extend(self):
        self.add_body(self.turtles[-1].position())
     
    def move(self):
        for number in range(len(self.turtles)-1,0,-1):
            x=self.turtles[number-1].xcor()
            y=self.turtles[number-1].ycor()
            self.turtles[number].goto(x,y) 
        self.head.forward(MOVE_DISTANCE)
        
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
        
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
                    
        
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
        
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
    
    def reset(self):
        for seg in self.turtles:
            seg.goto(1000,1000)
        self.turtles.clear()
        self.create_snake()
        self.head=self.turtles[0]
        
        
        
        
        
        
        
        
        