import time
import turtle
import random
import snake
import food
import scores

sc=turtle.Screen()
sc.setup(600,600)


sc.title("Snake Game")
sc.bgcolor("black")
sc.tracer(0)
snakes=snake.Snake()
food=food.Food()
score=scores.Score()

sc.listen()
sc.onkey(snakes.up,"Up")
sc.onkey(snakes.down,"Down")
sc.onkey(snakes.left,"Left")
sc.onkey(snakes.right,"Right")


is_on=True
while is_on:
    sc.update()
    time.sleep(0.05)
    snakes.move()
    if snakes.snake[0].distance(food)<15:
        snakes.cre_snake()
        food.refresh()
        score.change()
        snakes.extend()
        
    
   


    
   
     

sc.exitonclick()