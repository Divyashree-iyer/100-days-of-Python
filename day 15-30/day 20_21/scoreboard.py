from turtle import Turtle
ALIGNMENT="center"
FONT=("Courier",12,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as file:
            self.highscore=int(file.read())
        self.print_score()
        
    def print_score(self):
        self.clear()
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.write(arg=f"Score: {self.score}, High score: {self.highscore}",move=False, align=ALIGNMENT, font=FONT)
        self.hideturtle()
        
    def increase_score(self):
        self.score+=1
        self.print_score()
        
    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("data.txt",mode="w") as file:
                file.write(str(self.highscore))
        self.score=0
        self.print_score()    

    # def game_over(self):
        # self.goto(0,0)
        # self.write(arg=f"GAME OVER",move=False, align=ALIGNMENT, font=FONT)