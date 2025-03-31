import turtle
m=20
class Snake:
   
    def __init__(self):
        self.leng = 3
        
        self.snake=[]
        self.cre_snake()
        
    def increase(self,i):
       
        
        tl = turtle.Turtle()
        tl.shape("square")
        tl.penup()
        tl.color("white")

        if self.snake:  
            x, y = self.snake[-1].position()
        else:
            x, y = -20 * i, 0  

        tl.goto(x, y)
        self.snake.append(tl)
    
    def cre_snake(self):
        for i in range(self.leng):
            self.increase(i)

            
    def extend(self):
        last_segment = self.snake[-1]  # Get the last segment of the snake
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.penup()
        new_segment.color("white")
        
        # Place the new segment at the last segment's position
        new_segment.goto(last_segment.xcor(), last_segment.ycor())
        
        self.snake.append(new_segment)
    def move(self):
                        
       
                
        for i in range(len(self.snake)-1,0,-1):
            x=self.snake[i-1].xcor()
            y=self.snake[i-1].ycor()
            self.snake[i].goto(x,y)
        self.snake[0].forward(m)
        if self.snake[0].xcor()>=300 or self.snake[0].xcor()<=-300 or self.snake[0].ycor()>=300 or self.snake[0].ycor()<=-300:
            
            print("game over")
            self.snake[0].bye()
    def up(self):
        if self.snake[0].heading()!=270:


            self.snake[0].setheading(90)
    def down(self):
        if self.snake[0].heading()!=90:

            self.snake[0].setheading(270)
    def left(self):
        if self.snake[0].heading()!=0:

            self.snake[0].setheading(180)
    def right(self):
        if self.snake[0].heading()!=180:

            self.snake[0].setheading(0)