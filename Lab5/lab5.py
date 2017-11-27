from turtle import Turtle, colormode
import turtle
import random
colormode(255)
class Hexagon(Turtle):
    def __init__(self,size):
        Turtle.__init__(self)
        self.shapesize(size)
turtle.begin_poly()
turtle.forward(90)
turtle.right(50)
turtle.forward(90)
tortle.right(50)
turtle.forward(90)
turtle.right(50)
turtle.forward(90)
turtle.right(50)
turtle.forward(90)
turtle.right(50)
turtle.forward(90)
turtle.end_poly()
p=turtle.get_poly()
register_shape("myFavouriteShape",p)
class Square(Turtle):
    def __init__(self,size):
        Turtle.__init__(self)
        self.shapesize(size)
        self.shape("square")
    def random_color(self):
        r=random.randint(0,256)
        g=random.randint(0,256)
        b=random.randint(0,256)
        self.color(r,g,b)
hexagon1=Hexagon(30)
square1=Square(20)
square1.random_color()
turtle.mainloop()
