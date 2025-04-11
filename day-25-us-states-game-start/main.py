import turtle
import pandas as pd
sc=turtle.Screen()
tl=turtle.Turtle()

sc.title("Guess the country")
img = "day-25-us-states-game-start/blank_states_img.gif"
sc.addshape(img)
turtle.shape(img)
ans=sc.textinput("Guess the state","whats the state name: ")

state=pd.read_csv("day-25-us-states-game-start/50_states.csv")
x=state["x"].tolist()
y=state["y"].tolist()
name=state["state"].tolist()

tl.shape("circle")
tl.shapesize(.5)

if ans=="Alabama" :
    tl.goto(x[0],y[0])










sc.mainloop()