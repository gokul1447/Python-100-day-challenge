import turtle
from car import Car
import score
import time
import random
import player
sc=turtle.Screen()
game_on=True
sc.setup(1000,800)
sc.tracer(0)

sc.bgcolor("white")
sc.title("Turtle Crossing game")

player=player.Player()
car=Car()



score=score.Score()
sc.listen()
sc.onkey(player.up,"Up")
sc.onkey(player.down,"Down")


while game_on:
    time.sleep(0.1)
    

    sc.update()
    car.create_car()
    car.move()
    for i in car.all_cars:
        if player.distance(i) < 30 :
            print("game over")
            game_on=False
        elif player.ycor()>380 :
            player.goto(0,-370)
            score.scoreup()
            car.speed()

    
    



sc.exitonclick()