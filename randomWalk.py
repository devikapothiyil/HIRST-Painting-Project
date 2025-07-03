import turtle
import random

t=turtle.Turtle()
t.pensize(20)
t.speed(10)
color_list=["red","green","yellow","blue","orange","black","pink","aquamarine","DeepSkyBlue"]
angles=[90,180,270,360]
for _ in range(100):
    t.pencolor(random.choice(color_list))
    t.forward(100)
    t.setheading(random.choice(angles))
scn=turtle.Screen()
scn.exitonclick()
