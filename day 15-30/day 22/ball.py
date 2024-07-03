from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.xmove=2
        self.ymove=2
        self.move_speed=0.01
        
    def move(self):
        self.goto(self.xcor()+self.xmove,self.ycor()+self.ymove)
       
    def bounce_y(self):
        self.ymove*=-1
       
    def bounce_x(self):
        self.xmove*=-1
        self.move_speed*=0.9
        
    def reset_pos(self):
        self.setposition(0,0)
        self.move_speed=0.1
        self.bounce_x()
        