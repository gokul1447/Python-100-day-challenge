from turtle import Turtle
import random
col = [
    "black", "red", "green", "blue", 
    "yellow", "cyan", "magenta", "gray", "brown"
]
class Car(Turtle):
    def __init__(self):
       

        super().__init__()
        self.shape("square")
        self.shapesize(1,3)
        self.color(random.choice(col))
        

        