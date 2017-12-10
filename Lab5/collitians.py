from turtle import *
import random
import math
class Ball(Turtle):
    def __init__(self,radius,color,speed):
        Turtle.__init__(self)
        self.shape("circle")
        self.shapesize(radius)
        self.radius = radius
        self.color(color)
        self.speed(speed)
#def check_collision(ball1,ball2):
    #radius1 = ball1.shapesize()[0]
    #radius2 = ball2.shapesize()[0]
    #if math.sqrt(math.pow((ball1.xcor()-ball2.xcor()),2)+ math.pow((ball1.ycor()-ball2.ycor()),2))<=ball1.shapesize()[0]+ball2.shapesize()[0]:
        #ball1.shapesize(50)
        #ball2.shapesize(25)
           
ball1=Ball(20,"red",5)
ball2=Ball(15,"blue",10)
#check_collision(ball1,ball2)
new_list=[ball1,ball2]

def function(new_list):
    if math.sqrt(math.pow((new_list[0].xcor()-new_list[1].xcor()),2)+math.pow((new_list[0].ycor()-new_list[1].ycor()),2))<=new_list[0].shapesize()[0]+new_list[1].shapesize()[0]:
        if new_list[0].radius < new_list[1].radius:
            new_list[0].goto(50,50)
        else:
            new_list[1].goto(25,50)
        

function(new_list)

    
