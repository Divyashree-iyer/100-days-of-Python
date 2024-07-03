from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score=0
        self.print_score()
        
    def print_score(self):
        self.clear()
        self.goto(-210,255)
        self.write("Level = "+str(self.score),align="center",font=FONT)
        
    def score_inc(self):
        self.score+=1
        self.print_score()
    
    def game_over(self):
        self.setpos(0,0)
        self.write("Game Over",align="center",font=FONT)