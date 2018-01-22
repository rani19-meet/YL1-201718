from turtle import Turtle
import turtle
import time
import random
from ball import Ball



turtle.tracer(0)
turtle.hideturtle()
RUNNING = True
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanavas().winfo-width/2
SCREEN_HEIGHT = turtle.getcanavas().winfo_hieght/2



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
    x=random.randint(round(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
    y=random.randint(round(-SCREEN_HIEGHT+MAXIMUM_BALL_RADIUS,SCREEN_HIEGHT, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
    R=random.randint(0,255)
    G=random.randint(0,255)
    B=random.randint(0,255)
    dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
    while(dx==0):
        dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
    dy=random.randint(MINIMUM_BALL_DY,MAXIUM_BALL_DY)
    while(dy==0):
        dy=random.randint(MINIMUM_BALL_DY,MAXIUM_BALL_DY)
    r=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
    color = self.color(R,G,B)
    
    ball=(x,y,dx,dy,r,color)
    BALLS.append(ball)


def move_all_balls(SCREEN_WIDTH,SCREEN_HEIGHT,BALLS):
    for i in Balls:
        ball.penup()
        random_x_pos = random.randint(round(-SCREEN_WIDTH+Rr),round(SCREEN_WIDTH-r))
        random_y_pos = random.randint(round(-SCREEN_WIDTH+r),round(SCREEN_WIDTH-r))
        ball.goto(random_x_pos,random_y_pos)
move_all_balls(SCREEN_WIDTH,SCREEN_HIEGHT,BALLS)
ball_a=MY_BALL(25,10,5,15,15,"red")
ball_b=MY_BALL(30,45,10,24,9,"black")
BALLS.append(ball_a)
BALLS.append(ball_b)
        

def collide(ball_a,ball_b):
    if ball_a.r==ball_b.r and ball_a.pos()==ball_b.pos():
        return false
     d=math.sqrt(math.pow((ball_a.xcor()-ball_b.xcor(),2)+math.pow((ball_a.ycor()-ball_b.ycor()),2))<=ball_a.r+ball_b.r
    if d+10<=ball_a.r + ball_b.r:
        return True
    else return False
    
def check_all_balls_collision():
        for ball_a in BALLS:
        for bal_b in BALLS:
        if collide(ball_a,ball_b)==True:
                 a_radius= ball_a.r()
                 b_radius = ball_b.r()
    X_COORDINATE = random.randint(round(-SCREEN_WIDTH+ball_a.r,SCREEN_WIDTH+ball_a.r)
    Y_COORDINATE = random.randint(round(-SCREEN_HEIGHT + ball_a.r,SCREEN_HEIGHT+ball_a.r)
    X_axis_speed = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
    while (X_axis_speed==0):
        X_axis_speed = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
    Y_axis_speed = random.randint(MINIMUM_BALL_DY,MANXIMUM_BALL_DY)
    while(Y_axis_speed==0):
         Y_axis_speed = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
    r=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
    R = random.randint(0,255)
    G = random.randint(0,255)
    B = random.randint(0,255)
    color = self.color(R,G,B)
    if ball_a.r < ball_b.r:
        ball_a =(X_COORDNATE,Y_COORDINATE,X_axis_speed,Y_axis_speed,r,color)
        ball_b.r = ball_b.r + 1
    if ball_b.r < ball_a.r:
        ball_b =(X_COORDNATE,Y_COORDINATE,X_axis_speed,Y_axis_speed,r,color)
        ball_a.r = ball_a.r + 1 
#def check_myball_collision():
