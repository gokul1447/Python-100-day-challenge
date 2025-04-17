import turtle
import pandas as pd
sc=turtle.Screen()

is_on=True
sc.title("Guess the country")
img = "day-25-us-states-game-start/blank_states_img.gif"
sc.addshape(img)
turtle.shape(img)


data=pd.read_csv("day-25-us-states-game-start/50_states.csv")
# x=state["x"].tolist()
# y=state["y"].tolist()
name=data["state"].tolist()

guess=[]

while len(guess)<50:
    ans=sc.textinput(f"{len(guess)}/50 correct","whats the state name: ").title()

    if ans=="Exit":
        miss=[i for i in name if i not in guess]
       
        print(miss)
        data1=pd.DataFrame(miss)
        # data1.to_csv("missed_states")
        break
   
    if ans in name and ans not in guess:
        guess.append(ans)
        tl=turtle.Turtle()
        tl.hideturtle()
        tl.penup()
  
        
        state_data=data[data['state']==ans]
        tl.goto(state_data.x.item(),state_data.y.item())
        tl.write(ans)
    

sc.exitonclick()