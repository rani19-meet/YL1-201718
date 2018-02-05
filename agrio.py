from turtle import *
import turtle
import time
import random
from ball import Ball
import math



turtle.tracer(0)
turtle.hideturtle()
turtle.pu()
RUNNING = True
SLEEP = 0.0077
SCREEN_WIDTH = int(turtle.getcanvas().winfo_width()/2)
SCREEN_HEIGHT = int(turtle.getcanvas().winfo_height()/2)




NUMBER_OF_BALLS=5
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=100
MINIMUM_BALL_DX=-5
MAXIMUM_BALL_DX=5
MINIMUM_BALL_DY=-5
MAXIMUM_BALL_DY=5

BALLS=[]

MY_BALL = Ball(0, 0, 0, 0, 20, "blue")

for i in range(NUMBER_OF_BALLS):
    x=random.randint(round(-SCREEN_WIDTH)+MAXIMUM_BALL_RADIUS,(round(SCREEN_WIDTH) - MAXIMUM_BALL_RADIUS))
    y=random.randint(round(-SCREEN_HEIGHT)+MAXIMUM_BALL_RADIUS,(round(SCREEN_HEIGHT) - MAXIMUM_BALL_RADIUS))
    color = (random.random(), random.random(), random.random())
    dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
    while(dx==0):
        dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
    dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
    while(dy==0):
        dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
    r=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
    
    ball=Ball(x,y,dx,dy,r,color)
    BALLS.append(ball)


def move_all_balls():
    for ball in BALLS:
        ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)
        
move_all_balls()

def collide(ball_a,ball_b):
    if ball_a.r==ball_b.r and ball_a.pos()==ball_b.pos():
        return False
    ball_a_x = ball_a.xcor()
    ball_a_y = ball_a.ycor()

    ball_b_x = ball_b.xcor()
    ball_b_y = ball_b.ycor()

    d =math.sqrt(math.pow((ball_b.xcor()-ball_a.xcor()),2) + math.pow((ball_b.ycor()-ball_a.ycor()),2))

    if d+10 <= ball_a.r + ball_b.r:
       return True
    else:
        return False
def check_all_balls_collision():
        for ball_a in BALLS:
            for ball_b in BALLS:
                if collide(ball_a,ball_b)==True:
                    a_radius= ball_a.r
                    b_radius = ball_b.r
                    X_COORDINATE = random.randint(-SCREEN_WIDTH+ball_a.r,SCREEN_WIDTH+ball_a.r)
                    Y_COORDINATE = random.randint(-SCREEN_HEIGHT + ball_a.r,SCREEN_HEIGHT+ball_a.r)
                    X_axis_speed = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
                    while (X_axis_speed==0):
                        X_axis_speed = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
                    Y_axis_speed = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
                    while(Y_axis_speed==0):
                        Y_axis_speed = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
                    r=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
                    R = random.randint(0,255)
                    G = random.randint(0,255)
                    B = random.randint(0,255)
                    color = (R,G,B)
                if ball_a.r < ball_b.r:
                    
                    ball_a.goto(X_COORDINATE,Y_COORDINATE)
                    ball_a.X_axis_speed=X_axis_speed
                    ball_a.Y_axis_speed=Y_axis_speed
                    ball_a.r=r
                    ball_a.shapesize(ball_a.r/10)
                    ball_a.color(color )                      
                    ball_b.r = ball_b.r + 1
                    ball_a.shapesize(ball_a.r/10)
                if ball_b.r < ball_a.r:
                    
                    ball_b.X_COORDNATE=X_COORDNATE
                    ball_b.Y_COORDINATE=Y_COORDINATE
                    ball_b.X_axis_speed=X_axis_speed
                    ball_b.Y_axis_speed=Y_axis_speed
                    ball_b.r=r
                    ball_b.shapesize(ball_b.r/10)
                    ball_b.color(color)
                    ball_a.r = ball_a.r + 1
                    ball_b.shapesize(ball_b.r/10)
def check_myball_collision():
    for ball in BALLS:
        if collide(MY_BALL,ball) == True:
            ball_r4 = ball.r
            my_ball_r4 = MY_BALL.r
            if my_ball_r4 == ball_r4 and MY_BALL.shapesize() < BALL.shapesize():
                return False
            X_COORDINATE = random.randint(round(-SCREEN_WIDTH), round(SCREEN_WIDTH))
            Y_COORDINATE = random.randint(round(-SCREEN_HEIGHT) , round(SCREEN_HEIGHT))
            X_AXISSPEED = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
            Y_AXISSPEED = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
            while X_AXISSPEED and Y_AXISSPEED == 0:
                X_AXISSPEED = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
                Y_AXISSPEED = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)

            radius = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
            print(radius)

            color = (random.random(),random.random(),random.random())
            print(color)
            if my_ball_r4 > ball_r4 and MY_BALL.shapesize() > ball.shapesize():
                my_ball_r4 = my_ball_r4 + ball_r4
                ball_r4 = radius
                ball_x = X_COORDINATE
                ball_y = Y_COORDINATE
                ball_dx = X_AXISSPEED
                ball_dy = Y_AXISSPEED
                ball.color(color)
                ball.shapesize(ball.r/10)
                MY_BALL.shapesize(my_ball_r4/10)
    return True

def Movearound(event):
    MY_BALL.goto(event.x - SCREEN_WIDTH, SCREEN_HEIGHT - event.y)
    
    

turtle.getcanvas().bind("<Motion>" , Movearound)
turtle.getscreen().listen()

while RUNNING == True:
    if SCREEN_WIDTH!=turtle.getcanvas().winfo_width()/2 or SCREEN_HEIGHT!=turtle.getcanvas().winfo_height()/2:
        SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
        SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
    move_all_balls()
    check_all_balls_collision()
    MY_BALL.move(SCREEN_WIDTH,SCREEN_HEIGHT)
    RUNNING = check_myball_collision()
    turtle.update()
    time.sleep(SLEEP)


                    
            
        
        
