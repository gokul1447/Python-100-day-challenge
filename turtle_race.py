import turtle
import random

sc=turtle.Screen()

# racer2=turtle.Turtle(shape="turtle")
# racer3=turtle.Turtle(shape="turtle")
# racer4=turtle.Turtle(shape="turtle")
# racer5=turtle.Turtle(shape="turtle")
# racer6=turtle.Turtle(shape="turtle")

turtles=[]
sc.setup(800,400)
color=["red","yellow", "orange","blue","pink"]
posi=[-100,-50,0,50,100]


sel_col=sc.textinput(title="Do you want bet",prompt="Which color will be win? Type the color")
for i in range(0,5):

    racer1=turtle.Turtle(shape="turtle")
    racer1.penup()
    
    
   
    racer1.goto(-370,posi[i])
    racer1.color(color[i])
    turtles.append(racer1)
    
if sel_col: 
    is_on=True

while is_on:
    for tur in turtles:
        if tur.xcor()>370:
            is_on=False
            print(f"The {tur.pencolor()} win the race")

        l=random.randint(0,10)
        tur.fd(l)

sc.exitonclick()    


