from turtle import Turtle
import random
import time
game_on=True
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x=3
        self.y=3
      
    def move(self):
       
        self.goto( self.xcor()+self.x,self.ycor()+self.y) 
    def bounce_down(self):
        self.y=-1*self.y
    def bounce_left(self):
        self.x=-1*self.x
    def rego(self):
        self.goto(0,0)
        time.sleep(1)
    def speed(self):
        self.x=1.3*self.x
        self.y=1.3*self.y
        

