from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.hideturtle()
        self.color("black")
        self.score=0
        self.goto(0,360)
        self.write(f"Score : {self.score}",align="center",font=("Arial", 20 , "normal"))
    def scoreup(self):
        self.clear()
        self.score+=1

        self.write(f"Score : {self.score}",align="center",font=("Arial", 20 , "normal"))

    
        