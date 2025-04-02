from turtle import Turtle,Screen


class Pad(Turtle):

    def __init__(self,x):
        super().__init__()
       
        self.penup()
        self.goto(x,0)
        self.color("white")
        self.shape("square")
        self.shapesize(5,1)


    def up(self):
        y=self.ycor()+30
        self.goto(self.xcor(),y)
        
        
    def down(self):
        y=self.ycor()-30
        self.goto(self.xcor(),y)




   

   


