from turtle import Turtle
import random
col = [
    "black", "red", "green", "blue", 
    "yellow", "cyan", "magenta", "gray", "brown"
]
# pos_y = []
# while len(pos_y) < 5:  
#     new_y = random.randint(-330, 380)
#     if all(abs(new_y - y) > 40 for y in pos_y):  
#         pos_y.append(new_y)


class Car():
    def __init__(self):
        
        self.all_cars=[]
        self.carspeed=5
        
    def create_car(self):
        a=random.randint(1,7)

        if a==3:

            new_car=Turtle()


            new_car.penup()
            new_car.shape("square")
            
            new_car.shapesize(1,3)
            new_car.color(random.choice(col))
            new_car.goto(520,random.randint(-330,360))
            self.all_cars.append(new_car)
            
        

    def move(self):
        for car in self.all_cars:
            car.backward(self.carspeed)
    def speed(self):
        self.carspeed+=15

    
        

        