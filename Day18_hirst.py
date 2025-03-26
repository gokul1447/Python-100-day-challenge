import turtle
import random

tl=turtle.Turtle()
sc=turtle.Screen()
common_colors = [
    "red",
    "blue",
    "green",
    "yellow",
    "orange",
    "purple",
    "black",
    "brown"
]
tl.speed(0)
sc.colormode(255)
sc.bgcolor(213,223,213)
tl.penup()
sc.setup(height=1000,width=1000)
tl.hideturtle()

y=-480
for i in range(1000):
    color=random.choice(common_colors)

    
    
    tl.fd(40)
    if i%26==0:
        
        tl.setpos(-485,y)
        y+=50
    tl.dot(20,color)
    


sc.exitonclick()
