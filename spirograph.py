import turtle
import random

turtle.colormode(255)
t=turtle.Turtle()
t.speed(0)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    randcolor=(r,g,b)
    return  randcolor

def spirograph(size):
    for i in range(int(360/size)):
        t.pencolor(random_color())
        t.circle(100)
        t.left(size)

spirograph(10)
scn=turtle.Screen()
scn.exitonclick()
