import Turtle
class Ball(Turtle):
    def __init__(self,x,y,dx,dy,r,color)
    Turtle.__init__(self)
        self.x = x
        self.y = y
        self.goto(x,y)
        self.dx = dx
        self.dy = dy
        self.r=r
        self.color(color)
        self.shape("circle")
        self.shapesize(r/10)
        turtle.penup()

    def move(screen_width,screen_height):
        current_x =self.xcor()
        new_x = current_x + self.dx()
        current_y = self.ycor()
        new_y = current_y + self.dy()
        right_side_ball=new_x+r
        left_side_ball=new_x+r
        upper_side_ball=new_x+r
        down_side_ball=new_x+r
        self.goto(new_x,new_y)
        new_dx= dx
        new_dy= dy
        if(new_dx>screen_width/2):
            self.dx= -dx
        if(right_side_ball>screen_width/2):
            self.dx= -dx
        if(left_side_ball<-screen_width/2):
            self.dx= -dx
        if(upper_side_ball>screen_width/2):
            self.dx= -dx
        if(down_side_ball<-screen_width/2):
            self.dx= -dx
            
            
        


