import turtle
from pad import Pad
from ball import Ball
import time
from score import Score
game_on=True
sc=turtle.Screen()

sc.title("Pong Game")
sc.setup(800,600)
sc.bgcolor("black")

    

pa_r=Pad(380)
pa_l=Pad(-380)
ball=Ball()
score=Score()


sc.listen()
sc.onkey(pa_r.up,"Up")
sc.onkey(pa_r.down,"Down")
sc.onkey(pa_l.up,"W")
sc.onkey(pa_l.down,"S")

while game_on:
    

    ball.move()
 
        
    sc.update()
    if ball.ycor()>=300 or ball.ycor() <= -300:
        ball.bounce_down()
    if ball.distance(pa_r) < 30 and ball.xcor() > 370 or ball.distance(pa_l)< 30 and ball.xcor() < -370 :
        ball.bounce_left()
        ball.speed()
    elif ball.xcor()>380 :
        score.change_score(1)
        ball.bounce_left()

        #sc.textinput("Round over","Left player got score " )

        ball.rego()
    elif  ball.xcor()<-380 :
        score.change_score(2)
        ball.bounce_left()

        #sc.textinput("Round over","Right player got score " )

        ball.rego()
    
    
    
  




sc.exitonclick()