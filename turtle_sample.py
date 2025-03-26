from turtle import Screen, Turtle
import random 


tl=Turtle()
colors = [
    "red",
    "blue",
    "green",
    "yellow",
    "orange",
    "purple",
    "pink",
    "brown",
    "black",
    "gray",
    "cyan",
    "magenta"
]

sc=Screen()
lis=["right","backward","left"]
tl.pensize(10)
for i in range(15):
    ang=random.choice(lis)
    cl=random.choice(colors)
    tl.color(cl)

    tl.fd(50)

    if ang=="right":
        tl.right(90)
    if ang=="left":
        tl.left(90)
    if ang=="backward":
        tl.backward(50)




sc.exitonclick()