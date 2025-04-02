from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0,260)
        self.penup()
        self.score1=0
        self.score2=0
        self.hideturtle()
        self.color("white")
        
        self.write((f"Score {self.score1} : {self.score2}") ,align="center",font=("Arial",22,"normal"))

    def change_score(self,x):

        self.clear()
        if x==1:
            self.score1+=1
        elif x==2:
            self.score2+=1
        self.write((f"Score {self.score1} : {self.score2}") ,align="center",font=("Arial",22,"normal"))

        

       