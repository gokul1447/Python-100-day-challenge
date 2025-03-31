from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score =0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.write(f"score:{self.score}",align="center",font = ("Arial",22,"normal"))
        
    def change(self):
        self.score+=1

        self.clear()
        self.write(f"score:{self.score}",align="center",font = ("Arial",22,"normal"))

