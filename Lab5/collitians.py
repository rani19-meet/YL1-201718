from turtle import *
import random
import math
class Ball(Turtle):
    def __init__(self,radius,color,speed):
        Turtle.__init__(self)
        self.shape("circle")
        self.shapesize(radius)
        self.color(color)
        self.speed(speed)
def check_collision(ball1,ball2):
    radius1 = ball1.shapesize()[0]
    radius2 = ball2.shapesize()[0]
    if math.sqrt(math.pow((ball1.xcor()-ball2.xcor()),2)+ math.pow((ball1.ycor()-ball1.ycor(),2))<=ball1.shapesize()[0]+ball2.shapesize()[0]:
                 
            
        



    
