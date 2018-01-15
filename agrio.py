from turtle import Turtle
import turtle
import time
import random
from ball import Ball



turtle.tracer(0)
turtle.hideturtle()




def MY_BALL(Ball):
    NUMBER_OF_BALLS=5
    MINIMUM_BALL_RADIUS=10
    MAXIMUM_BALL_RADIUS=100
    MINIMUM_BALL_DX=-5
    MAXIMUM_BALL_DX=5
    MINIMUM_BALL_DY=-5
    MAXIMUM_BALL_DY=5

BALLS=[]

for i in NUMBER_OF_BALLS:
    self.x=random.randint(SCREEN_WIDTH,MAXIMUM_BALL_RADIUS)
    self.y=random.randint(SCREEN_WIDTH,MAXIMUM_BALL_RADIUS)
    self.dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
    self.dy=random.randint(MINIMUM_BALL_DY,MAXIUM_BALL_DY)
    self.radius=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
    color=(random.random(), random.random(), random.random())
    
ball=(50,25,10,15,25,"blue")
BALLS.append(ball)


def move_all_balls():
    for i in Balls:
     (screen_width,screen_height)

ball_1=(25,10,5,15,15,"red")
ball_2=(30,45,10,24,9,"black")
BALLS.append(ball_1)
BALLS.append(ball_2)
        

def collide():
    if ball_a==ball_b:
        return false
    if math.sqrt(math.pow((ball_a.xcor()-ball_b.xcor),2)+math.pow((ball_a.ycor()-ball_b.ycor()),2))<=ball_a.radius()+ball_b.radius():
        return true
    else:
        return false
def check_all_balls_collision():
    for i in ball_a:
        for i in ball_b:
            if math.sqrt(math.pow((ball_a.xcor()-ball_b.xcor),2)+math.pow((ball_a.ycor()-ball_b.ycor()),2))<=ball_a.radius()+ball_b.radius():
                radius_ball_a=ball_a.radius()
                radius_ball_b=ball_b.radius()



#def check_myball_collision():
