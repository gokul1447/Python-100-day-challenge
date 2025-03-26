import turtle

tl=turtle.Turtle()
sc=turtle.Screen()
def mov():
    tl.fd(100)

sc.listen()
sc.onkey(fun=mov,key="space")

sc.exitonclick()