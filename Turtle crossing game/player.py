from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()

      


        self.penup()
        self.shape("turtle")
        self.goto(0,-370)
        self.color("black")
        self.left(90)
        self.shapesize(1.5,1.5)
    def up(self):
        self.fd(10)
    def down(self):
        self.backward(10)