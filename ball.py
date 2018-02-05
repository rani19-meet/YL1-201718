from turtle import *
class Ball(Turtle):
    def __init__(self,x,y,dx,dy,r,color):
        Turtle.__init__(self)
        self.penup()
        self.x = x
        self.y = y
        self.goto(x,y)
        self.dx = dx
        self.dy = dy
        self.r=r
        self.color(color)
        self.shape("circle")
        self.shapesize(r/10)

    def move(self, screen_width,screen_height):
        current_x =self.xcor()
        new_x = current_x + self.dx
        current_y = self.ycor()
        new_y = current_y + self.dy
        right_side_ball=new_x+self.r
        left_side_ball=new_x+self.r
        upper_side_ball=new_x+self.r
        down_side_ball=new_x+self.r
        self.goto(new_x,new_y)
        new_dx= self.dx
        new_dy= self.dy
        if(new_dx>screen_width/2):
            self.dx= -self.dx
        if(right_side_ball>screen_width/2):
            self.dx= -self.dx
        if(left_side_ball<-screen_width/2):
            self.dx= -self.dx
        if(upper_side_ball>screen_width/2):
            self.dy= -self.dy
        if(down_side_ball<-screen_width/2):
            self.dy= -self.dy





